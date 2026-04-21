#!/usr/bin/env python3
"""Extract official RMM problems and classify combinatorics candidates."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "import_batches" / "extracted" / "rmm_official"
BASE = "https://rmms.lbi.ro/"

EDITION_CODES: list[tuple[int, str]] = [
    (2011, "rmm2011"),
    (2012, "rmm2012"),
    (2013, "rmm2013"),
    (2015, "rmm2015"),
    (2016, "rmm2016"),
    (2017, "rmm2017"),
    (2018, "rmm2018"),
    (2019, "rmm2019"),
    (2021, "rmm2021"),
    (2023, "rmm2023"),
    (2024, "rmm2024"),
    (2025, "rmm2025"),
]


GEOMETRY_PATTERNS = [
    r"\btriangle\b",
    r"\bcircle\b",
    r"\bcircumcircle\b",
    r"\bincircle\b",
    r"\bcircumcent(re|er)\b",
    r"\bincent(re|er)\b",
    r"\bangle\b",
    r"\bperpendicular\b",
    r"\bparallel\b",
    r"\btangent\b",
    r"\bmidpoint\b",
    r"\bcollinear\b",
    r"\bconvex\b",
    r"\bquadrilateral\b",
    r"\bpolygon\b",
    r"\barc\b",
    r"\bsegment\b",
]

ALGEBRA_PATTERNS = [
    r"\bfunction\b",
    r"\bfunctions\b",
    r"\bpolynomial\b",
    r"\bpolynomials\b",
    r"\breal number",
    r"\breal numbers\b",
    r"\bcomplex\b",
    r"\binequality\b",
]

NUMBER_THEORY_PATTERNS = [
    r"\bprime\b",
    r"\bprimes\b",
    r"\bdivides\b",
    r"\bdivisor\b",
    r"\bdivisors\b",
    r"\bgcd\b",
    r"\blcm\b",
    r"\bmodulo\b",
    r"\bcongruen",
    r"\bresidue\b",
    r"\bperfect square\b",
    r"\bperfect power\b",
    r"\bmultiple\b",
    r"\bfactorial\b",
]

COMBINATORICS_PATTERNS = [
    r"\bset\b",
    r"\bsets\b",
    r"\bsubset\b",
    r"\bsubsets\b",
    r"\bsequence\b",
    r"\bsequences\b",
    r"\barrangement\b",
    r"\barrangements\b",
    r"\bpermutation\b",
    r"\bpermutations\b",
    r"\bcolour",
    r"\bcolor",
    r"\bboard\b",
    r"\btable\b",
    r"\brows\b",
    r"\bcolumns\b",
    r"\bgame\b",
    r"\bplayers\b",
    r"\bcoins\b",
    r"\bcards\b",
    r"\bchoose\b",
    r"\bchosen\b",
    r"\bpartition\b",
    r"\bgraph\b",
    r"\bvertex\b",
    r"\bvertices\b",
    r"\bedge\b",
    r"\bedges\b",
    r"\btree\b",
    r"\bforest\b",
    r"\bpath\b",
    r"\bcycle\b",
    r"\btournament\b",
]

GRAPH_PATTERNS = [
    r"\bgraph\b",
    r"\bvertex\b",
    r"\bvertices\b",
    r"\bedge\b",
    r"\bedges\b",
    r"\btree\b",
    r"\bforest\b",
    r"\bpath\b",
    r"\bcycle\b",
    r"\bwalk\b",
    r"\bmatching\b",
    r"\btournament\b",
    r"\bconnected\b",
    r"\bcomponent\b",
    r"\bboard\b",
    r"\bgrid\b",
    r"\badjacent\b",
    r"\bdomino\b",
    r"\btiling\b",
    r"\bcolour",
    r"\bcolor",
]


def clean_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "п¬Ђ": "ff",
        "в€’": "-",
        "вЂ“": "-",
        "вЂ”": "-",
        "в€€": " in ",
        "в‰¤": "<=",
        "в‰Ґ": ">=",
        "в„•": "N",
        "в„¤": "Z",
        "в„ќ": "R",
        "\x0c": "\n",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def compact_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def fetch(url: str, path: Path | None = None, refresh: bool = False) -> tuple[bool, str | None, bytes | None]:
    if path is not None and path.exists() and not refresh:
        return True, None, path.read_bytes()
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=60) as response:
            data = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        return False, str(exc), None
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return True, None, data


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    text = "\n".join((page.extract_text() or "") for page in reader.pages)
    return clean_text(text)


def parse_pdf_links(html_text: str, page_url: str) -> list[str]:
    links = []
    for tag, attr in [("iframe", "src"), ("a", "href")]:
        pattern = rf"<{tag}[^>]+{attr}\s*=\s*[\"']([^\"']+\.pdf[^\"']*)"
        for link in re.findall(pattern, html_text, re.I):
            links.append(urljoin(page_url, unescape(link)))
    for raw in re.findall(r"[_A-Za-z0-9./ -]+\.pdf", html_text, re.I):
        links.append(urljoin(page_url, raw.strip()))
    normalized = []
    seen = set()
    for link in links:
        link = link.replace(" ", "%20")
        if link not in seen:
            seen.add(link)
            normalized.append(link)
    return normalized


def english_score(url: str) -> tuple[int, int]:
    lower = url.lower()
    return (
        1 if "english" in lower or "eng" in lower else 0,
        1 if "solution" in lower or "sol" in lower else 0,
    )


def choose_problem_links(links: list[str]) -> list[str]:
    links = [link for link in links if "grading" not in link.lower()]
    english = [link for link in links if english_score(link)[0]]
    if english:
        links = english
    links = [link for link in links if "solution" not in link.lower() and "sol" not in link.lower()]
    return links[:2]


def choose_solution_links(links: list[str]) -> list[str]:
    links = [link for link in links if "grading" not in link.lower()]
    solutionish = [link for link in links if "solution" in link.lower() or "sol" in link.lower()]
    english = [link for link in solutionish if english_score(link)[0]]
    if english:
        return english[:2]
    if solutionish:
        return solutionish[:2]
    return []


def split_problem_blocks(text: str, expected_numbers: set[int] | None = None) -> dict[int, str]:
    patterns = [
        re.compile(r"(?m)^\s*(?:Problem|P)\s*([1-6])[\.:]\s*"),
        re.compile(r"(?m)^\s*([1-6])\.\s+"),
    ]
    best_matches = []
    for pattern in patterns:
        matches = list(pattern.finditer(text))
        if len(matches) > len(best_matches):
            best_matches = matches
        if len(matches) >= 3:
            break
    matches = best_matches
    blocks: dict[int, str] = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end].strip()
        if expected_numbers and number not in expected_numbers:
            continue
        if number not in blocks or len(block) > len(blocks[number]):
            blocks[number] = block
    return blocks


def strip_problem_label(block: str, number: int) -> str:
    block = re.sub(rf"(?m)^\s*(?:Problem|P)\s*{number}[\.:]\s*", "", block, count=1).strip()
    block = re.sub(rf"(?m)^\s*{number}\.\s+", "", block, count=1).strip()
    return block


def extract_statements(text: str) -> dict[int, str]:
    blocks = split_problem_blocks(text)
    result = {}
    for number, block in blocks.items():
        cleaned = strip_problem_label(block, number)
        cleaned = re.sub(r"(?is)\bEach problem is worth.*$", "", cleaned).strip()
        cleaned = re.sub(r"(?is)\bTime allowed.*$", "", cleaned).strip()
        result[number] = cleaned
    return result


def extract_solutions(text: str, expected_numbers: set[int] | None = None) -> dict[int, str]:
    blocks = split_problem_blocks(text, expected_numbers=expected_numbers)
    result = {}
    for number, block in blocks.items():
        cleaned = strip_problem_label(block, number)
        result[number] = cleaned
    return result


def score_patterns(text: str, patterns: list[str]) -> int:
    return sum(1 for pattern in patterns if re.search(pattern, text, re.I))


def classify_problem(statement: str, solution: str) -> dict[str, object]:
    combined = f"{statement}\n{solution}"
    scores = {
        "geometry": score_patterns(combined, GEOMETRY_PATTERNS),
        "algebra": score_patterns(combined, ALGEBRA_PATTERNS),
        "number_theory": score_patterns(combined, NUMBER_THEORY_PATTERNS),
        "combinatorics": score_patterns(combined, COMBINATORICS_PATTERNS),
    }
    top_subject = max(scores, key=lambda key: scores[key])
    graph_terms = sorted(
        {
            pattern.strip(r"\b").replace("\\", "")
            for pattern in GRAPH_PATTERNS
            if re.search(pattern, combined, re.I)
        }
    )

    decision = "not_combinatorics"
    confidence = 0.55
    if scores["combinatorics"] >= 2 and scores["combinatorics"] >= scores["geometry"] and scores["combinatorics"] >= scores["algebra"]:
        decision = "candidate"
        confidence = 0.72 if scores["combinatorics"] >= 3 else 0.63
    elif top_subject == "combinatorics" and scores["combinatorics"] >= 1:
        decision = "needs_review"
        confidence = 0.58
    elif graph_terms:
        decision = "needs_review"
        confidence = 0.62

    return {
        "subject_guess": top_subject,
        "subject_scores": scores,
        "combinatorics_decision": decision,
        "confidence": confidence,
        "graph_terms": graph_terms,
        "reason": f"scores={scores}",
    }


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fetch_page(url: str, path: Path, refresh: bool = False) -> str:
    ok, err, data = fetch(url, path, refresh=refresh)
    if not ok or data is None:
        raise RuntimeError(f"failed to fetch {url}: {err}")
    return data.decode("utf-8", "ignore")


def process_year(year: int, code: str, out_dir: Path, refresh: bool = False) -> dict[str, object]:
    html_dir = out_dir / "html"
    pdf_dir = out_dir / "pdf" / f"rmm-{year}"
    problems_url = f"{BASE}{code}/index.php?id=problems_math"
    solutions_url = f"{BASE}{code}/index.php?id=solutions_math"

    problems_html = fetch_page(problems_url, html_dir / f"{code}-problems.html", refresh=refresh)
    try:
        solutions_html = fetch_page(solutions_url, html_dir / f"{code}-solutions.html", refresh=refresh)
    except RuntimeError:
        solutions_html = ""

    problem_links = choose_problem_links(parse_pdf_links(problems_html, problems_url))
    solution_links = choose_solution_links(parse_pdf_links(problems_html, problems_url))
    if not solution_links and solutions_html:
        solution_links = choose_solution_links(parse_pdf_links(solutions_html, solutions_url))

    statement_texts = []
    solution_texts = []
    problem_downloads = []
    solution_downloads = []

    for idx, link in enumerate(problem_links, start=1):
        filename = f"day{idx}-problems.pdf"
        path = pdf_dir / filename
        ok, err, _ = fetch(link, path, refresh=refresh)
        problem_downloads.append({"url": link, "ok": ok, "error": err, "local_pdf": str(path.relative_to(ROOT)).replace("\\", "/")})
        if ok:
            statement_texts.append(pdf_text(path))

    for idx, link in enumerate(solution_links, start=1):
        filename = f"day{idx}-solutions.pdf"
        path = pdf_dir / filename
        ok, err, _ = fetch(link, path, refresh=refresh)
        solution_downloads.append({"url": link, "ok": ok, "error": err, "local_pdf": str(path.relative_to(ROOT)).replace("\\", "/")})
        if ok:
            solution_texts.append(pdf_text(path))

    statements = {}
    for text in statement_texts:
        for number, block in extract_statements(text).items():
            if number not in statements or len(block) > len(statements[number]):
                statements[number] = block

    expected_numbers = set(statements) if statements else None
    solutions = {}
    for text in solution_texts:
        for number, block in extract_solutions(text, expected_numbers=expected_numbers).items():
            if number not in solutions or len(block) > len(solutions[number]):
                solutions[number] = block

    numbers = sorted(set(statements) | set(solutions))
    problems = []
    for number in numbers:
        statement = statements.get(number, "")
        solution = solutions.get(number, "")
        classification = classify_problem(statement, solution)
        problems.append(
            {
                "id": f"rmm-{year}-p{number}",
                "year": year,
                "problem_number": number,
                "statement_en": statement,
                "solution_text_en": solution,
                "source": {
                    "problems_page_url": problems_url,
                    "solutions_page_url": solutions_url,
                    "problem_pdfs": problem_downloads,
                    "solution_pdfs": solution_downloads,
                },
                "availability": {
                    "official_statement": bool(statement),
                    "official_solution": bool(solution),
                },
                **classification,
            }
        )

    return {
        "year": year,
        "edition_code": code,
        "problems_page_url": problems_url,
        "solutions_page_url": solutions_url,
        "problem_pdf_count": len(problem_downloads),
        "solution_pdf_count": len(solution_downloads),
        "problem_count_extracted": len(problems),
        "problems": problems,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=2011)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args(argv)

    out_dir: Path = args.out_dir
    year_dir = out_dir / "years"
    manifest = {
        "id": "rmm-official-problems-extract",
        "created_at": date.today().isoformat(),
        "official_source": "https://rmms.lbi.ro/",
        "scope": {
            "start_year": args.start_year,
            "end_year": args.end_year,
            "note": "Official RMM pages and English PDFs by year; only years with archived official math PDFs are included.",
        },
        "years": [],
    }
    combinatorics = []
    needs_review = []

    for year, code in EDITION_CODES:
        if year < args.start_year or year > args.end_year:
            continue
        payload = process_year(year, code=code, out_dir=out_dir, refresh=args.refresh)
        write_json(year_dir / f"rmm-{year}-official-extract.json", payload)
        manifest["years"].append(
            {
                "year": year,
                "edition_code": code,
                "problem_pdf_count": payload["problem_pdf_count"],
                "solution_pdf_count": payload["solution_pdf_count"],
                "problem_count_extracted": payload["problem_count_extracted"],
            }
        )
        for problem in payload["problems"]:
            compact = {
                "id": problem["id"],
                "year": problem["year"],
                "problem_number": problem["problem_number"],
                "statement_en": problem["statement_en"],
                "availability": problem["availability"],
                "subject_guess": problem["subject_guess"],
                "subject_scores": problem["subject_scores"],
                "combinatorics_decision": problem["combinatorics_decision"],
                "confidence": problem["confidence"],
                "graph_terms": problem["graph_terms"],
                "reason": problem["reason"],
            }
            if problem["combinatorics_decision"] == "candidate":
                combinatorics.append(compact)
            elif problem["combinatorics_decision"] == "needs_review":
                needs_review.append(compact)

    write_json(out_dir / "rmm-official-source-manifest.json", manifest)
    write_json(
        out_dir / "rmm-official-combinatorics.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "RMM problems with combinatorics classification candidate",
            "count": len(combinatorics),
            "problems": combinatorics,
        },
    )
    write_json(
        out_dir / "rmm-official-needs-review.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "RMM problems with ambiguous combinatorics or graph-like signals",
            "count": len(needs_review),
            "problems": needs_review,
        },
    )

    print(f"wrote {out_dir}")
    print(f"combinatorics candidates: {len(combinatorics)}")
    print(f"needs review: {len(needs_review)}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main(sys.argv[1:]))

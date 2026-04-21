#!/usr/bin/env python3
"""Extract official EGMO problems and select combinatorics candidates.

This is an extraction aid. It downloads official EGMO pages/PDFs, extracts
English problem statements (and official solutions when available), and writes
JSON for later graph-focused curation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from datetime import date
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "import_batches" / "extracted" / "egmo_official"
BASE = "https://www.egmo.org/egmos/"


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
    r"\bline\b",
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
    r"\bfind all functions\b",
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
    r"\bmatching\b",
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


MANUAL_COMBINATORICS_OVERRIDES = {
    (2012, 2): "candidate",
    (2012, 4): "candidate",
    (2012, 6): "candidate",
    (2012, 8): "candidate",
    (2013, 2): "candidate",
    (2013, 6): "candidate",
    (2014, 4): "candidate",
    (2014, 5): "candidate",
    (2015, 2): "candidate",
    (2015, 5): "candidate",
    (2016, 3): "candidate",
    (2016, 5): "candidate",
    (2017, 2): "candidate",
    (2017, 4): "candidate",
    (2018, 3): "candidate",
    (2018, 4): "candidate",
    (2019, 2): "candidate",
    (2019, 6): "candidate",
    (2020, 4): "candidate",
    (2021, 5): "candidate",
    (2022, 5): "candidate",
    (2023, 3): "candidate",
    (2023, 4): "candidate",
    (2024, 1): "candidate",
    (2024, 4): "candidate",
    (2025, 2): "candidate",
    (2025, 5): "candidate",

    (2020, 2): "not_combinatorics",
    (2021, 1): "not_combinatorics",
    (2021, 6): "not_combinatorics",
    (2022, 2): "not_combinatorics",
    (2023, 5): "not_combinatorics",
    (2024, 6): "not_combinatorics",
    (2025, 6): "not_combinatorics",
}


def clean_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "ﬀ": "ff",
        "вЂњ": '"',
        "вЂќ": '"',
        "вЂ": "'",
        "вЂ™": "'",
        "−": "-",
        "–": "-",
        "—": "-",
        "∈": " in ",
        "≤": "<=",
        "≥": ">=",
        "ℕ": "N",
        "ℤ": "Z",
        "ℝ": "R",
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


def parse_links(html_text: str, page_url: str) -> dict[str, str]:
    links: dict[str, str] = {}
    for href, label in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html_text, re.I | re.S):
        label_text = compact_text(unescape(re.sub(r"<[^>]+>", " ", label)))
        if label_text:
            links[label_text] = urljoin(page_url, href)
    return links


def strip_html(html_text: str) -> str:
    text = re.sub(r"<script\b.*?</script>", "", html_text, flags=re.I | re.S)
    text = re.sub(r"<style\b.*?</style>", "", text, flags=re.I | re.S)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p>|</div>|</li>|</h[1-6]>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return clean_text(unescape(text))


def extract_problem_count(page_text: str) -> int | None:
    match = re.search(r"Number of problems\s+(\d+)", page_text)
    return int(match.group(1)) if match else None


def split_problem_blocks(text: str) -> dict[int, str]:
    pattern = re.compile(r"(?m)^\s*Problem\s+(\d+)\.\s*")
    matches = list(pattern.finditer(text))
    blocks: dict[int, str] = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end].strip()
        blocks[number] = block
    return blocks


def strip_problem_label(block: str, number: int) -> str:
    text = re.sub(rf"(?m)^\s*Problem\s+{number}\.\s*", "", block, count=1)
    return text.strip()


def extract_statements_from_paper(text: str) -> dict[int, str]:
    blocks = split_problem_blocks(text)
    result = {}
    for number, block in blocks.items():
        stripped = strip_problem_label(block, number)
        stripped = re.sub(r"Language:.*$", "", stripped, flags=re.S).strip()
        stripped = re.sub(r"Each problem is worth.*$", "", stripped, flags=re.S).strip()
        result[number] = stripped
    return result


def extract_solutions_from_pdf(text: str) -> dict[int, str]:
    text = clean_text(text)
    if "Solutions" in text:
        split_at = text.find("Solutions")
        text = text[split_at:]
    blocks = split_problem_blocks(text)
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
    graph_terms = sorted(
        {
            pattern.strip(r"\b").replace("\\", "")
            for pattern in GRAPH_PATTERNS
            if re.search(pattern, combined, re.I)
        }
    )

    top_subject = max(scores, key=lambda key: scores[key])
    sorted_scores = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    decision = "not_combinatorics"
    confidence = 0.55
    reason = f"scores={scores}"

    if scores["combinatorics"] >= 2 and scores["geometry"] <= scores["combinatorics"] and scores["algebra"] <= scores["combinatorics"]:
        decision = "candidate"
        confidence = 0.75 if scores["combinatorics"] >= 3 else 0.64
    elif top_subject == "combinatorics" and scores["combinatorics"] >= 1:
        decision = "needs_review"
        confidence = 0.58
    elif graph_terms:
        decision = "needs_review"
        confidence = 0.62
        reason += "; graph-like signal present"

    return {
        "subject_guess": top_subject,
        "subject_scores": scores,
        "combinatorics_decision": decision,
        "confidence": confidence,
        "graph_terms": graph_terms,
        "reason": reason,
        "statement_preview": compact_text(statement)[:220],
    }


@dataclass
class EgmoEdition:
    number: int
    year: int
    page_url: str
    problem_count: int | None
    links: dict[str, str]
    link_items: list[tuple[str, str]]


def load_edition(number: int, html_dir: Path, refresh: bool = False) -> EgmoEdition | None:
    page_url = f"{BASE}egmo{number}/"
    html_path = html_dir / f"egmo{number}.html"
    ok, error, data = fetch(page_url, html_path, refresh=refresh)
    if not ok or data is None:
        print(f"failed to fetch {page_url}: {error}", file=sys.stderr)
        return None
    html_text = data.decode("utf-8", errors="replace")
    page_text = strip_html(html_text)
    year = 2011 + number
    link_items = []
    for href, label in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html_text, re.I | re.S):
        label_text = compact_text(unescape(re.sub(r"<[^>]+>", " ", label)))
        if label_text:
            link_items.append((label_text, urljoin(page_url, href)))
    links = parse_links(html_text, page_url)
    return EgmoEdition(
        number=number,
        year=year,
        page_url=page_url,
        problem_count=extract_problem_count(page_text),
        links=links,
        link_items=link_items,
    )


def get_paper_links(edition: EgmoEdition) -> list[tuple[str, str]]:
    direct = []
    for label, url in edition.link_items:
        if label == "English" and "paper-day" in url and "-bg-" not in url:
            direct.append((label, url))
    if len(direct) >= 2:
        return direct[:2]

    background = []
    for label, url in edition.link_items:
        if label == "English" and "paper-day" in url:
            background.append((label, url))
    if len(background) >= 2:
        return background[:2]

    fallback = []
    for label, url in edition.link_items:
        if "English" in label and "paper-day" in url and all(existing_url != url for _, existing_url in fallback):
            fallback.append((label, url))
    return fallback[:2]


def get_solution_links(edition: EgmoEdition) -> list[str]:
    urls = []
    for label in ("Problems and solutions", "Solutions", "Day 1 solutions", "Day 2 solutions"):
        url = edition.links.get(label)
        if url and url not in urls:
            urls.append(url)
    return urls


def process_edition(edition: EgmoEdition, out_dir: Path, refresh: bool = False) -> dict[str, object]:
    pdf_dir = out_dir / "pdf" / f"egmo-{edition.year}"
    statements: dict[int, str] = {}
    papers = []
    for index, (label, url) in enumerate(get_paper_links(edition), start=1):
        pdf_path = pdf_dir / f"paper-{index}.pdf"
        ok, error, _ = fetch(url, pdf_path, refresh=refresh)
        papers.append({"label": label, "url": url, "local_pdf": str(pdf_path.relative_to(ROOT)).replace("\\", "/"), "ok": ok, "error": error})
        if not ok:
            continue
        extracted = extract_statements_from_paper(pdf_text(pdf_path))
        statements.update(extracted)

    solutions: dict[int, str] = {}
    solution_files = []
    for index, url in enumerate(get_solution_links(edition), start=1):
        pdf_path = pdf_dir / f"solutions-{index}.pdf"
        ok, error, _ = fetch(url, pdf_path, refresh=refresh)
        solution_files.append({"url": url, "local_pdf": str(pdf_path.relative_to(ROOT)).replace("\\", "/"), "ok": ok, "error": error})
        if not ok:
            continue
        extracted = extract_solutions_from_pdf(pdf_text(pdf_path))
        for number, text in extracted.items():
            if number not in solutions or len(text) > len(solutions[number]):
                solutions[number] = text

    problem_numbers = sorted(set(statements) | set(solutions))
    problems = []
    for number in problem_numbers:
        statement = statements.get(number, "")
        solution = solutions.get(number, "")
        classification = classify_problem(statement, solution)
        override = MANUAL_COMBINATORICS_OVERRIDES.get((edition.year, number))
        if override is not None:
            classification["combinatorics_decision"] = override
            classification["reason"] = f"{classification['reason']}; manual_override={override}"
        problems.append(
            {
                "id": f"egmo-{edition.year}-p{number}",
                "year": edition.year,
                "egmo_number": edition.number,
                "problem_number": number,
                "statement_en": statement,
                "solution_text_en": solution,
                "source": {
                    "official_page_url": edition.page_url,
                    "paper_files": papers,
                    "solution_files": solution_files,
                },
                "availability": {
                    "official_statement": bool(statement),
                    "official_solution": bool(solution),
                },
                **classification,
            }
        )

    return {
        "year": edition.year,
        "egmo_number": edition.number,
        "official_page_url": edition.page_url,
        "problem_count_declared": edition.problem_count,
        "problem_count_extracted": len(problems),
        "papers": papers,
        "solution_files": solution_files,
        "problems": problems,
    }


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-egmo", type=int, default=1)
    parser.add_argument("--end-egmo", type=int, default=14)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args(argv)

    out_dir: Path = args.out_dir
    html_dir = out_dir / "html"
    year_dir = out_dir / "years"

    editions = []
    for number in range(args.start_egmo, args.end_egmo + 1):
        edition = load_edition(number, html_dir=html_dir, refresh=args.refresh)
        if edition is not None:
            editions.append(edition)

    manifest = {
        "id": "egmo-official-problems-extract",
        "created_at": date.today().isoformat(),
        "official_source": "https://www.egmo.org/",
        "scope": {
            "start_egmo_number": args.start_egmo,
            "end_egmo_number": args.end_egmo,
            "note": "Official EGMO archive pages, English papers, and official solutions where available.",
        },
        "years": [],
    }
    combinatorics = []
    needs_review = []

    for edition in editions:
        payload = process_edition(edition, out_dir=out_dir, refresh=args.refresh)
        write_json(year_dir / f"egmo-{edition.year}-official-extract.json", payload)

        manifest["years"].append(
            {
                "egmo_number": edition.number,
                "year": edition.year,
                "official_page_url": edition.page_url,
                "problem_count_declared": edition.problem_count,
                "problem_count_extracted": payload["problem_count_extracted"],
                "has_solution_files": any(item["ok"] for item in payload["solution_files"]),
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

    write_json(out_dir / "egmo-official-source-manifest.json", manifest)
    write_json(
        out_dir / "egmo-official-combinatorics.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "EGMO problems with combinatorics classification candidate",
            "count": len(combinatorics),
            "problems": combinatorics,
        },
    )
    write_json(
        out_dir / "egmo-official-needs-review.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "EGMO problems with ambiguous combinatorics or graph-like signals",
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

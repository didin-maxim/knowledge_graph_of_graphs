#!/usr/bin/env python3
"""Extract official APMO problems and classify combinatorics candidates."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "import_batches" / "extracted" / "apmo_official"
PROBLEM_BASE = "https://apmo-official.org/static/problems/apmo{year}_prb.pdf"
SOLUTION_BASE = "https://apmo-official.org/static/solutions/apmo{year}_sol.pdf"


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
        "ﬀ": "ff",
        "−": "-",
        "–": "-",
        "—": "-",
        "≤": "<=",
        "≥": ">=",
        "∈": " in ",
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


def split_problem_blocks(text: str) -> dict[int, str]:
    pattern = re.compile(r"(?m)^\s*(?:Problem|P)\s*([1-5])[\.:]\s*")
    matches = list(pattern.finditer(text))
    blocks: dict[int, str] = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end].strip()
        if number not in blocks or len(block) > len(blocks[number]):
            blocks[number] = block
    return blocks


def strip_problem_label(block: str, number: int) -> str:
    return re.sub(rf"(?m)^\s*(?:Problem|P)\s*{number}[\.:]\s*", "", block, count=1).strip()


def extract_statements(text: str) -> dict[int, str]:
    blocks = split_problem_blocks(text)
    result = {}
    for number, block in blocks.items():
        cleaned = strip_problem_label(block, number)
        cleaned = re.sub(r"Language:.*$", "", cleaned, flags=re.S).strip()
        cleaned = re.sub(r"Each problem.*$", "", cleaned, flags=re.S).strip()
        cleaned = re.sub(r"\bAPMO\s+\d{4}.*$", "", cleaned, flags=re.S).strip()
        result[number] = cleaned
    return result


def extract_solutions(text: str) -> dict[int, str]:
    blocks = split_problem_blocks(text)
    result = {}
    for number, block in blocks.items():
        result[number] = strip_problem_label(block, number)
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


def process_year(year: int, out_dir: Path, refresh: bool = False) -> dict[str, object]:
    pdf_dir = out_dir / "pdf"
    problem_url = PROBLEM_BASE.format(year=year)
    solution_url = SOLUTION_BASE.format(year=year)
    problem_path = pdf_dir / f"apmo{year}_prb.pdf"
    solution_path = pdf_dir / f"apmo{year}_sol.pdf"

    ok_prb, err_prb, _ = fetch(problem_url, problem_path, refresh=refresh)
    ok_sol, err_sol, _ = fetch(solution_url, solution_path, refresh=refresh)

    statements = extract_statements(pdf_text(problem_path)) if ok_prb else {}
    solutions = extract_solutions(pdf_text(solution_path)) if ok_sol else {}
    numbers = sorted(set(statements) | set(solutions))

    problems = []
    for number in numbers:
        statement = statements.get(number, "")
        solution = solutions.get(number, "")
        classification = classify_problem(statement, solution)
        problems.append(
            {
                "id": f"apmo-{year}-p{number}",
                "year": year,
                "problem_number": number,
                "statement_en": statement,
                "solution_text_en": solution,
                "source": {
                    "problem_pdf_url": problem_url,
                    "solution_pdf_url": solution_url,
                    "problem_local_pdf": str(problem_path.relative_to(ROOT)).replace("\\", "/"),
                    "solution_local_pdf": str(solution_path.relative_to(ROOT)).replace("\\", "/"),
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
        "problem_pdf_url": problem_url,
        "solution_pdf_url": solution_url,
        "problem_pdf_ok": ok_prb,
        "solution_pdf_ok": ok_sol,
        "problem_pdf_error": err_prb,
        "solution_pdf_error": err_sol,
        "problem_count_extracted": len(problems),
        "problems": problems,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=1989)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args(argv)

    out_dir: Path = args.out_dir
    year_dir = out_dir / "years"
    manifest = {
        "id": "apmo-official-problems-extract",
        "created_at": date.today().isoformat(),
        "official_source": "https://apmo-official.org/problems",
        "scope": {
            "start_year": args.start_year,
            "end_year": args.end_year,
            "note": "Official APMO problem and solution PDFs by year.",
        },
        "years": [],
    }
    combinatorics = []
    needs_review = []

    for year in range(args.start_year, args.end_year + 1):
        payload = process_year(year, out_dir=out_dir, refresh=args.refresh)
        write_json(year_dir / f"apmo-{year}-official-extract.json", payload)
        manifest["years"].append(
            {
                "year": year,
                "problem_pdf_ok": payload["problem_pdf_ok"],
                "solution_pdf_ok": payload["solution_pdf_ok"],
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

    write_json(out_dir / "apmo-official-source-manifest.json", manifest)
    write_json(
        out_dir / "apmo-official-combinatorics.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "APMO problems with combinatorics classification candidate",
            "count": len(combinatorics),
            "problems": combinatorics,
        },
    )
    write_json(
        out_dir / "apmo-official-needs-review.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "APMO problems with ambiguous combinatorics or graph-like signals",
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

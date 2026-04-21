#!/usr/bin/env python3
"""Extract official MEMO problems and classify combinatorics candidates."""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import unicodedata
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "import_batches" / "extracted" / "memo_official"

YEAR_CONFIG = {
    2010: {
        "page_url": "https://memo2010.skmo.sk/problems.php",
        "individual_problem_pdf_url": "https://memo2010.skmo.sk/docs/indiv_english.pdf",
        "team_problem_pdf_url": "https://memo2010.skmo.sk/docs/team_english.pdf",
        "solution_pdf_url": "https://memo2010.skmo.sk/docs/solutions.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
    2011: {
        "page_url": "https://memo2011.math.hr/",
        "solution_pdf_url": "https://memo2011.math.hr/documents/MEMO2011solutions.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6"],
    },
    2016: {
        "page_url": "https://www.math.aau.at/MEMO2016/",
        "individual_problem_pdf_url": "https://www.math.aau.at/MEMO2016/wp-content/uploads/2015/08/IndividualEnglish.pdf",
        "team_problem_pdf_url": "https://www.math.aau.at/MEMO2016/wp-content/uploads/2015/08/TeamEnglish.pdf",
        "solution_pdf_url": "https://www.math.aau.at/MEMO2016/wp-content/uploads/2015/08/MEMO2016_Solutions-3.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
    2019: {
        "page_url": "http://memo2019.karlin.mff.cuni.cz",
        "individual_problem_pdf_url": "http://memo2019.karlin.mff.cuni.cz/static/media/i_en.ae5e66f6.pdf",
        "team_problem_pdf_url": "http://memo2019.karlin.mff.cuni.cz/static/media/t_en.12071a9d.pdf",
        "individual_solution_pdf_url": "http://memo2019.karlin.mff.cuni.cz/static/media/individual.aba51a3a.pdf",
        "team_solution_pdf_url": "http://memo2019.karlin.mff.cuni.cz/static/media/team.c6a5f6c7.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
    2020: {
        "page_url": "https://memo2020.memo-official.org/",
        "solution_pdf_url": "https://memo2020.memo-official.org/wp-content/uploads/2020/11/2020-11-15-MEMO-2020-Problems-solutions.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4"],
    },
    2021: {
        "page_url": "https://memo2021.math.hr/competition/",
        "individual_problem_pdf_url": "https://memo2021.math.hr/wp-content/uploads/2021/09/MEMO_2021_Individual_en.pdf",
        "team_problem_pdf_url": "https://memo2021.math.hr/wp-content/uploads/2021/09/MEMO_2021_Team_en.pdf",
        "solution_pdf_url": "https://memo2021.math.hr/wp-content/uploads/2021/12/Problems-and-Solutions-Booklet.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
    2022: {
        "page_url": "https://memo22.olympiad.ch/",
        "individual_problem_pdf_url": "https://memo22.olympiad.ch/fileadmin/user_upload/Memo22/MEMO_2022_I_en.pdf",
        "team_problem_pdf_url": "https://memo22.olympiad.ch/fileadmin/user_upload/Memo22/MEMO_2022_T_en.pdf",
        "individual_solution_pdf_url": "https://memo22.olympiad.ch/fileadmin/user_upload/Memo22/MEMO_2022_I_sol_en.pdf",
        "team_solution_pdf_url": "https://memo22.olympiad.ch/fileadmin/user_upload/Memo22/MEMO_2022_T_sol_en.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
    2023: {
        "page_url": "http://memo2023.skmo.sk/problems.php",
        "individual_problem_pdf_url": "http://memo2023.skmo.sk/docs/indiv_english.pdf",
        "team_problem_pdf_url": "http://memo2023.skmo.sk/docs/team_english.pdf",
        "solution_pdf_url": "http://memo2023.skmo.sk/docs/solutions.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
    2024: {
        "page_url": "https://memo2024.bolyai.hu/competition/problems-solutions",
        "individual_problem_pdf_url": "https://www.bolyai.hu/files/MEMO_2024_I_en.pdf",
        "team_problem_pdf_url": "https://www.bolyai.hu/files/MEMO_2024_T_en.pdf",
        "solution_pdf_url": "https://www.bolyai.hu/files/MEMO-2024-SolutionBooklet-2.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
    2025: {
        "page_url": "https://www.memo2025.de/Erg_en.html",
        "individual_problem_pdf_url": "https://memo2025.de/media/MEMO_2025_I_en.pdf",
        "team_problem_pdf_url": "https://memo2025.de/media/MEMO_2025_T_en.pdf",
        "solution_pdf_url": "https://memo2025.de/media/MEMO-2025-SolutionBooklet.pdf",
        "labels": ["I-1", "I-2", "I-3", "I-4", "T-1", "T-2", "T-3", "T-4", "T-5", "T-6", "T-7", "T-8"],
    },
}


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
        "РїВ¬Р‚": "ff",
        "РІв‚¬вЂ™": "-",
        "РІР‚вЂњ": "-",
        "РІР‚вЂќ": "-",
        "РІвЂ°В¤": "<=",
        "РІвЂ°Тђ": ">=",
        "РІв‚¬в‚¬": " in ",
        "РІвЂћвЂў": "N",
        "РІвЂћВ¤": "Z",
        "РІвЂћСњ": "R",
        "Ã—": "x",
        "\x0c": "\n",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch(url: str, path: Path | None = None, refresh: bool = False) -> tuple[bool, str | None, bytes | None]:
    if path is not None and path.exists() and not refresh:
        return True, None, path.read_bytes()
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=60, context=ssl._create_unverified_context()) as response:
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


def normalize_label(kind: str, number: str) -> str:
    return f"{kind.upper()}-{int(number)}"


def split_problem_blocks(text: str, expected_labels: list[str]) -> dict[str, str]:
    label_set = set(expected_labels)
    patterns = [
        re.compile(r"(?mi)^\s*(?:Problem\s+)?([IT])\s*[-–— ]\s*([1-8])\b"),
        re.compile(r"(?mi)\b(?:Problem\s+)?([IT])\s*[-–— ]\s*([1-8])\b"),
    ]
    matches: list[re.Match[str]] = []
    for pattern in patterns:
        candidate = [m for m in pattern.finditer(text) if normalize_label(m.group(1), m.group(2)) in label_set]
        if len(candidate) > len(matches):
            matches = candidate
        if len(candidate) >= len(expected_labels):
            break

    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        label = normalize_label(match.group(1), match.group(2))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end].strip()
        if label not in blocks or len(block) > len(blocks[label]):
            blocks[label] = block
    return blocks


def strip_label(block: str, label: str) -> str:
    kind, number = label.split("-")
    pattern = rf"(?mi)^\s*(?:Problem\s+)?{kind}\s*[-–— ]\s*{number}\b[\.:]?\s*"
    return re.sub(pattern, "", block, count=1).strip()


def split_statement_solution(block: str) -> tuple[str, str]:
    marker = re.search(
        r"(?mi)^\s*(Answer\b|First solution\b|Second solution\b|Third solution\b|Alternative solution\b|Solution\b|Remark\b)",
        block,
    )
    if marker:
        return block[: marker.start()].strip(), block[marker.start() :].strip()
    marker = re.search(r"(?mi)\b(Answer\b|First solution\b|Second solution\b|Third solution\b|Alternative solution\b|Solution\b)", block)
    if marker:
        return block[: marker.start()].strip(), block[marker.start() :].strip()
    return block.strip(), ""


def extract_statements_from_text(text: str, expected_labels: list[str]) -> dict[str, str]:
    result = {}
    for label, block in split_problem_blocks(text, expected_labels).items():
        cleaned = strip_label(block, label)
        statement, _ = split_statement_solution(cleaned)
        statement = re.sub(r"(?is)\bTime\s*:.*$", "", statement).strip()
        statement = re.sub(r"(?is)\bTime for questions.*$", "", statement).strip()
        statement = re.sub(r"(?is)\bEach problem is worth.*$", "", statement).strip()
        statement = re.sub(r"(?is)\bThe order of the problems.*$", "", statement).strip()
        result[label] = statement
    return result


def extract_solutions_from_text(text: str, expected_labels: list[str]) -> dict[str, str]:
    result = {}
    for label, block in split_problem_blocks(text, expected_labels).items():
        cleaned = strip_label(block, label)
        _, solution = split_statement_solution(cleaned)
        result[label] = solution or cleaned
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


def load_pdf_text(url: str | None, path: Path, refresh: bool) -> tuple[bool, str | None, str]:
    if not url:
        return False, "no url configured", ""
    ok, err, _ = fetch(url, path, refresh=refresh)
    if not ok:
        return False, err, ""
    return True, None, pdf_text(path)


def process_year(year: int, config: dict[str, object], out_dir: Path, refresh: bool = False) -> dict[str, object]:
    pdf_dir = out_dir / "pdf"
    labels: list[str] = list(config["labels"])

    file_specs = {
        "individual_problem": config.get("individual_problem_pdf_url"),
        "team_problem": config.get("team_problem_pdf_url"),
        "individual_solution": config.get("individual_solution_pdf_url"),
        "team_solution": config.get("team_solution_pdf_url"),
        "solution": config.get("solution_pdf_url"),
    }

    texts: dict[str, str] = {}
    downloads = []
    for key, url in file_specs.items():
        if not url:
            continue
        path = pdf_dir / f"memo-{year}-{key}.pdf"
        ok, err, text = load_pdf_text(str(url), path, refresh=refresh)
        texts[key] = text if ok else ""
        downloads.append(
            {
                "kind": key,
                "url": url,
                "ok": ok,
                "error": err,
                "local_pdf": str(path.relative_to(ROOT)).replace("\\", "/"),
            }
        )

    statements: dict[str, str] = {}
    for key in ["individual_problem", "team_problem", "solution", "individual_solution", "team_solution"]:
        text = texts.get(key, "")
        if not text:
            continue
        extracted = extract_statements_from_text(text, labels)
        for label, block in extracted.items():
            if label not in statements or len(block) > len(statements[label]):
                statements[label] = block

    solutions: dict[str, str] = {}
    for key in ["individual_solution", "team_solution", "solution"]:
        text = texts.get(key, "")
        if not text:
            continue
        extracted = extract_solutions_from_text(text, labels)
        for label, block in extracted.items():
            if label not in solutions or len(block) > len(solutions[label]):
                solutions[label] = block

    problems = []
    for label in labels:
        statement = statements.get(label, "")
        solution = solutions.get(label, "")
        if not statement and not solution:
            continue
        kind, num = label.split("-")
        classification = classify_problem(statement, solution)
        problems.append(
            {
                "id": f"memo-{year}-{kind.lower()}{num}",
                "year": year,
                "problem_code": label,
                "statement_en": statement,
                "solution_text_en": solution,
                "source": {
                    "page_url": config["page_url"],
                    "downloads": downloads,
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
        "page_url": config["page_url"],
        "download_count": len(downloads),
        "problem_count_extracted": len(problems),
        "problems": problems,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=min(YEAR_CONFIG))
    parser.add_argument("--end-year", type=int, default=max(YEAR_CONFIG))
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args(argv)

    out_dir: Path = args.out_dir
    year_dir = out_dir / "years"
    manifest = {
        "id": "memo-official-problems-extract",
        "created_at": date.today().isoformat(),
        "official_source": "Official MEMO archive pages and official year sites.",
        "scope": {
            "start_year": args.start_year,
            "end_year": args.end_year,
            "note": "Only years with directly downloadable official English problem/solution PDFs are included in YEAR_CONFIG.",
        },
        "years": [],
    }
    combinatorics = []
    needs_review = []

    for year in sorted(YEAR_CONFIG):
        if year < args.start_year or year > args.end_year:
            continue
        payload = process_year(year, config=YEAR_CONFIG[year], out_dir=out_dir, refresh=args.refresh)
        write_json(year_dir / f"memo-{year}-official-extract.json", payload)
        manifest["years"].append(
            {
                "year": year,
                "page_url": payload["page_url"],
                "download_count": payload["download_count"],
                "problem_count_extracted": payload["problem_count_extracted"],
            }
        )
        for problem in payload["problems"]:
            compact = {
                "id": problem["id"],
                "year": problem["year"],
                "problem_code": problem["problem_code"],
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

    write_json(out_dir / "memo-official-source-manifest.json", manifest)
    write_json(
        out_dir / "memo-official-combinatorics.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "MEMO problems with combinatorics classification candidate",
            "count": len(combinatorics),
            "problems": combinatorics,
        },
    )
    write_json(
        out_dir / "memo-official-needs-review.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "MEMO problems with ambiguous combinatorics or graph-like signals",
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

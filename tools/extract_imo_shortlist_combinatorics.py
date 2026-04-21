#!/usr/bin/env python3
"""Extract IMO Shortlist combinatorics records from official PDFs.

This is an extraction aid, not a database-card generator. It downloads official
shortlist PDFs, extracts C-problems into JSON, and writes a compact graph-related
candidate catalogue for later manual import.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "import_batches" / "extracted" / "imo_shortlist"
OFFICIAL_BASE = "https://www.imo-official.org/problems"


SUBJECT_HEADERS = (
    "Algebra",
    "Combinatorics",
    "Geometry",
    "Number Theory",
)


GRAPH_TERMS = {
    "graph": r"\bgraph(s)?\b",
    "vertex": r"\bvertices\b|\bvertex\b",
    "edge": r"\bedges?\b",
    "tree": r"\btrees?\b",
    "forest": r"\bforests?\b",
    "path": r"\bpaths?\b",
    "cycle": r"\bcycles?\b",
    "walk": r"\bwalks?\b",
    "route": r"\broutes?\b",
    "connected": r"\bconnected\b|\bconnectivity\b",
    "component": r"\bcomponents?\b",
    "matching": r"\bmatching(s)?\b|\bmatched\b|\bpairing(s)?\b",
    "tournament": r"\btournament(s)?\b",
    "network": r"\bnetwork(s)?\b",
    "map": r"\bmaps?\b",
    "island_ferry": r"\bislands?\b|\bferr(y|ies)\b",
    "grid": r"\bgrid(s)?\b|\bchessboard(s)?\b|\bchess\s*boards?\b|\bchessb\s*oard(s)?\b|\bboard(s)?\b|\bb\s*oard(s)?\b|\blattice\b",
    "cell_adjacency": r"\badjacent\b|\badja\s*en\s*t\b|\bneighbou?ring\b|\bneighboring\b|\bshare a side\b|\bcommon side\b|\bside-adjacent\b",
    "domino_polyomino": r"\bdomino(es)?\b|\btromino(es)?\b|\bpolyomino(es)?\b|\btile(s|d|ing)?\b",
    "knight": r"\bknights?\b|\bknigh\s*ts?\b",
    "coloring": r"\bcolou?r(ed|ing)?\b|\bpaint(ed|ing)?\b",
    "complete_graph_language": r"\beach pair\b|\bevery pair\b|\bbetween each pair\b",
    "hamiltonian": r"\bHamiltonian\b|\bvisit all .* exactly once\b",
}


EXPLICIT_GRAPH_TERMS = {
    "graph",
    "tree",
    "forest",
    "path",
    "cycle",
    "walk",
    "route",
    "matching",
    "tournament",
    "network",
    "island_ferry",
    "hamiltonian",
}

GRID_GRAPH_TERMS = {
    "cell_adjacency",
    "domino_polyomino",
    "knight",
    "grid",
}


KNOWN_DECISION_OVERRIDES = {
    "imo-2024-sl-c1": ("skipped", "Known 2024 manual pass: graph connection is too weak."),
    "imo-2024-sl-c2": ("skipped", "Known 2024 manual pass: graph connection is too weak."),
    "imo-2024-sl-c5": ("skipped", "Known 2024 manual pass: tree comment/model is not central enough."),
    "imo-2024-sl-c6": ("skipped", "Known 2024 manual pass: graph connection is too weak."),
    "imo-2024-sl-c7": ("skipped", "Known 2024 manual pass: no meaningful graph model."),
}


def clean_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "´": "-",
        "ˆ": "x",
        "ě": ">=",
        "ď": "<=",
        "ą": ">",
        "ă": "<",
        "Ñ": "->",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def compact_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def download(url: str, path: Path, refresh: bool = False) -> tuple[bool, str | None]:
    if path.exists() and not refresh:
        return True, None
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=60) as response:
            data = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        return False, str(exc)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True, None


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    pages = []
    for page_no, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        pages.append(f"\n[[PAGE {page_no}]]\n{page_text}")
    text = "\n".join(pages)
    if text.count("/C") + text.count("/D") > 200:
        try:
            import fitz  # type: ignore

            doc = fitz.open(str(path))
            text = "\n".join(
                f"\n[[PAGE {page_no}]]\n{page.get_text()}"
                for page_no, page in enumerate(doc, start=1)
            )
        except Exception:
            pass
    return clean_text(text)


def split_problem_solution_text(text: str) -> tuple[str, str]:
    candidates = [
        match.start()
        for match in re.finditer(r"(?m)^Solutions\s*$", text)
    ]
    if not candidates:
        candidates = [
            match.start()
            for match in re.finditer(r"Shortlisted problems\s*[–-]\s*solutions", text, re.I)
        ]
    if not candidates:
        return text, ""
    split_at = candidates[0]
    return text[:split_at], text[split_at:]


def find_combinatorics_section(text: str) -> str:
    starts = [m.end() for m in re.finditer(r"(?m)^Combinatorics\s*$", text)]
    best = ""
    for start in starts:
        end = len(text)
        for header in SUBJECT_HEADERS:
            if header == "Combinatorics":
                continue
            m = re.search(rf"(?m)^{re.escape(header)}\s*$", text[start:])
            if m:
                end = min(end, start + m.start())
        section = text[start:end].strip()
        if len(section) > len(best):
            best = section
    return best


def find_c_label_region(text: str) -> str:
    start_match = re.search(r"(?<![A-Za-z0-9])C\s*1\s*\.?\s*(?=[A-Z\n])", text)
    if not start_match:
        return ""
    start = start_match.start()
    end = len(text)
    for prefix in ("G", "N"):
        end_match = re.search(rf"(?<![A-Za-z0-9]){prefix}\s*1\s*\.?\s*(?=[A-Z\n])", text[start_match.end():])
        if end_match:
            end = min(end, start_match.end() + end_match.start())
    return text[start:end].strip()


def extract_c_blocks(section: str) -> dict[str, str]:
    label_pattern = re.compile(
        r"^\s*C\s*(\d+)\s*\.?\s*$"
        r"|^\s*C\s*(\d+)\s+(?=[A-Z]{2,4}\s+\()"
        r"|(?<![A-Za-z0-9])C\s*(\d+)\s*\.\s*",
        re.M,
    )
    matches = list(label_pattern.finditer(section))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        number = match.group(1) or match.group(2) or match.group(3)
        if number is None:
            continue
        label = f"C{int(number)}"
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        block = section[start:end].strip()
        if label not in blocks or len(block) > len(blocks[label]):
            blocks[label] = block
    return blocks


def strip_label(block: str, label: str) -> str:
    number = label[1:]
    block = re.sub(rf"(?m)^\s*C\s*{number}\s*\.?\s*$\s*", "", block, count=3)
    block = re.sub(rf"(?m)^\s*C\s*{number}\s+(?=[A-Z]{{2,4}}\s+\()", "", block, count=3)
    block = re.sub(rf"(?<![A-Za-z0-9])C\s*{number}\s*\.\s*", "", block, count=3)
    return block.strip()


def extract_country(statement: str) -> str | None:
    prefix = re.match(r"^\s*[A-Z]{2,4}\s+\(([A-Za-z][A-Za-z .,&/-]{1,80})\)", statement)
    if prefix:
        return prefix.group(1).strip()
    matches = re.findall(r"\(([A-Za-z][A-Za-z .,&/-]{1,80})\)", statement)
    if not matches:
        return None
    country = matches[-1].strip()
    if len(country.split()) > 8:
        return None
    return country


def remove_country(statement: str) -> str:
    statement = re.sub(r"\n?\([A-Za-z][A-Za-z .,&/-]{1,80}\)\s*$", "", statement.strip()).strip()
    statement = re.sub(r"^\s*[A-Z]{2,4}\s+\([A-Za-z][A-Za-z .,&/-]{1,80}\)\s*", "", statement).strip()
    return statement


def matched_terms(text: str) -> list[str]:
    found = []
    for label, pattern in GRAPH_TERMS.items():
        if re.search(pattern, text, re.I | re.S):
            found.append(label)
    return found


def evidence_snippets(text: str, terms: list[str], limit: int = 4) -> list[str]:
    snippets = []
    seen = set()
    for term in terms:
        pattern = GRAPH_TERMS[term]
        for match in re.finditer(pattern, text, re.I | re.S):
            start = max(0, match.start() - 130)
            end = min(len(text), match.end() + 130)
            snippet = compact_text(text[start:end])
            if snippet not in seen:
                snippets.append(snippet)
                seen.add(snippet)
            break
        if len(snippets) >= limit:
            break
    return snippets


def graph_decision(statement: str, solution: str) -> dict[str, object]:
    statement_terms = matched_terms(statement)
    solution_terms = matched_terms(solution)
    all_terms = sorted(set(statement_terms + solution_terms))
    explicit = sorted(set(all_terms) & EXPLICIT_GRAPH_TERMS)
    grid_like = sorted(set(all_terms) & GRID_GRAPH_TERMS)

    if explicit and statement_terms:
        decision = "candidate"
        strength = "statement_or_explicit_graph_signal"
    elif explicit and solution_terms:
        decision = "candidate"
        strength = "central_solution_possible"
    elif len(grid_like) >= 2 or ("cell_adjacency" in grid_like and "grid" in grid_like):
        decision = "candidate"
        strength = "graph_like_statement"
    elif all_terms:
        decision = "needs_review"
        strength = "graph_like_or_weak_signal"
    else:
        decision = "skipped"
        strength = "none"

    reason = "Matched graph terms: " + ", ".join(all_terms) if all_terms else "No graph or graph-like terms matched."
    return {
        "decision": decision,
        "graph_signal": {
            "in_statement": bool(statement_terms),
            "in_solution": bool(solution_terms),
            "strength": strength,
            "matched_terms": all_terms,
            "reason": reason,
        },
        "evidence": evidence_snippets(statement + "\n" + solution, all_terms),
    }


@dataclass
class YearResult:
    year: int
    ok: bool
    error: str | None
    records: list[dict[str, object]]


def process_year(year: int, pdf_dir: Path, refresh: bool = False) -> YearResult:
    url = f"{OFFICIAL_BASE}/IMO{year}SL.pdf"
    pdf_path = pdf_dir / f"IMO{year}SL.pdf"
    ok, error = download(url, pdf_path, refresh=refresh)
    if not ok:
        return YearResult(year=year, ok=False, error=error, records=[])

    text = pdf_text(pdf_path)
    problems_text, solutions_text = split_problem_solution_text(text)
    problem_section = find_combinatorics_section(problems_text)
    solution_section = find_combinatorics_section(solutions_text)
    problem_c = extract_c_blocks(problem_section)
    solution_c = extract_c_blocks(solution_section)
    if not problem_c:
        problem_c = extract_c_blocks(find_c_label_region(problems_text))
    if not solution_c:
        solution_c = extract_c_blocks(find_c_label_region(solutions_text))

    records = []
    labels = sorted(set(problem_c) | set(solution_c), key=lambda item: int(item[1:]))
    for label in labels:
        statement_raw = strip_label(problem_c.get(label, ""), label)
        solution_raw = strip_label(solution_c.get(label, ""), label)
        country = extract_country(statement_raw)
        statement = remove_country(statement_raw)
        decision = graph_decision(statement, solution_raw)
        record = {
            "id": f"imo-{year}-sl-{label.lower()}",
            "year": year,
            "shortlist_id": label,
            "source": {
                "source_id": f"src-imo-{year}-shortlist",
                "pdf_url": url,
                "local_pdf": str(pdf_path.relative_to(ROOT)).replace("\\", "/"),
            },
            "country": country,
            "statement_en": statement,
            "solution_text_en": solution_raw,
            **decision,
        }
        override = KNOWN_DECISION_OVERRIDES.get(record["id"])
        if override:
            record["decision"] = override[0]
            record["decision_reason_override"] = override[1]
        records.append(record)
    return YearResult(year=year, ok=True, error=None, records=records)


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=2006)
    parser.add_argument("--end-year", type=int, default=2024)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args(argv)

    out_dir: Path = args.out_dir
    pdf_dir = out_dir / "pdf"
    year_dir = out_dir / "years"

    manifest = {
        "id": "imo-shortlist-combinatorics-2006-2024-extract",
        "created_at": date.today().isoformat(),
        "official_source": "https://www.imo-official.org/problems.aspx",
        "scope": {
            "start_year": args.start_year,
            "end_year": args.end_year,
            "subject": "Combinatorics (C*)",
            "note": "Official IMO Shortlist PDFs only; extraction is English source text, not final Russian card text.",
        },
        "years": [],
    }
    graph_candidates = []
    review_items = []

    for year in range(args.start_year, args.end_year + 1):
        result = process_year(year, pdf_dir, refresh=args.refresh)
        year_entry = {
            "year": year,
            "official_shortlist_pdf": result.ok,
            "pdf_url": f"{OFFICIAL_BASE}/IMO{year}SL.pdf",
            "error": result.error,
            "problem_count": len(result.records),
        }
        manifest["years"].append(year_entry)
        if not result.ok:
            continue

        year_payload = {
            "year": year,
            "source_ids": [f"src-imo-{year}-shortlist"],
            "availability": {"official_shortlist_pdf": True},
            "problems": result.records,
        }
        write_json(year_dir / f"imo-{year}-combinatorics-extract.json", year_payload)

        for record in result.records:
            decision = record["decision"]
            compact = {
                "id": record["id"],
                "year": record["year"],
                "shortlist_id": record["shortlist_id"],
                "country": record["country"],
                "source": record["source"],
                "statement_en": record["statement_en"],
                "graph_signal": record["graph_signal"],
                "decision": decision,
                "evidence": record["evidence"],
            }
            if decision == "candidate":
                graph_candidates.append(compact)
            elif decision == "needs_review":
                review_items.append(compact)

    write_json(out_dir / "imo-shortlist-combinatorics-source-manifest.json", manifest)
    write_json(
        out_dir / "imo-shortlist-combinatorics-graph-candidates.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "IMO Shortlist C-problems with strong graph signals",
            "count": len(graph_candidates),
            "problems": graph_candidates,
        },
    )
    write_json(
        out_dir / "imo-shortlist-combinatorics-needs-review.json",
        {
            "created_at": date.today().isoformat(),
            "scope": "IMO Shortlist C-problems with weak or graph-like signals",
            "count": len(review_items),
            "problems": review_items,
        },
    )

    print(f"wrote {out_dir}")
    print(f"graph candidates: {len(graph_candidates)}")
    print(f"needs review: {len(review_items)}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main(sys.argv[1:]))

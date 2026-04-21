#!/usr/bin/env python3
"""Extract combinatorics from remaining early IMO years.

Policy:
- For years where a Kalva shortlist page is available and the year has not
  already been covered by the earlier secondary shortlist extractor, use that
  shortlist page.
- Also read the actual IMO PDF for these years, because Kalva omits the
  problems used in the olympiad.
- For years without an available shortlist page, fall back to the actual IMO.

The classifier is intentionally conservative-but-auditable: every selected
record carries a short reason and a review status.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from datetime import date
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "import_batches" / "extracted" / "imo_remaining_combinatorics"

ALREADY_COVERED_SHORTLIST_YEARS = set(range(1993, 1997)) | set(range(1998, 2006))
NO_IMO_YEARS = {1980}
ALL_YEARS = [year for year in range(1959, 1993) if year not in NO_IMO_YEARS] + [1997]


def clean(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\u2212": "-",
        "\u00a0": " ",
        "": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def compact(text: str) -> str:
    text = clean(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def fetch(url: str, path: Path | None = None) -> tuple[bool, str | None, bytes | None]:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=45) as response:
            data = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        return False, str(exc), None
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return True, None, data


def strip_html(html: str) -> str:
    html = re.sub(r"<script\b.*?</script>", "", html, flags=re.I | re.S)
    html = re.sub(r"<style\b.*?</style>", "", html, flags=re.I | re.S)
    html = re.sub(r"<img[^>]*>", " ", html, flags=re.I)
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    html = re.sub(r"</p>|</div>|</h[1-6]>", "\n", html, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    return clean(unescape(text))


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    return clean("\n".join(f"\n[[PAGE {i}]]\n{page.extract_text() or ''}" for i, page in enumerate(reader.pages, 1)))


def split_numbered(text: str, max_number: int = 40) -> list[tuple[int, str]]:
    pattern = re.compile(r"(?m)^\s*(\d{1,2})\.\s+")
    matches = [m for m in pattern.finditer(text) if 1 <= int(m.group(1)) <= max_number]
    records: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = compact(text[match.end():end])
        block = re.sub(r"\s*Note: problems.*$", "", block, flags=re.I)
        block = re.sub(r"\s*Shortlist home.*$", "", block, flags=re.I)
        if len(block) >= 35:
            records.append((number, block))
    return records


def extract_kalva_shortlist(year: int) -> dict[str, object]:
    yy = str(year)[-2:]
    url = f"https://prase.cz/kalva/short/sh{yy}.html"
    ok, error, data = fetch(url)
    if not ok or data is None:
        return {"year": year, "ok": False, "source_type": "kalva_shortlist", "url": url, "error": error, "problems": []}
    text = strip_html(data.decode("latin1", errors="replace"))
    problems = []
    for number, statement in split_numbered(text):
        problems.append(
            {
                "id": f"imo-{year}-sl-kalva-{number}",
                "year": year,
                "shortlist_id": str(number),
                "statement_en": statement,
                "source": {
                    "source_id": f"src-kalva-imo-{year}-shortlist",
                    "url": url,
                    "source_note": "Kalva early shortlist page; unofficial secondary source and omits problems used in the IMO.",
                },
                "decision": "extracted",
            }
        )
    return {"year": year, "ok": bool(problems), "source_type": "kalva_shortlist", "url": url, "error": None if problems else "No numbered problems parsed", "problems": problems}


def extract_imo_year(year: int) -> dict[str, object]:
    url = f"https://imomath.com/othercomp/I/Imo{year}.pdf"
    pdf_path = OUT / "pdf" / f"Imo{year}.pdf"
    ok, error, _ = fetch(url, pdf_path)
    if not ok:
        return {"year": year, "ok": False, "source_type": "imomath_imo_pdf", "url": url, "error": error, "problems": []}
    text = pdf_text(pdf_path)
    problems = []
    for number, statement in split_numbered(text, max_number=6):
        problems.append(
            {
                "id": f"imo-{year}-p{number}",
                "year": year,
                "shortlist_id": f"IMO {number}",
                "statement_en": statement,
                "source": {
                    "source_id": f"src-imomath-imo-{year}",
                    "url": url,
                    "local_pdf": str(pdf_path.relative_to(ROOT)).replace("\\", "/"),
                    "source_note": "IMOmath IMO Compendium PDF for the actual IMO problems.",
                },
                "decision": "extracted",
            }
        )
    return {"year": year, "ok": bool(problems), "source_type": "imomath_imo_pdf", "url": url, "error": None if problems else "No IMO problems parsed", "problems": problems}


COMBINATORICS_PATTERNS: list[tuple[str, str]] = [
    ("graph", r"\bgraph\b|\bvertices\b|\bvertex\b|\bdegree\b|\bjoined to\b|\bclique\b|\bedges drawn\b"),
    ("coloring", r"\bcolou?r(ed|ing)?\b|\bpaint(ed|ing)?\b|\bred\b|\bblue\b|\bblack\b|\bwhite\b"),
    ("grid_board", r"\bgrid\b|\bchessboard\b|\bboard\b|\bcell(s)?\b|\brow\b|\bcolumn\b|\bmatrix\b"),
    ("counting_arrangements", r"\bnumber of ways\b|\bhow many ways\b|\barrange(d|ment)?\b|\bpermutation\b|\bsubsequence\b|\bsubset\b|\bpartition(ed)? into\b"),
    ("finite_set_extremal", r"\bfinite set\b|\bset of (?:positive )?integers\b|\bset of numbers\b|\bn points\b|\bpoints in the plane\b|\bno three\b"),
    ("matching_assignment", r"\bmatching\b|\bpartner\b|\bdance\b|\bpairs?\b"),
    ("tiling_polyomino", r"\bdomino\b|\btromino\b|\btile(d|s|ing)?\b"),
    ("pigeonhole_discrete", r"\bintegers?\b.*\bchoose\b|\bchoose\b.*\bintegers?\b"),
]

EXCLUDE_PATTERNS = [
    r"\btriangle\b.*\bcircle\b",
    r"\btetrahedron\b|\bcircumsphere\b|\bsphere\b tangent\b",
    r"\bpolynomial\b",
    r"\bfunction f\b|\bfunctions? f\b",
    r"\bpositive integers?\b.*\bprime\b",
]


MANUAL_INCLUDE: dict[str, str] = {
    "imo-1960-p6": "Combinatorial geometry / finite configuration problem.",
    "imo-1961-p4": "Party/Ramsey-style acquaintance problem.",
    "imo-1962-p6": "Tournament scheduling problem.",
    "imo-1964-p4": "Counting all subsets of a finite set.",
    "imo-1966-p6": "Combinatorial geometry: drawing segments among points.",
    "imo-1967-p5": "Permutation/ordering problem.",
    "imo-1968-p4": "Finite set of positive integers with subset-sum obstruction.",
    "imo-1969-p3": "Chessboard colouring/covering problem.",
    "imo-1970-p6": "Combinatorial geometry on all triangles determined by 100 points.",
    "imo-1971-p3": "Counting/ordering problem on integer sequences.",
    "imo-1972-p1": "Set of ten distinct two-digit numbers with divisibility property.",
    "imo-1972-p6": "Geometric graph/segment intersection problem.",
    "imo-1974-p4": "Partition of numbers into subsets with equal sums.",
    "imo-1975-p2": "Finite set of points with distance condition.",
    "imo-1975-p6": "Permutation of positive integers with inequalities.",
    "imo-1976-p1": "Sequence/subsequence selection problem.",
    "imo-1977-p6": "Finite set/covering inequality.",
    "imo-1978-p6": "Counting functions with divisibility constraints.",
    "imo-1979-p6": "Colouring of the plane / monochromatic rectangle problem.",
    "imo-1991-sl-kalva-8": "Combinatorial geometry: hitting all triangles determined by n points.",
    "imo-1991-sl-kalva-9": "Explicit graph theory problem.",
    "imo-1991-sl-kalva-13": "Subset sums modulo n.",
    "imo-1991-sl-kalva-24": "Permutation with cyclic alternating sums.",
    "imo-1992-p3": "Ramsey/edge-colouring problem on K9.",
    "imo-1992-p5": "Finite set/projection counting inequality.",
    "imo-1997-p1": "Chessboard colouring on the infinite grid.",
    "imo-1997-p4": "Matrix existence problem.",
    "imo-1997-p6": "Counting partitions into powers of two.",
}

MANUAL_EXCLUDE: set[str] = {
    "imo-1963-p2",
    "imo-1963-p3",
    "imo-1963-p6",
    "imo-1966-p3",
    "imo-1967-p1",
    "imo-1970-p3",
    "imo-1970-p5",
    "imo-1971-p2",
    "imo-1971-p4",
    "imo-1971-p5",
    "imo-1971-p6",
    "imo-1973-p2",
    "imo-1973-p5",
    "imo-1974-p6",
    "imo-1976-p3",
    "imo-1976-p5",
    "imo-1977-p1",
    "imo-1977-p2",
    "imo-1977-p3",
    "imo-1978-p1",
    "imo-1978-p2",
    "imo-1978-p3",
    "imo-1979-p2",
    "imo-1981-sl-kalva-2",
    "imo-1981-sl-kalva-3",
    "imo-1981-sl-kalva-4",
    "imo-1981-sl-kalva-6",
    "imo-1981-sl-kalva-10",
    "imo-1981-sl-kalva-11",
    "imo-1981-sl-kalva-12",
    "imo-1982-sl-kalva-11",
    "imo-1983-sl-kalva-18",
    "imo-1984-sl-kalva-19",
    "imo-1984-sl-kalva-20",
    "imo-1984-p3",
    "imo-1984-p5",
    "imo-1985-sl-kalva-9",
    "imo-1985-sl-kalva-14",
    "imo-1986-sl-kalva-17",
    "imo-1986-sl-kalva-20",
    "imo-1986-p2",
    "imo-1986-p4",
    "imo-1987-sl-kalva-3",
    "imo-1987-sl-kalva-10",
    "imo-1987-sl-kalva-12",
    "imo-1990-sl-kalva-19",
    "imo-1991-sl-kalva-3",
    "imo-1991-sl-kalva-22",
    "imo-1992-sl-kalva-3",
    "imo-1992-sl-kalva-2",
    "imo-1992-sl-kalva-14",
    "imo-1992-sl-kalva-18",
    "imo-1992-sl-kalva-5",
    "imo-1992-sl-kalva-7",
    "imo-1992-sl-kalva-11",
    "imo-1997-sl-kalva-12",
    "imo-1997-sl-kalva-20",
    "imo-1997-sl-kalva-25",
    "imo-1997-p3",
    "imo-1997-p5",
    "imo-1997-sl-kalva-5",
    "imo-1997-sl-kalva-7",
    "imo-1997-sl-kalva-9",
    "imo-1997-sl-kalva-23",
}


def classify(problem: dict[str, object]) -> tuple[bool, str, list[str]]:
    pid = str(problem["id"])
    text = str(problem["statement_en"])
    low = text.lower()
    if pid in MANUAL_INCLUDE:
        return True, "manual_include", [MANUAL_INCLUDE[pid]]
    if pid in MANUAL_EXCLUDE:
        return False, "manual_exclude", ["Manual exclusion: not primarily combinatorics."]

    reasons = []
    for label, pattern in COMBINATORICS_PATTERNS:
        if re.search(pattern, low, flags=re.I | re.S):
            reasons.append(label)

    if not reasons:
        return False, "not_selected", []

    exclude_hits = [pattern for pattern in EXCLUDE_PATTERNS if re.search(pattern, low, flags=re.I | re.S)]
    if exclude_hits and len(reasons) == 1 and reasons[0] in {"finite_set_extremal", "pigeonhole_discrete"}:
        return False, "excluded_by_geometry_algebra_filter", reasons + exclude_hits

    return True, "heuristic_selected_needs_review", reasons


@dataclass
class YearResult:
    year: int
    shortlist: dict[str, object] | None
    imo: dict[str, object] | None
    selected: list[dict[str, object]]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "years").mkdir(exist_ok=True)

    results: list[YearResult] = []
    for year in ALL_YEARS:
        shortlist = None
        if year not in ALREADY_COVERED_SHORTLIST_YEARS:
            trial = extract_kalva_shortlist(year)
            if trial["ok"]:
                shortlist = trial
        imo = extract_imo_year(year)

        source_records = []
        if shortlist is not None:
            source_records.extend(shortlist["problems"])
        else:
            source_records.extend(imo["problems"])
        if shortlist is not None and imo["ok"]:
            source_records.extend(imo["problems"])

        selected = []
        seen_statements: set[str] = set()
        for record in source_records:
            keep, status, reasons = classify(record)
            if not keep:
                continue
            fingerprint = compact(str(record["statement_en"])).lower()[:180]
            if fingerprint in seen_statements:
                continue
            seen_statements.add(fingerprint)
            item = dict(record)
            item["classification_status"] = status
            item["classification_reason"] = reasons
            selected.append(item)

        payload = {
            "year": year,
            "sources_used": {
                "shortlist": None if shortlist is None else {
                    "source_type": shortlist["source_type"],
                    "url": shortlist["url"],
                    "problem_count": len(shortlist["problems"]),
                    "official": False,
                },
                "imo": {
                    "source_type": imo["source_type"],
                    "url": imo["url"],
                    "problem_count": len(imo["problems"]),
                    "official": False,
                    "ok": imo["ok"],
                    "error": imo["error"],
                },
            },
            "selection_policy": "Use available Kalva shortlist for uncovered years; otherwise fall back to actual IMO. Add actual IMO problems when shortlist pages omit used problems.",
            "problems": selected,
        }
        (OUT / "years" / f"imo-{year}-remaining-combinatorics-extract.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        results.append(YearResult(year, shortlist, imo, selected))

    manifest = {
        "id": "imo-remaining-combinatorics-extract",
        "created_at": date.today().isoformat(),
        "scope": "Remaining early years not covered by official/secondary C-shortlist extraction; Kalva shortlist when available, actual IMO otherwise.",
        "sources_checked": [
            "Kalva early IMO shortlist pages https://prase.cz/kalva/short/shYY.html",
            "IMOmath actual IMO PDFs https://imomath.com/othercomp/I/ImoYYYY.pdf",
        ],
        "years": [
            {
                "year": result.year,
                "shortlist_found": result.shortlist is not None,
                "imo_found": bool(result.imo and result.imo["ok"]),
                "selected_combinatorics_count": len(result.selected),
                "source_mode": "shortlist_plus_imo_used_problem_fallback" if result.shortlist is not None else "imo_fallback",
            }
            for result in results
        ],
    }
    (OUT / "imo-remaining-combinatorics-source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    all_problems = []
    for result in results:
        all_problems.extend(result.selected)
    (OUT / "imo-remaining-combinatorics-all.json").write_text(
        json.dumps(
            {
                "id": "imo-remaining-combinatorics-all",
                "created_at": date.today().isoformat(),
                "problem_count": len(all_problems),
                "problems": all_problems,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print("years written:", len(results))
    print("shortlist years:", [r.year for r in results if r.shortlist is not None])
    print("total selected:", sum(len(r.selected) for r in results))
    print("empty years:", [r.year for r in results if not r.selected])
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())

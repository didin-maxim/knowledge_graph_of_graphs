#!/usr/bin/env python3
"""Extract early IMO Shortlist combinatorics from secondary archives.

These are not official IMO PDFs. The main source used here is an AoPS-mirrored
PDF collection hosted on allameamini.org. 2002 is available on AoPS Wiki, so it
is extracted from the wiki pages instead of the missing mirror PDF.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from datetime import date
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "import_batches" / "extracted" / "imo_shortlist_secondary"

PDF_YEARS = [1991, *range(1993, 2002), *range(2003, 2006)]
PDF_URL = "https://www.allameamini.org/wp-content/uploads/2019/03/International_Competitions-IMO_Shortlist-{year}-17.pdf"


def clean(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "“": '"',
        "”": '"',
        "’": "'",
        "´": "-",
        "≤": "<=",
        "≥": ">=",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


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


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    text = "\n".join(f"\n[[PAGE {i}]]\n{page.extract_text() or ''}" for i, page in enumerate(reader.pages, 1))
    return clean(text)


def section_between(text: str, start_header: str, end_headers: list[str]) -> str:
    matches = list(re.finditer(rf"(?im)^\s*{re.escape(start_header)}\s*$", text))
    if not matches:
        matches = list(re.finditer(rf"(?i)\b{re.escape(start_header)}\b", text))
    if not matches:
        return ""
    start = matches[-1].end()
    end = len(text)
    for header in end_headers:
        m = re.search(rf"(?im)^\s*{re.escape(header)}\s*$", text[start:])
        if not m:
            m = re.search(rf"(?i)\b{re.escape(header)}\b", text[start:])
        if m:
            end = min(end, start + m.start())
    return text[start:end].strip()


def split_numbered(section: str) -> list[dict[str, object]]:
    pattern = re.compile(r"(?m)^\s*(\d+)\s+(?![<>=])")
    raw_matches = []
    expected = 1
    for match in pattern.finditer(section):
        number = int(match.group(1))
        if number == expected:
            raw_matches.append(match)
            expected += 1
    matches = raw_matches
    records = []
    for index, match in enumerate(matches):
        number = int(match.group(1))
        # Avoid page numbers and formula line numbers by requiring a plausible shortlist id.
        if not 1 <= number <= 20:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        block = section[match.end():end].strip()
        if len(block) < 30:
            continue
        records.append({"shortlist_id": f"C{number}", "statement_en": clean(block)})
    # Keep first occurrence of each problem number.
    unique = {}
    for rec in records:
        unique.setdefault(rec["shortlist_id"], rec)
    return [unique[key] for key in sorted(unique, key=lambda x: int(x[1:]))]


def extract_pdf_year(year: int) -> dict[str, object]:
    url = PDF_URL.format(year=year)
    pdf_path = OUT / "pdf" / f"secondary-IMO{year}SL.pdf"
    ok, error, _ = fetch(url, pdf_path)
    if not ok:
        return {"year": year, "ok": False, "source_type": "secondary_pdf", "url": url, "error": error, "problems": []}
    text = pdf_text(pdf_path)
    section = section_between(text, "Combinatorics", ["Geometry", "Number Theory", "Number theory", "NT"])
    source_type = "secondary_pdf"
    classification_status = "combinatorics_section"
    if not section:
        section = section_between(text, "NT, Combs", ["Algebra", "Geometry"])
        if section:
            source_type = "secondary_pdf_mixed_nt_combs"
            classification_status = "mixed_number_theory_and_combinatorics_section"
    problems = split_numbered(section)
    for rec in problems:
        rec["id"] = f"imo-{year}-sl-{rec['shortlist_id'].lower()}"
        rec["year"] = year
        rec["source"] = {
            "source_id": f"src-secondary-imo-{year}-shortlist",
            "url": url,
            "local_pdf": str(pdf_path.relative_to(ROOT)).replace("\\", "/"),
            "source_note": "Unofficial/secondary mirror of an AoPS shortlist PDF.",
        }
        rec["decision"] = "extracted"
        rec["classification_status"] = classification_status
    return {"year": year, "ok": bool(problems), "source_type": source_type, "url": url, "error": None if problems else "Combinatorics section not parsed", "problems": problems}


def strip_html(html: str) -> str:
    html = re.sub(r"<script\b.*?</script>", "", html, flags=re.I | re.S)
    html = re.sub(r"<style\b.*?</style>", "", html, flags=re.I | re.S)
    html = re.sub(r"<img[^>]*alt=\"([^\"]*)\"[^>]*>", r" \1 ", html, flags=re.I)
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    html = re.sub(r"</p>|</div>|</h[1-6]>", "\n", html, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    return clean(unescape(text))


def extract_aops_problem(year: int, label: str) -> dict[str, object] | None:
    title = quote(f"{year}_IMO_Shortlist_Problems/{label}", safe="/")
    url = f"https://artofproblemsolving.com/wiki/index.php?title={title}"
    ok, error, data = fetch(url)
    if not ok or data is None:
        return None
    text = strip_html(data.decode("utf-8", errors="replace"))
    m = re.search(r"(?is)\bProblem\b(.*?)(?:\bSolution\b|\bResources\b|Retrieved from)", text)
    if not m:
        return None
    statement = compact(m.group(1))
    if len(statement) < 30:
        return None
    return {
        "id": f"imo-{year}-sl-{label.lower()}",
        "year": year,
        "shortlist_id": label,
        "statement_en": statement,
        "source": {
            "source_id": f"src-aops-imo-{year}-shortlist",
            "url": url,
            "source_note": "AoPS Wiki page; unofficial secondary source.",
        },
        "decision": "extracted",
    }


def extract_aops_year(year: int) -> dict[str, object]:
    records = []
    for index in range(1, 15):
        rec = extract_aops_problem(year, f"C{index}")
        if rec is not None:
            records.append(rec)
    return {
        "year": year,
        "ok": bool(records),
        "source_type": "aops_wiki",
        "url": f"https://artofproblemsolving.com/wiki/index.php/{year}_IMO_Shortlist_Problems",
        "error": None if records else "No C pages parsed from AoPS Wiki",
        "problems": records,
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    results = []
    for year in PDF_YEARS:
        results.append(extract_pdf_year(year))
    # The allameamini mirror URL for 2002 is missing, but AoPS Wiki has C pages.
    results.append(extract_aops_year(2002))
    results.sort(key=lambda item: item["year"])

    manifest = {
        "id": "imo-shortlist-secondary-combinatorics-early",
        "created_at": date.today().isoformat(),
        "scope": "Unofficial/secondary early IMO Shortlist combinatorics extraction before official PDF era.",
        "sources_checked": [
            "allameamini.org AoPS-mirror PDFs",
            "AoPS Wiki C-problem pages",
        ],
        "years": [
            {
                "year": result["year"],
                "ok": result["ok"],
                "source_type": result["source_type"],
                "url": result["url"],
                "error": result["error"],
                "problem_count": len(result["problems"]),
            }
            for result in results
        ],
    }
    (OUT / "years").mkdir(exist_ok=True)
    for result in results:
        if result["ok"]:
            payload = {
                "year": result["year"],
                "source_type": result["source_type"],
                "source_url": result["url"],
                "official": False,
                "problems": result["problems"],
            }
            (OUT / "years" / f"imo-{result['year']}-combinatorics-secondary-extract.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    (OUT / "imo-shortlist-secondary-source-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("years parsed:", [r["year"] for r in results if r["ok"]])
    print("failed:", [(r["year"], r["error"]) for r in results if not r["ok"]])
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())

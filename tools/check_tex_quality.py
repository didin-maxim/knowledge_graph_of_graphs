import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from lib import ROOT

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


VISIBLE_KEYS = {
    "title",
    "text",
    "note",
    "notes",
    "source_note",
    "review_notes",
    "description",
    "comment",
    "comments",
    "caption",
    "alt",
    "label",
    "hint",
    "hints",
    "basis",
    "forward_text",
    "backward_text",
}

SKIP_KEYS = {
    "_path",
    "accepted_latex",
    "definition_id",
    "definition_ids",
    "distinct_from",
    "href",
    "id",
    "idea_ids",
    "keywords",
    "path",
    "problem_id",
    "source_id",
    "source_ids",
    "standard_idea_id",
    "standard_idea_ids",
    "status",
    "tags",
    "url",
}

CURATED_DIRS = [
    ROOT / "data" / "problems",
    ROOT / "data" / "definitions",
    ROOT / "data" / "standard_ideas",
    ROOT / "data" / "relations",
    ROOT / "data" / "sources",
    ROOT / "data" / "comments",
]

TEXT_LETTER = r"A-Za-z0-9\u0400-\u04ff"
MATH_RE = re.compile(
    r"\\\[(?:.|\n)*?\\\]|\\\((?:.|\n)*?\\\)|\$\$(?:.|\n)*?\$\$|(?<!\\)\$(?:.|\n)*?(?<!\\)\$"
)
MATH_FRAGMENT_RE = re.compile(
    r"(?P<dd>\$\$(?P<dd_tex>.*?)\$\$)|"
    r"(?P<bracket>\\\[(?P<bracket_tex>.*?)\\\])|"
    r"(?P<paren>\\\((?P<paren_tex>.*?)\\\))",
    re.DOTALL,
)
CODE_SPAN_RE = re.compile(r"`[^`\n]+`")
URL_RE = re.compile(r"https?://\S+")
FILE_RE = re.compile(r"\b[\w.-]+(?:[/\\][\w.-]+)+\b|\b[\w.-]+\.(?:tex|zip|pdf|html|yaml|json)\b")

QUESTION_RUN_RE = re.compile(r"\?{4,}")
REPLACEMENT_CHARACTER_RE = re.compile(r"\ufffd|\u043f\u0457\u0405")
MOJIBAKE_RE = re.compile(
    r"(?:\u0413[\u0402\u2018\u201a\u0192])|"
    r"(?:\u0420[\u00a0\u0402\u0403\u040b\u201a-\u201e\u2020-\u2022\u2030\u2039-\u203a\u2122])|"
    r"(?:\u0421[\u0402\u0403\u0452\u0453\u201a-\u201e\u2020-\u2022\u2030\u2039-\u203a])"
)
RAW_DOLLAR_DELIM_RE = re.compile(r"(?<!\\)\${1,2}")
DOUBLE_ESCAPED_DELIM_RE = re.compile(r"\\\\[([]")
DOUBLE_ESCAPED_TEX_RE = re.compile(
    r"\\\\(?:sqrt|frac|binom|left|right|sum|prod|lim|int|operatorname|mathbb|"
    r"le|ge|ne|to|cdot|times|alpha|beta|gamma|theta|lambda|mu|pi|infty)\b"
)
BARE_TEX_RE = re.compile(r"(?<!\\)\\[A-Za-z]+(?:\s*\([^)]*\))?")
LITERAL_NEWLINE_RE = re.compile(r"\\n(?![A-Za-z])")
RAW_SUBSUP_RE = re.compile(
    r"(?<![\w/.])(?:"
    r"[A-Za-z]+_\{[^}\n]{1,80}\}|"
    r"[A-Za-z]+_[0-9][A-Za-z0-9]*|"
    r"[A-Za-z]+_[A-Z][A-Za-z0-9]*|"
    r"[A-Za-z]_[a-z][A-Za-z0-9]*|"
    r"[a-z]{2,}_[a-z](?![a-z])|"
    r"[A-Za-z]+\^\{[^}\n]{1,80}\}|"
    r"[A-Za-z]+\^[A-Za-z0-9]+"
    r")"
)
FORMULA_TEXT_GLUE_RE = re.compile(
    rf"(?<=[{TEXT_LETTER}])\\\(|\\\)(?=[{TEXT_LETTER}])|"
    rf"(?<=[{TEXT_LETTER}])\\\[|\\\](?=[{TEXT_LETTER}])"
)
NON_PUBLIC_BRANCHES = {
    "authors",
    "difficulty",
    "editorial",
    "review_notes",
    "sources",
    "source_note",
}


def strip_math(text):
    return MATH_RE.sub(" ", str(text or ""))


def strip_code_spans(text):
    return CODE_SPAN_RE.sub(" ", str(text or ""))


def strip_non_content(text):
    text = URL_RE.sub(" ", text)
    return FILE_RE.sub(" ", text)


def iter_data_files(paths):
    if paths:
        for raw in paths:
            path = (ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw)
            if path.is_dir():
                yield from sorted(path.rglob("*.yaml"))
                yield from sorted(path.rglob("*.json"))
            else:
                yield path
        return

    for base in CURATED_DIRS:
        if base.exists():
            yield from sorted(base.rglob("*.yaml"))
            yield from sorted(base.rglob("*.json"))


def iter_visible_strings(obj, path=(), force_visible=False):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in SKIP_KEYS:
                continue
            yield from iter_visible_strings(
                value,
                path + (str(key),),
                force_visible or key in VISIBLE_KEYS,
            )
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from iter_visible_strings(value, path + (str(index),), force_visible)
    elif isinstance(obj, str) and force_visible:
        yield ".".join(path), obj


def iter_math_fragments(text):
    for match in MATH_FRAGMENT_RE.finditer(str(text or "")):
        if match.group("dd") is not None:
            yield match.group("dd_tex"), True
        elif match.group("bracket") is not None:
            yield match.group("bracket_tex"), True
        elif match.group("paren") is not None:
            yield match.group("paren_tex"), False


def check_katex_fragments(fragments):
    script = ROOT / "tools" / "parse_tex_with_katex.js"
    if not fragments or not script.exists() or shutil.which("node") is None:
        return []
    try:
        completed = subprocess.run(
            ["node", str(script)],
            input=json.dumps(fragments, ensure_ascii=False),
            text=True,
            encoding="utf-8",
            capture_output=True,
            cwd=ROOT,
            timeout=20,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return [("error", Path("tools/parse_tex_with_katex.js"), "<katex>", "katex-runner-failed", str(exc))]
    if completed.returncode:
        message = (completed.stderr or completed.stdout or "").strip()
        return [("error", Path("tools/parse_tex_with_katex.js"), "<katex>", "katex-runner-failed", message)]
    try:
        errors = json.loads(completed.stdout or "[]")
    except json.JSONDecodeError as exc:
        return [("error", Path("tools/parse_tex_with_katex.js"), "<katex>", "katex-runner-invalid-json", str(exc))]
    reports = []
    for error in errors:
        tex = str(error.get("tex", ""))
        snippet = tex[:120].replace("\n", "\\n")
        message = str(error.get("message", "")).replace("\n", " ")
        reports.append(
            (
                "error",
                ROOT / str(error.get("path", "")),
                str(error.get("place", "")),
                "katex-parse-error",
                f"{snippet}: {message}",
            )
        )
    return reports


def is_non_public_context(place):
    return any(part in NON_PUBLIC_BRANCHES for part in place.split("."))


def is_statement_context(place):
    return place.startswith("statements.")


def find_hits(text, place):
    original = str(text or "")
    scrubbed = strip_non_content(strip_code_spans(original))
    outside = strip_non_content(strip_math(scrubbed))
    outside_without_literal_newlines = LITERAL_NEWLINE_RE.sub(" ", outside)
    checks = [
        ("question-mark-run", QUESTION_RUN_RE, scrubbed),
        ("replacement-character", REPLACEMENT_CHARACTER_RE, scrubbed),
        ("mojibake-sequence", MOJIBAKE_RE, scrubbed),
        ("raw-dollar-tex-delimiter", RAW_DOLLAR_DELIM_RE, scrubbed),
        ("double-escaped-math-delimiter", DOUBLE_ESCAPED_DELIM_RE, scrubbed),
        ("double-escaped-tex-command", DOUBLE_ESCAPED_TEX_RE, scrubbed),
        ("literal-backslash-n", LITERAL_NEWLINE_RE, outside),
        ("bare-tex-command-outside-math", BARE_TEX_RE, outside_without_literal_newlines),
        ("raw-subscript-or-superscript-outside-math", RAW_SUBSUP_RE, outside),
        ("formula-text-glue", FORMULA_TEXT_GLUE_RE, scrubbed),
    ]
    if is_statement_context(place):
        checks.append(("markdown-code-span-in-statement", CODE_SPAN_RE, original))
    if is_non_public_context(place):
        checks = [
            (kind, pattern, value)
            for kind, pattern, value in checks
            if kind in {"question-mark-run", "replacement-character", "mojibake-sequence"}
        ]
    for kind, pattern, value in checks:
        for match in pattern.finditer(value):
            snippet = value[max(0, match.start() - 40) : match.end() + 40]
            yield "error", kind, snippet.replace("\n", "\\n")


def rel_path(path):
    return path.relative_to(ROOT) if path.is_absolute() and path.is_relative_to(ROOT) else path


def main():
    parser = argparse.ArgumentParser(description="Check curated visible text for P1 TeX/rendering quality issues.")
    parser.add_argument("paths", nargs="*", help="Optional files or directories to check.")
    parser.add_argument("--max-items", type=int, default=80)
    args = parser.parse_args()

    hits = []
    math_fragments = []
    for path in iter_data_files(args.paths):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            hits.append(("error", path, "", "parse-error", str(exc)))
            continue

        for place, text in iter_visible_strings(data):
            for severity, kind, snippet in find_hits(text, place):
                hits.append((severity, path, place, kind, snippet))
            for tex, display in iter_math_fragments(text):
                math_fragments.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "place": place,
                        "tex": tex,
                        "display": display,
                    }
                )

    hits.extend(check_katex_fragments(math_fragments))

    errors = [hit for hit in hits if hit[0] == "error"]
    warnings = [hit for hit in hits if hit[0] == "warning"]

    for severity, path, place, kind, snippet in hits[: args.max_items]:
        print(f"{severity.upper()} {rel_path(path)}#{place}: {kind}: {snippet}")
    if len(hits) > args.max_items:
        print(f"... {len(hits) - args.max_items} more issue(s)")

    print(f"TeX quality check: {len(errors)} errors, {len(warnings)} warnings.")
    if errors:
        print(f"ERROR: TeX quality check found {len(errors)} P1 issue(s).")
        return 1
    print("OK: TeX quality check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

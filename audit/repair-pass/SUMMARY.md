# Repair pass summary

Date: 2026-04-26

Second pass policy: fix only easy, locally reliable cases; defer source hunts and nontrivial proof reconstruction.

## Reports

| scope | done/reviewed | backlog | notes |
|---|---:|---:|---|
| IMO + classical | 10 | 21 | Five classical cards had solution status moved to `ai_checked`; five IMO flags were confirmed already OK without YAML changes. |
| International misc | 20 | 9 | Several expanded official titles were normalized; one USAMO existence-only entry was marked `needs_human_review`. |
| Kolmogorov 2002-2014 | 24 | 32 | Three statuses were moved to `ai_checked`; many older compressed summaries still need reconstruction or sources. |
| Kolmogorov 2015-2024 | 17 | 2 | Most flags were accepted as already repaired against local official archive text. |
| Russian local series | 22 | 37 | One VOSH title was normalized; most YUMT archive-card placeholders remain missing solutions. |

## Backlog by Type

| label | count |
|---|---:|
| hard_math_reconstruction | 52 |
| missing_solution | 49 |
| hard_external_source | 7 |
| false_positive_needs_human | 1 |

## Main Queues

- Kolmogorov 2002-2014: compressed official summaries needing source/OCR lookup or real proof reconstruction.
- YUMT archive-card placeholders: mostly true missing solutions.
- IMO/classical hard cases: not many, but mathematically heavier; should be handled one by one.
- International misc: several files contain literal `????` in solution text and need source-based restoration.

## Verification

Final checks from repository root:

```text
python tools/validate.py
OK: 328 problems, 296 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 370 internal routes, 349 external source URLs syntactically valid.
```

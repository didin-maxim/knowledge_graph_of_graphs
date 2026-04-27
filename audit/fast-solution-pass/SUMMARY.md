# Fast solution completeness pass

Date: 2026-04-26

This is a speed-first triage pass. Labels mean "worth checking next", not a final verdict.

## Agent Reports

| report | scope | checked | flagged | incomplete_solution | missing_solution | suspicious_too_short | source_insufficient |
|---|---:|---:|---:|---:|---:|---:|---:|
| imo-classical.md | IMO + classical | 68 files | 31 | 20 | 0 | 10 | 1 |
| international-misc.md | APMO/BMO/EGMO/MEMO/RMM/USA | 34 files, 43 solutions | 30 | 18 | 0 | 11 | 1 |
| kolmogorov-2002-2014.md | Kolmogorov 2002-2014 | 57 files | 56 | 38 | 8 | 10 | 0 |
| kolmogorov-2015-2024.md | Kolmogorov 2015-2024 | 32 files | 19 | 17 | 0 | 1 | 1 |
| russian-local.md | FYUM/UTYUM/YUMT/TC/VOSH | 137 files, 141 solutions | 60 | 1 | 36 | 23 | 0 |

## Totals

| label | count |
|---|---:|
| incomplete_solution | 94 |
| missing_solution | 44 |
| suspicious_too_short | 55 |
| source_insufficient | 3 |
| total flagged | 196 |

## Scale Estimate

The largest repair class is compressed/incomplete solutions: 94 first-pass flags. Many are probably fast to resolve if a source solution exists locally, but the label is intentionally broad and includes false positives from already-expanded files whose solution_id still says compressed.

Missing solutions are a separate backlog: 44 flags, concentrated in YUMT archive-card placeholders and Kolmogorov 2009/2014 import notes. These are source-hunting tasks rather than expansion tasks.

The 55 suspicious_too_short cases should be sampled before bulk repair. Some are likely acceptable short olympiad solutions; others are hidden incomplete proofs.

The 3 source_insufficient cases need either source import or explicit marking as external theorem/source-only cards.

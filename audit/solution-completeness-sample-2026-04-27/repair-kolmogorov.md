# Repair Kolmogorov Sample

Date: 2026-04-27

Scope: sampled serious Kolmogorov problems only:

- `kolmogorov-2008-team-olympiad-seniors-problem-7`
- `kolmogorov-2004-round3-higher-league-problem-10`
- `kolmogorov-2024-t4-independent-cutset-2n-4`

## Repaired

| Problem | Action | Notes |
| --- | --- | --- |
| `data/problems/kolmogorov/kolmogorov-2008-team-olympiad-seniors-problem-7.yaml` | Added `sol-double-counting-expanded`. | The new Russian solution is self-contained: it double-counts monochromatic length-2 paths, derives the equality case, and uses the parity impossibility of a 5-regular graph on 21 vertices. |
| `data/problems/kolmogorov/kolmogorov-2004-round3-higher-league-problem-10.yaml` | Cleaned the existing `sol-official-expanded` text. | The repair preserves the contraction-cycle proof but removes damaged fragments such as `Б-г`, replaces ambiguous quoted variables with code-formatted variables, and makes the final contradiction explicit in `G-d`. |

## Deferred

| Problem | Reason |
| --- | --- |
| `data/problems/kolmogorov/kolmogorov-2024-t4-independent-cutset-2n-4.yaml` | Deferred. The current solution cites the Chen--Yu theorem on fragile graphs. Producing a complete self-contained Russian solution would require transferring a substantial external theorem proof, so this is outside the safe scope of this repair pass. |

## Validation

- Targeted JSON parse passed for the three in-scope Kolmogorov cards.
- `python tools\validate.py` passed: `OK: 328 problems, 379 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.`
- `python tools\check_links.py` passed: `OK: 370 internal routes, 349 external source URLs syntactically valid.`

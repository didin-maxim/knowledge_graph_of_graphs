# Metadata Pass: Early Kolmogorov 2002-2007

Date: 2026-04-26

Scope: repaired early Kolmogorov cards listed in the task, plus a dedicated relation shard:
`data/relations/relations.d/metadata-pass-kolmogorov-early-links.yaml`.

## Updated cards

Aligned tags, `problem_profile`, `central_method`, local idea tags, `standard_idea_ids`, statement/solution `definition_ids`, statuses, and repair notes for:

- `kolmogorov-2002-team-olympiad-seniors-problem-8`
- `kolmogorov-2003-team-olympiad-seniors-problem-8`
- `kolmogorov-2004-round1-higher-league-problem-3`
- `kolmogorov-2004-round2-higher-league-problem-9`
- `kolmogorov-2004-round3-higher-league-problem-10`
- `kolmogorov-2006-round-1-super-high-first-league-problem-1`
- `kolmogorov-2006-round-2-super-league-problem-6`
- `kolmogorov-2006-round-3-super-league-problem-3`
- `kolmogorov-2006-round-4-super-league-problem-5`
- `kolmogorov-2006-team-olympiad-seniors-problem-9`
- `kolmogorov-2007-round-2-first-league-problem-8`
- `kolmogorov-2007-team-olympiad-seniors-problem-7`

## Notes by cluster

- 2002 team seniors P8: marked the restored official proof as the primary checked repair; the old compressed solution is retained as a checked summary and marked superseded by the full solution. Metadata now reflects complement graph, Hall/augmenting-path flavor, minimal counterexample, clique/intersection structure.
- 2003 team seniors P8 and 2004 round 3 higher P10: normalized as directed strong-connectivity/extremal-component arguments.
- 2004 round 1 higher P3, 2006 round 2 super P6, 2006 round 4 super P5, and 2006 team seniors P9: normalized tree/dual-tree/spanning-tree profiles.
- 2004 round 2 higher P9 and 2007 team seniors P7: normalized as double-counting/counting profiles.
- 2006 round 1 super-high-first P1: normalized as shortest odd cycle/minimal-counterexample in a triangle-free graph.
- 2006 round 3 super P3: normalized as local recoloring with two-color components/Kempe-chain style metadata.
- 2007 round 2 first P8: corrected the metadata from construction/tree language to impossibility via cycle decomposition and parity.

## Relations Added

Added 9 relation records in the dedicated shard only:

- `rel-metadata-kolm-2004-ap-c4-usamo-rectangle`
- `rel-metadata-kolm-2006-triangle-free-shortest-odd-cycle`
- `rel-metadata-kolm-2006-triangle-free-mantel`
- `rel-metadata-kolm-2006-recoloring-brooks`
- `rel-metadata-kolm-2006-recoloring-five-color`
- `rel-metadata-kolm-2006-triangulation-euler-formula`
- `rel-metadata-kolm-2006-wheel-spanning-tree-basics`
- `rel-metadata-kolm-2007-induced-count-handshaking`
- `rel-metadata-kolm-2007-induced-count-imo-1995-nc5`

Existing relation files were not edited.

## Verification

Target-zone metadata/anchor check:

```text
OK target metadata and new relations
OK central_method properties aligned
```

Full validation:

```text
python tools/validate.py
OK: 328 problems, 336 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.
```

Full link check:

```text
python tools/check_links.py
OK: 370 internal routes, 349 external source URLs syntactically valid.
```

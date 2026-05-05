# High verification: Kolmogorov 2008 round 2 wheel cluster

## Verdict

Classification: **league/source-level adaptations of one parametrized wheel problem**.

This cluster is not an exact duplicate/reprint cluster. It is also stronger than "different tasks with a common wheel/cycle motif": all three cards ask the same counting question for two-color edge colorings of a wheel where both color classes must be connected, and the concrete answers are obtained from the same formula `2(2^n - 2)`.

The safest data decision is **no merge and no split**. Keep all three cards as distinct official Kolmogorov 2008 contest instances, but treat them as one parametrized family:

- `kolmogorov-2008-round-2-first-junior-league-problem-1`: concrete story version with `10` rim cities; answer `2(2^10 - 2) = 2044`.
- `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1`: abstract `W_n` version; answer `2(2^n - 2)`.
- `kolmogorov-2008-round-2-second-league-problem-2`: concrete story version with `100` rim cities; answer `2(2^100 - 2)`.

Confidence: high.

## Cards Checked

- `data/problems/kolmogorov/kolmogorov-2008-round-2-first-junior-league-problem-1.yaml`
- `data/problems/kolmogorov/kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1.yaml`
- `data/problems/kolmogorov/kolmogorov-2008-round-2-second-league-problem-2.yaml`
- Medium report: `docs/archive/direct-relation-duplicate-sweep/medium-russian-nonvosh.md`

Direct relations checked:

- `data/relations/relations.d/metadata-pass-cross-links-after-tags.yaml`, id `rel-after-tags-kolm-2008-recoloring-counting-pair`
- `data/relations/relations.d/kolmogorov-final-confirmed-links.yaml`, id `rel-kolm-2008-wheel-first-junior-first-league`
- `data/relations/relations.d/kolmogorov-final-confirmed-links.yaml`, id `rel-kolm-2008-wheel-first-second-league`
- `data/relations/relations.d/kolmogorov-final-deep-links.yaml`, id `rel-kolm-deep-2007-unique-coloring-2008-wheel`, checked only as an external edge into the abstract `W_n` card

## Source Check

Local source ids checked:

- `src-kolmogorov-2008-official`: official Kolmogorov Cup 2008 archive ZIP, `https://turmath.ru/kolm/files/archive/kolm12.zip`, marked `source_verified`.
- `src-kolmogorov-archive`: official Kolmogorov Cup archive index, `https://turmath.ru/kolm/archive.php`, marked `source_verified`.

All three cards cite both source ids. The local editorial notes distinguish the source-level placements:

- first junior league, problem 1, page 10;
- first league / higher junior league, problem 1, page 4;
- second league, problem 2, page 7.

This matters for merge policy: the abstract `W_n` card is not merely an AI-created canonical generalization. It is recorded as a separate official contest card from the same source packet.

## Mathematical Comparison

Normalized common problem:

For the wheel `W_n`, color every edge in one of two colors/firms. Count the colorings for which each color class spans a connected graph on all `n+1` vertices.

Common solution skeleton:

- The wheel has `2n` edges and `n+1` vertices.
- Each connected color class must contain at least `n` edges, so each color class has exactly `n` edges and is a spanning tree.
- The spoke coloring cannot be monochromatic.
- After choosing any nonconstant coloring of the `n` spokes, the rim edges are forced up to exactly two global choices by the block-boundary argument.
- Therefore the answer is `2(2^n - 2)`.

Substitutions:

- first junior `10`-city story: `n = 10`, answer `2044`;
- second league `100`-city story: `n = 100`, answer `2(2^100 - 2)`;
- first league / higher junior card: keeps `n` symbolic.

The three tasks are therefore parametrically identical in mathematical content, but not identical as contest/source records.

## Relation Assessment

Current direct relation types are defensible as `same_motif`, but imprecise for duplicate-sweep purposes.

Recommended relation model if cleanup is later done:

- Treat the abstract `W_n` card as the hub of the family.
- Link the `10`-city and `100`-city cards to the `W_n` card as `specialization`, `parametric_variant`, or `instance_of` if the relation vocabulary permits.
- If the current vocabulary must stay coarse, keep `same_motif`, distance `1`, but rewrite relation text to say "fixed-parameter source instance of the same parametrized wheel problem" rather than generic shared motif.
- The direct `10` <-> `100` edge is optional after hub cleanup. If retained, call it a sibling fixed-parameter pair. If graph density is a concern, it can be removed/downgraded because both concrete cards would already be connected through `W_n`.

Suggested confidence after cleanup:

- `10` concrete <-> `W_n`: `0.96`.
- `100` concrete <-> `W_n`: `0.96`.
- `10` concrete <-> `100` concrete: `0.94` as sibling parametrized variants, not duplicate/reprint.

## Merge / Split Recommendation

Do not merge these cards now.

Reason: merging would erase useful source provenance across different league placements and different official statements. The `W_n` version is source-level, so it should not simply absorb the two concrete versions unless the project explicitly supports preserving multiple contest instances under one canonical theorem card.

Do not split the cluster.

Reason: the cluster is mathematically coherent and the current direct edges are not false positives. The problem is relation precision, not cluster membership.

If a future canonicalization pass wants a single mathematical parent, use this safe plan:

- Preserve all three source ids/card ids as contest occurrences.
- Make `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1` the family hub, because it is the official symbolic `W_n` statement.
- Attach the two concrete cards as fixed-parameter league adaptations, not as duplicate aliases.
- Only consider a true merge if the data model can keep per-league source occurrence metadata without losing page/league/problem-number provenance.

## Content Notes / Follow-up

- There is a likely local text typo in the second-league solution: it says `v_1, ..., v_10` while discussing `100` rim cities. This is a card-quality issue, not a duplicate/split issue. Do not patch during the parallel split process without coordination.
- The first junior card uses `simple_graph` definitions while the other two use `tree`/`spanning_tree`; this is metadata drift inside the same family, not evidence of separate problems.
- This audit did not modify `data/` or relation files.

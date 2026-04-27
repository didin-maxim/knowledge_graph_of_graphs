# Solution Completeness Sample Audit

Date: 2026-04-27

## Method

The corpus contains 350 `solutions[]` entries across 328 problem cards. Six medium-reasoning agents checked disjoint hash buckets:

```text
bucket = sha1(problem_id#solution_id) % 6
```

The sampling inside each bucket was intentionally risk-weighted: short solutions, uncertain statuses, and several long `ai_checked` solutions were inspected. No data files were edited during the agent checks.

## Aggregate Result

Agent-inspected sample:

- bucket 0: 21 inspected / 63 total, 5 serious, 2 borderline.
- bucket 1: 24 inspected / 60 total, 10 serious, 6 borderline.
- bucket 2: 38 inspected / 65 total, 16 serious, 3 borderline.
- bucket 3: 30 inspected / 49 total, 11 serious, 5 borderline.
- bucket 4: 21 inspected / 49 total, 9 serious, 2 borderline.
- bucket 5: 39 inspected / 64 total, 20 serious, 6 borderline.

Totals:

- 173 inspected solutions.
- 71 confirmed serious problems.
- 24 borderline problems.
- Raw serious rate in the risk-weighted sample: 71 / 173 = 41.0%.
- Confirmed lower bound across the full database: 71 / 350 = 20.3%.

Because the sample was enriched for short and suspicious solutions, 41% should not be used as the whole-database estimate. A reasonable current estimate is:

- serious problems: about 25-32% of all solution entries;
- serious plus borderline: about 32-40% of all solution entries.

## Exact Obvious Problems

Independent local checks found:

- 44 solution entries whose text/title is `Решение пока не найдено`.
- 4 solution entries with damaged encoding markers such as `????`.

These 48 entries alone make up 13.7% of all `solutions[]` entries and should be treated as definite defects under the new rule: they should either be removed from `solutions[]` or replaced by full Russian solutions.

## Recurrent Problem Classes

1. Placeholder-as-solution.
   Many YUMT archive cards and several Kolmogorov import notes contain `Решение пока не найдено` as a solution.

2. Damaged encoding.
   A few official-compressed solutions are unreadable because the Russian text became `????`.

3. External dependency not transferred.
   Several cards cite a theorem, AoPS/source construction, paper result, table, drawing, or PDF instead of carrying a complete proof in the card.

4. Outline instead of proof.
   Common patterns: "standard local rearrangement", "one checks", "the construction is as in the source", "fan families give equality", or a named theorem without proof/card dependency.

5. Restored-but-still-schematic official solutions.
   Some repaired solutions are mathematically close but still skip the decisive contradiction, construction, or counting step.

## Confirmed Serious Non-Placeholder Examples

- `tree-equivalent-properties#sol-leaf-induction`
- `imo-2004-c3-delete-edge-from-4cycle#sol-reviewed-secondary`
- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`
- `tc-2013-14-vertex-transitive-not-transposition#sol-counterexample-from-source`
- `fyum-2013-tur2a-p1#sol-official-archive`
- `egmo-2025-p5-rotating-arrows-dynamic-cycle#sol-official-compressed`
- `fyum-2009-tur3a-p7#sol-official-archive`
- `fyum-2011-finalb-p4#sol-official-archive`
- `fyum-2010-tur3a-p7#sol-official-archive`
- `utyum-2012_komol39_8_binary_tree_ordering#sol-official`
- `utyum-2025_komol64_8_7_tree_matchings_path#sol-official`
- `usamo-2025-p3-gabriel-graph-road-network#sol-gabriel-planar-bound`
- `chen-yu-fragile-graphs-theorem#sol-paper-theorem`
- `tc-2001-02-rooks-odd-attacks#sol-construct-63`
- `tc-2023-24-coins-pairing-weighing-forest#sol-forest-accounting`
- `kolmogorov-2008-team-olympiad-seniors-problem-7#sol-official-compressed`
- `kolmogorov-2024-t4-independent-cutset-2n-4#sol-chen-yu`
- `imo-2005-c8-noncrossing-diagonals-crossings#sol-reviewed-web`
- `imo-1998-c6-complete-graph-rainbow-edges#sol-reviewed-web`
- `fyum-2009-final-p2#sol-official-archive`
- `benjamini-tzalik-shortest-paths-bound#sol-paper-bound`
- `imo-1994-c6-infinite-grid-pairing-strategy#sol-reviewed-secondary`
- `kolmogorov-2004-round3-higher-league-problem-10#sol-official-compressed`
- `utyum-2023_komol60_7_7_room_departures#sol-official`
- `utyum-2025_komol65_7_6_airlines_degree_sum#sol-official`
- `usamo-2021-p2-planar-national-park-turning-walk#sol-local-state-bound-and-prism`
- `usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph`
- `utyum-2019_komol_7_airline_costs#sol-official`

## Recommended Next Pass

1. First mechanically remove or repair the 44 `Решение пока не найдено` entries.
2. Repair the 4 damaged-encoding solutions from source.
3. Then process the confirmed non-placeholder serious list above one by one.
4. Leave borderline items for a later pass unless they block a relation or standard-idea card.

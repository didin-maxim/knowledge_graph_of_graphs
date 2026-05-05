# Direct relation duplicate sweep: medium global heuristic

Scope: global scan of relation files under `data/relations/relations.yaml` and `data/relations/relations.d/*.yaml`.

Mode: read-only for `data/`. I used local Python snippets to parse relation pairs and problem cards, then compared normalized titles, statement text, profile text, shared sources, and extracted numeric parameters.

Snapshot parsed: 596 problem cards, 726 relation rows, 706 unique unordered direct pairs, 0 missing relation endpoints.

Heuristic score: weighted title similarity, statement token Jaccard, shorter-statement containment, profile token Jaccard, numeric overlap, and shared-source bonus. This is only a triage signal: compound-card splits and paired variants naturally score high.

## Top same-card / merge-review candidates

### Strong merge review

| Score | Pair | Current relation | Why review |
|---:|---|---|---|
| 0.883 | `fyum-2011-tur1a-p5` vs `fyum-2011-tur1b-p5` | `same_motif`, `rel-fyum-2011-tur1a-p5-tur1b-p5-rainbow-counterexample` | Same title, statement overlap 0.93, profile overlap 0.92, same numbers. Relation text says the variants are "almost identical" and use the same three-level counterexample. This is the cleanest same-card candidate. |
| 0.875 | `usajmo-2023-p3-domino-slides-special-square-digraph` vs `usamo-2023-p3-domino-slides-special-square-digraph` | `paired_variant`, `rel-usamo-2023-p3-usajmo-2023-p3` | Same special-square digraph setup, shared source, near-identical title. Relation text says senior/junior versions differ mainly in final goal: classification vs maximum. Merge only if policy treats USAMO/USAJMO paired versions as one card with variants. |
| 0.675 | `usamo-1976-p1-monochromatic-rectangle-bipartite` vs `usamo-1976-p1a-4x7-monochromatic-rectangle-forcing` | `same_source`, `rel-usamo-1976-parent-p1a-forcing` | Parent card appears to contain the 4x7 forcing subproblem; child isolates it. This is not necessarily a duplicate if compound parents are retained, but it is a parent-child cleanup candidate. |

### Compound-card split review

These are high-score because a parent card and child cards intentionally share most of the statement. They are duplicate-like at the card-boundary level, not necessarily relation mistakes.

| Score | Pair | Current relation | Suggested action |
|---:|---|---|---|
| 0.875 | `sums-2012-p7-tree-connected-subsets-extrema` vs `sums-2012-p7-tree-connected-subsets-maximum` | `specialization`, `rel-sums-2012-p7-parent-maximum-split` | Decide whether the parent compound card should remain alongside max/min children. |
| 0.874 | `sums-2012-p7-tree-connected-subsets-extrema` vs `sums-2012-p7-tree-connected-subsets-minimum` | `specialization`, `rel-sums-2012-p7-parent-minimum-split` | Same parent-child issue as above. |
| 0.865 | `cmo-2006-p4-cycle-triplets-tournament` vs `cmo-2006-p4-max-cycle-triplets-tournament` | `specialization`, `rel-cmo-2006-cycle-triplets-parent-max-child` | Parent contains max/min extrema; child isolates maximum. |
| 0.818 | `baltic-way-1997-p19-edge-disjoint-hamiltonian-cycles` vs `baltic-way-1997-p19a-prime-edge-disjoint-hamiltonian-cycles` | `specialization`, `rel-bw1997-p19-parent-to-prime-child` | Parent contains part (a); child isolates prime-n case. |
| 0.785 | `baltic-way-1997-p19-edge-disjoint-hamiltonian-cycles` vs `baltic-way-1997-p19b-k9-edge-disjoint-hamiltonian-cycles` | `specialization`, `rel-bw1997-p19-parent-to-k9-child` | Parent contains part (b); child isolates K9 case. |
| 0.793 | `all-union-1986-final-9-tree-distances-one-to-nchoose2` vs `all-union-1986-final-9-tree-distances-n6-construction` | `specialization`, `rel-all-union-1986-n6-parent-compound` | Parent contains the n=6 construction subcase. |
| 0.721 | `all-union-1986-final-9-tree-distances-one-to-nchoose2` vs `all-union-1986-final-9-tree-distances-n1986-impossible` | `specialization`, `rel-all-union-1986-n1986-parent-compound` | Parent contains the n=1986 impossibility subcase. |

### High-score variants that deserve human policy review

| Score | Pair | Current relation | Why not automatic merge |
|---:|---|---|---|
| 0.905 | `sums-2012-p7-tree-connected-subsets-maximum` vs `sums-2012-p7-tree-connected-subsets-minimum` | `paired_variant`, `rel-sums-2012-p7-minimum-maximum-paired-extrema` | Same object and source, but opposite extrema. Likely sibling cards, not one card, unless min/max should live as one compound problem. |
| 0.895 | `imo-2024-c4-turbo-grid-monsters-three-attempts-strategy` vs `imo-2024-c4-turbo-grid-monsters-two-attempts-lower-bound` | `paired_variant`, `rel-imo-2024-c4-two-three-attempts-pair` | Same IMO problem split into lower/upper bound cards. This is a split-policy question, not a hidden duplicate. |
| 0.847 | `spbmo-2010-11-p3-k2009-long-cycle-game` vs `spbmo-2010-9-p5-k2010-cycle-game` | `paired_variant`, `rel-spbmo-2010-9-p5-spbmo-2010-11-p3-cycle-game` | Very high statement overlap, but different graph size and target cycle length. Keep separate unless parameterized variants are merged. |
| 0.831 | `kolmogorov-2018-team-olympiad-juniors-problem-6` vs `kolmogorov-2018-team-olympiad-seniors-problem-5` | `specialization`, `rel-kolm-2018-mobility-junior-senior` | Same formula/method at different scales: 20/10 vs 2018/1009. Looks like a legitimate junior/senior specialization. |
| 0.809 | `fyum-2013-tur1a-p4` vs `fyum-2013-tur1b-p10` | `specialization`, `rel-fyum-2013-tur1a-p4-tur1b-p10-modular-weighted-cycles` | n-modulus theorem vs prime-modulus case. Very close, but relation text already captures specialization. |

## Suspicious relation-type patterns

| Type | Pairs | Score >= 0.45 | Score >= 0.60 | Note |
|---|---:|---:|---:|---|
| `paired_variant` | 20 | 19 | 17 | Expected to score high. Useful for catching split-policy decisions, but most are not accidental duplicates. |
| `specialization` | 20 | 12 | 10 | Many high scores are parent-child compound splits. This type should be audited for whether both parent and child cards should coexist. |
| `same_motif` | 499 | 14 | 8 | Mostly safe, but it contains the strongest hidden-duplicate candidate: `fyum-2011-tur1a-p5` vs `fyum-2011-tur1b-p5`. |
| `false_friend` | 5 | 3 | 1 | High similarity is expected for false friends, but two look especially easy to misread: USAMO 2009 P3(a)/(b) and UTYUM 2023 departure variants. |
| `prerequisite` | 155 | 5 | 2 | High scores are usually theorem chains with shared source/style, e.g. Ramsey cards. They should not be merged by similarity alone. |
| `same_source` | 2 | 2 | 1 | Both are parent/source split situations; inspect manually rather than treating as duplicates. |
| `solution_transfer` | 7 | 0 | 0 | No duplicate-looking pair found by this heuristic. |
| `reformulation` | 1 | 0 | 0 | No duplicate-looking pair found by this heuristic. |

Suspicious type takeaways:

- `same_motif` should not be trusted as a non-duplicate label when title and statement overlap are both above 0.9.
- `specialization` is the main bucket for compound parent-child duplication, especially when the source is shared and the relation text says "parent", "child", "part", or "isolates".
- `false_friend` can score very high because it intentionally links near-identical statements with different goals; these need semantic checks, not text-only checks.
- `prerequisite` high scores are often theorem-family cards; treat them as "definitely not duplicate unless the statement is literally the same theorem".

## Definitely not duplicates

These pairs were highlighted by text similarity or relation confidence, but the relation text and numeric parameters make them safe to keep separate.

| Pair | Current relation | Reason |
|---|---|---|
| `sums-2012-p7-tree-connected-subsets-maximum` vs `sums-2012-p7-tree-connected-subsets-minimum` | `paired_variant` | Same invariant, opposite extremal questions. Sibling subproblems, not the same statement. |
| `cmo-2006-p4-max-cycle-triplets-tournament` vs `cmo-2006-p4-min-cycle-triplets-tournament` | `paired_variant` | Same tournament statistic, but maximum and minimum are distinct tasks. |
| `spbmo-2010-11-p3-k2009-long-cycle-game` vs `spbmo-2010-9-p5-k2010-cycle-game` | `paired_variant` | K2009/75-cycle vs K2010/11-cycle. Same game engine, different parameters and construction. |
| `kolmogorov-2018-team-olympiad-juniors-problem-6` vs `kolmogorov-2018-team-olympiad-seniors-problem-5` | `specialization` | Junior/senior scale change is explicit: 20 cities/10 bound vs 2018/1009. |
| `fyum-2013-tur1a-p4` vs `fyum-2013-tur1b-p10` | `specialization` | General modulus n theorem vs prime modulus p case; close but not identical. |
| `ramsey-r34` vs `ramsey-r35` | `prerequisite` | Shared Ramsey style and sources, but R(3,4) is used inside R(3,5); theorem statements differ. |
| `ramsey-r34` vs `ramsey-r44` | `prerequisite` | Similar Ramsey vocabulary, different Ramsey numbers and target structures. |
| `usamo-2009-p3-tasteful-domino-tiling-existence` vs `usamo-2009-p3-tasteful-domino-tiling-uniqueness` | `false_friend` | Same local tasteful condition, but existence and uniqueness are separate parts with different proof methods. |
| `imo-1996-c1-grid-knight-reachability-r73-path` vs `imo-1996-c1-grid-knight-reachability-r97-impossible` | `paired_variant` | Same grid-move family, but one is a constructive reachable case and the other is an impossible case. |
| `all-union-1986-final-9-tree-distances-n6-construction` vs `all-union-1986-final-9-tree-distances-n1986-impossible` | `paired_variant` | Same original problem family, but one is the constructive small-n part and the other is the large-n impossibility. |

## Recommended follow-up queue

1. Decide repository policy for compound parent cards that now have isolated child cards. This affects SUMS 2012/7, CMO 2006 P4, Baltic Way 1997 P19, All-Union 1986, USAMO 1976 P1, and similar future splits.
2. Manually inspect and likely merge or mark as reprint/variant: `fyum-2011-tur1a-p5` vs `fyum-2011-tur1b-p5`.
3. Manually inspect USAMO/USAJMO 2023 P3 policy: either keep as paired variants or consolidate into one card with contest-specific asks.
4. Add a future lint/triage rule: for direct pairs with `same_motif` and `title >= 0.95` plus `statement >= 0.85`, require explicit `paired_variant`, `reprint`, `same_source`, or a short human note explaining why not merge.

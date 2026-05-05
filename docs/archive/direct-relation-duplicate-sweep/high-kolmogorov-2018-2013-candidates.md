# High verification: Kolmogorov 2018/2013 duplicate candidates

Scope: two high-priority candidates promoted from `medium-russian-nonvosh.md`.

Write policy for this pass: documentation only. No `data/` files or split-related files were modified.

## Summary Verdicts

- `kolmogorov-2018-team-olympiad-juniors-problem-6` <-> `kolmogorov-2018-team-olympiad-seniors-problem-5`: **same_problem / parametrized specialization**. A single general theorem card would be mathematically natural, but the two existing cards should remain as official source-level contest instances unless the data model preserves source occurrences under a canonical parent.
- `kolmogorov-2013-team-olympiad-juniors-problem-7` <-> `kolmogorov-2013-team-olympiad-seniors-problem-8`: **extension / strengthening**. The senior task contains the junior upper-bound problem and adds sharpness. Do not merge as a duplicate.

## Candidate 1: Kolmogorov 2018 Mobility Pair

Cards checked:

- `data/problems/kolmogorov/kolmogorov-2018-team-olympiad-juniors-problem-6.yaml`
- `data/problems/kolmogorov/kolmogorov-2018-team-olympiad-seniors-problem-5.yaml`
- Medium report: `docs/archive/direct-relation-duplicate-sweep/medium-russian-nonvosh.md`
- Direct relation: `data/relations/relations.d/kolmogorov-2026-import-links.yaml`, id `rel-kolm-2018-mobility-junior-senior`
- Sources cited by both cards: `src-kolmogorov-2018-official`, `src-kolmogorov-archive`, both locally marked `source_verified`

### Verdict

Classification: **same_problem / parametrized specialization**, not `paired_variant`, not `false_friend`, and not a genuine `extension`.

The two statements are the same optimization problem after substituting a size parameter:

- junior: `20` cities, regions have size at most `10`;
- senior: `2018` cities, regions have size at most `1009`;
- common form: `2m` cities, regions have size at most `m`; define the two minimum color-cut mobilities `A` and `B`; minimize `A+B`.

Both cards have the same answer, `1`, and the same proof architecture. The senior card is not asking for an additional theorem beyond the junior card; it is the same theorem at a much larger official contest parameter.

### Mathematical Check

Common normalized model:

- Complete graph on `2m` cities with each edge colored bus or rail.
- A region is a nonempty vertex set of size at most `m`.
- Mobility of a region in one color is the number of color edges leaving the region divided by the region size.
- `A` is the minimum bus mobility over all regions; `B` is the minimum rail mobility over all regions.
- Find the minimum possible value of `A+B`.

The proof in both cards uses the same two extremal regions `M` and `N` and the same four-part decomposition:

- `X = M intersect N`
- `Y = M \ X`
- `Z = N \ X`
- `T = V \ (M union N)`

With sizes `a,b,c,d`, the shared lower-bound step counts edges between `T` and `X`, and between `Y` and `Z`, contributing at least one of the two color mobilities. The displayed inequality is the same after scaling:

- junior: `A+B >= (ad+bc)/10`;
- senior: `A+B >= (ad+bc)/1009`;
- common form: `A+B >= (ad+bc)/m`.

The case analysis is also parameter-identical:

- if all `a,b,c,d` are nonzero, use `ad+bc >= (a+d-1)+(b+c-1) = 2m-2`, which is enough for `m >= 2`;
- if `b=0` or `c=0`, the size constraint forces the outside part large enough to give `A+B >= 1`;
- if `bc != 0` and `ad = 0`, the edges between `Y` and `Z` give the needed lower bound.

The extremal construction is the same in both cards: one city has only rail routes to all others, and another city has bus routes to all cities except the first. Then one singleton region has bus mobility `0`, another has rail mobility `1`, so `A+B=1`.

### Data Recommendation

Recommended classification for duplicate-sweep purposes: **same parametrized problem with fixed official substitutions**.

If the project supports canonical mathematical cards, a safe future cleanup would be:

- create or designate a general card for the `2m`/`m` theorem, probably with `m >= 2`;
- attach the junior `m=10` and senior `m=1009` cards as official source instances or specializations;
- preserve page/league/problem-number provenance from both current cards.

If the project remains one card per contest occurrence, do **not** merge the cards. Keep both official cards and keep a direct relation, preferably typed as `specialization`, `parametric_variant`, or `same_problem_instance` if the vocabulary permits.

Confidence: **0.97**.

## Candidate 2: Kolmogorov 2013 Coloring Pair

Cards checked:

- `data/problems/kolmogorov/kolmogorov-2013-team-olympiad-juniors-problem-7.yaml`
- `data/problems/kolmogorov/kolmogorov-2013-team-olympiad-seniors-problem-8.yaml`
- Medium report: `docs/archive/direct-relation-duplicate-sweep/medium-russian-nonvosh.md`
- Direct relation: `data/relations/relations.d/kolmogorov-final-confirmed-links.yaml`, id `rel-kolm-2013-chromatic-team-junior-senior`
- Sources cited by both cards: `src-kolmogorov-2013-official`, `src-kolmogorov-archive`, both locally marked `source_verified`

### Verdict

Classification: **extension / strengthening**, not duplicate-level `same_problem`, not `paired_variant`, and not `false_friend`.

The junior statement asks only for the upper bound: prove that the full graph can be properly colored in `k+n-1` colors.

The senior statement asks for the minimum guaranteed number of colors. Its answer is again `k+n-1`, but proving that answer requires two parts:

- the same upper-bound argument as the junior problem;
- an additional lower-bound construction showing that `k+n-2` colors do not suffice in general.

Thus the senior problem strictly extends the junior problem. The junior card is a theorem/proof task; the senior card is a sharpness/exact-bound task.

### Shared Upper Bound

Both cards use the same setup:

- vertices are partitioned into `A`, `B`, `C`;
- there are no edges between `A` and `C`;
- `A union B` is `k`-colorable;
- `B union C` is `n`-colorable.

The common solution skeleton is:

- color `B union C` with `n` colors;
- let `D` be the vertices of `B` using one chosen color;
- color `A union D` with `k` colors while reusing that chosen color;
- keep or shift the other colors from the `B union C` coloring;
- use the lack of `A`-`C` edges and the definition of `D` to verify the combined coloring.

This proves the junior task and supplies only the upper-bound half of the senior task.

### Senior-Only Sharpness

The senior card adds a lower-bound construction absent from the junior card:

- take `kn` vertices in `B` as cells of an `n` by `k` grid;
- add a clique `A` of size `k`, one vertex per column;
- add a clique `C` of size `n`, one vertex per row;
- connect grid cells inside `B` exactly when they are in different rows and different columns;
- connect each `a_j` to all grid cells except column `j`;
- connect each `c_i` to all grid cells except row `i`;
- keep no edges between `A` and `C`.

The construction is `k`-colorable on `A union B` by columns and `n`-colorable on `B union C` by rows, but any coloring of the whole graph with `k+n-2` colors leads to a shared-color counting contradiction using common colors on the two cliques and a cyclic choice of grid cells.

That lower-bound construction is not a cosmetic add-on. It changes the task from "prove an upper bound" to "determine the exact guaranteed value."

### Data Recommendation

Do not merge these cards.

Recommended relation model:

- Replace or supplement coarse `same_motif` with `extension`, `strengthening`, or `upper_bound_to_exact_bound` if available.
- Direction should be junior -> senior: the senior problem extends the junior problem by adding sharpness.
- Keep distance `1`; the shared upper-bound proof is direct and substantial.
- If relation vocabulary cannot express extension, keep `same_motif` but rewrite relation text to state explicitly that the senior solution contains the junior result plus an additional lower-bound construction.

No general single-card collapse is recommended. A canonical theorem card for the exact value `k+n-1` would represent the senior problem, but it would not faithfully preserve the junior card's narrower proof-only ask unless contest occurrences are modeled separately.

Confidence: **0.94**.

## Final Classification Table

| Pair | Decision | General card? | Merge? | Relation guidance |
| --- | --- | --- | --- | --- |
| 2018 junior P6 / senior P5 | `same_problem` as fixed-parameter instances of one theorem | Optional and mathematically natural, if source occurrences are preserved | No direct merge under current source-card model | Keep as `specialization` / parametric instance relation |
| 2013 junior P7 / senior P8 | `extension` / exact-bound strengthening | Not recommended as a duplicate collapse | No | Model as junior upper bound extended by senior sharpness |


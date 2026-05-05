# False friends second pass: classical + university/misc

Reviewed source: `audit/false-friends-first-pass/classical-university-misc.md`.

Rule used in this pass: keep only cases where the card really hides two or more independent self-contained formulations/variants. Mere equivalent classical formulations, graph translations, proof subcases, or "upper bound plus sharpness example" are rejected.

## Survivors

| problem id | classification | note |
|---|---|---|
| `balanced-bipartite-edge-coloring-two-colors` | `pair_variant` | IMO point-colouring and direct bipartite edge-colouring are both self-contained contest statements; the graph statement is the common core, and the solution ideas are essentially the same. |
| `benjamini-tzalik-shortest-paths-kolmogorov-merged` | `lemma_split` | The Benjamini-Tzalik upper bound is a reusable theorem; the Kolmogorov even-degree problem asks for the exact extremum and additionally needs a construction. Better treated as theorem/lemma plus application, not as a pair relation between equivalent formulations. |
| `flashlight-batteries-tournament-cities-2015` | `pair_variant` | The `2n+1` and `2n` battery versions are self-contained variants with different parameters/answers, but both reduce to the same Turan/complement extremal template. |
| `gallai-hasse-roy-vitaver-theorem` | `lemma_split` | The two sides "every orientation has a long directed path" and "some orientation has no longer path" are independent self-contained directions of the equality. They should be split as lemmas/directions rather than marked as false friends. |
| `konig-line-coloring-bipartite` | `lemma_split` | Regular bipartite decomposition into perfect matchings is a standalone lemma used to prove the full edge-colouring theorem after regularization. |
| `line-arrangement-side-count-levels` | `false_friend` | The two claims look like nearby facts about the same level function, but one is local adjacency/change-by-one and the other is global existence of all levels via a sweep line. |
| `sums-2012-p7-tree-connected-subsets-extrema` | `false_friend` | The minimum and maximum of `s(T)` are separate extremal tasks; both are self-contained and their extremal structures/proofs are different. |
| `imc-1997-day1-p6-intersecting-families-finite-transversal` | `false_friend` | Part (a) is false in general, while part (b) becomes true under uniformity; the statements are close on the surface but the solutions are counterexample vs positive theorem. |
| `imc-2006-day2-p1-polygon-triangulation-parity` | `pair_variant` | The `3 | n` and `3 not | n` triangulation parity statements are independent cases with closely related induction ideas. |
| `imc-2011-day2-p2-tripartite-married-triples` | `false_friend` | The threshold counterexample at `k=n/2` and the positive perfect-cover theorem at `k>=3n/4` are genuinely different self-contained assertions. |
| `miklos-schweitzer-2009-p2-smooth-difference-graphs` | `false_friend` | The complete-graph and bounded-degree connected-graph realizability questions are externally similar but use different mechanisms. |
| `miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees` | `false_friend` | Classification for at most three spanning trees and oddness of the spanning-tree count are independent knot/Tait-graph statements rather than equivalent formulations. |

## Rejected Candidates

| problem id | classification | note |
|---|---|---|
| `bounded-forward-rays-balanced-sums` | `reject` | Sequence, functional-digraph, and `L=2015` versions are the same lemma/specialization, not independent variants. |
| `c4-free-kovari-sos-turan-bound` | `reject` | C4-free and "at most one common neighbour" are equivalent formulations of one double-counting estimate. |
| `cayley-prufer-labeled-trees` | `reject` | The Prüfer-code statement is the standard bijective form/proof of Cayley's formula, not a separate variant relation. |
| `chen-yu-independent-cutset-kolmogorov-merged` | `reject` | The Kolmogorov statement is essentially the same theorem wording as Chen-Yu in contest form. |
| `color-reduction-by-odd-deletion-and-doubling` | `reject` | Two allowed operations are ingredients of one problem, not separate self-contained formulations. |
| `degeneracy-greedy-coloring` | `reject` | Degeneracy and deletion-order forms are equivalent classical formulations with one greedy proof. |
| `erdos-gallai-path-edge-bound` | `reject` | Edge bound and average-degree form are contrapositives/equivalent forms of the same theorem. |
| `euler-trail-extension-center-forest` | `reject` | The forest condition, "all cycles pass through c", and road-network wording are equivalent faces of one criterion. |
| `eulerian-graph-criterion` | `reject` | Bridges and pencil-drawing versions are applications of the same Euler criterion, not independent variants. |
| `five-color-theorem` | `reject` | Map colouring is the usual planar-dual/application wording of the same theorem. |
| `hall-marriage-theorem` | `reject` | SDR, bipartite matching, and marriage wordings are equivalent classical formulations. |
| `havel-hakimi-graphical-degree-sequence` | `reject` | The algorithmic form is the same Havel-Hakimi step iterated. |
| `minimal-half-subset-exchange-lemma` | `reject` | The two "in particular" inequalities are consequences of one exchange inequality. |
| `no-two-color-cycle-edge-bound` | `reject` | The three-colour statement is a corollary/special case of the general bound; the forest observation is a proof step. |
| `planar-edge-bound` | `reject` | The two statements are duplicate notation for `e <= 3v-6`. |
| `ramsey-r33` | `reject` | Party/graph/colouring wordings are equivalent; the five-vertex example is sharpness, not a separate formulation. |
| `ramsey-r34` | `reject` | Exact Ramsey value combines upper bound and lower example; graph/party forms are equivalent. |
| `ramsey-r35` | `reject` | Exact Ramsey value combines upper bound and lower example; graph/party forms are equivalent. |
| `ramsey-r44` | `reject` | Exact Ramsey value combines upper bound and lower example; graph/party forms are equivalent. |
| `tree-equivalent-properties` | `reject` | This is explicitly a list of equivalent tree characterizations. |
| `turan-theorem` | `reject` | Clique-free, complement/independence, and flashlight forms are standard equivalent/applicative forms of Turan's theorem. |
| `sums-2011-p8-periodic-hexagon-tessellation-even-vertices` | `reject` | Geometric and periodic graph statements are translations of the same parity/construction problem. |
| `imc-2001-day2-p4-zero-principal-minors-acyclic-digraph` | `reject` | Nilpotency and simultaneous triangularization are two consequences of one acyclic-digraph argument; triangularization essentially implies nilpotency. |
| `imc-2003-day2-p4-steiner-triples-elementary-abelian-2-group` | `reject` | The two listed conditions define one structure; they are not alternative formulations or variants. |
| `imc-2024-day2-p9-young-tableaux-friend-graph` | `reject` | The nice-matrix conditions are a definition, and the graph formulation is a translation of the same problem. |
| `miklos-schweitzer-1959-p10-even-circuit-edge-bound` | `reject` | This is an upper bound plus sharpness example. |
| `miklos-schweitzer-2024-p1-bipartite-perfect-matching-edge-weights` | `reject` | The minimum-on-`S` and maximum-on-`T` requirements are simultaneous constraints in one theorem, not separate statements. |
| `mmo-2018-acquaintance-seating-clique-chromatic` | `reject` | Seating and graph colouring formulations are the same problem in different languages. |
| `simon-marais-2020-b4-rainbow-distance-clique-polygon` | `reject` | Part (a) is a special-case construction inside the full characterization in part (b), not an independent variant. |
| `simon-marais-2025-b1-beaut-functions-gcd-graph` | `reject` | Beaut functions and list-colouring of the gcd graph are equivalent formulations. |
| `vjimc-2009-cat1-p3-partial-hypergraph-bicoloring` | `reject` | The multiple colouring requirements are parts of one target colouring. |
| `vjimc-2009-cat2-p4-transversal-hypergraph-polynomial-bound` | `reject` | The hypergraph wording and proof cases are one polynomial-method estimate. |
| `vjimc-2017-cat1-p3-polyhedron-edge-products` | `reject` | Polyhedron and planar-skeleton formulations are direct translations of one inequality. |
| `vjimc-2022-cat1-p4-stone-game-state-graph` | `reject` | The two move types are rules of one game, not variants or separate formulations. |


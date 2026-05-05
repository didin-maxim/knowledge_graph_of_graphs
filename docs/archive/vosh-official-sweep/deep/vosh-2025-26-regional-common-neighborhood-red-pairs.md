# Deep check: vosh-2025-26-regional-common-neighborhood-red-pairs

Date: 2026-05-05

## Card

- File: `data/problems/vosh/vosh-2025-26-regional-common-neighborhood-red-pairs.yaml`
- Problem: LII Всероссийская математическая олимпиада школьников, региональный этап 2025/26, 9 класс, задача 9.10.
- Scope: one-card high-reasoning pass; only the card, this audit note, and the optional local relations file were edited.

## Official Source Check

Primary source checked:

- https://olympiads.mccme.ru/vmo/2026/iii-2.pdf

The PDF is the official second-day regional-stage material for 2-3 February 2026. It states that the 2025/26 regional stage is conducted from tasks prepared by the Central Subject-Methodical Commission in mathematics and then gives answers, solutions, and grading comments.

Relevant PDF anchors from the web text extraction:

- Lines 303-308: statement of problem 9.10 for grade 9.
- Line 309: answer `k = 50`.
- Lines 310-315: graph model with blue acquaintance edges, red non-acquaintance edges, and blue neighborhoods `N(v)`.
- Lines 316-319: extremal example on 102 vertices split into 51 red pairs.
- Lines 320-344: first proof of the lower bound via a red pair `v,w` with intersecting blue neighborhoods and the inequality `2a+b+c >= t(101-t)`.
- Lines 345-384: second proof via two lemmas and a maximal red degree in a neighborhood.
- Lines 385-399: grading comments.

## Author / Proposer

No individual author or proposer is printed for problem 9.10 in the checked PDF. The front matter attributes the tasks globally to the Central Subject-Methodical Commission in mathematics, but that is not an individual proposer attribution. The card therefore keeps the author as unknown and adds a checked note rather than inventing a name.

## Statement And Graph Model

The original statement in the card matches the official wording in substance:

- every person has exactly 100 acquaintances in the company;
- acquaintance is mutual;
- every person's 100-acquaintance neighborhood contains at least one non-acquainted pair;
- the required maximum `k` counts distinct non-acquainted pairs inside one such neighborhood, and one person may belong to several pairs.

The graph-theory formulation is equivalent when stated for a finite simple graph: vertices are people, edges are acquaintances, every vertex has degree 100, and every open neighborhood is not a clique. The target is the largest guaranteed number of nonedges inside some open neighborhood.

The red/blue complete-graph model used in the solution is also official: blue edges are acquaintances and red edges are non-acquaintances. The proof counts red edges inside blue neighborhoods.

## Solution Audit

Classification: `official_complete_or_near_complete`.

Reason: the official PDF contains the answer, the sharpness construction, two complete lower-bound proofs, and grading criteria. The local solution follows the first official proof closely and is self-contained. It also correctly fixes a minor typesetting/OCR issue around the size of `S = N(v) union N(w)`: since `|N(v)|=|N(w)|=100` and `|P|=t`, the union has `200-t` vertices.

Key proof check:

- Sharpness: 102 vertices paired into 51 red nonedges, all other edges blue. Each vertex has 100 blue neighbors, and its blue neighborhood contains exactly the other 50 red pairs, so no guarantee above 50 is possible.
- Existence: assume every blue neighborhood contains at most 49 red edges.
- Pick `v` and a red pair `u1,u2` inside `N(v)`. Because `u1` has 100 blue neighbors and `u2` is not one of them while `v` is, there is a blue neighbor `w` of `u1` outside `N(v) union {v}`. Thus `v,w` are red and `N(v) cap N(w)` is nonempty.
- Let `P=N(v) cap N(w)`, `|P|=t`, `Q=N(v)\P`, `R=N(w)\P`. Count red edges from vertices of `P` into `P union Q union R`.
- For each `p in P`, at most 98 of its blue neighbors lie in `P union Q union R`, because `v` and `w` are already two blue neighbors outside that set. Hence each `p` has at least `101-t` red incident edges inside the union.
- Therefore `2a+b+c >= t(101-t)`, while the assumption gives `a+b <= 49` and `a+c <= 49`, so `2a+b+c <= 98`.
- For integer `1 <= t <= 100`, `t(101-t) >= 100`, contradiction.

## Tags And Metadata

The final metadata is appropriate:

- Objects: finite simple/regular acquaintance graph, complement edges, neighborhoods.
- Methods: extremal construction/counterexample, neighborhood-intersection counting, double counting, degree counting.
- Tags: `extremal_graph_theory`, `double_counting`, `degree_counting`, `goal_exact_bound`.
- `kind.secondary`: `graph_in_solution` and `application`, because the original problem is a social-network formulation and the graph language appears in the solution.

## Relations

Added two local `same_motif` links:

- `apmo-2010-p3-common-acquaintance-extremal`: both problems are social graph problems about non-acquainted pairs seen through common acquaintances/neighborhoods. The APMO problem maximizes all nonedges with a common neighbor, while this VOS problem forces many nonedges inside one fixed-degree neighborhood.
- `vosh-2008-regional-bureaucrats-common-neighborhood`: both are Russian olympiad social-graph double-counting problems around common neighborhoods/non-neighborhoods. The 2008 problem is tripartite Ramsey-style averaging; the 2025/26 problem is a regular-graph exact bound.

I did not add weaker links to broad regular-graph or coloring cards: they share vocabulary but not the central neighborhood-intersection counting mechanism.

## Residual Risks

- Individual author/proposer remains unknown because the official PDF does not print one.
- The local card includes the first official proof but not the second official proof; classification remains official because one complete official proof is present.
- The source registry entry was not edited in this pass, per the requested scope; the card assumes the existing `src-vosh-2025-26-regional-day2-official` source id is valid.

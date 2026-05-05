# High verification: classical theorem-instance pairs from IMO cards

Date: 2026-05-05

Scope: high verification for two theorem-instance candidates promoted from `medium-classical-overlap.md`:

- `bounded-forward-rays-balanced-sums` vs `imo-2015-c5-sequence-rays`
- `third-fourth-distance-layer-bound` vs `imo-2013-c6-flight-distance-layers`

No `data/` files were edited in this audit.

## Verdict

Both pairs are best modeled as **one general theorem/lemma card with olympiad numeric source instances**, not as ordinary prerequisite-plus-application pairs.

The current `prerequisite` edges are navigationally understandable because the classical cards can be used to solve the contest cards, but they understate the mathematical identity. In each case, the olympiad card already contains a parameterized graph-theory statement matching the classical card, and the contest-language original is the same theorem with a concrete parameter:

- IMO 2015 C5: `L = 2015`, bound `1007^2 = floor((2015 - 1)^2 / 4)`.
- IMO 2013 C6: `M = 100`, bound `2550 = floor(101^2 / 4)`.

Recommendation: keep a single canonical general theorem card for each pair, and attach the IMO card/source as a numeric contest instance or alternate source statement. If the data model cannot merge because one card per contest problem is required, the relation should be upgraded from `prerequisite` to a duplicate-level/theorem-instance type such as `contest_instance`, `same_statement`, or `extracted_theorem`.

Confidence: high.

## Pair 1: `bounded-forward-rays-balanced-sums` vs `imo-2015-c5-sequence-rays`

Checked files:

- `data/problems/classical/bounded-forward-rays-balanced-sums.yaml`
- `data/problems/imo/imo-2015-c5-sequence-rays.yaml`
- `data/relations/relations.d/bounded-forward-rays-balanced-sums.yaml`
- Medium report: `docs/archive/direct-relation-duplicate-sweep/medium-classical-overlap.md`

Current direct relation:

- id `rel-bounded-forward-rays-balanced-sums-imo-2015-c5`
- type `prerequisite`, distance `1`
- anchors `sol-pool-of-balls` -> `sol-official-compressed`
- confidence `0.78`, status `needs_human_review`

### Statement comparison

The classical card states the general sequence/functional-digraph lemma:

- `L >= 1`
- `1 <= a_i <= L`
- endpoints `i + a_i` are pairwise distinct
- there exist positive integers `b, N` such that for all `n > m >= N`,
  `|sum_{i=m+1}^n(a_i - b)| <= floor((L - 1)^2 / 4)`

The IMO card's original statement is exactly the `L = 2015` case with bound `1007^2`. Its `graph_theory` statement already gives the same parameterized `L` formulation with the same bound `floor((L - 1)^2 / 4)`.

So this is not merely "classical lemma used inside the problem"; the olympiad card contains the same general theorem plus the original numerical instance.

### Solution comparison

The solutions are identical in mathematical structure after replacing `2015` by `L`:

- Build the pool of active forward arrows/balls crossing time `t`.
- Heights are distinct and lie in `0,1,...,L-1`, so the pool has at most `L` balls.
- The pool size is nondecreasing and eventually stabilizes at `b`.
- After stabilization, height `0` is always present.
- The height sum satisfies `S_{t+1} - S_t = a_{t+1} - b`.
- Partial sums telescope as `sum(a_i - b) = S_n - S_m`.
- The possible range of `S_t` is bounded by `(b - 1)(L - b) <= floor((L - 1)^2 / 4)`.

This matches the user's rule: the solution is the same proof with the large contest number replaced by a parameter. Therefore the preferred representation is one common theorem card with multiple sources/statements.

### Recommendation

Canonical card: `bounded-forward-rays-balanced-sums`.

Reason: it is already the clean reusable theorem card and records the IMO shortlist source. It also has both sequence and graph-theory formulations plus the `L = 2015` olympiad reformulation.

Preserve on the canonical card:

- General statement with parameter `L`.
- Original IMO 2015 C5 statement as the numeric `L = 2015` source instance.
- Source ids `src-imo-2015-shortlist` and `src-mathlib-imo-2015-q6` if the latter is retained as secondary solution support.
- The pool-of-balls/telescoping solution as the canonical proof.

Relation change:

- Replace `prerequisite` with `contest_instance` / `same_statement` / `extracted_theorem`, depending on supported taxonomy.
- Suggested distance: `0` if duplicate-level theorem-instance identity is represented by distance; otherwise keep distance `1` but encode identity in the relation type.
- Suggested confidence: raise to `0.98` or higher after taxonomy update.

## Pair 2: `third-fourth-distance-layer-bound` vs `imo-2013-c6-flight-distance-layers`

Checked files:

- `data/problems/classical/third-fourth-distance-layer-bound.yaml`
- `data/problems/imo/imo-2013-c6-flight-distance-layers.yaml`
- `data/relations/relations.d/distance-layer-bound.yaml`
- Medium report: `docs/archive/direct-relation-duplicate-sweep/medium-classical-overlap.md`

Current direct relation:

- id `rel-third-fourth-distance-layer-bound-imo-2013-c6`
- type `prerequisite`, distance `1`
- anchors `sol-mse-neighbor-partition` -> `sol-mse-neighbor-partition`
- confidence `0.99`, status `ai_checked`

### Statement comparison

The classical card states the general distance-layer theorem:

- `G` is a finite connected undirected graph.
- For every vertex `x`, `L_i(x) = {y : dist(x,y) = i}`.
- If `|L_3(x)| <= M` for every vertex `x`, then `|L_4(x)| <= floor((M + 1)^2 / 4)` for every vertex `x`.

The IMO card's original city/flight statement is exactly the `M = 100` instance, asking to prove that no city has more than `2550` cities at distance `4`. Its `graph_theory` and `stmt-graph-distance-layers` statements already state the same parameterized theorem with `M`.

So the mathematical statement is the same general theorem plus a contest-language numerical instance, not merely a prerequisite used in a larger olympiad problem.

### Solution comparison

The classical solution `sol-mse-neighbor-partition` and the IMO card's `sol-mse-neighbor-partition` are the same argument with `M = 100` substituted:

- Fix a vertex `v`.
- Partition or assign vertices of `L_4(v)` by the first neighbor `v_i` on a shortest path from `v`.
- Keep the nonempty classes, with count `q` and sizes `n_1,...,n_q`.
- For a fixed class, its vertices plus witnesses coming from the other nonempty classes force `|L_3(v_i)| >= n_i + q - 1`.
- Since every third layer has size at most `M`, get `n_i <= M + 1 - q`.
- Hence `|L_4(v)| <= q(M + 1 - q) <= floor((M + 1)^2 / 4)`.

For the IMO numeric instance this becomes `n_i <= 101 - q` and `q(101 - q) <= 2550`. This satisfies the user's rule for a common theorem card: the proof is identical after replacing the contest number by a parameter.

Nuance: the IMO card also preserves an official compressed solution using a minimal substantial subset and private shortest paths. That official proof is not textually the same as the classical MSE-style proof, but it proves the same theorem instance. This does not change the identity of the statement; it only means the canonical theorem card may want to retain the official proof as an alternate source-specific solution if provenance matters.

### Recommendation

Canonical card: `third-fourth-distance-layer-bound`.

Reason: it is already the clean reusable theorem card and directly states the parameterized result. The IMO card's contest-language statement should be preserved as a numeric source instance with `M = 100`.

Preserve on the canonical card:

- General statement with parameter `M`.
- Original IMO 2013 C6 city/flight statement as the numeric `M = 100` source instance.
- Source ids `src-imo-2013-shortlist` and `src-mse-imo-2013-c6-layer-counting`.
- The neighbor-partition proof as the canonical general proof.
- Optionally preserve the official minimal-subset/private-path proof as an alternate solution tied to the IMO source.

Relation change:

- Replace `prerequisite` with `contest_instance` / `same_statement` / `extracted_theorem`.
- Suggested distance: `0` if available for theorem-instance identity; otherwise keep distance `1` but do not leave it as an ordinary prerequisite.
- Existing confidence `0.99` is appropriate.

## Overall Data-Model Recommendation

These two pairs should be handled by the same pattern:

- One canonical general theorem/lemma card.
- Multiple statements on that card: parameterized theorem plus original olympiad numeric statement.
- Multiple sources on that card: official IMO shortlist source and any secondary/published solution source.
- Contest-instance relation or source-instance metadata rather than a plain prerequisite edge.

If the database intentionally keeps separate olympiad problem cards for contest browsing, do not merge away contest provenance. Instead, keep both records but make the relation duplicate-level/theorem-instance, with a note that the contest record is a numeric instance of the general theorem.

Future edit caution: the YAML terminal output is mojibake in this PowerShell session, so any later `data/` edits should use a UTF-8-safe path and avoid accidental re-encoding.

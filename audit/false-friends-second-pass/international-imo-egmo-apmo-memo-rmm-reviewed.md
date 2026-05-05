# False friends second pass: international IMO/EGMO/APMO/MEMO/RMM

Scope: reviewed candidates from `audit/false-friends-first-pass/international-imo-egmo-apmo-memo-rmm.md`.

Rule used in this pass: keep only cases where the material really contains two or more independent self-contained statements/parameter variants. Ordinary "upper bound + construction", "estimate + example", and proof subcases are rejected unless the right action is clearly to extract a standalone lemma rather than create a relation between variants. No problem cards or database files were edited.

## Surviving relation candidates

### `imo-1996-c1-grid-knight-reachability-*`

Files:
- `data/problems/imo/imo-1996-c1-grid-knight-reachability-divisible-2-or-3.yaml`
- `data/problems/imo/imo-1996-c1-grid-knight-reachability-r73-path.yaml`
- `data/problems/imo/imo-1996-c1-grid-knight-reachability-r97-impossible.yaml`

Classification: `false_friend`.

Reason: these are genuine self-contained regimes of the same original reachability problem. The surface language is almost identical: same board, same start/target, only the parameter `r` changes. But the mechanisms are not one proof split into cases:
- `r` divisible by 2 or 3: modular obstruction, via parity or residue classes.
- `r=73`: explicit positive path.
- `r=97`: special band-parity obstruction.

The obstruction cards are thematically related by coloring/invariants, but the cluster as a whole is a false-friend cluster because positive construction and two different obstruction mechanisms look like minor parameter variants while solving by different certificates.

### `imo-1998-c6-*`

Files:
- `data/problems/imo/imo-1998-c6-k-le-4-rainbow-edges-impossible.yaml`
- `data/problems/imo/imo-1998-c6-k5-rainbow-edges-construction.yaml`
- `data/problems/imo/imo-1998-c6-k-ge-6-one-factorization.yaml`

Classification: `false_friend`.

Reason: real parameter split, not just a proof subdivision. The goals and methods change materially:
- `k <= 4`: impossibility, with the nontrivial part using a Ramsey obstruction for `k=4`.
- `k = 5`: exceptional explicit coloring by five partition systems.
- `k >= 6`: construction from one-factorization and matching independence.

The statements are externally very close, but the key ideas are different enough that a relation should warn about false similarity rather than mark them as close paired variants.

### `imo-2024-c4-turbo-grid-monsters-*`

Files:
- `data/problems/imo/imo-2024-c4-turbo-grid-monsters-two-attempts-lower-bound.yaml`
- `data/problems/imo/imo-2024-c4-turbo-grid-monsters-three-attempts-strategy.yaml`

Classification: `false_friend`.

Reason: already split into two self-contained game statements: two attempts are not enough, and three attempts are enough. This is not merely a routine lower/upper half of an extremal count: each side is a complete adversarial-strategy problem.

The two solutions share the same game board and both watch first visits to early rows, but the proof roles are opposite and the mechanisms differ: an adaptive adversary traps attempts two rows in succession, while the constructive strategy scans row 2 and then uses safe columns/detours. Keep as a false-friend pair rather than a close `pair_variant`.

### `egmo-2025-p5-rotating-arrows-*`

Files:
- `data/problems/egmo/egmo-2025-p5-rotating-arrows-even-dynamic-cycle.yaml`
- `data/problems/egmo/egmo-2025-p5-rotating-arrows-odd-parity.yaml`

Classification: `false_friend`.

Reason: genuine parity split into self-contained statements. The even case asks for the exact maximum `n^2/4` and uses a Hamiltonian/dynamic-cycle encoding plus a mod-4 upper bound. The odd case has maximum `0` by a checkerboard parity obstruction. Same surface setup, but the solution content is fundamentally different.

## Lemma-split candidates, not variant relations

### `rmm-2023-p6-colored-spanning-tree-suspicious-edges`

File: `data/problems/rmm/rmm-2023-p6-colored-spanning-tree-suspicious-edges.yaml`

Classification: `lemma_split`.

Reason: the two branches `B(C)=b` and `B(C)>b` are proof subcases, not independent problem variants. However the "good family with minimal suspicious edges" exchange principle is close to a standalone lemma. If anything is extracted, it should be a lemma about eliminating suspicious edges by tree exchange, not a relation between the two cases.

## Rejected candidates

### `imo-1991-sl9-min-degree-for-k6`

Classification: `reject`.

Reason: the numeric `N=1991` statement and the generalized `d_6(N)` graph formulation are not two hidden contest variants in the original card. The proof is the same Turan/minimum-degree argument plus sharpness by the balanced 5-partite construction. Treat as one theorem/application, not a pair relation.

### `imo-1992-p3-nine-points-partial-ramsey`

Classification: `reject`.

Reason: exact threshold proof with a 32-edge avoiding construction and a 33-edge forcing argument. Both halves are necessary for one exact answer; they are not separate self-contained variants.

### `rmm-2017-p5-sieve-sticks-bipartite-matching`

Classification: `reject`.

Reason: the horizontal-stick upper construction and Hall/matching lower bound are standard sides of one exact-value proof. The graph formulation is a translation, not a second hidden variant.

### `memo-2025-t4-toll-complete-graph`

Classification: `reject`.

Reason: equal weights give the upper obstruction, and the minimal 100-part partition gives the guarantee. This is a normal minimax exact-bound proof, not two independent formulations. The partition argument may be useful internally, but the first-pass candidate should not become a relation.

### `imo-1989-sl14-seven-points-triangle-cover`

Classification: `reject`.

Reason: Mantel lower bound plus complement `K_{3,4}` attainability is the standard estimate-plus-example structure for one minimum. No independent hidden statement.

### `imo-1999-c5-grid-total-domination`

Classification: `reject`.

Reason: the two color/diagonal lower-bound halves are symmetric components of one proof, and the construction is the matching exactness example. No standalone variant relation.

### `imo-2004-c3-delete-edge-from-4cycle`

Classification: `reject`.

Reason: invariant lower bound plus explicit deletion sequence is one exact-minimum proof. The connected/non-bipartite invariant and the construction are not separate problem variants.

### `imo-2005-c8-noncrossing-diagonals-crossings`

Classification: `reject`.

Reason: upper estimate by pairing ear diagonals and construction reaching the bound are ordinary exact extremal halves. The ear-pairing estimate is a proof lemma at most, not a false-friend or paired-variant relation between statements.

## Summary

Accepted relation clusters:
- `false_friend`: IMO 1996 C1 split, IMO 1998 C6 split, IMO 2024 C4 split, EGMO 2025 P5 split.
- `pair_variant`: none from this batch.

Non-relation follow-up:
- `lemma_split`: RMM 2023 P6 only.

Everything else from the first-pass candidate list is rejected as ordinary exact-bound structure, proof subcases, or graph reformulation rather than multiple independent hidden formulations.

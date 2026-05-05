# False friends first pass: international IMO/EGMO/APMO/MEMO/RMM

Scope: only `data/problems/imo`, `data/problems/egmo`, `data/problems/apmo`, `data/problems/memo`, `data/problems/rmm`.

Pass type: wide, low-reasoning scan. I looked for explicit multi-part structure, separate parameter regimes, `prove/find/construct` mixtures, exact-bound proofs with separate lower/upper or construction parts, large independent cases in solutions, and graph reformulations that look like they split into standalone statements. I did not edit problem cards.

## Strong candidates

- `imo-1996-c1-grid-knight-reachability-*`
  - Files:
    - `data/problems/imo/imo-1996-c1-grid-knight-reachability-divisible-2-or-3.yaml`
    - `data/problems/imo/imo-1996-c1-grid-knight-reachability-r73-path.yaml`
    - `data/problems/imo/imo-1996-c1-grid-knight-reachability-r97-impossible.yaml`
  - Seen split: three cards already encode different regimes of the same original knight-reachability problem: divisibility obstruction for `r` divisible by 2 or 3, a positive/path case `r=73`, and an impossible case `r=97`.
  - Hypothesis: `ложный друг` / `парный вариант` mix. The parameter variants look close externally, but positive construction and invariant obstruction are different enough that the pair should be checked carefully.

- `imo-1998-c6-*`
  - Files:
    - `data/problems/imo/imo-1998-c6-k-le-4-rainbow-edges-impossible.yaml`
    - `data/problems/imo/imo-1998-c6-k5-rainbow-edges-construction.yaml`
    - `data/problems/imo/imo-1998-c6-k-ge-6-one-factorization.yaml`
  - Seen split: separate parameter regimes `k <= 4`, `k = 5`, `k >= 6`; filenames and goals indicate impossibility, special construction, and one-factorization construction.
  - Hypothesis: `ложный друг`. Same surface object, but the small impossible range, exceptional `k=5`, and large construction regime probably need materially different ideas.

- `imo-2024-c4-turbo-grid-monsters-*`
  - Files:
    - `data/problems/imo/imo-2024-c4-turbo-grid-monsters-two-attempts-lower-bound.yaml`
    - `data/problems/imo/imo-2024-c4-turbo-grid-monsters-three-attempts-strategy.yaml`
  - Seen split: original/game formulation appears split into two-attempt lower bound and three-attempt winning strategy.
  - Hypothesis: `ложный друг`. Same game and board language, but lower-bound/adversary side versus constructive strategy side are distinct proof tasks.

- `egmo-2025-p5-rotating-arrows-*`
  - Files:
    - `data/problems/egmo/egmo-2025-p5-rotating-arrows-even-dynamic-cycle.yaml`
    - `data/problems/egmo/egmo-2025-p5-rotating-arrows-odd-parity.yaml`
  - Seen split: even/odd cases are separate cards; names indicate dynamic-cycle argument for even and parity obstruction for odd.
  - Hypothesis: `ложный друг`. The cases are adjacent but likely use genuinely different mechanisms.

- `imo-1991-sl9-min-degree-for-k6`
  - File: `data/problems/imo/imo-1991-sl9-min-degree-for-k6.yaml`
  - Seen split: graph formulation asks for the general function `d_6(N)`, then additionally asks for the concrete case `N=1991` and exactness.
  - Hypothesis: `парный вариант`. General Turan-type threshold and the numeric exact case are closely related, but could be represented as paired variants if one wants to separate general theorem from computation/example.

## Medium candidates

- `imo-1992-p3-nine-points-partial-ramsey`
  - File: `data/problems/imo/imo-1992-p3-nine-points-partial-ramsey.yaml`
  - Seen split: solution has a very explicit lower construction on 32 colored edges and an upper argument for 33 colored edges using `K_6 -> monochromatic triangle`.
  - Hypothesis: `парный вариант`. Exact threshold proof naturally has two independent halves: construction avoiding the pattern and forcing above the threshold.

- `rmm-2023-p6-colored-spanning-tree-suspicious-edges`
  - File: `data/problems/rmm/rmm-2023-p6-colored-spanning-tree-suspicious-edges.yaml`
  - Seen split: solution defines a good family/minimal suspicious edges, then branches into `Случай 1: B(C)=b` and `Случай 2: B(C)>b`, with different exchange operations.
  - Hypothesis: `нужно проверить`. The two cases are parallel exchange arguments, so they may be paired variants inside one proof rather than separate problem variants.

- `rmm-2017-p5-sieve-sticks-bipartite-matching`
  - File: `data/problems/rmm/rmm-2017-p5-sieve-sticks-bipartite-matching.yaml`
  - Seen split: asks to find all possible values of `m(A)`; solution has immediate upper construction by horizontal sticks and lower bound via Hall matching.
  - Hypothesis: `парный вариант`. Construction and lower-bound certificate are distinct enough for future paired-variant audit, though still a standard exact-value structure.

- `memo-2025-t4-toll-complete-graph`
  - File: `data/problems/memo/memo-2025-t4-toll-complete-graph.yaml`
  - Seen split: solution explicitly has upper estimate for equal weights and lower estimate via partition minimizing internal weight.
  - Hypothesis: `парный вариант`. Same extremal value, but the witness and guarantee sides use different ideas.

## Weak candidates / standard exact-bound structure

- `imo-1989-sl14-seven-points-triangle-cover`
  - File: `data/problems/imo/imo-1989-sl14-seven-points-triangle-cover.yaml`
  - Seen split: Mantel lower bound plus explicit attainability using complement `K_{3,4}`.
  - Hypothesis: `нужно проверить`. Looks like ordinary exact-bound proof; include only if the relation type wants all estimate+example pairs.

- `imo-1999-c5-grid-total-domination`
  - File: `data/problems/imo/imo-1999-c5-grid-total-domination.yaml`
  - Seen split: lower bound has two color/diagonal halves, then a matching construction for both colors.
  - Hypothesis: `парный вариант`. The two lower-bound halves are symmetric, while lower versus construction are independent proof tasks.

- `imo-2004-c3-delete-edge-from-4cycle`
  - File: `data/problems/imo/imo-2004-c3-delete-edge-from-4cycle.yaml`
  - Seen split: lower bound via connected/non-bipartite invariant and attainability by explicit deletion sequence.
  - Hypothesis: `парный вариант`. Standard exact extremal pair; likely not a false friend unless paired with another deletion-process card.

- `imo-2005-c8-noncrossing-diagonals-crossings`
  - File: `data/problems/imo/imo-2005-c8-noncrossing-diagonals-crossings.yaml`
  - Seen split: upper estimate of total crossings by pairing diagonals, then construction reaching the bound.
  - Hypothesis: `парный вариант`. Different halves, but they are normal upper/lower sides of one extremal result.

## Explicit non-candidates from reviewed batches

- Reviewed all 4 `data/problems/egmo` cards. Besides the split `egmo-2025-p5-*`, `egmo-2016-p3-blue-cells-bipartite-incidence.yaml` and `egmo-2022-p5-domino-parity-bipartite-matching.yaml` did not show an obvious multi-part or paired-variant structure in this pass.

- Reviewed all 3 `data/problems/apmo` cards:
  - `apmo-2005-p4-firefighters-grid-spread.yaml`
  - `apmo-2010-p3-common-acquaintance-extremal.yaml`
  - `apmo-2016-p4-dreamland-28-step-coloring.yaml`
  No explicit `(a)/(b)`, parameter split, or clear two-statement structure surfaced in this wide scan.

- Reviewed all 4 `data/problems/memo` cards. Besides the exact-bound split in `memo-2025-t4-toll-complete-graph.yaml`, the files `memo-2021-i2-bishop-circuit-forest.yaml`, `memo-2022-t4-teleport-table-reachability.yaml`, and `memo-2025-i2-ruby-rooks-two-step-reachability.yaml` did not show an obvious candidate signal.

- Reviewed all 5 `data/problems/rmm` cards. Besides `rmm-2017-p5-*` and `rmm-2023-p6-*`, the files `rmm-2012-p1-sociable-sets-bipartite-parity.yaml`, `rmm-2013-p2-tester-pair-endomorphism-digraph.yaml`, and `rmm-2016-p6-ab-tree-termination-semiinvariant.yaml` did not show an obvious split in this pass.

- In the IMO batch, many cards have a single proof idea despite normal proof subcases or invariant setup. I did not list every such file as a non-candidate to keep the audit useful; the strong IMO nontrivial signals are the existing multi-card parameter splits and the exact-bound/construction pairs listed above.

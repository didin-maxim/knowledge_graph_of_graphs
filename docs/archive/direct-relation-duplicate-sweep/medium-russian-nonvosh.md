# Direct relation duplicate sweep: medium Russian non-VOSH

Scope B: `spbmo`, `mmo`, `school239`, `tournament-cities`, `utyum`, `yumt`, `fyum`, `kolmogorov`; VOSH excluded. Checked direct relations with `distance: 1` where both endpoints are in scope. Below are candidates that look closer than a shared motif: exact reprint, same parametrized problem, or the same task with a small level-dependent add-on.

## Candidates

### `fyum-2011-tur1a-p5` <-> `fyum-2011-tur1b-p5`

- relation: `rel-fyum-2011-tur1a-p5-tur1b-p5-rainbow-counterexample`; type `same_motif`; distance `1`; relation confidence `0.98`.
- statement comparison: essentially identical. Both ask whether every connected, 2-edge-connected graph of diameter at most 2 admits a 4-edge-coloring such that any two vertices are joined by a rainbow path. The wording differs only typographically: "все ребра в котором разного цвета" vs "все ребра в котором покрашены в разные цвета".
- solution/method comparison: identical counterexample with vertices `A`, `B_1,...,B_17`, `C_1,...,C_17`; use the same pigeonhole argument on 16 possible color-pairs at the `B_i`.
- confidence: `0.99` exact duplicate/reprint candidate.
- high-check question: Are `tur1a` and `tur1b` intended to be separate variants in the source, or is one an accidental duplicate import of the same FYUM problem?

### `kolmogorov-2008-round-2-first-junior-league-problem-1` <-> `kolmogorov-2008-round-2-second-league-problem-2`

- relation: `rel-after-tags-kolm-2008-recoloring-counting-pair`; type `same_motif`; distance `1`; relation confidence `0.93`.
- statement comparison: same wheel-graph/firms problem, with only the number of rim cities changed from `10` to `100`. Both ask how many ways to split all roads between two firms so that each firm's roads connect all cities.
- solution/method comparison: same counting of two-color edge colorings of a wheel; each color class must be a spanning tree, and the rim edges are forced after choosing a nonconstant spoke coloring.
- confidence: `0.96` same parametrized problem candidate.
- high-check question: Should the two fixed-size versions be represented as separate league instances, or collapsed under the parametrized wheel problem already present in the same Kolmogorov cluster?

### `kolmogorov-2008-round-2-first-junior-league-problem-1` <-> `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1`

- relation: `rel-kolm-2008-wheel-first-junior-first-league`; type `same_motif`; distance `1`; relation confidence `0.86`.
- statement comparison: the first endpoint is the concrete `10`-city wheel story; the second is the abstract `W_n` formulation of the same two-color connected wheel problem.
- solution/method comparison: same double-counting/tree argument and the same forced coloring of rim edges from spoke colors.
- confidence: `0.94` parametrized duplicate candidate.
- high-check question: Is the `W_n` card meant to be the canonical generalization of the concrete `10`-city card, or a separate source-level problem that should remain linked but not deduplicated?

### `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1` <-> `kolmogorov-2008-round-2-second-league-problem-2`

- relation: `rel-kolm-2008-wheel-first-second-league`; type `same_motif`; distance `1`; relation confidence `0.90`.
- statement comparison: abstract `W_n` version vs the concrete `100`-city wheel story. Same object and same requirement: edge 2-coloring so both color subgraphs are connected.
- solution/method comparison: same wheel counting method; the concrete `100` case is obtained by substituting `n=100` in the parametrized solution.
- confidence: `0.94` parametrized duplicate candidate.
- high-check question: If the abstract card remains, should both concrete `10` and `100` cards point to it as source instances rather than to each other?

### `kolmogorov-2018-team-olympiad-juniors-problem-6` <-> `kolmogorov-2018-team-olympiad-seniors-problem-5`

- relation: `rel-kolm-2018-mobility-junior-senior`; type `specialization`; distance `1`; relation confidence `0.98`.
- statement comparison: same bus/rail mobility problem. Junior version uses `20` cities and regions of size at most `10`; senior version uses `2018` cities and regions of size at most `1009`. Definitions of `A`, `B`, and the requested minimum of `A+B` are otherwise the same.
- solution/method comparison: same four-part decomposition of two extremal regions and same extremal construction; constants scale from `10` to `1009`.
- confidence: `0.95` same parametrized problem candidate.
- high-check question: Is there an intended general theorem for `2m` cities and regions of size at most `m`, with these two as league-specific substitutions?

### `kolmogorov-2013-team-olympiad-juniors-problem-7` <-> `kolmogorov-2013-team-olympiad-seniors-problem-8`

- relation: `rel-kolm-2013-chromatic-team-junior-senior`; type `same_motif`; distance `1`; relation confidence `0.83`.
- statement comparison: same setup with vertex partition `A,B,C`, no edges between `A` and `C`, and colorability of `A union B` in `k` colors and `B union C` in `n` colors. Junior asks to prove colorability in `k+n-1`; senior asks for the minimal guaranteed number.
- solution/method comparison: the senior solution contains the junior upper-bound proof verbatim in method, then adds the lower-bound/sharpness part.
- confidence: `0.86` borderline duplicate/extension candidate, not a pure reprint.
- high-check question: Should this be modeled as "senior problem extends junior by asking sharpness", rather than a duplicate relation?

## Near Misses Not Promoted

- `yumt-2017-start-first-round1-problem3` <-> `yumt-2017-start-high-round1-problem3`: very similar game statement, but the allowed move changes from one road to at most two roads and the extremal answer changes, so this is a variant rather than duplicate.
- `spbmo-2010-9-p5-k2010-cycle-game` <-> `spbmo-2010-11-p3-k2009-long-cycle-game`: same maker-breaker game motif, but target cycle length, complete graph size, and construction differ substantially.
- `mmo-2011-firms-programmers-geniuses` <-> `tc-2011-programmers-connected-hiring-game`: same hiring game setup, but parameters `4/3` vs `11/10` and constructions differ; keep as paired variant.

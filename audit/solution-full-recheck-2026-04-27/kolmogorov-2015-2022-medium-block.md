# Kolmogorov 2015-2022 Medium Audit

Date: 2026-04-27.

Scope:

- `data/problems/kolmogorov/kolmogorov-2015-*.yaml`
- `data/problems/kolmogorov/kolmogorov-2016-*.yaml`
- `data/problems/kolmogorov/kolmogorov-2017-*.yaml`
- `data/problems/kolmogorov/kolmogorov-2018-*.yaml`
- `data/problems/kolmogorov/kolmogorov-2019-*.yaml`
- `data/problems/kolmogorov/kolmogorov-2021-*.yaml`
- `data/problems/kolmogorov/kolmogorov-2022-*.yaml`

## Fixed / Cleared

Removed `tools/audit_rules.py` red flags in the scoped Kolmogorov block by replacing external-solution narration in solution titles/text, removing handwave markers where the local argument was already present, and deleting restored-TeX rubric tails in two 2022 entries.

Entries left as `ai_checked` after this pass:

- `kolmogorov-2015-individual-olympiad-juniors-problem-7#sol-official-compressed`
- `kolmogorov-2015-round-2-graph-coloring-problem#sol-official-compressed`
- `kolmogorov-2015-round-3-missionaries-and-cannibals-problem#sol-official-compressed`
- `kolmogorov-2017-individual-olympiad-seniors-problem-7#sol-official-compressed`
- `kolmogorov-2017-team-olympiad-juniors-problem-6#sol-official-compressed`
- `kolmogorov-2017-team-olympiad-seniors-problem-5#sol-official-compressed`
- `kolmogorov-2018-team-olympiad-juniors-problem-6#sol-official-compressed`
- `kolmogorov-2018-team-olympiad-seniors-problem-5#sol-official-compressed`
- `kolmogorov-2019-team-olympiad-juniors-problem-8#sol-official-compressed`
- `kolmogorov-2021-individual-olympiad-seniors-problem-1#sol-official-compressed`
- `kolmogorov-2021-individual-olympiad-seniors-problem-5#sol-official-compressed`
- `kolmogorov-2021-round1-second-league-problem-10#sol-official-compressed`
- `kolmogorov-2021-team-olympiad-seniors-problem-5#sol-official-compressed`
- `kolmogorov-2022-individual-seniors-p2-cycle-arrangements#sol-official-restored`
- `kolmogorov-2022-round1-third-binary-strings-pairing-graph#sol-official-restored`
- `kolmogorov-2022-round2-high-colored-integers-infinite-tree#sol-official-restored`
- `kolmogorov-2022-round2-juniors-hamiltonian-path-parity#sol-official-restored`
- `kolmogorov-2022-round2-second-third-red-blue-k10-triangles#sol-official-restored`
- `kolmogorov-2022-round4-high-airport-walk-parity#sol-official-restored`
- `kolmogorov-2022-round4-high-maximum-length-tree-diameter-circles#sol-official-restored`

## Hard / Backlog

- `kolmogorov-2015-round-4-spies-and-opergroups-problem#sol-official-compressed`
  - reason: The current text is a reconstruction plan for the spy graph, but the recognition of singleton operation groups and the reconstruction of adjacency from distance classes are not proved locally.
  - needed: Full official argument for identifying a singleton/non-cut vertex and the class-by-class recovery of all neighbors, or a new self-contained reconstruction proof.
  - next_agent: Fetch/check the cited local archive pages `tur4_19.pdf` and `tur4_19sol.pdf`, then expand the recognition/reconstruction lemmas before restoring `ai_checked`.

- `kolmogorov-2016-individual-olympiad-juniors-problem-7#sol-official-compressed`
  - reason: The blue/red arrow iteration is described, but the invariants proving termination, independence of the selected set, and coverage of every non-selected vertex are not proved.
  - needed: Official solution or a complete lemma for the iterative process.
  - next_agent: Use the cited `lichol20.pdf` source and write the invariant proof explicitly.

- `kolmogorov-2016-team-olympiad-juniors-problem-6#sol-official-compressed`
  - reason: The upper bound asserts a 12-coloring of the distance graph on the 2017-gon, and the lower bound compresses the pigeonhole/chain step.
  - needed: Explicit 12-coloring and a full lower-bound lemma for the relevant power of the cycle.
  - next_agent: Reconstruct the coloring by residues/blocks, then prove the chain-length lower bound without a hidden graph-coloring assertion.

- `kolmogorov-2021-round1-second-league-problem-8#sol-official-compressed`
  - reason: The key counting step is summarized as a lower bound on `sum c_i`; the classification of vertices in color components is not expanded.
  - needed: Complete official count showing `sum c_i >= 2n - 1` under the contrary assumption.
  - next_agent: Check `2_liga_1_tur_resheniya_pdf.txt`, page 3, and transfer the missing classification/count.

- `kolmogorov-2022-round1-high-edge-count-permutation-nonedges#sol-official-restored`
  - reason: After removing import/rubric tails, the induction still has a gap in extending the permutation when two leaves lie in different tree components.
  - needed: Complete induction for the complement graph with at most `n-2` edges.
  - next_agent: Find the original 2022 round 1 high-league solution and fill the two-leaf extension case.

- `kolmogorov-2022-round4-second-third-even-degree-odd-walks#sol-official-restored`
  - reason: The parity proof is not fully self-contained; the old text also mixed notation and used the typo-like term `доходы`.
  - needed: Official proof or a fresh complete parity/linear-algebra argument for even-degree graphs and odd walk counts.
  - next_agent: Compare against the high-league airport-walk parity solution and decide whether the same argument can be specialized safely.

## Validation

- Scoped parse of the target Kolmogorov 2015-2022 JSON/YAML files: OK, 29 files.
- Scoped `tools/audit_rules.py` filter for this block: OK, no warnings.
- `python tools/validate.py`: OK, 333 problems, 386 relations, 9 comments, 353 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools/check_links.py`: OK, 375 internal routes, 353 external source URLs syntactically valid.

USAMO 2023 P3 was not edited. It parsed successfully as the gate for running the global checks.

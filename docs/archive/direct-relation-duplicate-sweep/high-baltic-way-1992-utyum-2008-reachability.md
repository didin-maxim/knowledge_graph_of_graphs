# High verification: Baltic Way 1992 P14 vs UTYUM 2008 directed cities

Candidate from `medium-international.md`:

- `baltic-way-1992-p14-mother-vertex-reachability`
- `utyum-2008_tur4_31_6_directed_cities`

## Verdict

Classification: `prerequisite/theorem-instance`.

Confidence: high.

Not `same_problem/generalize`: the two tasks are not identical up to parameter changes and do not have the same solution after only changing numbers. Baltic Way 1992 asks for a single mother vertex in any finite directed reachability-comparable graph. UTYUM 2008 asks, on `2m + 1` vertices, for a vertex with at least `m` reachable vertices in both directions.

Not `paired_variant`: the overlap is stronger than a loose sibling variant, because the Baltic Way statement is a lemma-level fact used inside one UTYUM solution.

Not `false_friend`: the solutions are not unrelated. The reachability lemma is genuinely present in the UTYUM proof, in dual form.

Positive classification: Baltic Way 1992 is the standalone one-sided reachability theorem/lemma. UTYUM 2008 is a stronger median/two-sided application; one official solution route uses the same lemma on a subset of vertices, while another route uses the reachability closure and a Hamiltonian path.

## Evidence Checked

Cards:

- `data/problems/baltic-way/baltic-way-1992-p14-mother-vertex-reachability.yaml`: statement at line 46 asks to prove existence of a city from which all others are reachable under pairwise reachability comparability. The solution at line 76 is the maximal reachable set proof.
- `data/problems/utyum/utyum-2008_tur4_31_6_directed_cities.yaml`: original statement at line 41 asks for a city with at least 1003 reachable outgoing and incoming cities among 2007 cities. The graph-theory reformulation at line 58 generalizes this to `2m + 1` vertices and `m` in each direction. The solution at line 80 gives two approaches: reachability closure/Hamiltonian path, and an iterative argument using the dual mother-vertex lemma on a subset.

Sources:

- `src-baltic-way-1992-official-solutions` is source-verified official archive metadata in `data/sources/sources.yaml` at line 301.
- `src-utyum-2008_tur4_31_6_directed_cities-official` is source-verified official archive metadata in `data/sources/sources.yaml` at line 3900.

Relation:

- Existing relation `rel-baltic-way-1992-utyum-2008-directed-reachability-median` in `data/relations/relations.d/base-done-review-baltic-cmo-spbmo.yaml` is already `type: prerequisite`, `distance: 1`, `status: ai_checked`, `confidence: 0.9`.
- The relation text accurately says Baltic Way proves the mother-vertex lemma and UTYUM uses the dual form for a subset of vertices. This matches the checked solutions.

## Future Data Edit Plan

No data edits are required for this candidate.

If/when data editing is allowed, keep both problem cards separate and keep the existing `prerequisite` relation. Do not mark these as duplicates and do not merge either card. Optional nonessential cleanup would be to raise relation confidence slightly or add an editorial note to the UTYUM card saying that the second solution uses the dual Baltic Way mother-vertex lemma, but the current relation already captures the needed database-level fact.

# Direct relation duplicate sweep: medium VOSH / all-union

Date: 2026-05-05

Scope C: `data/problems/vosh`, `data/problems/all-union`, the problems.ru-derived VOSH cards already present in this subtree, and direct relations touching these ids. Read-only with respect to `data/`.

## Method notes

- Enumerated 22 in-scope problem ids: 18 VOSH cards and 4 all-union cards.
- Checked direct relations touching those ids across `data/relations/relations.d`.
- Checked shared source ids, especially `src-problems-*`, to catch older problems.ru-derived overlaps.
- Read the relevant `docs/archive/vosh-official-sweep/deep/*` notes for source/provenance and prior relation decisions.
- Tool limitation: `tools/source_collisions.py` and later full `tools/suggest_relations.py` runs currently abort on pre-existing invalid JSON in `data/problems/baltic-way/baltic-way-1997-p19a-prime-edge-disjoint-hamiltonian-cycles.yaml` (`Invalid \escape`, line 113). Earlier targeted `suggest_relations.py` runs did complete for `vosh-2000-01-final-universal-acquaintance`, `vosh-2010-11-final-nonbreakable-company`, and `vosh-2013-14-regional-even-rows-columns`.

## Strong Candidates

No strong local duplicate/reprint pair found among in-scope cards and direct relations.

The strongest source-level overlaps are intentionally not duplicate cards:

- `shortest-odd-cycle-external-neighbor-bound` and `vosh-2010-11-final-nonbreakable-company` share `src-problems-116640`, but the first is an extracted lemma from the VOSH solution. Existing relation: `prerequisite`, distance `1`, confidence `0.98`. Keep as non-duplicate.
- `tree-t-join-parity-lemma` and `vosh-2013-14-regional-even-rows-columns` share `src-problems-64633`, but the first is an extracted T-join/parity tool from the VOSH solution. Existing relation: `prerequisite`, distance `1`, confidence `0.98`. Keep as non-duplicate.
- `vosh-2000-01-final-tree-leaves-bridge-proof` matches external problems.ru card `109740`, but no separate local problems.ru problem card was found. This is a source/reprint provenance note, not a local duplicate.

## Medium Candidates

- `vosh-2000-01-final-universal-acquaintance` vs `all-union-1981-final-9-football-independent-triple`: suggested as a close `same_motif` candidate by local relation scoring. Both are small social/sports graph extremal problems with complement/Ramsey flavor. They are not duplicates: 2000/01 asks for a universal acquaintance under clique/independent-set constraints, while 1981 asks for three teams with no mutual games after 8 full rounds.
- `vosh-2010-11-regional-warehouses-cement-routing` vs `vosh-2022-23-regional-connected-country-cut`: existing `same_motif`, distance `2`, status `needs_human_review`. Both use induction on connected graphs via deleting a local part, but the goals differ: weight transport in `n-1` moves vs a coloring/cut inequality. Not a duplicate.
- `vosh-2025-26-regional-common-neighborhood-red-pairs` vs `vosh-2008-regional-bureaucrats-common-neighborhood`: existing `same_motif`, distance `3`, confidence `0.74`. Both are Russian social-graph common-neighborhood double-counting tasks, but 2025/26 is a sharp regular-graph bound and 2008 is tripartite Ramsey-style averaging. Not a duplicate.
- `vosh-2014-15-regional-grid-rainbow-rectangle` vs `usamo-1976-p1-monochromatic-rectangle-bipartite`: existing `same_motif`, distance `2`, confidence `0.86`. Same row-column bipartite/rectangle dictionary, but one forces a rainbow rectangle with many colors and the other a monochromatic rectangle in two colors. Not a duplicate.

## Weak Candidates

- `all-union-1987-final-9-tournament-score-squares` vs `polish-mo-2022-ii-p6-badminton-euler-cycles`, `imo-2010-c5-bad-company-tournament`, and `cmo-2006-p4-cycle-triplets-tournament`: existing `same_motif` tournament-score links. They share win/loss or tournament degree language, but the statements and proof targets differ substantially.
- `vosh-1992-zonal-air-travel-one-city-redundant` vs `baltic-way-1992-p14-mother-vertex-reachability`: existing `prerequisite`, distance `2`. The VOSH card is the unreachable-set lemma; Baltic Way is a stronger mother-vertex application. Not a duplicate.
- `vosh-2017-18-regional-friendship-triangle-factor` vs `cmo-2020-p5-friendship-induced-subgraphs` and `imc-2011-day2-p2-tripartite-married-triples`: existing `same_motif` links around triangle factors/social graph extremal arguments. Goals and machinery differ.
- `vosh-2018-19-final-shirt-recoloring` vs `five-color-theorem` / `no-two-color-cycle-edge-bound`: existing motif links through Kempe-style recoloring and two-color subgraph counting. These are tools/motifs, not duplicate problem statements.
- `vosh-2022-23-final-optimal-road-networks` vs `putnam-2013-b5-functions-iterate-into-roots`: existing rooted-forest `same_motif`, distance `2`. Shared forest encoding, different optimization/counting problems.
- `vosh-2025-26-final-regions-friendship-coloring` vs `five-color-theorem`, `brooks-theorem`, and `rmm-2012-p1-sociable-sets-bipartite-parity`: current direct links are broad color/recoloring or parity motifs, mostly `needs_human_review`. No duplicate signal found.

## Non-Duplicates Worth Noting

- The all-union source ids `src-djvuonline-vseross-9-1997` and `src-mathru-vsesoyuznye-1988` are shared by all four all-union cards because they come from the same collection/OCR source, not because the problems duplicate each other.
- `src-kvant-digital-1992-10-vseros-math` is shared by the two 1992 zonal VOSH air-travel cards; they are different problems from the same publication.
- `src-vosh-1993-2006-mccme-book` is shared by `vosh-2000-01-final-tree-leaves-bridge-proof` and `vosh-2005-06-final-dominoes-three-color-neighbors`; they are different VOSH final problems from the same MCCME collection.
- `src-vosh-2025-26-regional-day2-official` is shared by the two 2025/26 regional day-2 social-graph cards; they are adjacent official problems with related social graph language, not duplicates.
- Existing direct relation coverage is mostly motif/prerequisite hygiene rather than duplicate mapping. I did not see any `reprint`, `reformulation`, or `solution_transfer` relation touching scope that looked misclassified as a weaker relation.

## Follow-Up Suggestions

- After the invalid escape in `data/problems/baltic-way/baltic-way-1997-p19a-prime-edge-disjoint-hamiltonian-cycles.yaml` is fixed by the owning pass, rerun `tools/source_collisions.py` for all 22 scope ids and re-run `tools/suggest_relations.py` for the new VOSH/all-union files that were not covered by the earlier deep notes.
- Consider a provenance-only note for external problems.ru card `109740` if the project wants explicit tracking of official VOSH vs problems.ru mirror pages without creating duplicate problem cards.

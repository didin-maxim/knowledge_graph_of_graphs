# Cross-link pass: coloring / extremal graph motifs

Scope: synchronized metadata-driven pass over corrected/deep-done graph cards with coloring, recoloring, Kempe chains, Brooks, Turan/Zykov, extremal choice, clique, and independent-set motifs.

Files changed:

- `data/relations/relations.d/metadata-pass-cross-links-coloring-extremal.yaml`
- `audit/metadata-pass/cross-link-coloring-extremal.md`

Problem YAML was not edited.

## Inputs checked

- Existing relation files under `data/relations/relations.yaml` and `data/relations/relations.d/*.yaml`.
- Updated metadata fields in problem cards: `problem_profile.objects`, `problem_profile.methods`, `properties.central_method`, `tags`, `solutions[].standard_idea_ids`, and editorial review/relations status.
- Relation endpoint pairs were checked as unordered pairs against `tools.lib.load_relations()` to avoid adding duplicate cross-links.

## Added relations

Added 10 motif links:

1. `rel-color-extremal-kolm-2008-2013-greedy-recoloring`
   - KOLM 2008 team juniors problem 5 -> KOLM 2013 team seniors problem 8
   - Shared local recoloring / greedy-extremal coloring motif.

2. `rel-color-extremal-turan-imo-2012-independent-set`
   - Turan theorem -> IMO 2012 C7
   - Independent-set extremal viewpoint; marked for human review because IMO C7 uses Caro-Wei/averaging rather than Turan directly.

3. `rel-color-extremal-turan-utyum-2021-no-k5`
   - Turan theorem -> UTYUM 2021 no-K5 acquaintances
   - Forbidden-clique extremal construction motif.

4. `rel-color-extremal-kolm-2002-utyum-2021-forbidden-clique`
   - KOLM 2002 team seniors problem 8 -> UTYUM 2021 no-K5 acquaintances
   - Forbidden-clique/extremal graph model motif.

5. `rel-color-extremal-brooks-shortest-odd-cycle`
   - Brooks theorem -> shortest odd cycle external-neighbor bound
   - Odd-cycle/clique-exception obstruction bookkeeping.

6. `rel-color-extremal-ramsey-r33-kolm-2022-k10`
   - Ramsey R(3,3) -> KOLM 2022 red-blue K10 triangles
   - Two-colored complete-graph triangle counting motif.

7. `rel-color-extremal-imo-1998-kolm-2022-colored-complete-graphs`
   - IMO 1998 C6 -> KOLM 2022 red-blue K10 triangles
   - Colored complete-graph degree/local-count motif.

8. `rel-color-extremal-color-reduction-apmo-2016`
   - Color-reduction lemma -> APMO 2016 P4
   - Coloring reduction / auxiliary coloring motif.

9. `rel-color-extremal-brooks-fyum-2009-tur2a`
   - Brooks theorem -> FYUM 2009 tur2a P4
   - Minimal-counterexample proper coloring and two-color-subgraph motif.

10. `rel-color-extremal-brooks-yumt-2015-no-k5-chromatic`
    - Brooks theorem -> YUMT 2015 grand final problem 5
    - No-K5 high-chromatic obstruction motif; kept as needs_human_review because the primary card is archival.

## Duplicate checks

Skipped existing pairs found during audit:

- KOLM 2007 chromatic-number problem <-> KOLM 2013 team juniors problem 7: `rel-kolm-deep-2007-chromatic-2013-team-junior`.
- KOLM 2008 individual juniors problem 8 <-> KOLM 2008 individual seniors problem 5: `rel-kolm-2008-bipartite-coloring-pair`.
- Turan theorem <-> IMO 1991 SL9: `rel-turan-imo-1991-sl9`.
- Five-color theorem <-> VOSH 2025/26 regions coloring: `rel-five-color-vosh-2025-26-local-recoloring`.
- Brooks theorem <-> APMO 2016 P4 already exists, so the new APMO coloring relation was attached to the color-reduction lemma instead.

## Validation

Passed:

- `python tools/validate.py`
  - `OK: 328 problems, 384 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.`
- `python tools/check_links.py`
  - `OK: 370 internal routes, 349 external source URLs syntactically valid.`

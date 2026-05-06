# External theorem audit, group F, 2026-05-06

Scope: current `data/problems/**/*.yaml` cards whose `editorial.solution_classification.type` contains `external_theorem`, `heavy_external`, or `ai_complete_external_theorem`, plus cards with explicit `external_theorem_ids` or `problem_profile.methods: external_theorem`.

Important policy note: external-theorem solutions should not be deleted merely because a school solution exists or can be added. The preferred hygiene is: keep the self-contained/olympiad solution as the main route, and keep the short external-theorem route when it is genuinely useful, with an explicit label, source, and relation to the theorem card/reference.

## Summary

- Current remaining external-theorem references after this pass: 15 cards.
- Metadata-only fixes made in this pass: canonicalized theorem ids for Turan/Hall/Menger/Konig references, added explicit external ids for Kolmogorov 2021 and YUMT 2022, and corrected Kolmogorov 2010 from a false heavy-external label to official self-contained.
- Parse hygiene fixed while validating: several unrelated/concurrent JSON escaping issues were repaired only at the character/string level.

## 1. School theorem-card already exists

Core school theorem/tool cards present and suitable as explicit relation targets:

- `hall-marriage-theorem`
- `konig-vertex-cover-theorem`
- `konig-line-coloring-bipartite`
- `brooks-theorem`
- `dirac-theorem`
- `ore-theorem`
- `mantel-theorem`
- `turan-theorem`
- `ramsey-theorem`, `ramsey-r33`, `ramsey-r34`, `ramsey-r35`, `ramsey-r44`
- `five-color-theorem`
- `euler-formula-planar`, `eulerian-graph-criterion`
- `menger-theorem`
- `tournament-hamiltonian-path`, `redei-odd-hamiltonian-paths-tournament`
- `robbins-strong-orientation-theorem`
- `edge-critical-bridgeless-graphs-give-critical-strong-orientations`

Current cards whose external reference now points to an existing local theorem/tool card:

| card | classification | local theorem ids | note |
|---|---|---|---|
| `imo-2021-c4-anisotropy-menger` | `official_complete_or_near_complete` with explicit external id | `menger-theorem#stmt-edge-directed` | Good hygiene: card keeps official elementary and Menger/min-cut routes; Menger is covered by a local classical tool. |
| `kolmogorov-2021-t1-critical-strong-orientation` | `disputed_external_theorem_application` | `robbins-strong-orientation-theorem`; `edge-critical-bridgeless-graphs-give-critical-strong-orientations` | Relations exist; still disputed, so keep human-review status. |
| `miklos-schweitzer-2002-p2-edge-connected-short-paths` | `ai_complete_heavy_external_theorem_application` | `menger-theorem#stmt-edge-directed` | Local Menger covers only the ordinary part; Galil--Yu remains heavy. |

Resolved by metadata cleanup / no longer in the remaining external list: `flashlight-batteries-tournament-cities-2015`, `cmo-2023-p5-cut-bound-independent-set`, `imo-1991-sl9-min-degree-for-k6`, `imo-2010-c2-flags-diagonal-matching`, `usamo-2022-p1-amber-bronze-transversal`.

## 2. Needed or created school special case

| card | needed/available special case | recommendation |
|---|---|---|
| `alternating-boundary-pairs-noncrossing-arcs` | Jordan/disk separation special case | Keep as `external_theorem_application`; consider a small school lemma for disk separation instead of invoking full Jordan curve theorem everywhere. |
| `miklos-schweitzer-2016-p2-complete-graph-collinear-edge-labels` | Gallai coloring/no-rainbow-triangle theorem | Add a local theorem/lemma card if this card is meant to be school-facing. |
| `yumt-2021-grand-round4-problem3` | Kotzig bridge theorem for unique perfect matchings | Keep explicit external label; a local matching lemma would be useful if an olympiad proof is found. |
| `yumt-2022-grand-final-problem1` | Nonseparating induced odd cycle in 4-critical graphs | Heavy theorem remains; add a school critical-graph route only if sourced. |
| `kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic` | Bondy pancyclic theorem currently has a reference card | Keep external theorem route; a school special case would need a real proof, not a label change. |

## 3. Heavy external theorem consciously left

| card | external theorem/reference | reason to leave |
|---|---|---|
| `bondy-pancyclic-theorem` | Bondy pancyclic theorem | This is itself an external theorem reference card, not a school olympiad card. |
| `kolmogorov-2014-round3-four-regular-two-100-cycles` | Pfender--Royle quartic triangle-property classification | Structural classification is too heavy for silent use. |
| `miklos-schweitzer-2002-p2-edge-connected-short-paths` | Galil--Yu short-length Menger theorem | Ordinary Menger exists locally, but the short-length strengthening is genuinely external. |
| `miklos-schweitzer-2010-p2-infinite-vertex-transitive-perfect-matching` | Infinite vertex-transitive perfect matching theorem; Aharoni strongly maximal matching theorem | Infinite matching theory is not school-level. |
| `miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees` | Shank/Goeritz/Alexander knot-theory inputs | Topological graph/knot theory; keep explicit. |
| `miklos-schweitzer-2012-p10a-knot-black-graph-at-most-three-spanning-trees` | Shank theorem, Tait/nugatory reductions, small knot classification | Heavy topology remains. |
| `miklos-schweitzer-2012-p10b-knot-black-graph-odd-spanning-trees` | Matrix Tree, Goeritz determinant, Alexander parity, Shank theorem | Valid as external solution, not school proof. |
| `miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection` | Koebe--Andreev--Thurston circle-packing theorem | Circle packing is a serious external theorem. |
| `yumt-2022-grand-final-problem1` | Krusenstjerna-Hafstrom--Toft theorem | Keep as heavy until a sourced elementary proof is added. |

## 4. False positive or context, not a solution dependency

| card | action |
|---|---|
| `kolmogorov-2010-individual-olympiad-seniors-problem-4` | Changed from `ai_heavy_external_theorem` to `official_complete_or_near_complete`: the Busch-paper mention was contextual verification of the inequality direction, not a theorem used in the proof. |

No other current 15-card external list item looked like a pure false positive. Some are disputed or incomplete, but the external theorem is genuinely part of the recorded solution route.

## 5. Both solutions useful: school plus short external theorem

Use this pattern when applicable: keep the long self-contained/official solution and add the short external-theorem solution as a separate solution with `external_theorem_application`, explicit `external_theorem_ids`, source, and relation.

Current/recommended candidates:

- `imo-2021-c4-anisotropy-menger`: keep the local Menger route; if an official self-contained olympiad proof is present or added, keep both rather than replacing either.
- `kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic`: keep the short Bondy-pancyclic application; add a school special-case proof only if it is actually supplied.
- `yumt-2022-grand-final-problem1`: keep the Krusenstjerna-Hafstrom--Toft proof as the short heavy route; add a school 3-coloring/critical-graph proof if sourced.
- `miklos-schweitzer-2002-p2-edge-connected-short-paths`: keep ordinary local Menger context and the Galil--Yu shortcut explicitly separated.
- `miklos-schweitzer-2012-p10b-knot-black-graph-odd-spanning-trees`: the current routes are both external-heavy; if a school-combinatorial parity proof is found later, keep it alongside the Shank/Goeritz route.

## All remaining external-theorem references

| card | classification | external ids / method marker |
|---|---|---|
| `alternating-boundary-pairs-noncrossing-arcs` | `external_theorem_application` | `Jordan curve theorem`; methods `jordan_curve_separation`, `planar_separation` |
| `bondy-pancyclic-theorem` | `external_theorem_reference` | method `external_theorem` |
| `imo-2021-c4-anisotropy-menger` | `official_complete_or_near_complete` | `menger-theorem#stmt-edge-directed` |
| `kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic` | `external_theorem_application` | Bondy pancyclic route via relation/reference card |
| `kolmogorov-2014-round3-four-regular-two-100-cycles` | `heavy_external_theorem_application` | `Pfender--Royle quartic triangle-property classification` |
| `kolmogorov-2021-t1-critical-strong-orientation` | `disputed_external_theorem_application` | `robbins-strong-orientation-theorem`; `edge-critical-bridgeless-graphs-give-critical-strong-orientations` |
| `miklos-schweitzer-2002-p2-edge-connected-short-paths` | `ai_complete_heavy_external_theorem_application` | `menger-theorem#stmt-edge-directed`; `Galil--Yu short-length Menger theorem` |
| `miklos-schweitzer-2010-p2-infinite-vertex-transitive-perfect-matching` | `heavy_external_theorem_application` | infinite vertex-transitive matching theorem; Aharoni strongly maximal matching theorem |
| `miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees` | `heavy_external_theorem_application` | Shank/Goeritz/Alexander parity inputs |
| `miklos-schweitzer-2012-p10a-knot-black-graph-at-most-three-spanning-trees` | `heavy_external_theorem_application` | Shank theorem; P10(b); Tait/nugatory reductions; braid classification |
| `miklos-schweitzer-2012-p10b-knot-black-graph-odd-spanning-trees` | `heavy_external_theorem_application` | Matrix Tree; Goeritz determinant; Alexander parity; Shank theorem |
| `miklos-schweitzer-2016-p2-complete-graph-collinear-edge-labels` | `external_theorem_application` | Gallai no-rainbow-triangle coloring lemma/theorem |
| `miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection` | `heavy_external_theorem_application` | Koebe--Andreev--Thurston circle-packing theorem |
| `yumt-2021-grand-round4-problem3` | `classical_external_lemma_application` | Kotzig bridge theorem for unique perfect matchings |
| `yumt-2022-grand-final-problem1` | `heavy_external_theorem_application` | Krusenstjerna-Hafstrom--Toft nonseparating induced odd cycle theorem |

## Recommendations

- Do not auto-delete external theorem solutions. Keep them when they give a meaningful short route, but make the label/source/relation explicit.
- Prefer canonical local ids in `external_theorem_ids` when a theorem-card exists; use human-readable theorem names only for genuinely absent external references.
- For school-facing cards, prioritize small local special-case theorem cards for Jordan separation, Gallai no-rainbow-triangle coloring, and Kotzig bridge theorem before changing solution classifications.
- Leave the Miklos Schweitzer knot/circle-packing/infinite-matching cards explicitly heavy unless a sourced elementary route is added.

## Validation

- Targeted JSON parse passed for `data/problems/**/*.yaml` and `data/relations/**/*.yaml`: 0 parse errors.
- `python tools/validate.py`: passed after integration cleanup.
- `python tools/check_links.py`: passed after integration cleanup.
- `git diff --check`: passed; Git only reported expected LF-to-CRLF working-copy warnings on Windows.

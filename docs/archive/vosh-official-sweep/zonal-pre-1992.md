# Zonal VMO/VsOSh Pre-1992 Sweep

Date: 2026-05-05

Scope: zonal/penultimate Vserossiyskaya-stage materials before and around 1992, prioritizing official or primary archives. `data/` remains the source of truth.

## Sources Checked

- `https://olympiads.mccme.ru/vmo/` - VMO/MCCME index. It records the older structure with the IV stage as "окружной, зональный" before the later four-stage model, and links to the winners page and MCCME/math.ru book scans.
- `https://olympiads.mccme.ru/vmo/prisery.htm` - VMO/MCCME winners page. It explicitly says that in 1992 the Vserossiyskaya Olympiad was not yet the final stage; it was the penultimate stage before the Interrepublican Olympiad, later called zonal/okrug.
- `https://www.kvant.digital/issues/1991/10/agahanov_kuptsov_reznichenko-xvii_vserossiyskaya_olimpiada_shkolnikov_po_matematike-7e28f95c/` - primary contemporary Kvant publication for the XVII Vserossiyskaya Olympiad, page images 57-58.
- `https://www.kvant.digital/issues/1992/10/` - primary contemporary Kvant publication for the XVIII Vserossiyskaya Olympiad, page images 60-61.
- `https://www.kvant.digital/issues/1992/11/` - checked as nearby context for the XXVI Interrepublican Olympiad; not imported in this pass because the requested target was the Vserossiyskaya/zonal stage.
- `https://math.ru/lib/bib-mat-kr/18` - MCCME/math.ru scan page for "Задачи всесоюзных математических олимпиад"; checked as reliable background, but it covers all-union final materials and was not used for new zonal cards.

## Added Cards

- `vosh-1991-zonal-one-way-streets-return`: XVII Vserossiyskaya 1991, 10.3. Graph relevance: one-way streets form a directed planar graph; goal is existence of a directed face/quarter route. Added as condition/profile only; graph reformulation marked `needs_human_review`.
- `vosh-1992-zonal-airlines-route-transfer`: XVIII Vserossiyskaya 1992, 9.8. Graph relevance: flights are an edge-colored graph/multigraph with a proper incidence-color constraint; goal is equalizing color-class sizes. Added as condition/profile only; graph reformulation marked `needs_human_review` because the source does not explicitly exclude parallel flights.
- `vosh-1992-zonal-air-travel-one-city-redundant`: XVIII Vserossiyskaya 1992, 11.3. Graph relevance: directed reachability; the unreachable set has no incoming edges from the reachable complement. Added as condition/profile only.

All three cards use `relations_status: "base_done"` and do not include full solutions.

## Checked But Not Added

- XVIII Vserossiyskaya 1992, 10.4: grid-path routing is graph-adjacent, but the statement is more naturally a lattice/Hamiltonian-path construction and needs a separate careful pass before inclusion.
- XVIII Vserossiyskaya 1992, 11.6: geometry, not graph-relevant enough for this sweep.
- XXVI Interrepublican Olympiad 1992, 10.3 and 11.8: graph-relevant nearby final-stage problems were seen in `Квант` 1992 № 11, but they are not zonal/Vserossiyskaya; leave for a separate all-union/interrepublican pass.
- Problems.ru was not used as a source of truth in this pass.

## Validation

Command run:

```powershell
python tools\validate.py
```

Result: failed on pre-existing validation errors outside this sweep:

- `data/problems/vosh/vosh-2005-06-final-dominoes-three-color-neighbors.yaml`
- `data/problems/vosh/vosh-2025-26-regional-degree-difference-friendship.yaml`

No validation errors were reported for the new 1991/1992 cards or the new source records before the validator stopped with those existing issues.

## Risks

- The `Квант` digital article pages state that text representation is still in preparation, so statements were transcribed manually from page images. A second human/OCR check is useful before promotion.
- Individual problem authors are not indicated in the checked `Квант` pages; card authors record the publication authors only.
- Two graph-theory reformulations are intentionally conservative and marked `needs_human_review`.

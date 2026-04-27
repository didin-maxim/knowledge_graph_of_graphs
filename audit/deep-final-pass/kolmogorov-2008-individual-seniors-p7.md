# Kolmogorov 2008 Individual Seniors P7

## Verdict

`repaired_from_local_official_doc_and_kvant_article`.

The previous warning was correct for the imported statement, but the imported statement itself was wrong. The local official archive material is present at `tmp/kolm12/kolm12/lichol12.doc`; extracting the WordDocument stream shows the seniors problem 7 statement:

> Сумма телесных углов при вершинах выпуклого многогранника равна π. Докажите, что существует замкнутый маршрут по его ребрам, проходящий через каждую его вершину ровно один раз.

The source also names the author as И. Богданов. The same problem is published as Kvant M2153 in I. Bogdanov, "О сумме телесных углов многогранника", Kvant 2010 no. 3, with the projection solution: https://www.mathnet.ru/php/getFT.phtml?jrnid=kvant&paperid=2439&what=fullt

## Repair

- Replaced the false triangular-face statement with the official solid-angle statement.
- Updated the author from unknown to И. Богданов.
- Replaced the unsafe compressed Hamiltonicity argument with a complete projection proof.
- Marked the solution/editorial path as checked and public-ready.

## Mathematical Check

The fixed proof uses the standard spherical covering idea. Move each vertex solid angle to a common unit sphere, and also mark the antipodal copy. Since the sum of solid angles is π, the marked area counted with multiplicity is 2π, less than the sphere area 4π. Choose an unmarked direction, avoiding the finitely many directions parallel to faces. Project perpendicular to this direction. No vertex can project to the interior of the projection polygon, so every vertex appears on the boundary; adjacent boundary vertices lift to edges because the projection direction is not parallel to a face. The boundary cycle is therefore a Hamiltonian cycle in the edge graph.

## Files

- `data/problems/kolmogorov/kolmogorov-2008-individual-olympiad-seniors-problem-7.yaml`
- `audit/deep-final-pass/kolmogorov-2008-individual-seniors-p7.md`

## Tests

- Passed for the target file JSON syntax: `python -m json.tool data\problems\kolmogorov\kolmogorov-2008-individual-olympiad-seniors-problem-7.yaml`
- Passed: `python tools/check_links.py`
- Blocked by unrelated existing worktree issue: `python tools/validate.py` now fails only on `data\problems\kolmogorov\kolmogorov-2010-individual-olympiad-seniors-problem-4.yaml` with `unknown tag hamiltonian_paths`. I did not edit that file.

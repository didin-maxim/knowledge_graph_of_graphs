# SPbMO graph-problem pass, 1992-2008 classic archive

Agent scope: old/classic SPbMO archive, mainly 1992-2008. Write scope observed: only this report and `data/problems/spbmo/spbmo-*.yaml` were edited.

## Sources Checked

- Official PDMI archive PDFs found and downloaded:
- `https://www.pdmi.ras.ru/~olymp/1992/spbmo_1992.pdf`
- `https://www.pdmi.ras.ru/~olymp/1993/spbmo_1993.pdf`
- `https://www.pdmi.ras.ru/~olymp/1994/spbmo_1994.pdf`
- `https://www.pdmi.ras.ru/~olymp/1995/spbmo_1995.pdf`
- `https://www.pdmi.ras.ru/~olymp/1996/spbmo_1996.pdf`
- `https://www.pdmi.ras.ru/~olymp/1997/spbmo_1997.pdf`
- Local downloads/extracts are in `audit/_spbmo_1992_2008/`.
- Direct PDMI URL pattern returned 404 for 1998-2008, so those years were not confirmed from the same official PDF pattern in this pass.
- MCCME bibliography/TOC checked: `https://biblio.mccme.ru/sites/default/files/bookfiles/spbolymp-ogl.pdf`.
- Mathedu bibliographic page checked for Fomin's 1961-1993 book: `https://www.mathedu.ru/text/fomin_spb_matematicheskie_olimpiady_1994/`.
- Mirror located but not used for card source text: `https://dokumen.pub/1994-2006-239.html` for the 1994-2006 solutions collection. Shell download was blocked by Cloudflare; web snippet confirms metadata only.

## Confirmed Cards Added

- `spbmo-1993-7-p12-unsociable-eccentrics`: SPbMO 1993, 7th grade, problem 12. Explicit graph of acquaintances; proof is degree/edge counting between low-degree people and "eccentrics".
- `spbmo-1996-9-p46-strongly-connected-tournament-orientations`: SPbMO 1996, selection round, 9th grade, problem 46. Complete graph of cities with all edge orientations; proof counts bad non-strongly-connected tournaments via source strong components.

Both cards use temporary source ids:

- `src-spbmo-TODO-1993-pdmi-problems`
- `src-spbmo-TODO-1996-pdmi-problems`

Suggested permanent source entries should point to the official PDMI PDFs above and may mention local extracted text files under `audit/_spbmo_1992_2008/`.

## Candidate Scan Notes

- 1992.55, 11th grade: 100-city road graph remains connected after deleting all roads incident to any one city; split vertices into two connected 50-vertex induced subgraphs. Strong graph candidate, but I did not add it because I did not verify an official solution in this pass.
- 1993.12, 7th grade: added. Explicit acquaintance graph.
- 1996.46, selection round, 9th grade: added. Explicit complete graph orientation/tournament problem.
- 1996.63: metro lines/stations connectivity candidate, needs statement cleanup and official solution check.
- 1997.13: city without bridges/tunnels/dead ends, repeated edge during governor route. Likely Eulerian/graph walk candidate, but not added without solution verification.
- 1997.27, 10th grade: 3n people, any two have common acquaintance, choose n dominating people. Strong graph candidate, but proof/source needs manual verification.
- 1997.34, 11th grade: million people, any two have a common acquaintance among the others, choose 5000 dominating people. Related to 1997.27; needs manual verification.
- 1997.54, 11th grade: convex polyhedron with triangular faces and degree constraints. Graph/polyhedral discharging candidate, but it is geometrically phrased and needs official solution check before inclusion.

## Duplicate Check

- No existing `data/problems/spbmo/` cards were present before this pass.
- A broad repository text scan found many general graph cards but no exact SPbMO duplicates for the two added statements.
- Possible relation candidates, not edited due scope:
- 1993.12 relates to generic degree-counting/friendship graph cards.
- 1996.46 relates to tournament strong-connectivity and directed reachability cards, if such relation files are later created.

## Manual Follow-Up

- Find official or high-quality accessible solution source for the 1994-2006 collection. The MCCME TOC confirms the collection exists; the discovered Dokumen mirror is only suitable as a mirror and was not usable from shell due Cloudflare.
- Resolve permanent `source_id` values in `data/sources/sources.yaml` later, outside this agent's write scope.
- Revisit 1998-2008 using alternate official SPbMO/SPbU/LNMO archive paths or printed annual collections.
- Verify author metadata for 1993.12 and 1996.46; the checked PDMI yearly PDFs did not list per-problem authors.

## Counts

- Years actively checked from official PDFs: 1992, 1993, 1994, 1995, 1996, 1997.
- Years attempted but not retrieved by direct PDMI pattern: 1998-2008.
- Graph candidates noted: 8.
- Confirmed cards added: 2.
- Requires manual checking: 6 candidate problems plus the 1998-2008 source path.

## Files Written

- `audit/spbmo-agent-1992-2008-report.md`
- `data/problems/spbmo/spbmo-1993-7-p12-unsociable-eccentrics.yaml`
- `data/problems/spbmo/spbmo-1996-9-p46-strongly-connected-tournament-orientations.yaml`

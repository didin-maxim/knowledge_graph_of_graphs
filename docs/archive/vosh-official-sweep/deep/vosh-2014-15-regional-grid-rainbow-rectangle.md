# Deep Audit: vosh-2014-15-regional-grid-rainbow-rectangle

Date: 2026-05-05

## Verdict

- Statement/source: verified in the official MCCME PDF for the 2014/15 VOSH regional stage, second day, problem 10.8.
- Author/proposer: verified as Д. Храмцов from the author marker after the problem statement.
- Answer: \(k=2n\).
- Graph model: present in the official first solution, not merely an editorial motif. The solution explicitly maps rows and columns to the two parts of a bipartite graph, maps cells to colored edges, defines a rainbow cycle, and proves existence of a rainbow 4-cycle.
- Classification: `official_complete_or_near_complete`, because the card is based on the official source and expands the complete official graph solution.

## Sources Checked

- Official PDF: https://olympiads.mccme.ru/vmo/2015/iii-2.pdf
- Relevant PDF text locations from the browser extraction:
- Lines 303-305: problem 10.8, author marker `(Д. Храмцов)`, and answer \(k=2n\).
- Lines 306-315: official lower-bound construction in \(2n-1\) colors.
- Lines 316-335: official bipartite graph formulation, one-edge-per-color cycle, and shortest-rainbow-cycle shortening argument.
- Lines 360-369: grading comments, including that using the cycle lemma for a graph with at least as many edges as vertices costs no points.

## Formulation Notes

The original board statement is an application rather than a graph-theory statement. The first official solution gives the graph model:

- rows and columns become the two parts of \(K_{n,n}\);
- each cell becomes the edge joining its row and column;
- the cell color becomes the edge color;
- four cells at the intersection of two rows and two columns are exactly a 4-cycle;
- four different cell colors are exactly a rainbow 4-cycle.

The official PDF extraction renders some `\ge` symbols as `>` in the text layer, but the answer and construction show the intended threshold is \(2n\): the lower bound is \(2n-1\), and the upper bound applies once at least \(2n\) colors are present.

## Solution Notes

The card uses the first official solution. It proves sharpness by the row/column overwriting construction with \(2n-1\) colors. For the upper bound, it selects one edge of each color in the bipartite graph; with at least \(2n\) selected edges on \(2n\) vertices, a cycle exists. Since selected edges have pairwise different colors, there is a rainbow cycle. A shortest rainbow cycle must be a 4-cycle: otherwise the chord \(a_1b_2\) either closes a rainbow 4-cycle immediately or shortcuts the chosen cycle to a shorter rainbow cycle.

The second official solution is not used as the main card solution. It is a non-graph induction/generalization to an \(m\times n\) rectangle with more than \(m+n\) colors. This confirms the answer but is less central to the graph database.

## Local Relations

- `usamo-1976-p1-monochromatic-rectangle-bipartite`: close row-column bipartite model and 4-cycle/rectangle translation, but it forces a monochromatic rectangle by counting rather than a rainbow rectangle by shortest-cycle extremality.
- `imo-1998-c6-k-le-4-rainbow-edges-impossible`: more distant rainbow edge-coloring relative; it works in complete graphs and Ramsey-style color obstruction, not in complete bipartite row-column graphs.

## Risk Notes

- The source metadata in `data/sources/sources.yaml` is already present and marked official; this pass did not edit shared source metadata per scope.
- The statement is recorded with \(n\ge 2\). The accessible PDF text layer shows `n > 2`, but the same extraction also shows `k > 2n` where the proof context requires `k\ge 2n`; this appears to be a PDF symbol extraction issue.

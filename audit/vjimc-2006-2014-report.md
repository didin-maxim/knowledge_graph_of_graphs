# VJIMC 2006-2014 graph/hypergraph archive pass

Scope: official VJIMC Previous Problems archive for Annual 16-24, years 2006-2014. I checked the official problem and solution PDFs linked from https://vjimc.osu.cz/problems, using the `jNNproblems*.pdf` and `jNNsolutions*.pdf` files.

## Created cards

| Card | source_id | Official URLs | Reason included |
| --- | --- | --- | --- |
| `data/problems/vjimc/vjimc-2007-cat1-p2-key-ring-distinguishing-coloring.yaml` | `src-vjimc-2007-cat1-p2-official` | Problems: https://vjimc.osu.cz/storage/uploads/j17problems1.pdf; Solutions: https://vjimc.osu.cz/storage/uploads/j17solutions1.pdf | Circular key ring is naturally the cycle graph `C_n`; the official solution uses neighbours, distances on the cycle, rotations and flips, i.e. distinguishing coloring under the dihedral automorphism group. |
| `data/problems/vjimc/vjimc-2009-cat1-p3-partial-hypergraph-bicoloring.yaml` | `src-vjimc-2009-cat1-p3-official` | Problems: https://vjimc.osu.cz/storage/uploads/j19problems1.pdf; Solutions: https://vjimc.osu.cz/storage/uploads/j19solutions1.pdf | The sets `A_i` are hyperedges; the task is a nontrivial partial two-coloring where every colored edge is bichromatic. |
| `data/problems/vjimc/vjimc-2009-cat2-p4-transversal-hypergraph-polynomial-bound.yaml` | `src-vjimc-2009-cat2-p4-official` | Problems: https://vjimc.osu.cz/storage/uploads/j19problems2.pdf; Solutions: https://vjimc.osu.cz/storage/uploads/j19solutions2.pdf | An extremal `m`-uniform hypergraph/set-family problem; official solution uses polynomials and a parity evaluation matrix. |
| `data/problems/vjimc/vjimc-2013-cat2-p2-hypercube-segment-intersections.yaml` | `src-vjimc-2013-cat2-p2-official` | Problems: https://vjimc.osu.cz/storage/uploads/j23problems2.pdf; Solutions: https://vjimc.osu.cz/storage/uploads/j23solutions2.pdf | Included as a natural geometric drawing of the complete graph on the vertex set of the `n`-cube; intersections are centers of faces of dimension at least 2. |

## Skipped and checked items

- 2006 Annual 16, Category I/II: no substantial graph or hypergraph model found. Category II P3 is about secants of graphs of functions, not graph theory.
- 2008 Annual 18, Category I P4 is a modular coloring/counting problem on numbers, but no graph/hypergraph structure is essential in the statement or official solution.
- 2009 Annual 19: the expected "lines in space / Ramsey edge-coloring of a complete graph" candidate from the initial scan was not present in the official `j19problems1`, `j19problems2`, `j19solutions1`, or `j19solutions2` PDFs from the VJIMC archive. I did not add a card for it.
- 2010 Annual 20, Category II P4 uses the word "graph" only for the graph of a function and rectangles covering it; skipped.
- 2011 Annual 21 and 2012 Annual 22: checked problem and solution PDFs; no substantial graph/hypergraph task found.
- 2013 Annual 23, Category II P2 was borderline: the official solution is coordinate geometry/combinatorics, not graph-theoretic language. I included it because the object is exactly the straight-line drawing of a complete graph on hypercube vertices, and the hypercube model is not artificial.
- 2014 Annual 24, Category I P4 uses "graphs of quadratic polynomials"; this is graph-of-function terminology, not graph theory. No 2014 task was added.

## Possible relation ideas

- Link `vjimc-2007-cat1-p2-key-ring-distinguishing-coloring` to other cycle/circular coloring and graph symmetry cards, especially distinguishing coloring or automorphism-breaking examples.
- Link `vjimc-2009-cat1-p3-partial-hypergraph-bicoloring` to discrepancy/partial coloring and incidence-matrix sign-coloring lemmas if such cards are later added.
- Link `vjimc-2009-cat2-p4-transversal-hypergraph-polynomial-bound` to polynomial-method extremal set-system cards and to parity/odd-diagonal-even-offdiagonal matrix arguments.
- Link `vjimc-2013-cat2-p2-hypercube-segment-intersections` to hypercube, Hamming cube, and geometric graph intersection-counting cards.

# Hard FYUM repair pass, 2026-04-27

Scope: `fyum-2013-tur2a-p1`, `fyum-2009-tur3a-p7`, `fyum-2011-finalb-p4`, `fyum-2009-final-p2`.

## Repaired

- `fyum-2009-tur3a-p7`: expanded the Bondy--Simonovits periodic-coloring lemma into the solution. The proof now gives the dense-graph theta-subgraph reduction, the period argument on the three theta cycles, and the final propagation from the theta-subgraph to the whole connected graph. Source checked: J. A. Bondy and M. Simonovits, "Cycles of even length in graphs", Lemma 1.

## Deferred

- `fyum-2013-tur2a-p1`: still deferred as a theorem-level dependency. The problem is an immediate corollary of Chang--Montassier--Pecher--Raspaud, Theorem 5: every planar graph with maximum degree at most `Delta` and girth at least `10Delta+46` has a strong `(2Delta-1)`-edge-coloring for `Delta>=4`. Here `d>100` and the FYUM girth is `10d+100`, so the transfer is exact, but the proof uses the odd graph machinery plus a planar large-girth/minimal-counterexample argument and is too large for a compact card repair. Sources checked: NTU preprint `2013-09.pdf`, EUDML/Discussiones Mathematicae Graph Theory record, and FYUM 2013 `tur2a.tex` with `all-solutions.pdf`.
- `fyum-2011-finalb-p4`: still deferred as a theorem-level dependency. The desired Hamiltonian path has exactly two directed blocks, of lengths 100 and 99. Bang-Jensen--Gutin, Section 10, records the Alspach--Rosenfeld and H. J. Straight result that Rosenfeld's path conjecture is established for oriented Hamiltonian paths with two blocks. The transfer is direct, but a self-contained proof of the two-block tournament theorem is not compact. Sources checked: Bang-Jensen--Gutin survey PDF and FYUM 2011 `finalb.tex` / `solF.pdf`.
- `fyum-2009-final-p2`: still deferred for the upper bound. The lower-bound construction on 499 vertices is already written out in the card. The upper bound uses Burr--Erdos--Spencer, Theorem 2, `r(nK_3)=5n` for `n>=2`; at `n=100`, this forces 100 vertex-disjoint monochromatic triangles, hence 100 odd cycles. Importing the Ramsey theorem is possible but larger than a local gap fix. Sources checked: Burr--Erdos--Spencer 1975 PDF and FYUM 2009 `final.tex` / `sol4.pdf`.

## Source Notes

- Official FYUM source IDs already exist in `data/sources/sources.yaml` for all four problems.
- Reference-theorem source IDs already exist for the three external papers/survey.
- No placeholder tasks with `Решение пока не найдено` were edited.

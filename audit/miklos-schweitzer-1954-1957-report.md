# Miklos Schweitzer 1954-1957 graph audit

Source checked: REAL-EOD old book PDF, `audit/_schweitzer_1949_1961/AkademiaiKiado_007070.pdf`, <https://real-eod.mtak.hu/14558/1/AkademiaiKiado_007070.pdf>.

Scope: years 1954, 1955, 1956, 1957 in "Problems of the contests", with published solutions cross-checked when relevant.

## Added

- `data/problems/miklos-schweitzer/miklos-schweitzer-1954-p9-translated-broken-line-intersection.yaml`
  - Source id: `src-miklos-schweitzer-1954-p9-old-book`
  - Statement: PDF page 25.
  - Solution: PDF pages 202-203.
  - Reason: the object is a simple embedded polygonal path, i.e. a geometric path graph, and the proof uses a genuine planar/topological separation argument for translated paths.

- `data/problems/miklos-schweitzer/miklos-schweitzer-1956-p3-convex-polygon-triangulations.yaml`
  - Source id: `src-miklos-schweitzer-1956-p3-old-book`
  - Statement: PDF page 27.
  - Solution: PDF pages 252-254.
  - Reason: triangulations are maximal outerplanar graphs on a fixed convex cycle; the solution is an enumerative graph/combinatorial decomposition.

## Checked but not added

- 1954/1-8, 1954/10: no substantive graph-theoretic content found. Mostly analysis, algebra, number theory, probability, and geometry without a natural graph formulation.
- 1955/1-9: no substantive graph-theoretic content found.
- 1955/10, convex polyhedron with vertex-transitive vertex set and congruent faces (statement PDF page 27, solution immediately before G.12 around PDF page 220): skipped. It can be associated with a polyhedral graph, but the published argument is metric/polyhedral geometry; adding it would violate the "no polyhedra without substantial graph method" rule.
- 1956/1-2, 1956/4-5, 1956/7-10: no substantive graph-theoretic content found.
- 1956/6, centrally symmetric faces imply an even number of faces (statement PDF page 28, solution PDF pages 220-221): skipped as a doubtful polyhedral-geometry item. The solution pairs parallel faces by a height/convexity argument; it is not essentially a graph problem. The book's own remark says that merely having even-sided faces is insufficient, reinforcing that this is geometric rather than purely graph-theoretic.
- 1957/1-10: no substantive graph-theoretic content found. 1957/2 has spherical triangle geometry but no meaningful graph method.

## OCR / source notes

- The old-book OCR is noisy: several mathematical symbols are dropped or replaced, and `n` is often confused with Cyrillic-looking glyphs.
- For 1954/9, the statement and the main strip lemma are readable, but the counterexample relies on Figure 5; the card states only the conclusion needed for the problem and marks the construction as from the book.
- For 1956/3, formulas are partly distorted in OCR. The recursive formulas and final answers were checked against the PDF text: all triangulations are counted by `1/(n-1) * binom(2n-4, n-2)`, and the special triangulations by `n * 2^(n-5)` for `n >= 4` plus `1` for `n = 3`.

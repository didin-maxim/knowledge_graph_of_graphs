# Final audit: yumt-2015-grand-final-problem5

Date: 2026-04-27

## Status

Complete via local theorem-card.

The previous route was correct but deferred: the YUMT problem reduces to Stiebitz's theorem that the only double-critical 5-chromatic graph is \(K_5\). In this pass I ported the proof of that theorem into `data/problems/classical/stiebitz-double-critical-k5.yaml`, including the two compressed steps in the paper:

- why a maximal uniquely 3-colourable induced subgraph yields an edge whose common neighbourhood inside the subgraph is monochromatic;
- why the final \(K_4\) plus an outside vertex forces exactly \(K_5\), not a larger joined graph.

The YUMT solution now uses the theorem-card as a proved local prerequisite. Given a minimal induced \(5\)-chromatic \(K_5\)-free subgraph \(H\), either some edge \(xy\) has \(\chi(H-\{x,y\})\ge 4\), giving the required partition with \(B=\{x,y\}\), or \(H\) is double-critical 5-chromatic and Stiebitz gives the forbidden \(K_5\).

## Source

- Michael Stiebitz, "K5 is the only double-critical 5-chromatic graph", Discrete Mathematics 64 (1987), 91--93.
- PDF: `https://kostochk.web.illinois.edu/math583/stiebitz.pdf`

## Changed files

- `data/problems/classical/stiebitz-double-critical-k5.yaml`
- `data/problems/yumt/yumt-2015-grand-final-problem5.yaml`
- `data/relations/relations.d/yumt-links.yaml`
- `audit/solution-completeness-sample-2026-04-27/final-yumt-2015-gf-p5.md`

## Validation

- `python tools/validate.py` — OK: 333 problems, 386 relations, 9 comments, 352 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools/check_links.py` — OK: 375 internal routes, 352 external source URLs syntactically valid.

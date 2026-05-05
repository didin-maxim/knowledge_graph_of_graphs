# All-Union Pre-1992 Sweep

Date: 2026-05-05

Scope: old USSR / All-Union Mathematical Olympiad graph-relevant problems before the collapse of the USSR. Primary preference was reliable published scans/archives; problems.ru was not used as a primary source for the added cards in this pass.

## Sources Checked

- Math.ru archive page for N.B. Vasilyev, A.A. Egorov, *Zadachi vsesoyuznykh matematicheskikh olimpiad*, Nauka, 1988: https://math.ru/lib/bib-mat-kr/18
- Math.ru downloadable scan from that page: https://math.ru/lib/files/djvu/olimp/vsesojuznye.djvu
- OCR access copy for the 9th-grade all-union section: https://djvu.online/file/A6gSDRaJgDboJ
- Secondary duplicate sanity checks against local `data/problems/**` by distinctive text fragments; no matching existing cards were found for the four added statements.

## Added Cards

- `all-union-1981-final-9-football-independent-triple`
  - Metadata: All-Union Mathematical Olympiad 1981, final stage, grade 9, problem 135, first day.
  - Graph relevance: match graph / complement graph; existence of an independent triple in an 8-regular graph on 18 vertices.
  - Status: condition-only base card, `relations_status = base_done`.

- `all-union-1985-final-9-complete-graph-edge-coloring`
  - Metadata: All-Union Mathematical Olympiad 1985, final stage, grade 9, problem 164, first day.
  - Graph relevance: edge coloring of the complete graph `K_n`.
  - Status: condition-only base card, `relations_status = base_done`.

- `all-union-1986-final-9-tree-distances-one-to-nchoose2`
  - Metadata: All-Union Mathematical Olympiad 1986, final stage, grade 9, problem 172, first day.
  - Graph relevance: weighted tree metric with prescribed pairwise distance multiset.
  - Status: condition-only base card, `relations_status = base_done`.

- `all-union-1987-final-9-tournament-score-squares`
  - Metadata: All-Union Mathematical Olympiad 1987, final stage, grade 9, problem 177, first day.
  - Graph relevance: tournament in/out-degree identity.
  - Status: condition-only base card, `relations_status = base_done`.

## Provenance Notes

- The added statements are based on published scan/OCR access rather than problems.ru as a primary source.
- Authors/proposers were not visible in the checked OCR fragments. Each card explicitly records this as `not_found` and notes it in `editorial.notes`.
- No full local solutions were added: this pass was limited to confident condition/base cards.

## Risks And Follow-Up

- OCR source risk: the OCR access copy is useful for statement text and numbering, but the Math.ru scan remains the stronger bibliographic source. A future high-reasoning/OCR pass should compare against page images for every symbol and punctuation detail before promoting to public-ready.
- Author attribution risk: the 1988 book includes a list of authors near the end, but it was not text-searchable in this environment. A future image/OCR pass over that author list may be able to fill proposers.
- Coverage risk: this was a conservative sweep, not an exhaustive import. Other all-union graph-relevant problems likely remain in the 10th and 11th grade sections and in problems where the graph is only in the solution.

## Validation

- `python tools\validate.py`
- Result: `OK: 584 problems, 673 relations, 9 comments, 603 sources, 29 definitions, 17 standard ideas, 32 import batches.`

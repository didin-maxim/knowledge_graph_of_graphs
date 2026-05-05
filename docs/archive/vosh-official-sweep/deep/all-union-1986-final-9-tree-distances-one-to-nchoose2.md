# all-union-1986-final-9-tree-distances-one-to-nchoose2

Date: 2026-05-05

Scope: deep pass for one card only.

## Sources Checked

- `https://math.ru/lib/bib-mat-kr/18` - Math.ru page for Н.Б. Васильев, А.А. Егоров, "Задачи всесоюзных математических олимпиад", Наука, 1988. The source record says the scan contains final-round USSR Mathematical Olympiad problems in chronological order with solutions.
- `https://djvu.online/file/A6gSDRaJgDboJ` - OCR access copy of "Математические олимпиады школьников. 9 класс", 1997. Checked problem 172 statement and solution.

## Statement And Provenance

- Statement confirmed: 1986 All-Union Mathematical Olympiad, final stage, grade 9, problem 172, first day.
- The graph-theory reformulation as a weighted tree on `n` vertices is faithful: `n-1` roads plus connectivity gives a tree, and the noncrossing-road phrase is geometric packaging for a planar drawing of a tree.
- Individual author/proposer was not found in the checked statement or solution fragments. The card keeps `authors.status: not_found`.

## Solution Audit

Classification: `unofficial_published`.

Reason: a complete published solution is available in the checked 1997 OCR copy, and Math.ru confirms the corresponding 1988 collection with solutions. However, the local source registry marks both source records as `official: false`, so the solution should not be promoted to `official_complete_or_near_complete`.

The published solution gives the answer "yes" for `n=6` and "no" for `n=1986`. Its obstruction is the parity coloring of tree vertices: if the color classes have sizes `x,y`, the number of odd distances is `xy`. Comparing this with the count of odd numbers in `1,...,binom(n,2)` yields that either `n` or `n-2` must be a square.

The source's construction for `n=6` is referenced by Figure 143. The card expands it explicitly:

- central edge `AB` has length `5`;
- two leaves at `A` have edge lengths `1` and `2`;
- two leaves at `B` have edge lengths `4` and `8`.

This gives all distances `1,2,...,15`.

## Card Changes

- Added two solution ideas: parity bipartition and six-vertex construction.
- Added a complete local solution derived from the published solution, with the figure construction written out textually.
- Updated source roles to include solution checking.
- Set `public_ready: true`, `relations_status: deep_done`, and added `solution_classification`.

## Risks

- The exact drawing in Figure 143 was not embedded in the OCR text; the textual construction was independently reconstructed and verified by distance calculation.
- No individual proposer/author attribution was found. The card intentionally does not infer one from book editors/authors.

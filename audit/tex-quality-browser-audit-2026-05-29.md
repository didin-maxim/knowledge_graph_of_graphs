# TeX/browser quality audit, 2026-05-29

Scope: `viewer/index.html` after `python tools/build_viewer.py`, opened in Edge through Playwright with MathJax enabled.

Checked routes:

- `#home`
- `#putnam-2021-b5-very-odd-matrices-dag`
- `#imc-2001-day2-p4-zero-principal-minors-acyclic-digraph`
- `#spbmo-2019-9-11-p6-regular-graph-2-switches`
- `#utyum-2024_komol62_6_3_circle_graph_coloring`
- `#cmo-2023-p2-three-regular-bootstrap-friendship`
- `#def-simple_graph`
- `#stdidea-double_counting`
- `#comments`

Browser findings:

- Home, definition, standard idea, comments, and sampled problem pages render Russian text without visible mojibake or `????`.
- MathJax rendered sampled formulas on problem pages; no raw `\(...\)` / `\[...\]` delimiters remained after MathJax.
- Relation navigation works from `#putnam-2021-b5-very-odd-matrices-dag` to `#imc-2001-day2-p4-zero-principal-minors-acyclic-digraph`.
- Search navigation works for query `matching`; first selected result was `#utyum-2025_komol64_8_7_tree_matchings_path`.
- Fixed visible raw TeX command `\signed` in `#spbmo-2019-9-11-p6-regular-graph-2-switches`.

Remaining queue from `python tools/check_tex_quality.py --max-items 20`:

- `data/problems/classical/hall-marriage-theorem.yaml`: visible raw commands such as `\A`, `\N`.
- `data/problems/classical/menger-theorem.yaml`: visible raw command `\R`.
- `data/problems/fyum/fyum-2008-final-p8.yaml`: visible raw command `\N`.
- `data/problems/fyum/fyum-2009-final-p2.yaml`: visible raw commands `\lfloor`, `\rfloor`, `\cup` inside backtick text.
- `data/problems/imc/imc-1997-day1-p6-intersecting-families-finite-transversal.yaml`: literal `\n` sequences in visible solution text.
- `data/problems/imo/imo-2014-c9-snail-circles-tree.yaml`: literal `\n` sequences in visible solution text.

Current status: the new checker reports 73 total issues. This is a real cleanup queue, not a small one-card fix.

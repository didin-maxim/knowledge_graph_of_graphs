verdict: completed_full_solution

changed files:
- data/problems/kolmogorov/kolmogorov-2011-individual-olympiad-seniors-problem-7.yaml
- audit/plan-to-solution-pass/kolmogorov-2011-individual-seniors-p7.md

tests:
- python tools/validate.py: passed
- python tools/check_links.py: passed

notes:
- The compressed plan was sufficient to identify the target theorem: the cube of every connected graph with at least three vertices is Hamiltonian.
- Replaced the abbreviated induction sketch with a complete self-contained proof: reduce to a spanning tree, take a doubled-edge DFS tour, select first occurrences of even-depth vertices and last occurrences of odd-depth vertices, and verify consecutive selected vertices are at tree-distance at most 3.
- Marked the solution `ai_checked` with `repair_status: completed_full_solution`; source/authorship metadata remains under human review in the surrounding card.

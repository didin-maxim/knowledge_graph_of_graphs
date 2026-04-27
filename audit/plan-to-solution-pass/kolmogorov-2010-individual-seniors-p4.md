# kolmogorov-2010-individual-seniors-p4

verdict: deferred_needs_source_or_reconstruction

changed files:
- data/problems/kolmogorov/kolmogorov-2010-individual-olympiad-seniors-problem-4.yaml
- audit/plan-to-solution-pass/kolmogorov-2010-individual-seniors-p4.md

notes:
- The compressed plan is not sufficient for a safe full solution.
- The available summary proves or states a path-merging construction from two republic Hamiltonian paths to a global Hamiltonian path. That direction is not enough to prove the required upper bound `N <= N1 * N2`.
- A complete repair needs either the original official solution text/OCR or a fresh verified reconstruction of the counting/injection argument.
- The YAML solution remains `needs_human_review` and now has `repair_status: deferred_needs_source_or_reconstruction`.

tests:
- passed: python tools/validate.py
- passed: python tools/check_links.py
- passed: target file parses as JSON via ConvertFrom-Json
- passed: git diff --check for target problem file and audit report
  - note: Git printed an LF-to-CRLF normalization warning for the YAML file, but reported no whitespace errors.

# Kolmogorov 2006 Round 2 Super League Problem 6

verdict: completed_ai_checked

changed files:
- data/problems/kolmogorov/kolmogorov-2006-round-2-super-league-problem-6.yaml
- audit/deep-final-pass/kolmogorov-2006-round2-super-p6.md

source check:
- The repository did not contain `work/kolm/text/2006/tur2_10sol.txt`, but it did contain the original local DOC artifact at `tmp/kolm10/Problems/tur2_10sol.doc`.
- Extracted text from that DOC confirms the official outline: prove the `3n+1` black-cell bound by a tree, then induct on the number of white cells and remove a `T`-tetromino from a longest path.
- The DOC outline is still compressed at the crucial local-removal step, so the YAML solution now gives a self-contained repair.

repair:
- Replaced the deferred compressed solution with a complete proof using an arbitrary spanning tree of the cell-adjacency graph.
- Key lemma: if the figure has `W` white and `3W` black cells, any spanning tree has `4W-1` edges, and the sum of degrees over white vertices is `4W-1`. Since each white cell has degree at most 4, exactly one white vertex has degree 3 and all other white vertices have degree 4.
- A longest path in this tree has black leaves at its ends. For `W > 1`, at least one endpoint is adjacent to a degree-4 white vertex. The three neighbours of that white vertex away from the path are black leaves, hence form a removable `T`-tetromino.
- Removing that white vertex and its three black leaf neighbours leaves the remaining tree connected and preserves the ratio `black = 3 white`, closing the induction.

status updates:
- solution status set to `ai_checked`.
- solution `repair_status` set to `completed_ai_checked`.
- problem-level authorship/difficulty review flags were left unchanged; this pass repaired the proof, not the metadata provenance.

tests:
- passed: `python tools/validate.py`
- passed: `python tools/check_links.py`
- passed: `git diff --check -- data/problems/kolmogorov/kolmogorov-2006-round-2-super-league-problem-6.yaml audit/deep-final-pass/kolmogorov-2006-round2-super-p6.md`

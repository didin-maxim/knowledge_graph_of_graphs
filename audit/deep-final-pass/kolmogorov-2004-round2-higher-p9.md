# Kolmogorov 2004 Round 2 Higher League Problem 9

verdict: completed_ai_checked

changed files:
- data/problems/kolmogorov/kolmogorov-2004-round2-higher-league-problem-9.yaml
- audit/deep-final-pass/kolmogorov-2004-round2-higher-p9.md

notes:
- Rechecked the previously deferred numerical gap. The direct 5-progression count does close once one counts all pairs of positions in a 5-term progression.
- Number of 5-term progressions in `[1, 10^5]` is `1,249,950,000`.
- A fixed edge can lie in at most `binom(5,2)=10` of those progressions, because choosing the two positions determines the common difference and the start.
- If every 5-term progression contained an edge, then the graph would have at least `124,995,000` edges.
- A `C_4`-free graph on `100000` vertices has fewer than `15,850,000` edges by the standard codegree count
  `sum_v binom(deg v,2) <= binom(N,2)` and Jensen's inequality.
- This contradiction gives a complete self-contained proof of the desired edge-free 5-term arithmetic progression.

status updates:
- solution status set to `ai_checked`.
- solution `repair_status` set to `completed_ai_checked`.
- problem profile, idea, and central method updated to the direct double-counting proof.
- statement/authorship-level human review flags were not upgraded; this pass repaired the proof, not authorship/source transcription.

tests:
- passed: `python tools/validate.py`
- passed: `python tools/check_links.py`
- passed: target file parses as JSON with Python `json.loads`
- passed: `git diff --check -- data/problems/kolmogorov/kolmogorov-2004-round2-higher-league-problem-9.yaml audit/deep-final-pass/kolmogorov-2004-round2-higher-p9.md`

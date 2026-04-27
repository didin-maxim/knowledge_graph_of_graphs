# Kolmogorov 2006 Round 2 Super League Problem 6

## Verdict

`deferred_needs_source_or_reconstruction`.

The current YAML contains a compressed official summary. It gives the intended strategy: build a cell-adjacency tree, use the colour count `black = 3 white`, choose a longest path, remove a `T`-tetromino, and continue by induction.

I did not expand it into a full solution, because the summary omits the key local lemma. In particular, it does not justify why the relevant penultimate white vertex on a longest path must provide exactly three removable black neighbours, nor why deleting that proposed `T`-tetromino always leaves a connected figure to which the induction hypothesis applies. Those are the steps that would make or break the proof.

Per the pass instructions, the YAML now records the deferred verdict while keeping the solution status as `needs_human_review`, because `deferred_needs_source_or_reconstruction` is a repair marker rather than a normal solution status.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2006-round-2-super-league-problem-6.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2006-round2-super-p6.md`

## Tests

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`

# high: imo-1991-p4-connected-graph-gcd-edge-labels

Task: `sol-aops-maximal-path-labeling` from full recheck bucket 1.

## Verdict

Fixed in card. The previous path-processing sketch was not strong enough: starting a fresh path at an arbitrary unprocessed vertex does not prove that this start vertex eventually receives two consecutive incident labels.

I replaced the sketch by a trail algorithm with an explicit invariant:

- labels are used in increasing order;
- after each completed trail, every vertex already incident to a labelled edge is either irrelevant (`degree < 2`) or already has two incident labelled edges with gcd 1;
- every later trail starts at a boundary vertex already satisfying the invariant, which exists by connectedness whenever unlabelled edges remain.

This closes the missing case. A new endpoint of a trail is safe because if it first appears only as the last vertex and has no unlabelled incident edges left, then it has degree 1; otherwise it either appeared earlier on the same trail and got consecutive labels, or was already good before the trail.

## Source check

- Official IMO PDF confirms the statement, but not a full official solution: https://www.imo-official.org/problems/1991/eng.pdf
- AoPS has an algorithmic longest-path sketch, but it is too terse for this audit gap: https://artofproblemsolving.com/wiki/index.php/1991_IMO_Problems/Problem_4
- John Scholes/Kalva and the IMO 1959-2003 solution collection give the consecutive-label trail idea; I reconstructed the missing invariant rather than copying the short proof:
  - https://prase.cz/kalva/imo/isoln/isoln914.html
  - https://mathwo.github.io/assets/files/IMO-1959-2003-Problems-Solutions.pdf

## Files touched

- `data/problems/imo/imo-1991-p4-connected-graph-gcd-edge-labels.yaml`
  - updated idea wording from simple path to trail/route;
  - replaced `sol-aops-maximal-path-labeling` text by a complete Russian invariant proof.
- `audit/solution-full-recheck-2026-04-27/high-imo-1991-p4.md`
  - this audit note.

Note: the target card already had unrelated pre-existing edits before my change (`stmt-graph` removed and `graph_theory_duplicate_removed` present). I did not revert them.

## Checks

- `python tools/validate.py` passed.
- `python tools/check_links.py` passed.

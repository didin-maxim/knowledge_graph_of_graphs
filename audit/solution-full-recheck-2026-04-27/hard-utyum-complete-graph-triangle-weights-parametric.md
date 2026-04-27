# Hard Backlog: Utyum Complete Graph Triangle Weights Parametric

Problem: `complete-graph-triangle-edge-weights-minimum-parametric`.

## Reason

The card is intentionally not public-ready: `sol-parametric` is still `needs_human_review`. The upper-bound construction is clear, but the lower-bound paragraph relies on a compressed local-replacement step: replacing a `1,3` pair by `2,2` is asserted to preserve all triangle constraints and reduce the number of bad vertices. That step is not fully self-contained in the local text.

## Needed

Provide a complete Russian proof of the local replacement lemma, including:

- which two edges are changed;
- why every triangle containing one or both changed edges still has total weight at least 5;
- why the total sum is unchanged;
- why the number of bad vertices strictly decreases or why a terminating measure is available.

## Next Agent

Do not mark `sol-parametric` as `ai_checked` until the replacement lemma is written out or verified directly from the official UТЮМ sources for the `n = 2000` and `n = 2019` variants. Keep `editorial.public_ready=false` meanwhile.

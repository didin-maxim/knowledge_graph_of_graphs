# XHard FYUM 2013 Tur2A P1

Date: 2026-04-27

Card: `fyum-2013-tur2a-p1`

## Verdict

Repaired. The card now has a self-contained Russian proof for the FYUM-strength special case, not just a citation to Chang--Montassier--Pecher--Raspaud.

The full theorem source was found and checked:

- Gerard Jennhwa Chang, Mickael Montassier, Arnaud Pecher, Andre Raspaud, "Strong chromatic index of planar graphs with large girth", NTU preprint dated March 20, 2013, `https://www.math.ntu.edu.tw/~mathlib/preprint/2013-09.pdf`.
- Published record: Discussiones Mathematicae Graph Theory 34(4), 723-733, 2014, DOI `10.7151/dmgt.1763`.
- Theorem 5 states the `2Delta-1` strong edge-coloring bound for planar graphs with maximum degree at most `Delta` and girth at least `10Delta+46`, `Delta >= 4`.

## Transfer

The full paper proof is larger than an olympiad card if copied verbatim, but the FYUM statement has extra girth: `10d+100` instead of `10d+46`. I used this slack to transfer a shorter special case:

- Euler/suppression lemma gives a path with `2d+19` internal degree-2 vertices.
- The removed path is restored using the odd graph `O_d` on `(d-1)`-subsets of a `2d-1` color set.
- The larger path length `2d+20` avoids the exact-length odd-graph claim from the paper; the missing length is filled by even closed walks lifted from 3-, 4-, and 5-cycles in the one-element-replacement graph.

## Files

- `data/problems/fyum/fyum-2013-tur2a-p1.yaml`: replaced the source-only solution with a self-contained proof and updated solution status/metadata.
- `data/comments/comment-fyum-2013-tur2a-p1-outline-solution.yaml`: updated the old deferred note to record the repair.
- `data/sources/sources.yaml`: clarified the theorem source metadata with journal/DOI details and the special-case transfer note.

## Blockers

None for this card. The remaining human-review flag is only for non-solution metadata such as the unknown original author.

## Validation

- `python tools/validate.py` — passed.
- `python tools/check_links.py` — passed.

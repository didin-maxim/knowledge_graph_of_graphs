# Hard TC Repair

Date: 2026-04-27

Scope:

- `tc-2013-14-vertex-transitive-not-transposition#sol-counterexample-from-source`
- `tc-2001-02-rooks-odd-attacks#sol-construct-63`
- `tc-2023-24-coins-pairing-weighing-forest#sol-forest-accounting`

## Source Search

Checked local cards, source registry, sampled backlog, and public sources:

- problems.ru `98546` / official 2001/02 Tournament of Towns archive for the 63-rook construction.
- problems.ru `64663` and Kvant 2014 issue 4 for the original 12-city counterexample with a figure.
- problems.ru `67417` and SDAMGIA problem `10512` for the full 2023/24 coin-weighing algorithm and the forest accounting.

## Repaired

- `tc-2001-02-rooks-odd-attacks`: replaced the external-picture construction by an explicit coordinate order on the `8 x 8` board. The proof now checks why every new rook attacks an odd number of previous rooks and why a 64th rook is impossible.
- `tc-2013-14-vertex-transitive-not-transposition`: replaced the source-figure dependency by a fully explicit 12-vertex counterexample: the graph of the truncated tetrahedron on ordered pairs `(i,j)`. The solution proves vertex-transitivity and proves that no automorphism swaps `(1,2)` with `(2,3)`.
- `tc-2023-24-coins-pairing-weighing-forest`: expanded the missing algorithm. The solution now describes bunches, groups, ambiguous end cases, reconstruction of pair types, and why the comparison graph is a forest.

## Remaining Deferred

None in this TC scope.

## Validation

- `python tools/validate.py` - OK: 329 problems, 379 relations, 9 comments, 350 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools/check_links.py` - OK: 371 internal routes, 350 external source URLs syntactically valid.

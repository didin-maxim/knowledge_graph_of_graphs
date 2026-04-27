# High recheck: menger-theorem#sol-flow-sketch

Date: 2026-04-27

## Verdict

Resolved as full local solution.

## Issue

The previous proof used the standard max-flow/min-cut theorem and integral flow decomposition as external black boxes. No local theorem-card for these facts was available, so the solution was not self-contained enough for a high recheck.

## Repair

- Expanded `data/problems/classical/menger-theorem.yaml`.
- Added an in-solution proof of the finite integral max-flow/min-cut case via augmenting paths and the terminal residual reachable set.
- Added an in-solution proof that an integral flow of value `k` decomposes into `k` unit source-sink paths.
- Kept the vertex-splitting reduction and tied it explicitly to the proved finite integral flow facts.

## Validation

- `python tools/validate.py` - OK: 333 problems, 386 relations, 9 comments, 353 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools/check_links.py` - OK: 375 internal routes, 353 external source URLs syntactically valid.

## Changed files

- `data/problems/classical/menger-theorem.yaml`
- `audit/solution-full-recheck-2026-04-27/high-menger-theorem.md`

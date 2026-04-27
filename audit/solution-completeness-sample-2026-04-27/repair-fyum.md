# FYUM repair pass, 2026-04-27

Scope: sampled serious problems from the FYUM tournament archive.

## Repaired

- `fyum-2010-tur3a-p7`: replaced the outline with a complete counting proof. For every pair of colors the induced two-color subgraph is a forest; summing over the ten color pairs gives `|E(G)| <= 4n`, contradicting 100-regularity.
- `fyum-2010-tur1a-p8`: replaced the outline with a self-contained proof via dummy edges, splitting vertices into degree-`k` copies, and decomposing a regular bipartite multigraph into perfect matchings. The matching lemma is proved inside the solution by a maximal matching and alternating-path argument.
- `fyum-2011-tur2a-p9`: replaced the outline with the full Smith-Thomason parity argument: auxiliary graph on Hamiltonian paths starting with a fixed edge, rotation operation, parity of auxiliary degrees, and handshake lemma.

## Deferred

- `fyum-2013-tur2a-p1`: deferred. The current archive solution depends on the Chang--Montassier--Pecher--Raspaud theorem on strong edge colorings of planar graphs with large girth, specifically the `2Delta-1` bound under girth at least `10Delta+46`. Reproducing the discharging/minimal-counterexample proof is too large for a compact self-contained repair.
- `fyum-2009-tur3a-p7`: deferred. The current solution depends on the Bondy--Simonovits periodic-coloring lemma from the even-cycle extremal theory. A self-contained proof would require importing the long extremal theta/cycle argument rather than filling a local gap.
- `fyum-2011-finalb-p4`: deferred. The current solution depends on the Alspach--Rosenfeld/Straight theorem that every tournament realizes any two-block oriented Hamiltonian path. The transfer is direct, but proving the theorem here would be disproportionate.
- `fyum-2009-final-p2`: deferred. The lower-bound construction is present, but the upper bound uses the Burr--Erdos--Spencer Ramsey theorem for `m` disjoint monochromatic triangles, `R(mK_3,mK_3)=5m`. Importing that Ramsey theorem is too large for this pass.

## Not changed

- No placeholder-only tasks were edited.
- Comment files were left untouched.

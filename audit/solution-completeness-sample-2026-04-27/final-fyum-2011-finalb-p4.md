# Final FYUM 2011 Final (b) P4

Problem: `fyum-2011-finalb-p4`.

Final status: **solved locally**.

## What Changed

- Replaced the theorem-level deferred note in `data/problems/fyum/fyum-2011-finalb-p4.yaml` with a full Russian self-contained solution for exactly 200 vertices and block lengths 100/99.
- Updated the main idea from an external Alspach--Rosenfeld/Straight dependency to a direct construction of two outgoing directed branches from one root.
- Marked the solution and editorial review as `ai_checked` and `public_ready: true`.
- Updated the related resolved comment so it no longer says the card depends on the external two-block theorem.

## Proof Route

The desired path is equivalent to two directed paths starting at one vertex, of lengths 100 and 99, disjoint except for the root and covering all vertices.

The proof uses only elementary tournament facts, included in the solution text:

- every tournament has a directed Hamiltonian path;
- every strong tournament has a directed Hamiltonian cycle;
- strong components of a tournament are linearly ordered, and the first component dominates all later components.

Let `C` be the first strong component and `R` the rest.

- If `|C| <= 100`, concatenate Hamiltonian paths in `C` and `R`; the first vertex of the whole path beats the 101st vertex, so the path splits into branches of lengths 99 and 100.
- If `|C| >= 101`, cut a Hamiltonian cycle in `C`.
  - For even `|C|=2d`, use an opposite chord to get branch lengths `d` and `d-1`.
  - For odd `|C|=2d+1`, either a chord of cyclic distance `d+1` gives two branches of length `d`, or all such chords go backward, forcing chords of cyclic distance `d` forward and giving lengths `d+1` and `d-1`.
- The missing vertices needed to reach lengths 100 and 99 sum to `|R|`; split a Hamiltonian path in `R` into two pieces and append them, since every vertex of `C` beats every vertex of `R`.

## External Search Notes

I also rechecked the known theorem route:

- Bang-Jensen--Gutin survey: `https://www.cs.rhul.ac.uk/~gutin/paperstsp/t1.pdf`.
- Havet--Thomasse, *Oriented Hamiltonian Paths in Tournaments: A Proof of Rosenfeld's Conjecture*, JCTB 78 (2000), 243--273; accessible mirror found via CiteSeerX: `https://citeseerx.ist.psu.edu/document?doi=01e83f719d1dd1405343fb0fa6687273da524394&repid=rep1&type=pdf`.
- Bou Hanna, *Paths in tournaments: a simple proof of Rosenfeld's Conjecture*, arXiv:2011.14394, `https://arxiv.org/abs/2011.14394`.
- Bibliographic original two-block references remain: Brian Alspach and Moshe Rosenfeld, *Realization of certain generalized paths in tournaments*, Discrete Mathematics 34 (1981), 199--202, DOI `10.1016/0012-365X(81)90068-6`; H. J. Straight, *The existence of certain type of semi-walks in tournaments*, Congressus Numerantium 29 (1980), 901--908.

The final card no longer needs these external theorem proofs for completeness.

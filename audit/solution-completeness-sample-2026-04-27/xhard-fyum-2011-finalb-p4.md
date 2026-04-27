# xhard FYUM 2011 final (b) P4

Problem: `fyum-2011-finalb-p4`.

Verdict: **deferred**. I did not replace the card by a full self-contained Russian proof, because the proof dependency is still theorem-level.

## Exact Dependency

The task needs the following special case:

> Every tournament on 200 vertices contains a Hamiltonian oriented path of type
> `(-1)^100(+1)^99`, i.e. a Hamiltonian path with two maximal directed blocks
> of lengths 100 and 99.

Equivalently, it is enough to use the two-block case of Rosenfeld's path conjecture: every tournament contains every Hamiltonian oriented path with two directed blocks, apart from the classical small antidirected exceptions, which are irrelevant at order 200.

The transfer to FYUM is immediate. If the path is written as
`v_0,v_1,...,v_199`, then the first 100 edges oriented toward the beginning mean
`v_100 -> v_99 -> ... -> v_0`, and the next 99 edges oriented toward the end mean
`v_100 -> v_101 -> ... -> v_199`. Thus the desired object is exactly a two-block Hamiltonian oriented path.

## Sources Checked

- FYUM official source: `src-fyum-2011-finalb-p4-official`, `https://www.guas.info/competit/fest/fest22/finalb.tex`. The statement/source metadata already existed in the repository.
- Bang-Jensen--Gutin survey: `https://www.cs.rhul.ac.uk/~gutin/paperstsp/t1.pdf`. The existing source note records Section 10 as the reference for the Alspach--Rosenfeld/Straight two-block result.
- Havet--Thomasse, *Oriented Hamiltonian Paths in Tournaments: A Proof of Rosenfeld's Conjecture*, JCTB 78 (2000): accessible text mirror `https://paperzz.com/doc/7970060/oriented-hamiltonian-paths-in-tournaments--a`. The abstract states the full theorem with only three small exceptions; the introduction attributes the earlier two-block case to Alspach--Rosenfeld and Straight and says the full proof uses a long case analysis.
- Bou Hanna, *Paths in tournaments: a simple proof of Rosenfeld's Conjecture*, arXiv:2011.14394, `https://arxiv.org/abs/2011.14394`. This is an accessible proof source for the full theorem, but it is still a global theorem proof, not a compact olympiad-sized repair.
- Bibliographic confirmation for the original two-block paper: AMS/ScienceDirect records cite Brian Alspach and Moshe Rosenfeld, *Realization of certain generalized paths in tournaments*, Discrete Math. 34 (1981), 199--202, DOI `10.1016/0012-365X(81)90068-6`, and H. J. Straight, *The existence of certain type of semi-walks in tournaments*, Congressus Numerantium 29 (1980), 901--908.

## Why Deferred

I found reliable theorem statements and an accessible proof of the stronger Rosenfeld theorem, but not an open full text of the short Alspach--Rosenfeld/Straight two-block proof. The accessible complete proof route goes through Havet--Thomasse/Bou Hanna and a nontrivial exception analysis, so importing it would make the card a theorem citation rather than a compact self-contained solution.

## Repository Action

- `data/problems/fyum/fyum-2011-finalb-p4.yaml`: changed the solution entry to an explicit deferred note, kept the exact reduction to the two-block theorem, and marked the solution as `needs_human_review`.
- `data/sources/sources.yaml`: added `src-bou-hanna-rosenfeld-simple-proof` as an accessible proof source for the full Rosenfeld theorem.

No placeholder-task files were edited.

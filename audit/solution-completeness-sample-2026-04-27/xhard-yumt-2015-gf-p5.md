# XHard Audit: YUMT 2015 Grand Final Problem 5

Date: 2026-04-27

Scope:

- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`

## Verdict

`deferred_needs_self_contained_theorem_transfer`.

The missing step is now pinned down precisely. The task reduces to the theorem of Michael Stiebitz, "K5 is the only double-critical 5-chromatic graph", Discrete Mathematics 64 (1987), 91--93.

## Source Search

Checked local card/source registry and prior audit note. Public sources checked:

- YUMT official statement PDF: `https://adygmath.ru/content/files/smena2015/turnir15/final/zadan_grand.pdf`
- Math StackExchange related partition argument: `https://math.stackexchange.com/questions/2799049/partition-of-graph-in-two-sets-so-that-the-sum-of-chromatic-numbers-of-the-subgr`
- Stiebitz PDF mirror: `https://kostochk.web.illinois.edu/math583/stiebitz.pdf`
- Song survey on Erdős-Lovász Tihany: `https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2022/02/Survey_V1.pdf`
- Chudnovsky--Fradkin--Plumettaz paper overview: `https://web.math.princeton.edu/~mchudnov/ELT.pdf`

## Mathematical Status

The direct color-class/MSE argument is still insufficient: it makes one side independent, so it cannot prove the required "not 1-colorable" side.

The correct reduction is:

1. Take a vertex-minimal induced subgraph `H` with `χ(H)>4`; then `χ(H)=5`, `H` is 5-critical, and `H` is still `K_5`-free.
2. It is enough to find an edge `xy` of `H` with `χ(H-{x,y})>=4`; then `{x,y}` is the non-1-colorable side and the complement is non-3-colorable.
3. If no such edge exists, 5-criticality forces `χ(H-{x,y})=3` for every edge `xy`, so `H` is double-critical 5-chromatic.
4. Stiebitz 1987 proves that the only double-critical 5-chromatic graph is `K_5`, contradiction.

This is a complete theorem route, but not yet a self-contained Russian solution because the proof of Stiebitz's theorem itself was not imported into the card.

## Changes Made

- Added source `src-stiebitz-double-critical-k5`.
- Added the Stiebitz source to `yumt-2015-grand-final-problem5`.
- Rewrote the deferred note so it records the exact reduction through a 5-critical subgraph and the double-critical theorem.
- Corrected the draft idea that previously misdescribed a color class as potentially non-independent.

## Remaining Blocker

To promote the solution to `ai_checked`, import or independently reconstruct a self-contained Russian proof of Stiebitz's theorem `K_5` is the only double-critical 5-chromatic graph. The accessible paper is only three pages, but its proof has not been fully ported and checked here.

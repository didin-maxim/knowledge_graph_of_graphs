# Primary Sources Status

Date: 2026-04-27

This note summarizes which hard blockers now have usable primary sources and which still lack a portable proof/construction source.

## Extracted And Used

- `fyum-2013-tur2a-p1`
  - Primary source: Chang--Montassier--Pecher--Raspaud, NTU preprint / DMGT paper.
  - URL: `https://www.math.ntu.edu.tw/~mathlib/preprint/2013-09.pdf`
  - Status: enough proof text found and transferred.

- `fyum-2009-final-p2`
  - Primary source: Burr--Erdos--Spencer, 1975.
  - URL: `https://www.renyi.hu/~p_erdos/1975-35.pdf`
  - Status: enough proof text found and transferred for the needed diagonal case `r(qK_3)=5q`.

## Exact Primary Sources Found, But Not Yet Transferred

- `fyum-2011-finalb-p4`
  - Needed result: two-block Alspach--Rosenfeld/Straight theorem for oriented Hamiltonian paths in tournaments.
  - Bibliographic sources:
    - Alspach--Rosenfeld, Discrete Math. 34 (1981), DOI `10.1016/0012-365X(81)90068-6`.
    - Straight, Congressus Numerantium 29 (1980), 901--908.
  - Accessible proof route:
    - Bou Hanna, arXiv:2011.14394, `https://arxiv.org/abs/2011.14394`
    - Havet--Thomasse mirror, `https://paperzz.com/doc/7970060/oriented-hamiltonian-paths-in-tournaments--a`
  - Status: proof exists, but transfer is theorem-sized, not a local olympiad repair.

- `yumt-2015-grand-final-problem5`
  - Needed result: Stiebitz, "K5 is the only double-critical 5-chromatic graph".
  - URL: `https://kostochk.web.illinois.edu/math583/stiebitz.pdf`
  - Status: exact short paper found; proof still needs a careful Russian transfer or separate theorem card.

- `usamo-2023-p3-domino-slides-special-square-digraph`
  - Primary/proposal sources:
    - Evan Chen notes: `https://web.evanchen.cc/exams/USAMO-2023-notes.pdf`
    - Holden Mui proposal: `https://www.mit.edu/~hsmui/files/proposals/2023usamo3.pdf`
    - AoPS: `https://artofproblemsolving.com/wiki/index.php/2023_USAMO_Problems/Problem_3`
    - USAMO draft report: `https://campus.lakeforest.edu/trevino/USAMO2023.pdf`
  - Status: answer and upper bound are usable; small-value construction still figure-based and needs coordinate/text reconstruction.

## Still Missing Portable Primary Proof

- `chen-yu-independent-cutset-kolmogorov-merged` / Kolmogorov 2024 reduction
  - Primary source: Chen--Yu, "A note on fragile graphs", Discrete Mathematics 249 (2002), 41--43, DOI `10.1016/S0012-365X(01)00226-6`.
  - Metadata URL: `https://www.sciencedirect.com/science/article/pii/S0012365X01002266`
  - Status: statement and DOI confirmed; full PDF/proof blocked by access. Secondary papers cite or strengthen the theorem but do not reproduce the contraction induction.

## Practical Next Steps

1. For Chen--Yu, get the actual paper PDF through library access or another legitimate full-text source.
2. For YUMT 2015 GF P5, port Stiebitz's three-page proof into a theorem card.
3. For FYUM 2011 final B P4, decide whether the database should host a full Rosenfeld theorem card; otherwise keep citation-based deferred.
4. For USAMO 2023 P3, convert the diagram construction into coordinates or a proved alternating-path retile algorithm.

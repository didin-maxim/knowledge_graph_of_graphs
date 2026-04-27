# Solution Full Recheck 2026-04-27: Bucket 0

Bucket rule: `sha1(problem_id#solution_id) % 6 == 0`.

## Counts

- total: 67
- placeholders: 7
- checked_non_placeholder: 60
- repaired_easy: 1
- hard_cases: 3
- borderline: 4

## Repair Made

- `vosh-2000-01-final-universal-acquaintance#sol-complement-domination`:
  replaced a shaky one-sentence domination lemma proof with a self-contained proof via spanning trees of the complement graph components; promoted the solution status to `ai_checked`.

## Placeholders Counted Only

These entries are exact `Решение пока не найдено` placeholders and were not edited.

- `kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic#sol-import-note`
- `yumt-2014-grand-round1-problem5#sol-archive-card`
- `yumt-2017-start-high-round1-problem3#sol-archive-card`
- `yumt-2020-start-round1-problem4#sol-archive-card`
- `yumt-2021-grand-round1-problem2#sol-archive-card`
- `yumt-2024-unior-final-problem2#sol-archive-card`
- `yumt-2025-grand-round2-problem1#sol-archive-card`

## Hard List

- `kolmogorov-2015-round-2-graph-coloring-problem#sol-official-compressed`:
  not self-contained. The proof says a separating pair case "is shown" to preserve the cycle condition and then invokes the existence of a subdivision of `K_4` in the remaining case. Needs the official solution or a fully written proof of the 2-separation reduction and the `K_4`-subdivision/cycle-count step.
- `kolmogorov-2015-round-4-spies-and-opergroups-problem#sol-official-compressed`:
  not self-contained. It describes the reconstruction algorithm only at a high level ("split into classes by neighborhood and distance 2", "repeat") without the actual tests proving that the spy graph is uniquely recovered. Needs the official archive solution or a detailed reconstruction proof.
- `yumt-2015-grand-final-problem5#sol-archive-card`:
  this entry is an archive note, not a solution. The actual repaired solution is the separate `sol-external-mse-chromatic-partition` entry using the local Stiebitz theorem card. This entry should be removed/reclassified later or replaced by the real solution text; I did not change structure in this pass.

## Borderline

- `chen-yu-independent-cutset-kolmogorov-merged#sol-chen-yu-reference`:
  previously hard, now contains a full local proof route. I count it as passable, but borderline because it is a compact reconstruction of a paper theorem; independent source cross-check remains desirable.
- `stiebitz-double-critical-k5#sol-stiebitz-proof`:
  previously added to support YUMT 2015 GF P5. The proof is local and coherent, but it is a dense theorem-card proof of Stiebitz's result; keep as borderline until someone compares it line-by-line with the paper.
- `imo-2024-c3-knights-chord-uncrossing#sol-chord-uncrossing-induction`:
  the solution is likely correct, and the second non-bucket solution gives a clearer route, but this specific entry relies on a compressed "lemma" about reducing `2k+l`. Borderline for exposition/self-containedness.
- `utyum-2025_komol64_6_6_odd_degree_game#sol-official`:
  likely correct, but the lower-bound strategy compresses the terminal-forest argument ("each degree > 1 vertex has at least two leaves") enough that a future polish should expand it.

## Checked As Self-Contained

- `augmenting-path-matching-lemma#sol-symmetric-difference`
- `eulerian-graph-criterion#sol-cycle-splicing`
- `ferry-network-repartition-lemma#sol-repartition-network`
- `handshaking-lemma#sol-double-counting`
- `longest-path-endpoints-shortest-detour#sol-cycle-longer-than-path`
- `shortest-odd-cycle-external-neighbor-bound#sol-odd-arc-or-k4`
- `tree-equivalent-properties#sol-leaf-induction` (previously repaired; now covers all stated equivalences)
- `egmo-2025-p5-rotating-arrows-even-dynamic-cycle#sol-dynamic-cycle-bound` (previously repaired; no remaining encoding damage found)
- `fyum-2008-tur2a-p5#sol-official-archive`
- `fyum-2008-tur3b-p7#sol-official-archive`
- `fyum-2011-tur1b-p5#sol-official-archive`
- `imo-1979-p6-octagon-walks-cycle-graph#sol-graph-review`
- `imo-1996-c2-grid-vertices-two-red#sol-secondary-sketch`
- `imo-1998-c6-k-le-4-rainbow-edges-impossible#sol-k-le-4-impossible`
- `imo-2004-c3-delete-edge-from-4cycle#sol-reviewed-secondary` (previously repaired; lower and construction parts now explicit)
- `imo-2010-c2-flags-diagonal-matching#sol-official-compressed`
- `imo-2012-c7-equal-sum-chords-independent-set#sol-official-compressed`
- `imo-2019-c3-coin-process-digraph#sol-official-compressed`
- `imo-2019-c5-social-network-refriending#sol-official-compressed`
- `imo-2020-c4-fibonacci-difference-forest#sol-official-compressed`
- `imo-2023-c7-ferry-companies-hamiltonian-paths#sol-official-compressed`
- `imo-2024-c4-turbo-grid-monsters-three-attempts-strategy#sol-three-attempt-strategy`
- `kolmogorov-2002-individual-olympiad-10-11-output-problem-5#sol-official-compressed`
- `kolmogorov-2004-round4-first-junior-league-problem-10#sol-official-compressed`
- `kolmogorov-2006-round-1-super-high-first-league-problem-1#sol-official-compressed`
- `kolmogorov-2006-round-1-super-high-first-league-problem-9#sol-official-compressed`
- `kolmogorov-2006-round-4-super-league-problem-5#sol-official-compressed`
- `kolmogorov-2007-round-1-high-league-problem-5#sol-official-compressed`
- `kolmogorov-2007-round-4-first-league-problem-1#sol-official-compressed`
- `kolmogorov-2008-individual-olympiad-juniors-problem-8#sol-official-compressed`
- `kolmogorov-2008-individual-olympiad-seniors-problem-7#sol-official-compressed` (previously repaired from source; current proof is self-contained)
- `kolmogorov-2008-round-2-second-league-problem-2#sol-official-compressed`
- `kolmogorov-2008-team-olympiad-juniors-problem-5#sol-official-compressed`
- `kolmogorov-2010-individual-olympiad-juniors-problem-5#sol-official-compressed`
- `kolmogorov-2010-individual-olympiad-seniors-problem-4#sol-official-compressed`
- `kolmogorov-2011-team-olympiad-juniors-problem-6#sol-official-compressed`
- `kolmogorov-2012-individual-olympiad-seniors-problem-1#sol-official-compressed`
- `kolmogorov-2012-individual-olympiad-seniors-problem-6#sol-official-compressed` (previously repaired; diagonal estimate and construction are present)
- `kolmogorov-2013-team-olympiad-seniors-problem-8#sol-official-compressed`
- `kolmogorov-2021-komol-chip-firing-edge-discrepancy#sol-cut-flow`
- `memo-2021-i2-bishop-circuit-forest#sol-official-compressed`
- `rmm-2023-p6-colored-spanning-tree-suspicious-edges#sol-official-compressed` (previously repaired; exchange proof is now local)
- `tc-2009-10-acquaintances-even-cycle#sol-longest-path-parity`
- `usa-tst-2011-p2-weighted-road-orientation#sol-eulerian-augmentation`
- `utyum-2012_komol39_5_republic_in_complete_graph#sol-official`
- `utyum-2018_komol_7_acquaintance_scores#sol-official`
- `utyum-2018_komol_7_red_blue_cycle_game#sol-official`
- `vosh-2000-01-final-universal-acquaintance#sol-complement-domination`
- `vosh-2008-regional-bureaucrats-common-neighborhood#sol-double-counting-triples`
- `vosh-2013-14-regional-even-rows-columns#sol-complement-forest-tjoin`
- `yumt-2012-start-team-olympiad-problem5#sol-archive-card`
- `yumt-2014-start-round1-problem1#sol-archive-card`
- `yumt-2015-start-round4-problem6#sol-archive-card`

## Validation

- `python tools\validate.py` was run after the edit. It still fails on pre-existing, out-of-bucket issues:
  `usamo-2025-p3-gabriel-graph-road-network.yaml` graph-theory statement wording/duplicate similarity, and
  `yumt-2013-start-round1-problem3.yaml` unknown definition route `graph`.
- `python tools\check_links.py` was run after the edit. It still fails on the same out-of-bucket broken definition route:
  `yumt-2013-start-round1-problem3 -> graph`.
- `git diff --check` passed; Git only printed CRLF normalization warnings for existing modified files.

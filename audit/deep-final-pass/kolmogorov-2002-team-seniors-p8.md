# Kolmogorov 2002 Team Seniors P8

Verdict: `repaired_full_solution_from_official_source`.

Target file:

- `data/problems/kolmogorov/kolmogorov-2002-team-olympiad-seniors-problem-8.yaml`

Source work:

- Local repository had only the previous compressed card and the earlier `plan-to-solution-pass` deferral.
- The official source entry points to `https://turmath.ru/kolm/files/archive/kolm6.zip`.
- I downloaded that archive into `tmp/kolm6.zip`, extracted `tmp/kolm6/OlympVI.doc`, and parsed the legacy Word `.doc` text through its OLE `WordDocument`/`1Table` streams.
- The extracted official text contains `КОМАНДНАЯ ОЛИМПИАДА 2.12.02. ЗАДАНИЯ ДЛЯ СЕНЬОРОВ`, problem 8 statement, and a full `Решение` section for `Задача 8`.

What was missing before:

- Lemma 1 was only named; the Hall/minimal-counterexample proof was absent.
- The parameter `k` in Lemma 2 was underspecified.
- The reduction from intersections of blocks to the auxiliary subgraph `T\L` was not justified.
- The final step needed the quantitative inequality `2(n-k-1)>n`.

Repair made:

- Added `sol-official-full` with status `ai_checked`.
- Set its `repair_status` to `repaired_full_solution_from_official_source`.
- Added detailed `review_notes` naming the official archive and extracted `OlympVI.doc`.
- Kept the older compressed solution as historical context; the complete repaired solution is now the first solution entry.
- Added an editorial note recording this deep final pass.

Mathematical content now present:

- Defines `Delta` and `k=Delta-n`, deriving `2(k+1)<n`.
- Proves Dolnikov's lemma via the complement graph, maximal bad sets, Hall's lemma, and minimal counterexample descent.
- Proves the block-intersection lower bound `|L| >= n-k-1`.
- Finishes by adding blocks intersecting a fixed block `H` one at a time and using `2(n-k-1)>|H|`.

Validation:

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`

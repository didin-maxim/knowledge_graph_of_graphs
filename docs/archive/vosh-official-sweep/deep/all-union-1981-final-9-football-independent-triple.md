# Deep check: all-union-1981-final-9-football-independent-triple

Date: 2026-05-05

## Card

- File: `data/problems/all-union/all-union-1981-final-9-football-independent-triple.yaml`
- Problem: All-Union Mathematical Olympiad 1981, final round, grade 9, problem 7 / collection problem 135.
- Scope: one-card high-reasoning pass; no shared generated files edited.

## Sources checked

- `src-djvuonline-vseross-9-1997`: OCR page for "Математические олимпиады школьников. 9 класс", 1997. It gives the statement as problem 135 and includes the short solution by fixing one team and counting possible matches inside the 9 non-opponents.
- `src-mathru-vsesoyuznye-1988`: Math.ru page for Н.Б. Васильев, А.А. Егоров, "Задачи всесоюзных математических олимпиад", Наука, 1988. The local source entry records this as the published collection scan.
- Internet check: `https://djvu.online/file/HVkVYzyetRjkZ`, journal publication "XV Всесоюзная математическая олимпиада" in "Математика в школе", 1981. The problem list states that problem authors are given in parentheses and attributes the grade-9 problem 7 to "С. Конягин".

## Statement and graph-theory check

The original statement depends on the fact that 18 teams played 8 full rounds, not only on every team having 8 played opponents. The previous graph-theory statement, "every vertex has degree 8", was too strong and false: two disjoint copies of \(K_9\) form an 8-regular graph on 18 vertices with no independent set of size 3.

The corrected graph formulation keeps the round structure: the edge set is split into 8 matchings, and each vertex is incident to one edge in each matching.

## Solution classification

Type: `unofficial_published`.

Reason: a complete short published solution was found in the OCR/published collection sources. I did not mark it as official because the local source registry marks the available source ids as non-official, and this pass was not allowed to add a new `data/sources/sources.yaml` entry for the 1981 journal publication.

## Relations

Local relation search suggested only broad motif neighbors: Ramsey-type and complement/degree-counting graph problems. No confident `reprint`, `reformulation`, `solution_transfer`, or `prerequisite` link was added. Set `relations_status` to `reviewed_no_links`.

## Risk notes

- The author is recorded as "С. Конягин" exactly at the source granularity seen in the 1981 publication; the card does not infer a full first name.
- `public_ready` remains `false`, because the source registry does not yet contain the 1981 journal source used for the author/proposer check.

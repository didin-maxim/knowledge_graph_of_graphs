# Full solution recheck, bucket 5

Дата: 2026-04-27.

Bucket rule: `sha1(problem_id#solution_id) % 6 == 5`.

## Counts

- total: 70
- placeholders: 11
- checked_non_placeholder: 59
- repaired_easy: 0
- hard_cases: 7
- borderline: 6

Placeholder `Решение пока не найдено` считался no-solution entry и не редактировался.

## Hard Cases

1. `fyum-2008-tur4a-p7#sol-official-archive`
   - Причина: решение ссылается на лемму о замыкании и затем говорит, что в замыкании условие на степени заставляет существовать гамильтонов цикл. Сам ключевой переход фактически является теоремой Хватала/Оре и не доказан в карточке.
   - Нужно: либо самодостаточное доказательство замыкания и финального шага для данной последовательности степеней, либо точная ссылка на официальное решение/теорему, после чего перенести доказательство в карточку.

2. `fyum-2010-tur2a-p1#sol-official-archive`
   - Причина: нижняя часть доказательства держится на фразе "для каждой вершины вспомогательного графа степень нечётна; это напрямую проверяется", но сама проверка степени не выписана. Для задачи о чётности это ключевой шаг.
   - Нужно: официальное архивное решение или полное доказательство нечётности степени во вспомогательном графе недоминирующих множеств.

3. `kolmogorov-2004-round3-higher-league-problem-10#sol-official-compressed`
   - Причина: текст является пересказом плана: "подробно исследуются ребра", "выводятся жесткие ограничения". Проверить доказательство локально невозможно.
   - Нужно: официальный разбор компоненты `K` в `G-a` с полным перечислением случаев и противоречием с исходящей степенью не меньше 2.

4. `kolmogorov-2016-individual-olympiad-juniors-problem-7#sol-official-compressed`
   - Причина: описан итерационный алгоритм с синими/красными стрелками, но не доказаны инварианты процесса и финальное покрытие каждой невыбранной вершины выбранной.
   - Нужно: официальное решение или подробная лемма о завершении процесса и сохранении независимости выбранных вершин.

5. `kolmogorov-2021-round1-second-league-problem-8#sol-official-compressed`
   - Причина: ключевой подсчёт заменён фразой "из этого получается нижняя оценка на sum c_i". Это главный шаг доказательства.
   - Нужно: полный официальный подсчёт по цветовым компонентам, включая классификацию вершин и вывод `sum c_i >= 2n - 1`.

6. `usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph`
   - Причина: карточка сама помечена `Deferred`; нижняя конструкция для всех `m,k` не доказана, нужен общий алгоритм перекладки/покрытия красных домино после разреза змейки.
   - Нужно: официальный USAMO 2023 P3 разбор или полное доказательство общей конструкции; имеющиеся схемы для `n=7` недостаточны.

7. `utyum-2018_lichol_8_tree_cities#sol-official`
   - Причина: решение ссылается на общий локальный шаг в дереве и "разбирают ещё один локальный случай", но сами случаи не выписаны.
   - Нужно: официальный текст или самостоятельная индукция по дереву с полным разбором листовых конфигураций.

## Borderline

1. `fyum-2009-tur2a-p4#sol-official-archive`
   - Почти читается, но фраза "условие задачи показывает, что циклы через выбранное плохое ребро не могут быть нечётными" требует локального пояснения связи с числом важных нечётных циклов. Нужен небольшой абзац из официального решения.

2. `fyum-2009-tur4a-p2#sol-official-archive`
   - Идея понятна, но "максимальный ациклический подграф" и замена развёрнутого ребра ориентированным путём в `H` требуют аккуратной формализации максимальности.

3. `imo-2005-c3-black-paths-injection#sol-reviewed-secondary`
   - Инъекция выглядит правильной, но для полной самодостаточности нужно явно доказать единственность нижнего прохода и обратимость операции по нижнему пути. Статус уже `needs_human_review`.

4. `usamo-2021-p2-planar-national-park-turning-walk#sol-local-state-bound-and-prism`
   - Верхняя оценка содержит топологический шаг про два противоположных поворота в одной траектории; формулировка правдоподобна, но не полностью доказана.

5. `complete-graph-triangle-edge-weights-minimum-parametric#sol-parametric`
   - Пример и ответ проверяются, но нижняя оценка зависит от "локального шага из официального решения", который не выписан. Статус уже `needs_human_review`.

6. `usamo-2022-p1-amber-bronze-transversal#sol-hall-matchings-and-uncrossing`
   - Главная идея с двумя паросочетаниями ясна, но uncrossing-шаг через пустую строку и столбец требует уточнить, что удаляемое конфликтующее ребро всегда можно выбрать так, чтобы сохранить паросочетание и уменьшить число конфликтов.

## Checked As Self-Contained

- `apmo-2005-p4-firefighters-grid-spread#sol-official-compressed`
- `bmo-2022-p4-frog-grid-boundary-graph#sol-official-compressed`
- `bmo-2025-p4-flights-long-short-paths#sol-official-compressed`
- `benjamini-tzalik-shortest-paths-kolmogorov-merged#sol-bound-and-even-exact`
- `brooks-theorem#sol-sketch`
- `color-reduction-by-odd-deletion-and-doubling#sol-even-core-and-double`
- `pairwise-intersecting-edges-star-or-triangle#sol-star-or-triangle`
- `tournament-king-radius-two#sol-max-outdegree`
- `fyum-2008-final-p8#sol-official-archive`
- `fyum-2011-tur2a-p9#sol-official-archive`
- `imo-1994-c2-city-ages-harmonic-graph#sol-secondary-sketch`
- `imo-1994-c6-infinite-grid-pairing-strategy#sol-reviewed-secondary`
- `imo-1996-c1-grid-knight-reachability-r73-path#sol-explicit-r73-path`
- `imo-1996-c1-grid-knight-reachability-r97-impossible#sol-aops-band-invariant`
- `imo-1998-c6-k-ge-6-one-factorization#sol-k-ge-6-one-factorization`
- `imo-2013-c3-imons-graph-coloring#sol-official-compressed`
- `imo-2013-c6-flight-distance-layers#sol-mse-neighbor-partition`
- `imo-2014-c9-snail-circles-tree#sol-official-compressed`
- `imo-2016-c6-ferry-graph-dynamics#sol-official-compressed`
- `imo-2021-c4-anisotropy-menger#sol-official-compressed`
- `imo-2024-c4-turbo-grid-monsters-two-attempts-lower-bound#sol-two-attempt-adversary`
- `kolmogorov-2004-round2-higher-league-problem-9#sol-official-compressed`
- `kolmogorov-2006-round-2-super-league-problem-6#sol-official-compressed`
- `kolmogorov-2006-team-olympiad-seniors-problem-9#sol-official-compressed`
- `kolmogorov-2011-individual-olympiad-seniors-problem-7#sol-official-compressed`
- `kolmogorov-2013-team-olympiad-juniors-problem-7#sol-official-compressed`
- `kolmogorov-2014-round1-oriendiriya-road-orientation-game#sol-second-player-block-strategy`
- `kolmogorov-2022-round2-high-colored-integers-infinite-tree#sol-official-restored`
- `kolmogorov-2023-lichol-large-monochromatic-bipartite-component#sol-degree-sum-component`
- `rmm-2017-p5-sieve-sticks-bipartite-matching#sol-official-compressed`
- `tc-2017-18-polyhedron-three-colors-parity#sol-bicolor-paths`
- `tc-2018-19-simple-state-tree-game#sol-petya-tree-invariant`
- `tc-2020-21-gnomes-two-cycles-even-n#sol-even-color-obstruction`
- `usa-tst-2011-p2-weighted-road-orientation#sol-mse-auxiliary-vertex-euler-tour`
- `usa-tst-2013-dec-p1-language-club-rainbow-triangles#sol-count-local-repeats`
- `usajmo-2023-p3-domino-slides-special-square-digraph#sol-directed-graph-and-spanning-tree-bound`
- `usamo-2004-p4-black-path-grid-game#sol-bob-useless-squares`
- `utyum-2016_tur1_start2_1_octahedron_acquaintances#sol-official`
- `utyum-2019_komol_7_airline_costs#sol-official`
- `utyum-2021_komol_6_archipelago_bridges#sol-official`
- `utyum-2023_komol60_7_7_room_departures#sol-official`
- `utyum-2023_komol61_8_5_yozhgorod_registry#sol-official`
- `utyum-2025_komol65_7_6_airlines_degree_sum#sol-official`
- `vosh-2010-11-final-nonbreakable-company#sol-minimal-odd-cycle`
- `yumt-2020-start-round2-problem4#sol-archive-card`

## Placeholders Counted Only

- `kolmogorov-2014-round3-city-triangle-routes#sol-import-note`
- `kolmogorov-2014-round3-four-regular-two-100-cycles#sol-import-note`
- `yumt-2011-grand-round4-problem9#sol-archive-card`
- `yumt-2014-grand-round2-problem9#sol-archive-card`
- `yumt-2017-premier-round1-problem2#sol-archive-card`
- `yumt-2017-start-first-round1-problem3#sol-archive-card`
- `yumt-2018-grand-final-problem1#sol-archive-card`
- `yumt-2025-grand-final-problem3#sol-archive-card`
- `yumt-2025-grand-round1-problem4#sol-archive-card`
- `yumt-2025-grand-round1-problem9#sol-archive-card`
- `yumt-2025-unior-round3-problem1#sol-archive-card`

## Notes

- Полный проход включал уже ранее исправленные решения; они перечислены выше в self-contained, borderline или hard в зависимости от текущей проверки.
- Лёгких содержательных правок в bucket 5 не сделал: найденные дефекты либо не мешают самодостаточности, либо требуют внешнего официального текста/теоремы и попали в hard/borderline.

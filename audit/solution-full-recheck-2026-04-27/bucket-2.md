# Full solution recheck: bucket 2

Дата: 2026-04-27.

Bucket rule: `sha1(problem_id#solution_id) % 6 == 2`.

## Counts

- total: 65
- placeholders: 10
- checked_non_placeholder: 55
- repaired_easy: 7
- hard_cases: 7
- borderline: 5

Placeholders counted as no-solution entries and not edited:

- `kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths#sol-import-note`
- `yumt-2012-start-round3-problem1#sol-archive-card`
- `yumt-2014-grand-round4-problem1#sol-archive-card`
- `yumt-2020-100-v-shapes-disjoint#sol-archive-card`
- `yumt-2022-grand-final-problem1#sol-archive-card`
- `yumt-2023-granda-final-problem6#sol-archive-card`
- `yumt-2023-granda-round4-problem3#sol-archive-card`
- `yumt-2024-grand-round3-problem8#sol-archive-card`
- `yumt-2024-start-final-problem7#sol-archive-card`
- `yumt-2025-unior-round1-problem8#sol-archive-card`

## Easy Repairs

- `kolmogorov-2006-round-2-first-junior-league-problem-8#sol-official-compressed`: добавлена явная конструкция связной фигуры с `n` чёрными и `3n+1` белыми клетками.
- `kolmogorov-2022-individual-seniors-p2-cycle-arrangements#sol-official-restored`: убран TeX-хвост `\footnote{...}`/лишняя скобка, решение переписано как самодостаточная биекция с перестановками.
- `kolmogorov-2022-round1-high-edge-count-permutation-nonedges#sol-official-restored`: удалён явный хвост импорта с критериями оценивания и началом следующего листа.
- `kolmogorov-2022-round4-second-third-even-degree-odd-walks#sol-official-restored`: удалён явный хвост импорта с критериями оценивания и чужой задачей.
- `usamo-2008-p6-even-friends-two-rooms#sol-adjacency-matrix-over-f2`: добавлена проверка совместности линейной системы над `F_2`; решение больше не ссылается на AoPS для существования.
- `usamo-2025-p3-gabriel-graph-road-network#sol-gabriel-planar-bound`: добавлен финальный переход от связности и планарности к вершине степени не больше 5 через оценку `E <= 3V-6`.
- `utyum-1995_final_10_writers_committee#sol-official`: исправлена фраза про среднюю степень в оставшемся подграфе: нужна средняя входящая степень не больше 3, а не сохранение исходящей ровно 3.

## Hard Cases

- `fyum-2009-tur1a-p7#sol-official-archive`: решение опирается на две нетривиальные леммы о сильносвязных турнирах и укорачивании циклов без доказательства. Нужен официальный источник или локальное доказательство этих лемм.
- `kolmogorov-2008-round-1-first-league-and-higher-junior-problem-1#sol-official-compressed`: верхняя оценка `n-3` изложена как ссылка на официальный приём; фраза про звезду не даёт самодостаточного алгоритма между двумя произвольными деревьями. Нужен официальный текст/полное доказательство.
- `kolmogorov-2008-round-4-first-league-and-higher-junior-problem-1#sol-official-compressed`: решение предполагает, что красно-синяя раскраска является правильной двудольной раскраской дерева, но текущая формулировка этого не говорит. В произвольной раскраске утверждение ложно, например путь `blue-red-red-blue`. Нужен источник для уточнения условия.
- `kolmogorov-2022-round1-high-edge-count-permutation-nonedges#sol-official-restored`: после удаления TeX-хвоста остаётся существенный пробел в индукционном продолжении перестановки при двух листьях разных компонент. Нужен полный официальный аргумент.
- `kolmogorov-2022-round4-second-third-even-degree-odd-walks#sol-official-restored`: после удаления TeX-хвоста решение всё ещё не самодостаточно: смешаны обозначения `n`/`d`, есть опечатка `доходы`, а ключевой parity-аргумент для замкнутых маршрутов не доведён. Нужен официальный источник или новая полная линейно-алгебраическая версия.
- `utyum-2011_tur4_37_8_equal_sums_bipartite_graph#sol-official`: текущее решение неверно: оно требует 100 попарно различных степеней в двудольном графе с долями по 50, хотя степень вершины не может превышать 50; также предложенные степени в двух долях имеют разные суммы. Нужен официальный метод изменения чисел/весов, не просто степени.
- `yumt-2016-start-high-round1-problem7#sol-archive-card`: подсчёт 68 опирается на официальный рисунок и нераскрытый разбор четвёртого квадрата. Нужен рисунок/официальный разбор 4 исключительных конфигураций.

## Borderline

- `fyum-2009-tur3a-p7#sol-official-archive`: доказательство леммы Bondy--Simonovits развёрнуто, но место про продолжение пути внутри theta-подграфа на любую длину `0..t-1` очень плотное; желательно отдельная проверка.
- `imo-2024-c3-knights-chord-uncrossing#sol-distance-and-walking-count`: верхняя оценка использует сжатую хордную терминологию `k,l,m`; решение читается, но для полной автономности полезен рисунок или более явное описание движения.
- `usamo-2008-p6-even-friends-two-rooms#sol-good-configurations-as-group`: альтернативное решение предполагает существование хорошего разбиения; теперь оно доказано в соседнем линейно-алгебраическом решении, но эта запись не полностью независима.
- `utyum-2002_carousel_senior_8x8_polyline#sol-official`: верхняя оценка доказана, но пример ломаной длины 80 только заявлен; нужен явный маршрут или рисунок.
- `yumt-2019-start-high-round1-problem7#sol-archive-card`: финальный шаг с критерием степеней дерева стандартен, но не доказан; допустимо как известный факт, однако для полной автономности лучше добавить Prüfer/индукционное доказательство.

## Checked OK

Остальные non-placeholder решения bucket 2 проверены как самодостаточные для первого прохода:

- `apmo-2016-p4-dreamland-28-step-coloring#sol-official-compressed`
- `konig-vertex-cover-theorem#sol-alternating`
- `planar-edge-bound#sol-face-counting`
- `ramsey-r33#sol-pigeonhole`
- `ramsey-theorem#sol-recursive-bound`
- `turan-theorem#sol-symmetrization`
- `fyum-2010-tur3a-p7#sol-official-archive`
- `fyum-2011-finalb-p4#sol-official-archive`
- `fyum-2013-tur1b-p10#sol-official-archive`
- `imo-1986-sl12-increasing-edge-trail#sol-graph-review`
- `imo-2010-c5-bad-company-tournament#sol-official-compressed`
- `imo-2013-c6-flight-distance-layers#sol-official-compressed`
- `imo-2016-c8-domino-unique-tiling-cycles#sol-official-compressed`
- `imo-2020-c6-colored-coins-eulerian-multigraph#sol-official-compressed`
- `imo-2023-c4-strip-pieces-eulerian-graph#sol-official-compressed`
- `kolmogorov-2006-round-2-first-junior-league-problem-8#sol-official-compressed`
- `kolmogorov-2007-round-2-high-and-first-league-chromatic-number-problem#sol-official-compressed`
- `kolmogorov-2008-round-3-high-league-problem-1#sol-official-compressed`
- `kolmogorov-2008-team-olympiad-seniors-problem-7#sol-double-counting-expanded`
- `kolmogorov-2011-team-olympiad-seniors-problem-4#sol-official-compressed`
- `kolmogorov-2013-individual-olympiad-seniors-problem-5#sol-official-compressed`
- `kolmogorov-2019-team-olympiad-juniors-problem-8#sol-official-compressed`
- `kolmogorov-2021-individual-olympiad-seniors-problem-5#sol-official-compressed`
- `kolmogorov-2022-individual-seniors-p2-cycle-arrangements#sol-official-restored`
- `kolmogorov-2022-round1-third-binary-strings-pairing-graph#sol-official-restored`
- `memo-2022-t4-teleport-table-reachability#sol-official-compressed`
- `tc-2010-11-odd-main-roads#sol-path-parity`
- `tc-2018-19-complex-state-cycle-game#sol-vasya-cycle-induction`
- `usamo-2008-p6-even-friends-two-rooms#sol-adjacency-matrix-over-f2`
- `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles#sol-induction-plus-alternating-cycles`
- `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles#sol-community-overlay-boundary`
- `usamo-2025-p3-gabriel-graph-road-network#sol-gabriel-planar-bound`
- `utyum-1995_final_10_writers_committee#sol-official`
- `utyum-2001_olymp8_6_countries_route#sol-official`
- `utyum-2004_line_acquaintances_endpoints#sol-official`
- `utyum-2012_komol39_8_binary_tree_ordering#sol-official`
- `utyum-2016_tur2_3_min_acquaintance_pairs#sol-official`
- `utyum-2021_komol_7_no_k5_many_acquaintances#sol-official`
- `utyum-2024_komol62_6_3_circle_graph_coloring#sol-official`
- `utyum-2024_komol62_8_5_average_degree_friends#sol-official`
- `utyum-2024_komol63_8_4_lipshire_roads#sol-official`
- `utyum-2025_komol64_8_7_tree_matchings_path#sol-official`
- `vosh-2000-01-final-universal-acquaintance#sol-clique-extension`

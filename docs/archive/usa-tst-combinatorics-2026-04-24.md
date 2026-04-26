# USA TST Combinatorics Scan

Дата просмотра: `2026-04-24`

Рабочее допущение для этой подборки: под `TST` здесь понимается `USA Team Selection Test`.

Основные найденные источники:

- `2005 USA TST`: <https://artofproblemsolving.com/downloads/printable_post_collections/4635.pdf>
- `2007 USA TST`: <https://artofproblemsolving.com/wiki/index.php/2007_USA_TST_Problems>
- `2009 USA TST`: <https://artofproblemsolving.com/downloads/printable_post_collections/4639>
- `2010 USA TST`: <https://artofproblemsolving.com/downloads/printable_post_collections/4640>
- `2011 USA TST`: <https://artofproblemsolving.com/downloads/printable_post_collections/4641>
- `2013 USA TST`: <https://artofproblemsolving.com/downloads/printable_post_collections/4643>

## Короткий реестр

| Год | Задача | Короткая тема | Графовый слой | Решение по базе |
| --- | --- | --- | --- | --- |
| 2005 | Day 1, Problem 1 | семейство `2n` подмножеств с попарными пересечениями не более 1 | сильный граф в решении: простой `m`-регулярный граф на `2n` вершинах | `added` |
| 2005 | Day 2, Problem 5 | конечные множества точек, замкнутые относительно параллелограмма | графовая модель не обязательна | `saved_only` |
| 2007 | Problem 2 | последовательности с одинаковым мультимножеством разностей | графовый слой не центральный | `saved_only` |
| 2009 | Day 2, Problem 6 | шахматный турнир с условием на цепочки побед длины `M` | граф в условии: турнир | `added` |
| 2010 | Day 2, Problem 6 | хорошие подмножества множества чисел по НОД | графовая модель не центральна | `saved_only` |
| 2011 | Day 1, Problem 2 | дороги с пропускными способностями `1/2` и баланс входа-выхода | граф в условии: взвешенный граф и ориентация | `added` |
| 2011 | Day 3, Problem 8 | плотное семейство пар `(a,b)` внутри `[1,2^n]` | можно читать как граф на вершинах `1..2^n`, но граф не нужен как основной язык | `saved_only` |
| 2013 | December TST, Problem 1 | языки в клубе и радужные тройки | граф в условии: раскраска рёбер полного графа | `added` |
| 2013 | January TST, Problem 3 | преобразование `0/1`-таблиц | графовый слой не центральный | `saved_only` |

## Что реально импортировано

- `usa-tst-2005-p1-set-system-incidence-graph`
- `usa-tst-2009-p6-tournament-gap-ordering`
- `usa-tst-2011-p2-weighted-road-orientation`
- `usa-tst-2013-dec-p1-language-club-rainbow-triangles`

## Почему именно эти три

- `2005 P1`: графовая модель не декоративная, а полностью решает задачу через простой регулярный граф.
- `2011 P2`: граф присутствует прямо в условии, а решение естественно идёт через доведение до эйлерова случая.
- `2013 Dec P1`: задача по существу является задачей о `k`-раскраске рёбер `K_{2k+1}` без одноцветных треугольников и максимуме радужных троек.

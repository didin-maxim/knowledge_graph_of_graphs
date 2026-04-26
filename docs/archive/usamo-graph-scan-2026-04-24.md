# USAMO Graph Scan

Дата просмотра: `2026-04-24`

Текущее состояние базы:

- отдельного слоя `USAMO` в `data/problems/` пока нет;
- по текущим карточкам идентификаторы/заголовки `USAMO` не находятся;
- значит архив `USAMO` ещё не заведён в базу как самостоятельная серия.

Основные открытые точки входа:

- `USAMO Problems and Solutions` (AoPS Wiki): <https://artofproblemsolving.com/wiki/index.php/USAMO_Problems_and_Solutions>
- `2022 USAMO`: <https://artofproblemsolving.com/wiki/index.php/2022_USAMO>
- `2022 USAMO Problems`: <https://artofproblemsolving.com/wiki/index.php/2022_USAMO_Problems>
- `2022 USAMO Problems/Problem 1`: <https://artofproblemsolving.com/wiki/index.php?title=2022_USAMO_Problems%2FProblem_1>
- `2024 USAMO`: <https://artofproblemsolving.com/wiki/index.php/2024_USAMO>
- `2024 USAMO Problems`: <https://artofproblemsolving.com/wiki/index.php/2024_USAMO_Problems>
- `2024 USAMO Problems/Problem 3`: <https://artofproblemsolving.com/wiki/index.php/2024_USAMO_Problems/Problem_3>

## Подходящие задачи: сильное ядро

| Год | Задача | Короткая тема | Почему подходит | Открытый источник |
| --- | --- | --- | --- | --- |
| 1976 | Problem 1 | монохроматический прямоугольник на `4x7` доске | естественно читается как двухцветная раскраска рёбер `K_{4,7}` с поиском одноцветного `C_4`; графовый язык не декоративный | <https://artofproblemsolving.com/wiki/index.php/1976_USAMO_Problems> |
| 1999 | Problem 1 | шашки на доске с локальным покрытием и связностью | в AoPS-решении прямо вводится граф по занятым клеткам и используется circuit rank | <https://artofproblemsolving.com/wiki/index.php/1999_USAMO_Problems/Problem_1> |
| 2004 | Problem 4 | игра на сетке `6x6` и чёрный путь сверху вниз | условие уже почти сформулировано через достижимость/перколяцию на клеточном графе | <https://artofproblemsolving.com/wiki/index.php/2004_USAMO_Problems/Problem_4> |
| 2008 | Problem 3 | разбиение ромбовидного множества решётчатых точек на пути | граф в условии: вершины решётки и пути по рёбрам соседства | <https://artofproblemsolving.com/wiki/index.php/2008_USAMO_Problems/Problem_3> |
| 2008 | Problem 6 | друзья/незнакомцы и рассадка по двум комнатам с чётностью друзей | чистая задача на граф дружбы и паритет в индуцированных подграфах | <https://artofproblemsolving.com/wiki/index.php/2008_USAMO_Problems/Problem_6> |
| 2021 | Problem 2 | прогулка по 3-регулярному планарному графу с чередованием поворотов | граф прямо в условии: cubic planar graph, обход, локальные правила на вершинах | <https://artofproblemsolving.com/wiki/index.php/2021_USAMO_Problems/Problem_2> |
| 2022 | Problem 1 | выбор янтарных и бронзовых клеток без общих строк и столбцов | сильная двудольная модель через клетки как рёбра между строками и столбцами; естественный язык Hall/matching | <https://artofproblemsolving.com/wiki/index.php/2022_USAMO_Problems/Problem_1> |
| 2022 | Problem 6 | социальная сеть, новые дружбы при двух общих друзьях | граф в условии и динамика замыкания по общим соседям | <https://artofproblemsolving.com/wiki/index.php/2022_USAMO_Problems/Problem_6> |
| 2024 | Problem 3 | `m`-сбалансированная триангуляция правильного `n`-угольника | триангуляция сама по себе графовый объект; можно строить карточку как polygon triangulation / outerplanar structure | <https://artofproblemsolving.com/wiki/index.php/2024_USAMO_Problems/Problem_3> |
| 2025 | Problem 3 | города и дороги, возникающие по геометрическому правилу | AoPS-решение прямо распознаёт Gabriel graph, планарность и связность | <https://artofproblemsolving.com/wiki/index.php/2025_USAMO_Problems/Problem_3> |

## Пограничные, но, вероятно, тоже полезные

| Год | Задача | Короткая тема | Комментарий | Открытый источник |
| --- | --- | --- | --- | --- |
| 2008 | Problem 4 | триангуляция правильного `n`-угольника из одних равнобедренных треугольников | триангуляция есть в условии, но решение может оказаться более арифметико-геометрическим, чем графовым | <https://artofproblemsolving.com/downloads/printable_post_collections/4506> |
| 2009 | Problem 3 | tasteful domino tilings шахматного многоугольника | естественно хочется переводить в matching/tiling graph, но на AoPS-странице нет решения | <https://artofproblemsolving.com/wiki/index.php/2009_USAMO_Problems/Problem_3> |
| 2023 | Problem 3 | maximal domino configurations на нечётной доске | по условию это задача о домино на сетке; возможно полезна как matching-производная, но нужен отдельный просмотр решения | <https://artofproblemsolving.com/wiki/index.php/2023_USAMO_Problems> |

## Что уже ясно

- `USAMO` действительно отсутствует в базе как серия.
- Уже сейчас есть хороший shortlist из `10` сильных кандидатов и `3` пограничных.
- Для первого импорта разумнее всего брать задачи из сильного ядра, где:
  - граф прямо в условии;
  - или AoPS/стандартное решение явно использует графовую модель как основной язык.
- Самые удобные стартовые задачи для импорта:
  - `2022 P1`;
  - `2021 P2`;
  - `2025 P3`;
  - `1999 P1`.

## Что делать дальше

- импортировать задачи из сильного ядра по одной серии;
- отдельно проверять `proposer/authors` по каждому году;
- для пограничных задач сначала быстро просмотреть решения, а уже потом решать, входят ли они в базу на равных правах с основным графовым слоем.
## РџРѕРіСЂР°РЅРёС‡РЅС‹Рµ: РїРµСЂРµРїСЂРѕРІРµСЂРµРЅРЅС‹Р№ РІРµСЂРґРёРєС‚

- `2008 P4`: triangulation есть в условии, но в notes Evan Chen решение идёт через разбор маленьких/больших равнобедренных треугольников, паритет и рекурсию `n -> n/2` или `n-1`. Графовая структура тут скорее фон, чем основной инструмент.
- `2009 P3`: пока не включаю в graph-core. Domino/matching-модель естественна, но в доступных открытых решениях я не нашёл достаточного подтверждения, что именно нетривиальная графовая техника несёт основную proof load, а не просто даёт удобный язык.
- `2023 P3`: после перепроверки это уже почти не пограничная задача. В notes Evan Chen явно строится ориентированный граф на special squares, доказывается, что компонентa empty cell ациклична, то есть является деревом, и через этот граф точно выражается `k(C)`. Это содержательное использование графа, а не мотив; хороший кандидат на следующий импорт.

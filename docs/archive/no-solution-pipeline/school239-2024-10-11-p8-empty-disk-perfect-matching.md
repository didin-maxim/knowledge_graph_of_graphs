# school239-2024-10-11-p8-empty-disk-perfect-matching

## Краткий итог

Карточка была без решения. Официальный разбор ФМЛ 239 для задачи 8 параллели 10-11 классов 2024 года в публичном поиске не найден; в уже зафиксированном источнике `src-school239-2024-official-conditions` есть только условия.

Добавлено ИИ-решение: берём триангуляцию Делоне данных точек. Каждое её ребро даёт допустимую пару, потому что имеет пустой круг. По теореме Делленкура триангуляция Делоне множества точек общего положения 1-жёсткая, а значит по теореме Татта при чётном числе вершин содержит совершенное паросочетание.

## Найденные источники

- Официальная карточная формулировка уже ссылается на `src-school239-2024-official-conditions`: https://disk.yandex.ru/i/Vqxe1jiDePZ3eA.
- Официальный сайт/новости 239.ru были проверены поиском по фразам условия и по "Открытая олимпиада ФМЛ 239 2024 решения"; отдельный официальный разбор не найден.
- Использованная внешняя теорема: M. B. Dillencourt, "Toughness and Delaunay Triangulations", Discrete & Computational Geometry 5, 575-601, 1990, DOI `10.1007/BF02187810`.
- Более короткий открытый источник с самодостаточным доказательством: Ahmad Biniaz, "A Short Proof of the Toughness of Delaunay Triangulations", Journal of Computational Geometry 12(1), 35-39, 2021, DOI `10.20382/jocg.v12i1a2`, https://jocg.org/index.php/jocg/article/view/3126.
- Теорема Татта: W. T. Tutte, "The Factorization of Linear Graphs", Journal of the London Mathematical Society s1-22(2), 107-111, 1947, DOI `10.1112/jlms/s1-22.2.107`.

## Внешняя теорема

Использованная теорема Делленкура: для триангуляции Делоне `T` конечного множества точек общего положения на плоскости и любого множества вершин `S` граф `T-S` имеет не больше `|S|` компонент. Поэтому число нечётных компонент также не больше `|S|`, и по теореме Татта в `T` есть совершенное паросочетание, если число вершин чётно.

Оценка школьности: теорема Татта иногда встречается в продвинутых кружках, но не является стандартным школьным инструментом. 1-жёсткость триангуляций Делоне существенно менее школьная: короткое доказательство Biniaz занимает несколько страниц и использует структурные свойства Делоне-триангуляций. Для базы стоит добавить отдельную карточку-теорему; без неё олимпиадная карточка честно решена только как применение внешнего результата.

## Предлагаемые source entries

Не редактировал `data/sources/sources.yaml`, потому что это вне зоны разрешённых правок. Предлагаемые записи:

```json
{
  "id": "src-dillencourt-delaunay-toughness-1990",
  "type": "research_paper",
  "title": "M. B. Dillencourt, Toughness and Delaunay Triangulations",
  "url": "https://doi.org/10.1007/BF02187810",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Discrete & Computational Geometry 5, 575-601, 1990; proves 1-toughness of nondegenerate Delaunay triangulations and derives perfect matchings."
}
```

```json
{
  "id": "src-biniaz-short-delaunay-toughness-2021",
  "type": "research_paper",
  "title": "Ahmad Biniaz, A Short Proof of the Toughness of Delaunay Triangulations",
  "url": "https://jocg.org/index.php/jocg/article/view/3126",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Journal of Computational Geometry 12(1), 35-39, 2021; open short proof of Dillencourt's theorem and notes the perfect matching implication."
}
```

```json
{
  "id": "src-tutte-factorization-linear-graphs-1947",
  "type": "research_paper",
  "title": "W. T. Tutte, The Factorization of Linear Graphs",
  "url": "https://doi.org/10.1112/jlms/s1-22.2.107",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Journal of the London Mathematical Society s1-22(2), 107-111, 1947; original source for Tutte's perfect matching criterion."
}
```

## Предлагаемые relation entries

Не редактировал `data/relations/relations.yaml`. После добавления отдельной карточки `delaunay-triangulation-1-tough-perfect-matching` можно добавить:

```json
{
  "id": "rel-delaunay-perfect-matching-school239-2024-empty-disk",
  "from": "delaunay-triangulation-1-tough-perfect-matching",
  "to": "school239-2024-10-11-p8-empty-disk-perfect-matching",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "1-жёсткость триангуляций Делоне вместе с теоремой Татта даёт совершенное паросочетание в графе допустимых пустых кругов.",
  "backward_text": "Задача ФМЛ 239 является прямым геометрическим применением теоремы о совершенном паросочетании в триангуляции Делоне.",
  "anchors": {
    "to_solution_id": "sol-ai-delaunay-tutte"
  },
  "status": "ai_draft",
  "confidence": 0.96
}
```

Если будет добавлена отдельная карточка `tutte-perfect-matching-theorem`, полезна ещё одна связь:

```json
{
  "id": "rel-tutte-delaunay-perfect-matching",
  "from": "tutte-perfect-matching-theorem",
  "to": "delaunay-triangulation-1-tough-perfect-matching",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Теорема Татта переводит 1-жёсткость чётного графа в существование совершенного паросочетания.",
  "backward_text": "Следствие о паросочетании в триангуляции Делоне использует теорему Татта после оценки числа компонент.",
  "status": "ai_draft",
  "confidence": 0.95
}
```

## Изменения в карточке

- Убрана метка `condition_only`, потому что теперь есть решение.
- Добавлено решение `sol-ai-delaunay-tutte` со статусом `ai_checked`.
- В editorial notes зафиксировано, что это ИИ-решение через внешнюю теорему; `review_status` и `public_ready` оставлены осторожными из-за отсутствия официального решения и пока не добавленных source entries.

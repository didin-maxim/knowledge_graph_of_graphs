# miklos-schweitzer-2010-p2-infinite-vertex-transitive-perfect-matching

## Краткий итог

Карточка была без решения. Официальный PDF с условиями найден и уже был привязан к карточке через `src-miklos-schweitzer-2010-p2-official`; официального разбора именно задачи 2010/2 при поиске не нашёл.

Добавлено ИИ-решение: задача является прямым следствием известной бесконечной версии теоремы Годсила--Ройла: каждый счётный бесконечный связный вершинно-транзитивный граф имеет совершенное паросочетание. В карточку добавлена не только ссылка на теорему, но и сжатая схема доказательства через сильно максимальные паросочетания, критические вершины, перенос возможной пропущенной вершины автоморфизмом и компактность.

## Найденные источники

- Официальная формулировка Schweitzer 2010: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2010-eng.pdf.
- Georgakopoulos--Wendland, "Presentations for vertex-transitive graphs", J. Algebraic Combinatorics 55, 795--826 (2022), Theorem 5.9: https://link.springer.com/article/10.1007/s10801-021-01070-6.
- arXiv v1 той же работы содержит Appendix "Perfect matchings in infinite transitive graphs" by Matthias Hamann and Alex Wendland: https://arxiv.org/abs/2007.06432.
- Leemann, "On subgroups and Schreier graphs of finitely generated groups", Proposition 3.2.17 and surrounding lemmas: https://access.archive-ouverte.unige.ch/access/metadata/508af692-2825-4ccd-9640-6451a2a80c8b/download.
- Aharoni--Berger--Georgakopoulos--Sprüssel, "Strongly Maximal Matchings in Infinite Graphs", Electronic Journal of Combinatorics 15(1), #R136 (2008): https://doi.org/10.37236/860.
- Csóka--Lippner, "Invariant random perfect matchings in Cayley graphs", Groups Geom. Dyn. 11(1), 211--243 (2017), cited by Theorem 5.9: https://doi.org/10.4171/GGD/395.

## Внешняя теорема

Использованная теорема: каждый счётный бесконечный связный вершинно-транзитивный граф имеет совершенное паросочетание. В задаче дополнительно дано `d`-регулярность, так что граф локально конечен, и локально конечная версия теоремы применима напрямую.

Оценка школьности: доказательство не школьное. Ключевой внешний кусок -- существование сильно максимального паросочетания в бесконечном локально конечном графе (теорема Аарони) и последующий компактностный переход от покрытия каждого конечного множества к глобальному совершённому паросочетанию. Это хороший кандидат на отдельную карточку-теорему, но скорее как advanced/theorem card, а не как стандартная школьная лемма.

## Предлагаемые source entries

Не редактировал `data/sources/sources.yaml`, потому что это вне разрешённой зоны. Предлагаемые записи:

```json
{
  "id": "src-georgakopoulos-wendland-2022-presentations-vertex-transitive-graphs",
  "type": "research_paper",
  "title": "Agelos Georgakopoulos and Alex Wendland, Presentations for vertex-transitive graphs",
  "url": "https://doi.org/10.1007/s10801-021-01070-6",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Journal of Algebraic Combinatorics 55, 795--826 (2022); Theorem 5.9 states that every countably infinite connected vertex-transitive graph has a perfect matching."
}
```

```json
{
  "id": "src-georgakopoulos-hamann-wendland-2020-arxiv-vt-presentations",
  "type": "preprint",
  "title": "Agelos Georgakopoulos, Matthias Hamann and Alex Wendland, Presentations for Vertex Transitive Graphs, arXiv v1 appendix",
  "url": "https://arxiv.org/abs/2007.06432",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "arXiv v1 contains Appendix: Perfect matchings in infinite transitive graphs, authored by Matthias Hamann and Alex Wendland."
}
```

```json
{
  "id": "src-aharoni-berger-georgakopoulos-spruessel-2008-strongly-maximal-matchings",
  "type": "research_paper",
  "title": "Ron Aharoni, Eli Berger, Agelos Georgakopoulos and Philipp Sprüssel, Strongly Maximal Matchings in Infinite Graphs",
  "url": "https://doi.org/10.37236/860",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Electronic Journal of Combinatorics 15(1), #R136 (2008); supplies the strongly maximal matching existence result used in Leemann's proof."
}
```

```json
{
  "id": "src-leemann-2016-subgroups-schreier-graphs-thesis",
  "type": "phd_thesis",
  "title": "Paul-Henry Leemann, On subgroups and Schreier graphs of finitely generated groups",
  "url": "https://access.archive-ouverte.unige.ch/access/metadata/508af692-2825-4ccd-9640-6451a2a80c8b/download",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Proposition 3.2.17 proves existence of a 1-factor in infinite locally finite transitive graphs of odd degree; later literature notes the proof applies to the even-degree case as well."
}
```

## Предлагаемые relation entries

Не редактировал `data/relations/relations.yaml`. Если добавить отдельную карточку `infinite-vertex-transitive-perfect-matching-theorem`, можно добавить:

```json
{
  "id": "rel-infinite-vt-perfect-matching-theorem-to-schweitzer-2010-p2",
  "from": "infinite-vertex-transitive-perfect-matching-theorem",
  "to": "miklos-schweitzer-2010-p2-infinite-vertex-transitive-perfect-matching",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Теорема о совершенном паросочетании в счётном бесконечном связном вершинно-транзитивном графе напрямую доказывает задачу Miklós Schweitzer 2010/2.",
  "backward_text": "Задача Miklós Schweitzer 2010/2 является олимпиадной формулировкой этой бесконечной теоремы о паросочетаниях.",
  "anchors": {
    "to_solution_id": "sol-ai-infinite-transitive-matching-theorem"
  },
  "status": "ai_draft",
  "confidence": 0.97
}
```

Если в базе появится отдельная карточка теоремы Аарони о strongly maximal matching, уместна ещё одна связь:

```json
{
  "id": "rel-aharoni-strongly-maximal-matching-to-infinite-vt-perfect-matching",
  "from": "aharoni-strongly-maximal-matching-theorem",
  "to": "infinite-vertex-transitive-perfect-matching-theorem",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Существование сильно максимального паросочетания является ключевым внешним шагом в доказательстве бесконечной версии теоремы Годсила--Ройла.",
  "backward_text": "Доказательство теоремы о совершенном паросочетании в бесконечном вершинно-транзитивном графе использует strongly maximal matching и компактность.",
  "status": "ai_draft",
  "confidence": 0.9
}
```

## Изменения в карточке

- Добавлено решение `sol-ai-infinite-transitive-matching-theorem` со статусом `ai_checked`.
- В `editorial.notes` зафиксировано, что решение является ИИ-решением через внешнюю бесконечную теорему.
- Отдельно отмечено, что внешний инструмент не является школьным и его стоит вынести в отдельную карточку-теорему.

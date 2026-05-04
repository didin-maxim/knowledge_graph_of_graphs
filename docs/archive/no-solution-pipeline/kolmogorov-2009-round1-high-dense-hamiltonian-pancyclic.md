# kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic

## Краткий итог

Карточка была без решения. Публичный/официальный разбор именно этой задачи Кубка Колмогорова 2009 по точной формулировке не найден.

Добавлено ИИ-решение: задача является прямым следствием теоремы Бонди о панцикличности гамильтоновых графов с числом рёбер не меньше \(n^2/4\). При \(n=100\) имеем \(n^2/4=2500\), а в задаче рёбер строго больше 2500, поэтому исключение \(K_{50,50}\) невозможно.

## Найденные источники

- Официальная карточная формулировка уже ссылается на `src-kolmogorov-2009-official`: архив `https://turmath.ru/kolm/files/archive/kolm13.zip`.
- Точная внешняя теорема: J. A. Bondy, "Pancyclic graphs I", Journal of Combinatorial Theory, Series B 11(1), 80-84, 1971, DOI `10.1016/0095-8956(71)90016-5`, страница ScienceDirect: https://www.sciencedirect.com/science/article/pii/0095895671900165.
- Дополнительная проверка формулировки: D. W. Cranston et al., "Weakly Pancyclic Graphs", Theorem 2.10: https://people.computing.clemson.edu/~goddard/papers/weakpanFinal.pdf.
- Формализованное доказательство теоремы Бонди в AFP: https://www.isa-afp.org/entries/Bondy.html.

## Внешняя теорема

Использованная теорема Бонди: каждый гамильтонов граф порядка \(n\) и размера \(e(G)\ge n^2/4\) панцикличен, либо \(n=2r\) и \(G=K_{r,r}\).

Оценка школьности: как чёрный ящик теорема слишком сильная для обычной школьной карточки; доказательство короткое по меркам экстремальной теории графов, но не является стандартным школьным приёмом уровня Дирака/Мантеля. Стоит добавить отдельную карточку-теорему в `data/problems/classical/`, потому что текущая олимпиадная задача тогда станет честным однострочным применением.

## Предлагаемые source entries

Не редактировал `data/sources/sources.yaml`, потому что это вне зоны разрешённых правок. Предлагаемая запись:

```json
{
  "id": "src-bondy-pancyclic-graphs-i-1971",
  "type": "research_paper",
  "title": "J. A. Bondy, Pancyclic graphs I",
  "url": "https://doi.org/10.1016/0095-8956(71)90016-5",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Journal of Combinatorial Theory, Series B 11(1), 80-84, 1971; contains the theorem that a Hamiltonian graph with e(G) >= n^2/4 is pancyclic or K_{n/2,n/2}."
}
```

Опционально, если в базе принято хранить формальные доказательства:

```json
{
  "id": "src-avigad-hetzl-bondy-afp-2012",
  "type": "formal_proof",
  "title": "Jeremy Avigad and Stefan Hetzl, Bondy's Theorem",
  "url": "https://www.isa-afp.org/entries/Bondy.html",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Archive of Formal Proofs formalization following Bollobas, Combinatorics, 1986."
}
```

## Предлагаемые relation entries

Не редактировал `data/relations/relations.yaml`. После добавления отдельной карточки `bondy-pancyclic-theorem` можно добавить:

```json
{
  "id": "rel-bondy-pancyclic-kolmogorov-2009-dense-hamiltonian",
  "from": "bondy-pancyclic-theorem",
  "to": "kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Теорема Бонди сразу даёт панцикличность гамильтонова графа при e(G)>n^2/4; исключение K_{n/2,n/2} имеет ровно n^2/4 рёбер.",
  "backward_text": "Задача Кубка Колмогорова 2009 является числовым применением теоремы Бонди при n=100.",
  "anchors": {
    "to_solution_id": "sol-ai-bondy-pancyclic-theorem"
  },
  "status": "ai_draft",
  "confidence": 0.97
}
```

## Изменения в карточке

- Добавлено решение `sol-ai-bondy-pancyclic-theorem` со статусом `ai_checked`.
- В editorial notes зафиксировано, что это ИИ-решение через внешнюю теорему, а доказательство теоремы Бонди лучше вынести в отдельную карточку.

# kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths

## Что проверено

- Карточка: `data/problems/kolmogorov/kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths.yaml`.
- Официальный источник из реестра уже есть: `src-kolmogorov-2009-official`, `https://turmath.ru/kolm/files/archive/kolm13.zip`.
- Поиск по точной русской формулировке, числам `2009`, `1004`, `2500`, имени `tur4_13.txt` и фразам про Кубок Колмогорова не дал опубликованного разбора этой конкретной задачи.
- Найден не официальный разбор задачи, а внешний сильный результат, который напрямую закрывает задачу: Arthur H. Busch, "A Note on the Number of Hamiltonian Paths in Strong Tournaments", Electronic Journal of Combinatorics 13(1), #N3, 2006, DOI `10.37236/1141`, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1n3.
- Также подтверждён альтернативный короткий путь через Brian Alspach, "Cycles of Each Length in Regular Tournaments": https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/cycles-of-each-length-in-regular-tournaments/743EC70B8964AAC5777C2E3142944FEF.

## Решение и статус

Добавлено теоремное ИИ-решение `sol-ai-busch-strong-tournament-bound` со статусом `needs_human_review`.

Локальная часть доказательства элементарна: регулярный турнир на `2009` вершинах сильно связен, потому что иначе первая компонента сильной связности должна иметь размер хотя бы `1005` по входящим степеням, а последняя компонента тоже размер хотя бы `1005` по исходящим степеням.

Дальше применена теорема Busch: любой сильный турнир порядка `n` имеет не менее `5^((n-1)/3)` гамильтоновых путей; для `n = 2009`, точнее `n ≡ 2 (mod 3)`, нижняя оценка из статьи даёт `9*5^668`, что намного больше `2500`.

Теорема не выглядит школьной в формате "можно просто сослаться на кружке": доказательство короткое, комбинаторное и занимает 4 страницы, но использует структурную лемму о сильных турнирах и индуктивный подсчёт. Лучше добавить отдельную карточку-теорему, если база допускает такие внешние инструменты.

## Предложенный source entry

Не редактировал `data/sources/sources.yaml`. Предлагаю добавить:

```json
{
  "id": "src-busch-2006-hamiltonian-paths-strong-tournaments",
  "type": "paper",
  "title": "Arthur H. Busch, A Note on the Number of Hamiltonian Paths in Strong Tournaments",
  "url": "https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1n3",
  "doi": "10.37236/1141",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Electronic Journal of Combinatorics paper proving the exact minimum number of Hamiltonian paths in strong tournaments; used as an external theorem for the Kolmogorov 2009 regular tournament problem."
}
```

Возможный дополнительный источник для альтернативного решения через циклы:

```json
{
  "id": "src-alspach-1967-cycles-each-length-regular-tournaments",
  "type": "paper",
  "title": "Brian Alspach, Cycles of Each Length in Regular Tournaments",
  "url": "https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/cycles-of-each-length-in-regular-tournaments/743EC70B8964AAC5777C2E3142944FEF",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Classical arc-pancyclicity theorem for regular tournaments; would imply many Hamiltonian cycles, hence many Hamiltonian paths."
}
```

## Предложенные relation entries

Не редактировал общий `relations.yaml`. Если будет создана отдельная карточка `strong-tournament-hamiltonian-path-count-busch`, предлагаю:

```json
{
  "from": "kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths",
  "to": "strong-tournament-hamiltonian-path-count-busch",
  "type": "prerequisite",
  "confidence": 0.95,
  "status": "needs_human_review",
  "note": "ИИ-решение использует нижнюю оценку Busch для числа гамильтоновых путей в сильном турнире."
}
```

Если будет создана карточка `regular-tournament-arc-pancyclic-alspach`, возможна альтернативная связь:

```json
{
  "from": "kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths",
  "to": "regular-tournament-arc-pancyclic-alspach",
  "type": "prerequisite",
  "confidence": 0.8,
  "status": "needs_human_review",
  "note": "Альтернативное решение: каждое ребро регулярного турнира лежит на гамильтоновом цикле; по подсчёту рёбер получается много циклов и путей."
}
```

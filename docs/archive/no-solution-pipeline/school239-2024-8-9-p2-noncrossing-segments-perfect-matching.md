# school239-2024-8-9-p2-noncrossing-segments-perfect-matching

## Краткий итог

Карточка была без решения. Официальный разбор задачи Открытой олимпиады ФМЛ 239 2024 для 8-9 классов по веб-поиску не найден; в локальном извлечённом тексте `audit/school239/239_24_all.txt` есть только условия.

Добавлено ИИ-решение: ответ отрицательный. Контрпример строится как прямолинейная триангуляция на 16 точках аполлонова типа: сначала строятся 7 "старых" вершин, затем в 9 треугольных областей добавляются 9 новых вершин, каждая соединяется только с тремя вершинами своей области. Эти 9 новых вершин образуют независимое множество и могут матчиться только в 7 старых вершин, поэтому совершенного паросочетания нет.

## Найденные источники

- Официальная карточная формулировка уже ссылается на `src-school239-2024-official-conditions`: https://disk.yandex.ru/i/Vqxe1jiDePZ3eA.
- Точный официальный разбор или автор задачи по запросам с фрагментами условия не найден.
- Найден родственный внешний источник: статья Wikipedia "Apollonian network", раздел "Matching-free graphs", где описана конструкция Plummer (1992) максимальных планарных графов чётного порядка без совершенного паросочетания: https://en.wikipedia.org/wiki/Apollonian_network#Matching-free_graphs.
- В той же статье указан первоисточник: Michael D. Plummer, "Extending matchings in planar graphs IV", Discrete Mathematics 109 (1992), 207-219, DOI `10.1016/0012-365X(92)90292-N`.

## Внешняя теорема

В решении карточки внешняя теорема не используется как чёрный ящик: контрпример и невозможность паросочетания доказаны прямо подсчётом независимых новых вершин.

Внешняя конструкция Plummer/аполлоновых сетей полезна как контекст. Доказательство школьное в локальной форме: достаточно знать, что триангуляция максимальна по непересекающимся отрезкам, и применить принцип Дирихле к 9 новым и 7 старым вершинам. Отдельную карточку-теорему добавлять не обязательно; если добавлять, лучше как стандартную идею/пример "максимальная планарная триангуляция чётного порядка без perfect matching", а не как тяжёлую теорему.

## Неоднозначность формулировки

В PDF/OCR условие говорит "любой отрезок с концами в двух данных точках". Буквально это включает уже проведённые отрезки, но проведённый отрезок не может пересекать другой проведённый отрезок во внутренней точке, потому что все проведённые отрезки попарно не пересекаются по внутренним точкам. Поэтому содержательное чтение задачи зафиксировано как стандартная максимальность: любой непроведённый отрезок между двумя данными точками пересекает какой-то проведённый.

В карточке графовая формулировка уточнена именно для этого чтения, а оригинальная формулировка из источника оставлена без изменения.

## Предлагаемые source entries

Не редактировал `data/sources/sources.yaml`, потому что это вне зоны разрешённых правок. Если нужно зафиксировать родственный источник, предлагаю:

```json
{
  "id": "src-plummer-extending-matchings-planar-graphs-iv-1992",
  "type": "research_paper",
  "title": "Michael D. Plummer, Extending matchings in planar graphs IV",
  "url": "https://doi.org/10.1016/0012-365X(92)90292-N",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Discrete Mathematics 109 (1992), 207-219; cited for the construction of even maximal planar graphs without perfect matchings."
}
```

Дополнительный обзорный источник, если в базе допустимы Wikipedia references:

```json
{
  "id": "src-wikipedia-apollonian-network-matching-free",
  "type": "encyclopedia_article",
  "title": "Wikipedia, Apollonian network",
  "url": "https://en.wikipedia.org/wiki/Apollonian_network#Matching-free_graphs",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Overview page summarizing Plummer's matching-free Apollonian/maximal planar graph construction."
}
```

## Предлагаемые relation entries

Не редактировал `data/relations/relations.yaml`. Если позже появится отдельная карточка `matching-free-apollonian-triangulation`, можно добавить:

```json
{
  "id": "rel-matching-free-apollonian-school239-2024-noncrossing-segments",
  "from": "matching-free-apollonian-triangulation",
  "to": "school239-2024-8-9-p2-noncrossing-segments-perfect-matching",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Аполлонова триангуляция чётного порядка с большой независимой долей даёт контрпример к существованию совершенного паросочетания среди максимальной системы непересекающихся отрезков.",
  "backward_text": "Задача ФМЛ 239 2024 сводится к вопросу о perfect matching в максимальной прямолинейной триангуляции и решается контрпримером аполлонова типа.",
  "anchors": {
    "to_solution_id": "sol-ai-apollonian-counterexample"
  },
  "status": "ai_draft",
  "confidence": 0.9
}
```

## Изменения в карточке

- Добавлено решение `sol-ai-apollonian-counterexample` со статусом `ai_checked`.
- В графовой переформулировке уточнено содержательное чтение условия: речь о непроведённых отрезках.
- В editorial notes зафиксированы отсутствие найденного официального разбора, ИИ-решение и формальная неоднозначность исходной фразы.

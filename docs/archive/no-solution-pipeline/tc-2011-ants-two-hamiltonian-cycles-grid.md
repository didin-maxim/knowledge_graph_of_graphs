# tc-2011-ants-two-hamiltonian-cycles-grid

## Что проверено

- Прочитаны `README.md`, `docs/ARCHITECTURE.md`, `docs/AI_CARD_RULES.md` и карточка задачи ровно для формата: JSON-совместимый YAML, полноценные доказательства в `solutions[]`, редакторские пометки в `editorial.notes`.
- В интернете найден официальный разбор в сборнике 32-го Турнира городов: `https://matematickitalent.mk/uploads/books/ahDDRerVFk6iguuNOVlxDA.pdf`, стр. 20, строки 809-817 в извлечении web: ответ 16, пример дан рисунком, нижняя оценка через подсчёт `64+64-112`.
- В реестре уже есть подходящий источник `src-tc-2011-32-vs32sl-official` с URL `https://www.turgor.ru/problems/32/vs32sl-avt.pdf`, поэтому `data/sources/sources.yaml` не редактировался.

## Решение

Карточка была решена. Добавлено ИИ-решение: официальная нижняя оценка сохранена, а официальный рисунок заменён самодостаточной координатной конструкцией двух гамильтоновых циклов в решётке 8 на 8.

Проверка конструкции:

- каждый список содержит 64 разные вершины;
- соседние вершины, включая замыкание последней с первой, смежны по стороне клетки;
- общие рёбра двух циклов ровно 16, все они являются чередующимися граничными сторонами.

Внешние теоремы не использовались. Доказательство опирается только на подсчёт рёбер и явную конструкцию; отдельная карточка для теоремы не нужна.

## Источники и связи

Новые source entries не нужны: существующий `src-tc-2011-32-vs32sl-official` покрывает и условие, и официальный разбор.

Предлагаемые relation entries, если редактор захочет связать карточку с близкими мотивами:

```yaml
- from: tc-2011-ants-two-hamiltonian-cycles-grid
  to: cmo-2015-p3-grid-hamiltonian-turtle
  type: same_motif
  confidence: 0.55
  note: "Обе задачи используют гамильтоновы обходы решётки и явные змейковые/координатные конструкции."
- from: tc-2011-ants-two-hamiltonian-cycles-grid
  to: baltic-way-1997-p19-edge-disjoint-hamiltonian-cycles
  type: same_motif
  confidence: 0.50
  note: "Общий мотив: точная оценка для гамильтоновых циклов через подсчёт рёбер плюс конструкция; графы разные."
```

## Правки

- `data/problems/tournament-cities/tc-2011-ants-two-hamiltonian-cycles-grid.yaml`: добавлено решение, обновлены `problem_profile`, `difficulty.status`, роль источника и редакторские статусы/заметки.
- `docs/archive/no-solution-pipeline/tc-2011-ants-two-hamiltonian-cycles-grid.md`: добавлен этот отчёт.

# Miklos Schweitzer 2009 P1: K17 edge-coloring cards

## Итог

Карточка решена. Найден официальный венгерский отчёт Bolyai János Mathematical Society с автором задачи и разбором: автор задачи Andras Gyarfas, ответ \(34\). В карточку добавлено русское самодостаточное ИИ-решение, развёрнутое по этому разбору.

Использованные источники:

- Existing card/source registry: `src-miklos-schweitzer-2009-p1-official`, English archive PDF, https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2009-eng.pdf. По открытию PDF содержит только условия задач.
- New found source, not added to `data/sources/sources.yaml` by task constraint: official Hungarian report, https://www.bolyai.hu/files/Schweitzer_2009_jelentes.pdf. In the PDF, Problem 1 starts at lines 39-43, solution and answer \(34\) at lines 43-69, construction at lines 53-62, lower bound at lines 63-98.

## Математика

Решение состоит из двух частей.

- Верхняя оценка: рёбра \(K_{17}\) разбиваются на 34 четырёхцикла. Два базовых цикла \((1,2,10,8,1)\) и \((3,6,12,8,3)\) имеют рёбра всех восьми возможных циклических расстояний; их 17 поворотов покрывают все рёбра. Для каждого четырёхцикла строится карточка, которая делает радужными ровно четыре \(K_{15}\), полученные удалением концов рёбер этого цикла.
- Нижняя оценка: на одной карточке не больше четырёх радужных 15-вершинных множеств. Ключевой подсчёт: если одно такое множество есть, то есть хотя бы \(105-31=74>\binom{12}{2}\) уникальных рёбер, их концы образуют множество \(V\) размера 13, 14 или 15, причём любое радужное множество обязано содержать \(V\). Случаи \(|V|=15,14\) дают не больше 1 или 3 множеств; при \(|V|=13\) пять дополняющих пар дали бы треугольник вне \(V\) и уже \(\binom{13}{2}+3\cdot13=117>105\) различных цветов.

Внешняя теорема не использована. Факт о разбиении \(K_{17}\) на 34 четырёхцикла доказан прямо в решении через циклические расстояния, это школьно-олимпиадный аргумент. Отдельную карточку стоит заводить только если базе нужен общий факт о \(C_4\)-разложениях \(K_n\) при \(n\equiv1\pmod 8\); для текущей задачи отдельная карточка не обязательна.

## Source Entry

Точный source entry, который стоит добавить отдельно в `data/sources/sources.yaml`:

```json
{
  "id": "src-miklos-schweitzer-2009-report-bolyai",
  "type": "problem_and_solution",
  "title": "Jelentes a 2009. evi Schweitzer Miklos Matematikai Emlekversenyrol, Bolyai Janos Matematikai Tarsulat",
  "url": "https://www.bolyai.hu/files/Schweitzer_2009_jelentes.pdf",
  "browser_openable": true,
  "language": "hu",
  "official": true,
  "status": "source_verified"
}
```

После добавления source entry можно привязать решение `sol-ai-expanded-official-report` к этому источнику, если локальный стиль решений допускает `source_ids`.

## Relations

Новых relation entries не предлагаю: уверенной уже существующей карточки про нужное \(C_4\)-разложение не нашёл, а редактировать общий `relations.yaml` в этой задаче нельзя.

## Проверка

Запущено:

```powershell
python tools\validate.py
```

Промежуточный результат после правки целевой карточки был успешным: `OK: 565 problems, 673 relations, 9 comments, 591 sources, 29 definitions, 17 standard ideas, 32 import batches.`

Повторный запуск в конце упал до проверки схемы на другом, неразрешённом для этой карточки файле:

```text
json.decoder.JSONDecodeError: Invalid \escape: line 86 column 1521 (char 4626)
data\problems\miklos-schweitzer\miklos-schweitzer-2009-p2-smooth-difference-graphs.yaml
```

Целевой файл `data/problems/miklos-schweitzer/miklos-schweitzer-2009-p1-k17-edge-coloring-cards.yaml` отдельно проверен через `json.loads`: `target card JSON OK`.

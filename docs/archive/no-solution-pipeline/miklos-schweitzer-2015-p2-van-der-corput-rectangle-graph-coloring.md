# miklos-schweitzer-2015-p2-van-der-corput-rectangle-graph-coloring

## Краткий итог

Карточка была без решения. Найден официальный венгерский PDF с решениями конкурса: задача 2 указана как задача Gábor Tardos, а официальный разбор даёт 7-раскраску вершины \((n,x_n)\) по остатку \(n \bmod 7\).

В карточку добавлено решение `sol-ai-official-mod-7-coloring`: это русская ИИ-адаптация официального решения, не самостоятельная новая теорема. Основной ход: кодировать вершины двоичными последовательностями, сравнивать пары по первому и последнему отличающимся битам, затем показать, что разность первых координат любого возможного ребра не делится на \(7\).

## Найденные источники

- Официальный PDF с решениями 2015 года: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-meg.pdf. В нём задача 2 начинается на стр. 2, решение занимает стр. 2-3, постановщик указан как Gábor Tardos.
- Официальный английский PDF с условиями: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-eng.pdf. Он уже был указан в карточке/реестре источников.
- KöMaL A.657: https://www.komal.hu/feladat?a=feladat&f=A657&l=en. Это публикация условия и статистики отправленных решений, не разбор.
- Свежая статья "Coloring Questions on Axis-Parallel Rectangles and Arithmetic Progressions" упоминает эту задачу как Problem 4.1 и связывает её с темой прямоугольников и последовательности Ван дер Корпута, но не использовалась как источник решения: https://www.researchgate.net/publication/401058361_Coloring_Questions_on_Axis-Parallel_Rectangles_and_Arithmetic_Progressions.

## Внешние теоремы

Внешние теоремы не использованы. Доказательство школьное по технике: нужны только двоичная запись, сравнение двоичных последовательностей, простая геометрическая интерпретация "третья точка между двумя" и остатки по модулю \(7\). Отдельную карточку-теорему добавлять не требуется.

## Предлагаемые source entries

Общий `data/sources/sources.yaml` не редактировался. В реестре уже есть `src-miklos-schweitzer-2015-p2-official`, но на момент проверки его URL указывает на английский PDF с условиями, тогда как найденный официальный разбор лежит в `schweitzer-2015-meg.pdf`. Если нужно нормализовать это в реестре, предлагаю либо обновить существующую запись, либо добавить отдельный источник:

```json
{
  "id": "src-miklos-schweitzer-2015-official-solutions",
  "type": "problem_and_solution",
  "title": "A 2015. évi Schweitzer Miklós Matematikai Emlékverseny feladatai és megoldásai",
  "url": "https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-meg.pdf",
  "browser_openable": true,
  "language": "hu",
  "official": true,
  "status": "source_verified",
  "preference_note": "Official Hungarian problem-and-solution PDF; Problem 2 solution gives the mod 7 coloring."
}
```

## Предлагаемые relation entries

Новых связей не предлагаю: решение самодостаточное и не ссылается на отдельную внешнюю теорему или уже существующую карточку базы.

## Изменения в карточке

- Добавлен автор/постановщик `Gábor Tardos` по официальному PDF.
- Идея `idea-dyadic-levels` переписана из гипотетической заметки в проверенный план решения.
- Добавлено решение `sol-ai-official-mod-7-coloring` со статусом `ai_checked`.
- Источник в карточке переведён на роль `problem_and_solutions_official` и снабжён ссылкой на официальный PDF с решениями.
- В `editorial.notes` зафиксировано, что решение является русской ИИ-адаптацией официального разбора.

## Валидация

`python tools\validate.py` завершился успешно:

```text
OK: 565 problems, 673 relations, 9 comments, 591 sources, 29 definitions, 17 standard ideas, 32 import batches.
```

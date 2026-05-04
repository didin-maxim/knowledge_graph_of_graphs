# Miklos Schweitzer 2024 P1: bipartite perfect matching edge weights

## Итог

Карточка была без решения. Найден официальный венгерский PDF Bolyai János Mathematical Society с предварительными решениями 2024 года: `Schweitzer_2024_elozetes_megoldasok.pdf`. В нём задача 1 начинается на странице 1, автор указан как Kristóf Bérczi, а решение дано сразу после условия.

В карточку добавлено самодостаточное русское ИИ-решение `sol-ai-official-induction-alternating-cycle`, адаптированное по официальному разбору. Автор в карточке заменён с `?` на `Kristóf Bérczi` со статусом `source_verified`.

Использованные источники:

- Existing card/source registry: `src-miklos-schweitzer-2024-p1-official`, English official statement PDF, https://www.bolyai.hu/files/Schweitzer_2024_Feladatsor_angol.pdf.
- New found source, not added to `data/sources/sources.yaml` by task constraint: official Hungarian preliminary solutions PDF, https://www.bolyai.hu/files/Schweitzer_2024_elozetes_megoldasok.pdf. In the browser extraction, Problem 1 statement and author are at lines 2-8, the unique-perfect-matching lemma at lines 9-16, the induction proof at lines 17-38, and the matroid-conjecture remark at lines 39-41.

## Математика

Решение состоит из двух стандартных, но аккуратных шагов.

- Если совершенное паросочетание единственно, используется лемма: его рёбра можно занумеровать \((s_i,t_i)\) так, что при \(i>j\) ребра \(s_i t_j\) нет. Тогда вес \(s_i t_i\) равен \(i\), а каждое дополнительное ребро \(s_i t_j\) при \(i<j\) получает вес между \(i\) и \(j\). Это сразу делает matching минимальным со стороны \(S\) и максимальным со стороны \(T\).
- Если есть два совершенных паросочетания, их симметрическая разность содержит чередующийся цикл \(C\). Удаляем вершины \(C\), применяем индукцию к \(G'\), затем одно из двух паросочетаний цикла кладём в очень малые веса, другое в очень большие. Рёбра между \(S'\) и \(T\cap C\) делаются высокими, а между \(S\cap C\) и \(T'\) низкими, чтобы старые минимумы/максимумы в \(G'\) не изменились.

Внешние теоремы не использованы. Лемма о единственном совершенном паросочетании доказана внутри решения через элементарную индукцию и чередующийся цикл; доказательство школьно-олимпиадное. Отдельную карточку для леммы можно завести как полезный reusable-факт про уникальное совершенное паросочетание, но для корректности текущей карточки это не обязательно.

Официальный разбор также замечает, что задача является частным случаем открытой матроидной гипотезы о взвешивании двух матроидов с общей базой. Это не использовалось в решении; отдельную карточку в базу задач графов добавлять не предлагаю без явной матроидной секции.

## Source Entry

Точный source entry, который стоит добавить отдельно в `data/sources/sources.yaml`:

```json
{
  "id": "src-miklos-schweitzer-2024-preliminary-solutions",
  "type": "problem_and_solution",
  "title": "2024. evi Schweitzer Miklos Matematikai Emlekverseny: A feladatok megoldasa",
  "url": "https://www.bolyai.hu/files/Schweitzer_2024_elozetes_megoldasok.pdf",
  "browser_openable": true,
  "language": "hu",
  "official": true,
  "status": "source_verified"
}
```

После добавления source entry можно привязать решение `sol-ai-official-induction-alternating-cycle` к этому источнику, если локальный стиль решений допускает `source_ids`.

## Relations

Общий `relations.yaml` не редактировался. Новых relation entries не предлагаю: решение самодостаточно и не ссылается на уже существующую внешнюю теорему. Если позже будет создана отдельная карточка для леммы об уникальном совершенном паросочетании, можно добавить связь:

```json
{
  "id": "rel-schweitzer-2024-p1-unique-perfect-matching-ordering",
  "from": "miklos-schweitzer-2024-p1-bipartite-perfect-matching-edge-weights",
  "to": "unique-perfect-matching-ordering-lemma",
  "type": "prerequisite",
  "status": "needs_human_review",
  "confidence": 0.82
}
```

## Проверка

Запущено:

```powershell
python tools\validate.py
```

Результат: целевая карточка прочиталась корректно, но общая валидация базы упала на уже существующих несвязанных файлах:

```text
Validation failed:
- data\problems\miklos-schweitzer\miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection.yaml: unknown idea tag circle_packing
- data\problems\miklos-schweitzer\miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection.yaml: solution sol-ai-koebe-radius-shift missing standard_idea_ids list
- data\problems\miklos-schweitzer\miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection.yaml: unknown relations status needs_human_review
- data\problems\school239\school239-2021-10-11-p8-friendship-parity-postcards.yaml: unknown idea tag linear_algebra_over_f2
- data\problems\school239\school239-2021-10-11-p8-friendship-parity-postcards.yaml: unknown idea tag parity_argument
```

Падение не связано с отсутствующим `source_id` для найденного PDF с решениями: новый источник в карточку не добавлялся, а точный source entry предложен выше.

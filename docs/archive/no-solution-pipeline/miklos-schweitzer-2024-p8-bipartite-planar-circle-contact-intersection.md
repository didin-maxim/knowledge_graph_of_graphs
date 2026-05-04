# Miklos Schweitzer 2024/8: окружности для двудольного планарного графа

Карточка: `data/problems/miklos-schweitzer/miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection.yaml`

## Что проверено

- Формат карточки сверялся по `README.md`, `docs/ARCHITECTURE.md`, `docs/AI_CARD_RULES.md` и соседним карточкам с заполненным `solutions[]`.
- Официальное условие уже было привязано к `src-miklos-schweitzer-2024-p8-official`: [Problems posed in the 2024 Miklos Schweitzer Memorial Competition](https://www.bolyai.hu/files/Schweitzer_2024_Feladatsor_angol.pdf).
- Найден официальный предварительный PDF с решениями на венгерском: [Schweitzer_2024_elozetes_megoldasok.pdf](https://www.bolyai.hu/files/Schweitzer_2024_elozetes_megoldasok.pdf).
- В PDF с решениями задача 8 указана с автором Damásdi Gábor; решение занимает строки с применением теоремы Кёбе-Андреева-Тёрстона и последующим изменением радиусов по двум долям.

## Что внесено в карточку

- Автор заменен с `?` на `Damásdi Gábor` со статусом `source_verified`.
- Добавлена идея `idea-koebe-radius-shift`: сначала круговая упаковка исходного планарного графа, затем радиусы `R-r_v` на одной доле и `R+r_v` на другой.
- Добавлено полное русское решение `sol-ai-koebe-radius-shift` с пометкой "ИИ-решение" в названии и editorial notes. Текст является самостоятельным пересказом официального решения, а не ссылкой на внешний PDF.
- `difficulty.comment` обновлен: решение короткое, но опирается на нетривиальную внешнюю теорему.

## Внешняя теорема

Используется теорема Кёбе-Андреева-Тёрстона о круговых упаковках: всякий конечный планарный граф можно реализовать как контактный граф попарно непересекающихся кругов.

Ее доказательство не школьное в обычном олимпиадном смысле. Для уровня Schweitzer ссылка естественна, но для базы лучше не считать эту теорему "встроенной очевидностью": стоит завести отдельную карточку теоремы, если в базе появится слой продвинутых внешних инструментов. Для школьной карточки полное доказательство теоремы было бы слишком тяжелым.

## Источники

В `data/sources/sources.yaml` нет отдельного `source_id` для найденного PDF с решениями, поэтому общий реестр не редактировался. Предлагаемый source entry:

```json
{
  "id": "src-miklos-schweitzer-2024-preliminary-solutions",
  "type": "problem_and_solution",
  "title": "Miklos Schweitzer Memorial Competition 2024 preliminary official solutions",
  "url": "https://www.bolyai.hu/files/Schweitzer_2024_elozetes_megoldasok.pdf",
  "browser_openable": true,
  "language": "hu",
  "official": true,
  "status": "source_verified",
  "preference_note": "Hungarian preliminary official solutions; contains Problem 8 solution and names Damásdi Gábor as author."
}
```

После добавления этого источника в карточку можно добавить второй элемент в `sources[]`:

```json
{
  "source_id": "src-miklos-schweitzer-2024-preliminary-solutions",
  "role": "problem_and_solutions_official",
  "status": "source_verified"
}
```

## Предложенные связи

Не редактировал общий `relations.yaml`. Если будет создана отдельная карточка теоремы, предлагаю связь:

```json
{
  "id": "rel-schweitzer-2024-p8-koebe-andreev-thurston",
  "from": "miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection",
  "to": "koebe-andreev-thurston-circle-packing-theorem",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Решение Schweitzer 2024/8 начинается с круговой упаковки произвольного конечного планарного графа, а затем меняет радиусы по двум долям.",
  "backward_text": "Теорема Кёбе-Андреева-Тёрстона дает исходную контактную модель, из которой в задаче получается нужное пересекающееся семейство окружностей.",
  "status": "needs_human_review",
  "confidence": 0.93
}
```

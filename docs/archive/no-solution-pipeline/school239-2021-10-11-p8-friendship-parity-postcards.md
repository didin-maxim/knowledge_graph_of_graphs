# school239-2021-10-11-p8-friendship-parity-postcards

## Что проверено

- Прочитаны `README.md`, `docs/ARCHITECTURE.md` и карточка задачи; формат карточки — JSON-совместимый YAML.
- В локальном источнике `src-school239-2021-official-conditions` есть только официальный файл условий: Google Drive PDF, локальная копия `audit/school239/239_2021_conditions.pdf`, извлечённый текст `audit/school239/239_2021_conditions.txt`.
- Поиск в интернете по точным фразам из условия, по названию олимпиады и по Google Drive id официального файла не дал публичного авторского или официального разбора.

## Итог по решению

Решение добавлено в карточку как `sol-ai-f2-cauchy-binet`; в заголовке стоит пометка `ИИ-решение`.

Ключевая идея: открытки надо считать как паросочетания в двудольном графе между копией отправителей и копией получателей, а не как простую ориентацию части рёбер, потому что встречные открытки между двумя друзьями разрешены. Для фиксированного множества отправителей `R` паритет числа инъективных выборов получателей равен `det((A^2)[R,R])` над `F_2`, где `A` — матрица смежности графа друзей. Условие задачи даёт, что `A^2` диагональна: вне диагонали стоят чётности чисел общих соседей, а на диагонали — чётности степеней. Поэтому ненулевой вклад даёт только `R = O`, множество всех вершин нечётной степени, и общий паритет равен `1`.

## Внешняя теорема

Использована формула Коши-Бине в варианте над `F_2`. Её доказательство короткое через раскрытие детерминанта, но для обычной школьной аудитории это скорее продвинутая линейная алгебра, чем стандартная олимпиадная техника. Стоит добавить отдельную карточку-лемму про паритет паросочетаний и миноры `AA^T`: она будет полезна не только здесь.

## Источники

В карточке уже есть подходящий источник условия:

```yaml
source_id: src-school239-2021-official-conditions
role: official_problem_statement
status: source_verified
```

Новый `source entry` не предлагается: публичный источник решения не найден, а использованное решение является локальным ИИ-решением.

Официальный URL из существующего source entry: `https://drive.google.com/file/d/1nSLF56jHpVisEKYsQGCHUZ5WEdeCvF_N/view?usp=sharing`.

## Предлагаемые связи

`relations.yaml` не редактировался. Возможные связи после появления отдельной карточки-леммы:

```yaml
- from: school239-2021-10-11-p8-friendship-parity-postcards
  to: cauchy-binet-f2-matching-parity
  type: prerequisite
  confidence: 0.85
```

Если отдельную лемму не заводить, можно связать с уже существующими карточками по двудольным паросочетаниям слабее:

```yaml
- from: school239-2021-10-11-p8-friendship-parity-postcards
  to: miklos-schweitzer-1951-p13-determinant-nonzero-pattern-matchings
  type: related_method
  confidence: 0.55
```

## Валидация

`python tools\validate.py` запущен. После исправления локальных тегов в этой карточке валидация падает только на чужой карточке:

```text
data\problems\miklos-schweitzer\miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection.yaml: unknown idea tag circle_packing
data\problems\miklos-schweitzer\miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection.yaml: solution sol-ai-koebe-radius-shift missing standard_idea_ids list
data\problems\miklos-schweitzer\miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection.yaml: unknown relations status needs_human_review
```

Отсутствующих `source_id`, связанных с этой карточкой, валидатор не показал.

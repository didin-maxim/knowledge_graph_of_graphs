# Miklos Schweitzer 2017-2024 graph curation report

Дата: 2026-05-02

## Источники

- Индекс: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/index.html
- 2017 English problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2017-eng.pdf
- 2017 Hungarian solutions: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2017-meg.pdf
- 2018 English problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2018-eng.pdf
- 2019 English problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2019-eng.pdf
- 2020 English problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2020-eng.pdf
- 2020 Hungarian solutions: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2020-meg.pdf
- 2021 Hungarian problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2021.pdf
- 2021 Hungarian solutions: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2021-meg.pdf
- 2022 English problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2022-eng.pdf
- 2022 Hungarian solutions: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2022-meg.pdf
- 2023 Hungarian problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2023.pdf
- 2023 Hungarian solutions: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2023-meg.pdf
- 2024 English problems: https://www.bolyai.hu/files/Schweitzer_2024_Feladatsor_angol.pdf
- 2024 Hungarian problems: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2024.pdf

## Добавленные карточки

- `miklos-schweitzer-2017-p1-triangle-tiling-no-shared-side`: граф разбиения квадрата на треугольники; статус `needs_human_review`, решение не внесено.
- `miklos-schweitzer-2018-p1-continuous-graph-countable-coloring`: явный бесконечный граф, счетная раскраска через локальные независимые окрестности.
- `miklos-schweitzer-2019-p4-nice-matrices-bipartite-shellings`: графовая формулировка через упорядочения ребер `K_{n,m}`; статус `needs_human_review` из-за использования известной формулы для шеллингов.
- `miklos-schweitzer-2020-p4-axis-parallel-segments-curves-planar-graph`: геометрическая задача с планарным графом в официальном решении; добавлено русское решение по венгерскому PDF.
- `miklos-schweitzer-2024-p1-bipartite-perfect-matching-edge-weights`: явная задача о двудольном графе и совершенных паросочетаниях; решение не внесено.
- `miklos-schweitzer-2024-p8-bipartite-planar-circle-contact-intersection`: явная задача о реализации двудольного планарного графа окружностями; решение не внесено.

## Пропущенные и сомнительные

- 2017 P3 про неотрицательные целочисленные матрицы и собственные значения: можно интерпретировать как матрицы смежности ориентированных мультиграфов, но графовая формулировка не является самостоятельной задачей из условия.
- 2020 P3 про репрезентативные матрицы: можно представить достижимость как ориентированный граф состояний, но это искусственная state graph-модель; пропущено.
- 2021: по венгерским условиям и решениям явных содержательных графовых задач не выявлено.
- 2022: английский PDF просмотрен по списку задач; явных графовых задач не выявлено. Задача про ходы фигур в правильном `k`-угольнике оставлена как геометрико-групповая, не графовая.
- 2023 P7 про 4-элементные множества и условия на пересечения: потенциально кодирует отношения/гаджеты, но не дает естественной самостоятельной графовой задачи; пропущено.
- 2024 P7 про подгруппы `Sym(N)` не добавлялась: это групповая задача, несмотря на возможные действия на счетных структурах.

## Замечания по языку и решениям

- Для 2017-2020 и 2022 использовались английские PDF условий, где они доступны.
- Для 2020 P4 решение взято из венгерского PDF решений; математическая структура ясная и переведена на русский.
- Для 2021, 2023 и части 2024 источники/решения на венгерском. Если уверенного доказательства не было, карточки оставлены без полного решения и со статусом `needs_human_review`.
- Общий реестр `data/sources` не изменялся; источники указаны локально в карточках через требуемые `source_id`.

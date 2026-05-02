# Simon Marais 2017-2019 graph curation report

Дата прохода: 2026-05-02.

## Добавлены карточки

- `data/problems/simon-marais/simon-marais-2017-a1-pentagon-triangle-game.yaml` - SMMC 2017 A1, игра на рёбрах полного графа `K_5` до одноцветного треугольника.
- `data/problems/simon-marais/simon-marais-2017-b3-red-lattice-connected-graph.yaml` - SMMC 2017 B3, официальный граф красных решётчатых точек с единичными рёбрами.
- `data/problems/simon-marais/simon-marais-2018-b3-dodecahedron-spider-pursuit.yaml` - SMMC 2018 B3, погоня на метрическом графе додекаэдра; официальное решение через деревья и симметрию.
- `data/problems/simon-marais/simon-marais-2019-b3-motzkin-straus-clique-labeling.yaml` - SMMC 2019 B3, графовая задача о максимуме взвешенной суммы по рёбрам и кликовом числе.

## Сомнительные пропуски

- SMMC 2017 B4: перечисление разбиений правильного `2n`-угольника ромбами и комментарии про псевдопрямые, сортировочные сети и ориентированные матроиды. Это открытая перечислительная задача; графовая формулировка не является самодостаточным ядром официального условия или решения.
- SMMC 2018 A4: случайная рассадка в ряд сидений с подстаканниками допускает модель через путь/паросочетания, но официальная задача и решение являются вероятностно-рекуррентными; не включено как искусственная графовая модель.
- SMMC 2019 B4: бинарные строки с добавлением символов слева/справа можно представить деревом порождения состояний, но это именно дерево случаев/процесса, которое по инструкции не включалось.

## Официальные URL архивов

- 2017 Problems and Solutions page: https://www.simonmarais.org/20171.html
- 2017 Session A paper: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-1_1.pdf
- 2017 Session B paper: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf
- 2017 preliminary solutions: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf
- 2018 Problems and Solutions page: https://www.simonmarais.org/2018.html
- 2018 Session A paper: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-a_1.pdf
- 2018 Session B paper: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf
- 2018 solutions: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions_1.pdf
- 2019 Problems and Solutions page: https://www.simonmarais.org/20191.html
- 2019 Session A paper: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-a_1.pdf
- 2019 Session B paper: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf
- 2019 solutions: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-solutions_1.pdf

## Проверка

- Все созданные карточки должны быть валидным JSON (`json.loads`).
- Все теги в карточках сверены с `data/taxonomy/tags.yaml`.

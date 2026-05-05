# vosh-2022-23-final-optimal-road-networks

Deep pass date: 2026-05-05

## Source Check

Primary source: official XLIX Vseross final-stage mathematics materials, 2022-2023, grade 11, second day.

Checked URLs:

- https://olympiads.mccme.ru/vmo/2023/final/day2.pdf
- https://vos.olimpiada.ru/upload/files/Arhive_tasks/2022-23/final/math/tasks-math-11-day2-final-22-23.pdf
- https://vos.olimpiada.ru/upload/files/Arhive_tasks/2022-23/final/math/sol-math-11-day2-final-22-23.pdf
- https://vos.olimpiada.ru/math/2022_2023

The official MCCME PDF says that authors are listed in parentheses after each problem. Problem 11.8 is the one about \(N(N-1)\) one-way roads, \(k\) selected cities, and \(N-k\) selected roads; the author printed after the statement is "В. Буслов". The separate VOS archive PDFs for tasks and solutions give the same statement and solution split.

## Statement And Graph Formulation

The original statement in the card matches the official task. The graph formulation is equivalent:

- cities become vertices of the complete directed graph without loops;
- every ordered pair \(X\ne Y\) has exactly one directed edge \(X\to Y\);
- road maintenance costs become edge weights;
- a feasible \(k\)-system is a choice of \(k\) roots and \(N-k\) directed edges such that each vertex reaches at least one root;
- an optimal \(k\)-system is a minimum-weight rooted directed forest among such choices.

The card correctly records this as a graph-in-statement/application problem rather than a hidden graph model. I kept both the original and graph-theory statements because the graph formulation removes the road-language wrapper without changing the extremal object.

## Solution Audit

Classification kept as `official_complete_or_near_complete`.

Reason: the official PDF contains a full solution. The local solution follows the official proof closely, with the same structure:

- first prove that every feasible \(k\)-network is an underlying forest with exactly \(k\) components, each directed toward its unique selected city;
- compare an optimal \((k+1)\)-network \(A\) and an optimal \(k\)-network \(B\);
- choose a root \(y_0\) of \(A\) that is not reachable from any selected root \(x_i\) of \(B\);
- for the \(A\)-basin \(U\) of \(y_0\), swap the outgoing edges from \(U\) between \(A\) and \(B\);
- the two swapped networks are feasible in the neighboring classes, and the sum of their costs is preserved, so optimality is preserved;
- iterate the deletion step from the empty \(N\)-network and number vertices in reverse deletion order.

I made one small wording repair in the local proof: the existence of \(y_0\) follows because the \(k\) vertices \(x_i\) can occupy at most \(k\) components of the \((k+1)\)-forest \(A\), while \(A\) has \(k+1\) selected roots/components. This is the intended pigeonhole step in the official "without loss of generality" line.

## Tags And Metadata

The current tags are appropriate:

- `trees`: feasible networks are rooted forest components;
- `extremal_choice`: optimal networks are exchanged without losing minimality;
- `goal_existence`: the target is existence of one nested chain of optimal root sets.

The profile objects/methods are also appropriate: complete directed weighted graph, rooted forest/arborescence components, exchange argument, forest structure, and reverse induction.

## Relations

Added two high-signal local relations:

- `tree-equivalent-properties` -> this card as a prerequisite: the proof uses the edge-count/component-count characterization of forests.
- `putnam-2013-b5-functions-iterate-into-roots` <-> this card as a same-motif relation: both encode "each vertex eventually reaches a root set" as a rooted directed forest; the Putnam card counts such forests, while this VOS card optimizes over weighted forests and proves nested optimal root sets.

I did not add weaker relations to broad road-orientation or connectivity cards, because they do not share the core rooted-forest exchange mechanism.

## Residual Risks

- The source registry currently points to the MCCME combined day2 PDF, while the VOS archive page also exposes split task/solution PDFs. Both are official and agree; I did not edit `data/sources/sources.yaml` because it was outside the requested scope and the existing source is sufficient.
- The local solution is a paraphrase of the official proof, not a verbatim copy; classification remains official because the proof structure and all key steps are official.

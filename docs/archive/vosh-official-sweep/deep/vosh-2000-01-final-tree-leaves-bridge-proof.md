# vosh-2000-01-final-tree-leaves-bridge-proof

Deep pass date: 2026-05-05

## Source Check

Primary source: Н. Х. Агаханов, И. И. Богданов, П. А. Кожевников, О. К. Подлипский, Д. А. Терешин, *Всероссийские олимпиады школьников по математике 1993-2006: окружной и финальный этапы*, МЦНМО, 2007, PDF at Math.ru.

Checked URLs:

- https://math.ru/lib/files/pdf/olimp/Vseross.pdf
- https://problems.ru/view_problem_details_new.php?id=109740
- https://kvant.mccme.ru/pdf/2001/05/kv0501olimp_mat.pdf

The Math.ru PDF lists this as problem 628 in the 2000-2001 final-stage section, grade 10. The statement matches the local card, and the author is printed as "(Д. Карпов)". Problems.ru gives the same statement and names "Карпов Д.В."; Kvant 2001 N5 also confirms the 2000/01 final, grade 10, problem 4 context and author "Д. Карпов".

## Solution Audit

Classification kept as `official_complete_or_near_complete`.

Reason: the Math.ru/MCCME book contains a full solution. The local solution follows the official argument closely but is written as an independent complete proof:

- convert the road network with a unique simple path between any two cities into a tree;
- choose a pairing of the 100 leaves maximizing the sum of tree distances inside the pairs;
- add the 50 edges of this pairing;
- if an old edge remained a bridge, both components after deleting it would contain an internal paired leaf-pair;
- cross-pairing those four leaves strictly increases the total paired distance, contradiction.

The strict distance inequality is correct because each cross path must traverse the deleted old edge, while the two within-component paths do not. The proof also correctly handles new edges: each new edge lies on a cycle formed by itself plus the old tree path, so it cannot be a bridge.

## Graph Formulation Audit

The graph translation is sound: a finite road network with exactly one simple path between every two cities is a tree, and "after closing any road the country remains connected" is equivalent to saying the augmented graph has no bridges.

I adjusted the graph statement slightly. The previous wording only stated the stronger constructive version "add 50 edges pairing leaves"; this is true and is exactly what the official proof constructs, but the original task only asks to add 50 roads. The updated formulation first states the equivalent bridge-free augmentation goal and then records the stronger leaf-pairing construction.

## Relations

Added one local relation:

- `tree-equivalent-properties` -> this card, `prerequisite`, distance 1. The problem directly uses the classical equivalence between unique simple paths and being a tree, plus the usual behavior of deleting a tree edge.

I did not add weaker edge-connectivity relatives: several cards share the broad motif "remain connected after edge deletions", but their methods are different enough that a local relation would be low signal in this pass.

## Residual Risks

- The source author format differs only in abbreviation: Math.ru/Kvant print "Д. Карпов", while Problems.ru expands this to "Карпов Д.В.".
- The card records a strengthened constructive graph formulation; this is intentional and now explicitly marked as "moreover" rather than being the whole graph statement.

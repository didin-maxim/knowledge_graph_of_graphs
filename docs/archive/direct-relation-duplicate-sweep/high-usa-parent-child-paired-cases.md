# High verification: USA parent-child and paired-variant candidates

Scope: high-verification follow-up for two high global duplicate candidates:

- `usajmo-2023-p3-domino-slides-special-square-digraph` vs `usamo-2023-p3-domino-slides-special-square-digraph`
- `usamo-1976-p1-monochromatic-rectangle-bipartite` vs `usamo-1976-p1a-4x7-monochromatic-rectangle-forcing`

Mode: read-only for `data/`. This report intentionally accounts for the parallel split process: split child files and split relation files may exist before `index/generated.sqlite` is regenerated.

## Summary

| Pair | Classification | Merge? | Confidence | Short reason |
|---|---|---:|---:|---|
| `usamo-2023-p3-domino-slides-special-square-digraph` <-> `usajmo-2023-p3-domino-slides-special-square-digraph` | `paired_variant` / senior-junior nested variant | No, unless policy allows one card with contest variants | High | Same board model, same slide moves, same `k(C)`, same special-square digraph/tree core; different requested output: all possible values vs maximum only. |
| `usamo-1976-p1-monochromatic-rectangle-bipartite` <-> `usamo-1976-p1a-4x7-monochromatic-rectangle-forcing` | `parent_child_split` / compound source parent to part (a) child | No ordinary duplicate merge | High | Parent contains both the `4x7` forcing assertion and the `4x6` sharp construction; child intentionally isolates only the `4x7` forcing half. |

Neither reviewed pair is a `false_friend`. Both are genuinely close because they share mathematical core and source lineage, but their card-boundary semantics are different.

## Case 1: USAMO 2023 P3 vs USAJMO 2023 P3

Verdict: **paired variant**, not a false friend and not an automatic same-card merge.

More precise classification: **official senior/junior nested variant with the same graph core and a weaker junior goal**.

Cards checked:

- `data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml`
- `data/problems/usajmo/usajmo-2023-p3-domino-slides-special-square-digraph.yaml`
- Direct relation in `data/relations/relations.yaml`, id `rel-usamo-2023-p3-usajmo-2023-p3`
- Prior audits: `audit/false-friends-first-pass/usa-putnam.md`, `audit/false-friends-second-pass/usa-putnam-reviewed.md`, `docs/archive/direct-relation-duplicate-sweep/medium-global-heuristic.md`, `docs/archive/direct-relation-duplicate-sweep/medium-usa-putnam.md`

Local evidence:

- USAMO statement asks: find **all possible values** of `k(C)` as a function of odd `n`.
- USAJMO statement asks: find the **maximum possible value** of `k(C)`.
- Both cards have the same core objects: `domino_tiling`, `odd_board`, `empty_square`, `special_square_digraph`, `tree_component`.
- Both cards have the same transformation: `domino_configuration_to_special_square_digraph`.
- Both cards use the same core invariant: the empty-square component is a tree, and `k(C)` is counted through the tree component.
- The USAMO profile goal is `classify_possible_values_of_kc`; the USAJMO profile goal is `maximize_kc`.
- The relation record says this is the senior and junior version of one story: same oriented graph of special cells, with the difference mainly in final goal.

Relation assessment:

- Current source relation type in `data/relations/relations.yaml`: `paired_variant`, distance `1`, status `ai_checked`, confidence `0.99`.
- The generated SQLite index currently reports this same direct pair as `same_motif`; this appears to be an index/staleness or type-normalization mismatch, because the source relation file has `type: paired_variant`.
- Recommended semantic type remains `paired_variant` or a more specific subtype such as `paired_variant/same_core_weaker_goal`.

Merge policy:

- If the project deduplicates by **mathematical identity of the exact requested task**, keep both cards separate.
- If the project allows a single card to represent **official senior/junior variants** with substatements, this pair is eligible for "one card with variants"; however, that would be a policy choice, not a duplicate-cleanup necessity.
- Safe default: keep two cards, preserve the `paired_variant` relation, and avoid labeling this as `same_motif` in human-facing duplicate-sweep summaries.

## Case 2: USAMO 1976 P1 parent vs P1a child

Verdict: **parent-child split**, not a paired variant between these two endpoints and not a false friend.

More precise classification: **compound/source parent containing an extracted self-contained part (a) child**.

Cards checked:

- `data/problems/usamo/usamo-1976-p1-monochromatic-rectangle-bipartite.yaml`
- `data/problems/usamo/usamo-1976-p1a-4x7-monochromatic-rectangle-forcing.yaml`
- Split relation file: `data/relations/relations.d/usamo-1976-p1-rectangle-split-links.yaml`, id `rel-usamo-1976-parent-p1a-forcing`
- Prior audits: `audit/false-friends-first-pass/usa-putnam.md`, `audit/false-friends-second-pass/usa-putnam-reviewed.md`, `docs/archive/direct-relation-duplicate-sweep/medium-global-heuristic.md`

Local evidence:

- The parent statement has two explicit parts:
  - (a) every two-coloring of a `4x7` board forces a monochromatic rectangle;
  - (b) construct a `4x6` coloring with no such rectangle.
- The child `p1a` statement contains only the `4x7` forcing assertion.
- The parent editorial notes explicitly say it is a compound/source parent kept as the original combined source card, split into `p1a` and `p1b`.
- The child editorial notes explicitly say it was extracted from compound USAMO 1976 P1 and proves only the `4x7` forcing assertion, without the `4x6` construction.
- The parent and child share the same source id `src-usamo-1976-aops-wiki`, the same row-column bipartite model, and the same double-counting/pigeonhole method family.
- The split relation text says the original card contains the `4x7` forcing part and the `4x6` construction part, while this child isolates the `4x7` forcing assertion with a self-contained proof.

Index/split-process note:

- `data/problems/usamo/usamo-1976-p1a-4x7-monochromatic-rectangle-forcing.yaml` exists locally.
- `data/relations/relations.d/usamo-1976-p1-rectangle-split-links.yaml` exists locally and contains the parent-child relation.
- `index/generated.sqlite` did not yet include `usamo-1976-p1a-4x7-monochromatic-rectangle-forcing` at the time of this check, so global heuristic reports based on the index may under-report this endpoint until regeneration.

Relation assessment:

- Current source relation type: `same_source`, distance `1`, status `ai_checked`, confidence `0.99`.
- Semantically this is better described in duplicate-sweep language as `parent_child_split`, `compound_parent_to_part_child`, or `same_source/part_split`.
- Do not classify the parent-to-p1a edge as `paired_variant`: the child is not a sibling variant of the parent; it is contained in the parent.
- The true paired/sharpness relation is between the two children, `p1a` and `p1b`, where the `4x7` forcing half is paired with the `4x6` construction half.

Merge policy:

- Do not perform an ordinary duplicate merge from child into parent while the project keeps compound source cards.
- If policy later forbids retaining compound parents after splits, then the parent could become an archival/source wrapper rather than a problem card; that is a broader split-policy decision.
- Safe default under the current split process: keep the parent as the original combined source card, keep the `p1a` and `p1b` children as self-contained task cards, and link parent-to-child via `same_source` or a more explicit parent-child relation type.

## Policy Note For Similar Parent-Child Cases

The following medium-global candidates look like the same structural issue, not automatic duplicates:

- SUMS 2012 P7 parent/extrema vs maximum/minimum children: classify as `parent_child_split` from compound/extrema parent to each child; classify max vs min children as `paired_variant` siblings only if both are kept as separate self-contained tasks.
- CMO 2006 P4 cycle-triplets parent vs max/min children: same policy as SUMS; parent-child for parent edges, paired/sibling variant for max-vs-min if both child cards remain.
- Baltic Way 1997 P19 parent vs part (a)/(b) children: parent-child split; do not merge as duplicates unless compound parents are removed by policy.
- All-Union 1986 tree-distance parent vs `n=6` construction and `n=1986` impossibility children: parent-child split; the two children are complementary subcases, not false friends.

General rule: high text/profile overlap between a compound source parent and an extracted child is expected. Treat it as a card-boundary/split-policy question, not as a same-task duplicate, unless the child fully exhausts the parent and no sibling part remains.

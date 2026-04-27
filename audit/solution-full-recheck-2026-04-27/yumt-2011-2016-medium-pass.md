# YUMT 2011-2016 Medium Pass

Date: 2026-04-27.

Scope: `data/problems/yumt/yumt-2011-*.yaml` through `yumt-2016-*.yaml`.

## Fixed in this pass

- `yumt-2011-grand-round4-problem9#sol-archive-card`: replaced the placeholder with a full proof that the maximal guaranteed bound is `k=1507`, using source/sink strong components in a tournament and a sharp `k=1508` construction.
- `yumt-2012-start-round2-problem5#sol-archive-card`: replaced the placeholder with the direct extremal count `C(8,2)+8*248=2012`.
- `yumt-2015-grand-round3-problem9#sol-archive-card`: expanded the Bondy-Chvatal closure dependency into an in-card proof and promoted the solution to `ai_checked`.
- `yumt-2016-team-olympiad-9-11-problem8#sol-archive-card`: replaced the placeholder with the deletion/reversal proof via a topological order; answer `1000`.

## Marked Incomplete

- `yumt-2014-start-round4-problem2#sol-archive-card`: status changed to `needs_human_review`; the upper bound is present, but the lower bound only cites the official "propeller" construction.
- `yumt-2016-start-high-round1-problem7#sol-archive-card`: status changed to `needs_human_review`; the count `68` relies on an official diagram and an unexpanded case analysis.

## Hard / Backlog

- `yumt-2011-grand-round1-problem9#sol-archive-card`
  - reason: exact placeholder; no local solution found for the two-colour extremal graph with monochromatic girth at least 6.
  - needed: official solution or a complete proof of `m <= floor(n^2/3)` for the stated colouring condition.
  - next_agent: source-transfer / extremal graph proof agent.
- `yumt-2011-premier-round4-problem1#sol-archive-card`
  - reason: exact placeholder and model ambiguity: the answer depends on whether opposite one-way roads between the same pair are allowed.
  - needed: official statement/solution clarifying the directed graph model, then a complete edge-connectivity extremal construction.
  - next_agent: source-verification agent.
- `yumt-2012-start-round3-problem1#sol-archive-card`
  - reason: exact placeholder; translating gives a 4-colouring of edges of `K_20` with no monochromatic triangle, but the card lacks an explicit construction or source.
  - needed: explicit 4-colour triangle-free edge-colouring of `K_20`, or official proof if the intended answer is negative.
  - next_agent: construction/search agent.
- `yumt-2014-grand-round1-problem5#sol-archive-card`
  - reason: exact placeholder; the simple spanning-forest argument is insufficient for `3n` vertices and `5n` edges, and the related RMM material has not been transferred.
  - needed: full stronger lemma/proof from the related RMM source or an independent proof.
  - next_agent: source-transfer / extremal cycles agent.
- `yumt-2014-grand-round2-problem9#sol-archive-card`
  - reason: exact placeholder; no local derivation for the planar graph of glued cubes was found.
  - needed: official cubical-planar argument and extremal construction for the minimum number of marked vertices.
  - next_agent: geometry/planar graph source agent.
- `yumt-2014-grand-round4-problem1#sol-archive-card`
  - reason: exact placeholder; no local solution for the airline-company connectivity extremal value.
  - needed: official solution or a complete extremal construction and upper bound.
  - next_agent: source-transfer agent.
- `yumt-2014-start-final-problem1#sol-archive-card`
  - reason: exact placeholder; likely a cactus/block extremal problem, but the role of parallel roads and 2-cycles must be confirmed.
  - needed: official clarification plus a complete maximum-edge proof.
  - next_agent: source-verification / graph blocks agent.
- `yumt-2014-start-round4-problem2#sol-archive-card`
  - reason: lower bound construction is not self-contained.
  - needed: actual 14-queen board placement and an order of placement satisfying the "beats at most one earlier queen" rule.
  - next_agent: diagram reconstruction agent.
- `yumt-2016-start-high-round1-problem7#sol-archive-card`
  - reason: count `68` uses an omitted official diagram/case analysis.
  - needed: explicit partition of the knight graph and full enumeration of the four exceptional configurations.
  - next_agent: case-analysis / diagram reconstruction agent.

## Validation

Validation commands were run after this pass; see the turn summary for current results.

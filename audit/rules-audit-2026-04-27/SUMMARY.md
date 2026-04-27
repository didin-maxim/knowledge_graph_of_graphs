# Rules Audit 2026-04-27

Scope: full audit of AI editing rules for the graph-problem database.

Three high-reasoning agents reviewed independent areas:

- data/tool/schema rules: JSON-compatible YAML, sources, statements, shared
  statement groups, encoding, LaTeX escaping, validation pipeline;
- mathematical content: statements, solutions, titles, tags, relations,
  merged/split cards, reformulations;
- workflow: how to keep high-reasoning scopes small, when to escalate, how to
  document skipped hard cases without bloating context.

No subagent edited files directly.

## Repeated Error Classes

- Invalid JSON caused by single LaTeX backslashes such as `\(` or `\le`.
- UTF-8 BOM in files read by `json.load`.
- Incomplete proof sketches placed inside `solutions[]`.
- Graph-theory statements written as solution summaries instead of standalone
  graph formulations.
- Merged or split cards upgraded without a separate mathematical check.
- `public_ready: true` despite local `needs_review` / `needs_human_review`.
- Low-confidence `same_motif` relations marked as `ai_checked`.
- Source scope missing when a source applies only to one statement of a merged
  card.

## Added Safeguards

- `docs/AI_CARD_RULES.md`: compact rules for AI edits.
- `tools/audit_rules.py`: warning-level editorial audit for common AI mistakes.
- `tools/lib.py`: explicit failure on UTF-8 BOM before JSON parsing.
- `tools/validate.py`: image examples must point to existing local assets.
- README, handoff, architecture docs now link the new AI rules and audit tool.

## Current Known Warnings

`python tools/audit_rules.py --max-items 5` reports no hard errors and a
non-empty warning set. The largest categories are legacy/ongoing editorial
work:

- placeholder solutions still present in older imported cards;
- `public_ready` conflicts with local uncertain statuses;
- low-confidence `same_motif` relations marked `ai_checked`;
- compressed/restored solution texts whose status should be revisited in later
  mathematical audits.

These warnings are intentionally not hard validation errors yet. They identify
cleanup queues and should prevent new work from silently repeating the same
patterns.

## Escalation Rule

If an edit changes mathematical force, graph type, exact constants, proof
method, source attribution, or relation type, the agent must not fill the gap by
guessing. It should mark the object `needs_human_review`, add a precise
`review_notes` or comment, and launch a narrow high-reasoning check for that
specific hard case.

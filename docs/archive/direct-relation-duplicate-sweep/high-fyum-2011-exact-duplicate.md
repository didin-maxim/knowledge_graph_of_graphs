# High verification: `fyum-2011-tur1a-p5` <-> `fyum-2011-tur1b-p5`

## Verdict

This is duplicate-level: the two cards are the same mathematical problem, not merely the same motif.

More precise classification: **same task / official parallel-variant reprint**. It does not look like an accidental duplicate import from one source file: the local source registry has two separate official FYUM entries, `tur1a.tex` and `tur1b.tex`, titled "First tour (a), Problem 5" and "First tour (b), Problem 5". But the imported statements differ only by line breaks and the phrase "все ребра в котором разного цвета" vs "все ребра в котором покрашены в разные цвета"; the construction and pigeonhole solution are the same.

Recommendation: merge if the database is deduplicating mathematical problem identity, while preserving both FYUM source occurrences on the canonical card.

Confidence: high.

## Cards Checked

- `data/problems/fyum/fyum-2011-tur1a-p5.yaml`
- `data/problems/fyum/fyum-2011-tur1b-p5.yaml`
- Direct relation: `data/relations/relations.d/fyum-idea-links.yaml`, id `rel-fyum-2011-tur1a-p5-tur1b-p5-rainbow-counterexample`
- Medium report: `docs/archive/direct-relation-duplicate-sweep/medium-russian-nonvosh.md`
- Source registry: `data/sources/sources.yaml`
- Import batch: `data/import_batches/fyum-official-graph-curation-2008-2013.yaml`

## Source Check

Local source ids checked:

- `src-fyum-2011-tur1a-p5-official`: `https://www.guas.info/competit/fest/fest22/tur1a.tex`, marked `official: true`, `source_verified`, access note `Files: tur1a.tex / sol1.pdf. Pages: statement: 1; solution: 1.`
- `src-fyum-2011-tur1b-p5-official`: `https://www.guas.info/competit/fest/fest22/tur1b.tex`, marked `official: true`, `source_verified`, access note `Files: tur1b.tex / sol1.pdf. Pages: statement: 1; solution: 2.`

Live internet check on 2026-05-05:

- `https://www.guas.info/competit/fest/fest22/tur1a.tex` returned `404 NOT FOUND`.
- `https://www.guas.info/competit/fest/fest22/tur1b.tex` returned `404 NOT FOUND`.
- `https://www.guas.info/competit/fest/fest22/sol1.pdf` returned `404 NOT FOUND`.
- `https://www.guas.info/competit/fest/` returned a hosting `403` page.

So the source links are currently link-rotted or blocked, but the local registry records both as previously verified official sources. I did not treat the live URLs as confirming the text; the high verdict is based on the verified local source records plus the two imported cards.

## Statement Comparison

Normalized statement of both cards:

- Given a connected graph that remains connected after deletion of any edge.
- Any two vertices are either adjacent or have a common neighbor; equivalently the graph has diameter at most `2`.
- Is it true that the edges can be colored in four colors so that every two vertices are connected by a path whose edges have pairwise distinct colors?

The only textual differences found:

- `tur1a`: "можно покрасить в четыре цвета так, чтобы ... все ребра в котором разного цвета".
- `tur1b`: "можно покрасить в четыре цвета так, чтобы ... все ребра в котором покрашены в разные цвета".
- Line breaks differ.

There is no parameter change, no strengthened/relaxed condition, and no changed conclusion.

## Solution Comparison

Both cards use the same negative answer and the same counterexample:

- Vertices: `A`, `B_1,\dots,B_17`, `C_1,\dots,C_17`.
- Edges: `A` joined to all `B_i`; each `B_i` joined to `C_i`; all `C_i` form a clique.
- The graph is connected, 2-edge-connected, and has diameter at most `2`.
- For any four-edge-coloring, each `B_i` gives a color pair `(col(AB_i), col(B_iC_i))`.
- There are at most `16` color pairs and `17` indices, so two indices `i != j` have the same pair.
- The paths between `B_i` and `B_j` through `A`, through the corresponding `C` vertices, or mixed through one `A` side and one `C` side cannot be rainbow.

The `tur1a` solution text is slightly more explicit about representative mixed paths, while `tur1b` is slightly more compact. These are editorial differences, not different methods.

## Merge Recommendation

Canonical card id: `fyum-2011-tur1a-p5`.

Reason:

- It is the first listed official variant, `First tour (a), Problem 5`.
- Its statement is marginally cleaner as the main statement.
- Its solution is slightly more explicit about path cases.
- Both cards otherwise have the same title, metadata, tags, status, difficulty, standard idea ids, and source role.

Statements to preserve/merge:

- Keep `fyum-2011-tur1a-p5` `stmt-original` as the canonical statement.
- Preserve the `tur1b` wording only if source-level exact wording is important; otherwise it is safe to record `src-fyum-2011-tur1b-p5-official` as an additional source for the same statement.

Sources to preserve/merge:

- Keep `src-fyum-2011-tur1a-p5-official`.
- Add/preserve `src-fyum-2011-tur1b-p5-official` on the canonical card, because the duplicate is a separate official FYUM occurrence rather than a pure import accident.
- Add an access note or editorial note that live URL checks on 2026-05-05 returned `404`, while local records mark the sources as `source_verified`.

Solutions to preserve/merge:

- Keep `fyum-2011-tur1a-p5` `sol-official-archive` as the canonical solution.
- Do not keep `fyum-2011-tur1b-p5` `sol-official-archive` as a separate displayed solution unless provenance requires two official text variants; it is the same counterexample and proof.
- If preserving both solution provenances, attach `src-fyum-2011-tur1b-p5-official` to the canonical solution/source list rather than duplicating the solution body.

Relation change:

- Delete `rel-fyum-2011-tur1a-p5-tur1b-p5-rainbow-counterexample` after merge; it becomes an internal duplicate edge.
- If both cards must remain as contest-instance records, replace the relation type from `same_motif` to a duplicate-level relation such as `reprint` or `same_problem`, with distance `0` if supported. In that non-merge scenario, keep confidence at `0.99`.
- No other relations involving either endpoint were found in `data/relations`, so there are no external relation rewrites needed beyond removing/replacing this direct relation.

## Risks / Follow-up

- The source URLs are currently inaccessible live, so a future data edit should avoid claiming fresh live verification. Treat the existing `source_verified` status as historical/local verification unless an archived copy is recovered.
- The two source ids should not be lost. They likely represent two official FYUM first-tour variants with the same problem, not a single duplicated source row.
- If downstream tooling expects one card per contest variant rather than one card per mathematical problem, merging may hide that `tur1a` and `tur1b` both contained Problem 5. In that model, keep both cards but mark the relation as duplicate-level instead of `same_motif`.
- Future merge edits should be UTF-8-safe; PowerShell terminal output can mojibake these YAML files if read without explicit UTF-8 handling.
- This audit did not edit `data/` or relation files.

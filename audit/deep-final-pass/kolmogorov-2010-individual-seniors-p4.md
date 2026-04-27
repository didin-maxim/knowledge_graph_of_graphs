# Kolmogorov 2010 Individual Seniors Problem 4

## Verdict

`repaired_full_solution_from_official_archive_and_busch_paper`.

The earlier deferred note asked for a verified counting step for `N <= N1*N2`. A deeper source pass shows that this upper-bound direction is the imported error, not the missing proof. The official solution and the cited Busch paper prove the opposite inequality:

`N >= N1 * N2`.

## Sources Checked

- Local OCR/text: `C:\Users\Admin\Documents\Codex\2026-04-25-2020-2020-1-2-work-kolm\work\kolm\text\2010\lichol14.txt`
- Local original DOC: `C:\Users\Admin\Documents\Codex\2026-04-25-2020-2020-1-2-work-kolm\work\kolm\archive\2010\extracted\lichol14.doc`
- Official archive downloaded during this pass: `https://turmath.ru/kolm/files/archive/kolm14.zip`
- External cited paper: Arthur H. Busch, "A Note on the Number of Hamiltonian Paths in Strong Tournaments", Electronic Journal of Combinatorics 13 (2006), #N3, `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1n3/pdf`

The `lichol14.doc` extraction loses several inequality glyphs as `(`, including the final problem inequality. The recovered official solution, however, is the same construction as Busch Theorem 1, lines 119-126 in the PDF text extraction: from Hamiltonian paths in two strong subtournaments meeting in one vertex, it constructs a Hamiltonian path of the whole tournament and concludes `hp(T) >= hp(T[A])hp(T[B])`.

## Counting Step

Let `w` be the common capital and let `A`, `B` be the two republic subtournaments. For any Hamiltonian paths

- `P = P1 w P2` in `A`,
- `Q = Q1 w Q2` in `B`,

the path-merging lemma gives a merge `R1` of `P1` and `Q1`, and a merge `R2` of `P2` and `Q2`, each preserving the internal order inherited from `P` and `Q`. Because the last vertex of nonempty `R1` has an edge to `w`, and `w` has an edge to the first vertex of nonempty `R2`, `R = R1 w R2` is a Hamiltonian path of the whole country.

Distinct pairs `(P,Q)` give distinct global paths, since restricting the constructed global path to the vertices of `A` and `B` recovers the original orders `P` and `Q`. Thus there is an injection

`HamiltonianPaths(A) x HamiltonianPaths(B) -> HamiltonianPaths(T)`,

so `N >= N1*N2`.

The previous statement `N <= N1*N2` is false. For example, take three cities forming a directed triangle, with the common capital as one vertex and one non-capital city in each republic. Then each two-city republic has exactly one Hamiltonian path, so `N1*N2 = 1`, while the full directed triangle has three Hamiltonian paths, so `N = 3`.

## Changes

- Corrected the statement from `N <= N1 * N2` to `N >= N1 * N2`.
- Corrected the country name to the official source spelling `Гельбии`.
- Expanded the solution into a complete proof of the official lower bound, including the injection/counting step.
- Set solution `status` to `ai_checked`.
- Replaced the deferred repair marker with `repair_status: repaired_full_solution_from_official_archive_and_busch_paper`.
- Left the existing `hamiltonian_cycles` tag unchanged because the current project taxonomy rejects `hamiltonian_paths`; the path-specific content is represented in `problem_profile.keywords`, `definition_ids`, and the solution text.
- Added editorial notes documenting why the old upper-bound version was not repairable.

## Validation

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
- Passed: `git diff --check -- data\problems\kolmogorov\kolmogorov-2010-individual-olympiad-seniors-problem-4.yaml audit\deep-final-pass\kolmogorov-2010-individual-seniors-p4.md`
  - Note: Git printed an LF-to-CRLF normalization warning for the YAML file, but reported no whitespace errors.

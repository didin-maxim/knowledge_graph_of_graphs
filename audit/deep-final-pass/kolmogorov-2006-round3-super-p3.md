# Kolmogorov 2006 Round 3 Super League Problem 3

## Verdict

`repaired_full_solution_from_official_archive`.

I downloaded the official archive listed in `data/sources/sources.yaml`:

- `https://turmath.ru/kolm/files/archive/kolm10.zip`
- extracted file: `Problems/tur3_10sol.doc`

The official solution contains exactly the missing step: after assuming at most `499` colors around `A`, choose a color appearing at least three times among neighbors of `A`; call those vertices `B_1, ..., B_k`, `k >= 3`. For each absent color `501`, `502`, `503`, the two-color component on colors `2` and that absent color must contain all `B_i`, otherwise a Kempe swap increases the number of colors around `A`. Minimality/local recoloring forces the component to be path-like and forces every internal `B_i` on such a path to have only that absent color repeated among its neighbors. Three such paths through `B_2, ..., B_k` force one vertex to be internal for two paths, giving two distinct repeated absent colors, contradiction.

## Changes

- Expanded `sol-official-compressed` into a complete official-solution exposition.
- Set solution `status` to `ai_checked`.
- Replaced the deferred repair marker with `repair_status: repaired_full_solution_from_official_archive`.
- Updated `review_notes` to record the official archive and the minor `.doc` extraction gaps that were filled from the surrounding argument.

## Validation

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`

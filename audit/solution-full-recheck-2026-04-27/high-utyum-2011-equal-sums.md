# High Recheck: Utyum 2011 Equal Sums

Problem: `utyum-2011_tur4_37_8_equal_sums_bipartite_graph`.

Solution: `sol-official`.

## Source

- Official archive: `https://turmath.ru/uraltur/files/archive/ural37.zip`.
- Archive files checked locally: `tur4_37.doc` and `tur4_37sol.doc`.
- The solution text is in `tur4_37sol.doc`, junior group, higher league, math battle 4, problem 8.

The official answer is `66`.

## Finding

The previous card was mathematically false. It treated changed cells as unweighted edges and required all 100 vertex degrees in a bipartite graph with parts of size 50 to be pairwise distinct. That is impossible because every degree is at most 50. The proposed even/odd degree construction also had different total degree sums in the two parts.

## Repair

Replaced the degree-only solution with the official weighted-support-graph argument:

- vertices are rows and columns;
- an edge marks a changed cell;
- the edge weight is the numerical change in that cell;
- the new row/column sum is the original common sum plus the sum of incident edge weights.

Lower bound: no component of size 2 is possible, at most one vertex can be isolated, so the support graph has at most `1 + 99/3 = 34` components. Hence with `m` changed cells,
`m >= 100 - 34 = 66`.

Construction: leave one column isolated, split the remaining 99 vertices into 17 triples of type two rows plus one column and 16 triples of type one row plus two columns. In each triple change two cells. Assign the 66 changed cells distinct weights `10^1, ..., 10^66`; each triple then gives increments `10^a`, `10^b`, and `10^a + 10^b`, all distinct by decimal representation, plus the isolated increment `0`.

## Validation

- `python tools/validate.py` - OK.
- `python tools/check_links.py` - OK.

# Repair pass done: IMO + classical

| path | action | reason |
|---|---|---|
| data/problems/classical/dirac-theorem.yaml | set solution status `ai_checked` | Standard longest-path proof is complete enough: endpoint-neighbor position argument closes a longest path, then minimum degree gives connectivity and Hamiltonicity. Solution id retained because relations outside this zone reference it. |
| data/problems/classical/five-color-theorem.yaml | set solution status `ai_checked` | Kempe-chain proof includes the low-degree vertex, induction, the 1-3 chain recoloring case, and the planar separation alternative for 2-4 chains. Solution id retained because relations outside this zone reference it. |
| data/problems/classical/hall-marriage-theorem.yaml | set solution status `ai_checked` | Induction proof has both strict Hall deletion and tight-subset splitting; a second checked tight-set solution already supplies the same residual Hall verification. |
| data/problems/classical/konig-vertex-cover-theorem.yaml | set solution status `ai_checked` | Alternating-reachability construction of `(X\Z) union (Y cap Z)` and size equality with a maximum matching are the standard complete proof. |
| data/problems/classical/mantel-theorem.yaml | set solution status `ai_checked` | Degree-sum proof is complete; the integer edge count gives the stated floor bound from `m <= n^2/4`. |
| data/problems/imo/imo-2015-c5-sequence-rays.yaml | checked; no YAML change | Text is already expanded and status is already `ai_checked`; only the historic solution id still says compressed, and it was not renamed to avoid cross-file anchor churn. |
| data/problems/imo/imo-2019-c3-coin-process-digraph.yaml | checked; no YAML change | Short but self-contained recurrence proof; status already `ai_checked`. |
| data/problems/imo/imo-2020-c4-fibonacci-difference-forest.yaml | checked; no YAML change | Forest lower bound and construction are explicit enough; status already `ai_checked`. |
| data/problems/imo/imo-2020-c6-colored-coins-eulerian-multigraph.yaml | checked; no YAML change | Eulerian multigraph alternating-coloring argument is explicit enough; status already `ai_checked`. |
| data/problems/imo/imo-2023-c4-strip-pieces-eulerian-graph.yaml | checked; no YAML change | Lower-bound graph argument is present in enough detail; status already `ai_checked`. |

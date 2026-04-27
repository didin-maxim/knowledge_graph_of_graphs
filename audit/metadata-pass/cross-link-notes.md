# Metadata pass cross-link notes

Date: 2026-04-26

Problem YAML was not edited in this pass.

## Metadata gaps noticed

- `kolmogorov-2002-team-olympiad-seniors-problem-8.yaml`: the restored `sol-official-full` uses Hall's theorem and matching-deficiency language in the proof of Dolnikov's lemma, but the problem profile still has an empty `methods` list and no matching/Hall keyword.
- `kolmogorov-2004-round2-higher-league-problem-9.yaml`: the repaired solution uses the standard `C4`-free codegree/Jensen extremal estimate. There is no existing classical card in the current repository for the Zarankiewicz/Kovari-Sos-Turan `C4`-free edge bound, so no precise classical prerequisite relation was added for that step.

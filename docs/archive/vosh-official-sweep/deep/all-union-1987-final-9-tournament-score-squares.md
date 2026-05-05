# Deep Audit: all-union-1987-final-9-tournament-score-squares

Date: 2026-05-05

## Verdict

- Statement/source: verified. The OCR access copy lists the problem as No. 177 under "Олимпиада 1987 г.", first day, with the same table-tennis round-robin statement.
- Solution: found online in the same OCR access copy. The printed solution proves \(x_i+y_i=9\), \(\sum x_i=\sum y_i\), and then subtracts sums of squares.
- Author/proposer: not found. The checked sources identify collection/article authors, but not a proposer for this specific problem.
- Classification: `unofficial_published`. The solution is published and complete, but the checked source is a published collection/OCR copy rather than an official olympiad solution source.

## Sources Checked

- Math.ru bibliographic page for N.B. Vasilyev and A.A. Egorov, *Zadachi vsesoyuznykh matematicheskikh olimpiad*, Nauka, 1988: https://math.ru/lib/bib-mat-kr/18
- OCR access copy, *Matematicheskie olimpiady shkolnikov. 9 klass*, 1997: https://djvu.online/file/A6gSDRaJgDboJ
- Kvant Digital article metadata, V.V. Vavilov, S.V. Reznichenko, A.M. Slinko, "XXI Vsesoyuznaya olimpiada po matematike", Kvant 1987 no. 11: https://www.kvant.digital/issues/1987/11/vavilov_reznichenko_slinko-xxi_vsesoyuznaya_olimpiada_po_matematike-4787f2d7/
- Infourok mirror with a later copied statement and short solution: https://infourok.ru/zadaniya-dlya-olimpiadi-po-matematike-klass-2071143.html

## Formulation Notes

The local statement matches the reliable OCR source modulo OCR distortions in indices and powers. The problem is a 10-player round-robin table-tennis tournament, so every player has \(x_i+y_i=9\). Since each game contributes one win and one loss, \(\sum_i x_i=\sum_i y_i\). The square identity follows from
\[
\sum_i x_i^2-\sum_i y_i^2=\sum_i (x_i-y_i)(x_i+y_i)=9\sum_i(x_i-y_i)=0.
\]

## Local Relations

- `polish-mo-2022-ii-p6-badminton-euler-cycles`: same sports-tournament encoding and win/loss balance, but the Polish problem needs an even-degree graph and cycle decomposition.
- `imo-2010-c5-bad-company-tournament`: another tournament-score problem using wins/losses and degree sums, substantially harder.
- `cmo-2006-p4-cycle-triplets-tournament`: same finite-tournament language and degree-counting style, but counts triples rather than proving a score-sequence identity.
- `tournament-king-radius-two` and `tournament-hamiltonian-path`: standard tournament relatives by object, more distant by goal.

## Risk Notes

- The proposer remains unknown; Vavilov, Reznichenko, and Slinko are recorded only as article authors for the Kvant olympiad report.
- The solution classification is not `official_complete_or_near_complete` because no official solution source was confirmed in this pass.

# Catalan partial-sum denominators

Haobo Ma (ChronoAI Pte Ltd, Singapore) and Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

For every positive integer n, the reduced denominator of the sum of C(k)/4^(k-1), for 1 <= k <= n, is the reduced denominator of C(n)/4^(n-1). It equals 2^(2n-1-s_2(n+1)), where s_2 counts binary ones, and therefore equals 2^(A283208(n)-2).

## Files and build

- `note.tex`: complete mathematical text with embedded bibliography.
- `note.pdf`: readable mathematical note.
- `metadata.json`: scientific description and creator information.
- `verify.py`: exact rational and integer checks, using Python's standard library.
- `verification.json`: the finite ranges checked and their outcomes.

Build with Tectonic 0.17.0:

```sh
tectonic note.tex
python3 verify.py > verification.json
```

Alternatively run `pdflatex note.tex` twice. The bibliography is embedded, so BibTeX is not needed.

## Mathematical coverage

The written proof derives the denominator equality from Pieter Mostert's 2012 finite-sum identity. It also proves Alexander Staunton's 2026 linked formula, a binary-digit expression, and the companion numerator formula, and rederives the related identities and generating function in A283208. It corrects the index in the Meijer convolution formula in A119951 from a(n-1) to a(n), and replaces the literal minimum expression in A283208 with the equivalent positive-residue minimum.

The exponent formula is Theorem 6 of Isabel Cação, Maria Irene Falcão and Helmuth R. Malonek, *Hypercomplex Polynomials, Vietoris' Rational Numbers and a Related Integer Numbers Sequence*, Complex Analysis and Operator Theory 11 (2017), 1059–1076, DOI 10.1007/s11785-017-0649-5. Their equation (5.6) identifies the rational whose denominator defines A283208. The two A120069 conjectures are explicit consequences of this earlier theorem and Mostert's identity; the note supplies short proofs, the binary-digit expression and the two stated corrections.

The declaration `D5.S3.ArithSums.GrouxA120069Denominator.result` in the [pinned Lean file](https://github.com/the-omega-institute/trureturing/blob/3378450a2176909e857354ab064dde6ec7679b71/D5/S3/ArithSums/GrouxA120069Denominator.lean) states the universal denominator equality for positive natural indices. The other claims have written proofs in the note. `verification.json` records supplemental finite checks, not a replacement for the proofs.

Primary sources: OEIS A120069 revision 30, A119951 revision 32, and A283208 revision 103. The exact posing lines and attributions appear in the bibliography and coverage table.

License: Creative Commons Attribution 4.0 International (CC BY 4.0), `cc-by-4.0`.

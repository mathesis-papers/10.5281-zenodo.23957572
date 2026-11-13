# Question 31, §2.2.5, p. 24, arXiv:2610.22248v1

Haobo Ma (ChronoAI Pte Ltd, Singapore) and Wenlin Zhang (National University of
Singapore; ChronoAI Pte Ltd, Singapore). Licensed CC BY 4.0.

The note answers the algebraic-group and group-scheme clauses of Question 31,
§2.2.5, p. 24, of Kaygorodov–Martín González–Viruel, arXiv:2610.22248v1.
It proves that no finite-dimensional complex evolution algebra has full
automorphism group scheme or algebraic group SLₙ for n=3 or n≥5. The written
structural proof establishes Conjecture 5 and the semisimple clause of Question 36.
For zero-annihilator algebras it also classifies the semisimple quotient of the
derivation algebra. The comment after Conjecture 5 is treated with separate
statements about simple ideals, nonzero annihilators, and faithful subalgebra actions.
Question 14's last clause is answered in minimal dimension two: a zero-annihilator
algebra has exactly two automorphisms but infinitely many natural bases modulo
permutations and independent nonzero scalings. The algebra and its group are
credited to the 2018 primary source, with later related results dated explicitly.

## Files and reproduction

- `note.tex`: complete mathematical text with an embedded bibliography.
- `note.pdf`: typeset note.
- `verify.py`: standard-library Python 3 exact rational checks.
- `verification.json`: the checks' deterministic output.
- `verify_siblings.py` and `sibling_verification.json`: exact rational checks of
  signed-form examples, the zero-product algebra, the split SL₃ Lie action and
  the rank–dimension comparison through n=100, plus 25 natural bases and all
  625 ordered parameter pairs in their separation test.
- `metadata.json`: scientific description, creators, license and source links.

Build with Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, run `pdflatex -interaction=nonstopmode -halt-on-error note.tex`
twice. The bibliography is embedded; BibTeX is not required.

Reproduce the finite checks:

```sh
python3 verify.py > verification.json
python3 verify_siblings.py > sibling_verification.json
```

The checks cover derivation dimensions of the orthogonal examples for 1 ≤ m ≤ 7,
the exact eight-dimensional adjoint Killing matrix of sl₃, and all sums of
orthogonal dimensions at most eight. These finite checks are not premises for
the unbounded written proof.

## Formal coverage

All following files are pinned at `da4f665789a4b88cdf9eda07a8454fc517979ba5`.
Their declaration namespace prefix is
`D5.S3.QuadraticForms.EvolutionAlgebras`.

- [AlgebraicGroupRealizationRefutation.lean](https://github.com/the-omega-institute/trureturing/blob/da4f665789a4b88cdf9eda07a8454fc517979ba5/D5/S3/QuadraticForms/EvolutionAlgebras/AlgebraicGroupRealizationRefutation.lean):
  `AlgebraicGroupRealizationRefutation.result` negates universal full-functor
  realization over ℂ, with SL₃ as witness.
- [EvolutionAutomorphismTangentBridge.lean](https://github.com/the-omega-institute/trureturing/blob/da4f665789a4b88cdf9eda07a8454fc517979ba5/D5/S3/QuadraticForms/EvolutionAlgebras/EvolutionAutomorphismTangentBridge.lean):
  `EvolutionAutomorphismTangentBridge.tangent_lie_equivalence` identifies the
  tangent Lie algebra with sl₃ under a natural full-functor realization.
- [SemisimpleDerivationClassification.lean](https://github.com/the-omega-institute/trureturing/blob/da4f665789a4b88cdf9eda07a8454fc517979ba5/D5/S3/QuadraticForms/EvolutionAlgebras/SemisimpleDerivationClassification.lean):
  `SemisimpleDerivationClassification.result` proves Conjecture 5 over every
  algebraically closed field of characteristic zero.
- [DerivationAnnihilatorObstruction.lean](https://github.com/the-omega-institute/trureturing/blob/da4f665789a4b88cdf9eda07a8454fc517979ba5/D5/S3/QuadraticForms/EvolutionAlgebras/DerivationAnnihilatorObstruction.lean):
  `DerivationAnnihilatorObstruction.Annihilator.semisimple_natural_squares_ne_zero`
  gives the nonzero-square conclusion.
- [FiniteAutomorphismsInfiniteNaturalBases.lean](https://github.com/the-omega-institute/trureturing/blob/da4f665789a4b88cdf9eda07a8454fc517979ba5/D5/S3/QuadraticForms/EvolutionAlgebras/FiniteAutomorphismsInfiniteNaturalBases.lean):
  `FiniteAutomorphismsInfiniteNaturalBases.result` proves existence over ℂ,
  in dimension two, with zero annihilator, finite full automorphism group, and
  an infinite quotient of all natural Fin(2)-indexed bases by permutations and
  independent nonzero scalings. Minimality follows from the written argument.

The note proves its structural and converse statements in writing. The
algebraic-group comparison uses Cartier's characteristic-zero smoothness theorem,
as identified in the note's bibliography. The semisimple-quotient theorem,
the higher-n special-linear exclusion, the distinction between ideals and
actions, and characteristic-zero smoothness are written proofs; the tangent
Lean declaration listed above is specific to SL₃. The abstract-group clause,
positive characteristic, full SL₂ and SL₄ group realization, and nilpotent or
solvable realization are not covered.

## Source coverage

The PDF's coverage table maps Questions 14 and 31, Conjecture 5 and its comment,
Question 36, Proposition 14, Remark 15 and Question 37 to precise statements.
The signed-form construction is attributed to the survey; smoothness is an
application of Cartier's theorem. For perfect algebras, the stronger prior
result Der(A)=0 in characteristic zero is cited to Elduque–Labra, §4.

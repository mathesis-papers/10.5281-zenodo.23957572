# Sources, formal evidence, and contributions

This explanation develops Haobo Ma and Wenlin Zhang's version 2 paper and its public reading for that exact version. Original Theorem, Lemma and Corollary numbers locate the manuscript. Descriptive links in the reading avoid confusing those numbers with the book's generated numbering.

## Who asked the question, and what came earlier?

The survey is by Kaygorodov, Martín González and Viruel; it attributes Question 31 to Costoya and Viruel. Elduque–Labra already use the automorphism group scheme and its derivation tangent space. Calderón Martín, Fernández Ouaridi and Kaygorodov give proportional-square blocks and derivation equations. The orthogonal construction is already in survey Proposition 14 and Remark 15, and the two-dimensional algebra and its full group have earlier sources. These contributions are credited separately from the paper's semisimple reduction, group obstruction, semisimple quotient and natural-basis quotient arguments. Smoothness is an application of Cartier's theorem. Classical Lie ranks, dimensions and accidental isomorphisms are prior theory.

## What exactly does Lean check?

The [semisimple classification](01-proof.md#classification) matches its public declaration completely: any algebraically closed field of characteristic zero, finite-dimensional evolution multiplication, semisimple derivations and a finite orthogonal sum, including the empty sum. That declaration does not assert the converse construction.

The SL₃ file's public main conclusion refutes universal realization of linear algebraic groups by full natural automorphism functors, using SL₃. Its derivation obstruction is a private lemma; the complete manuscript headline also explicitly states the derivation obstruction for each algebra and the algebraic-group comparison. The tangent bridge is specific to SL₃. The natural-basis file proves dimension two, zero annihilator, a finite full group and an infinite quotient of all natural bases; its main statement does not assert exactly two automorphisms or minimality. Public components also cover nonzero natural squares, the block decomposition and stabilizer quotients; composing them into the full source lemma statements remains a contribution task.

Accordingly the book distinguishes the exactly matched classification from the other complete written arguments. The semisimple quotient, higher special linear obstruction, functorial orthogonal realization and ideal/action examples retain written proofs; nearby declarations are not presented as checking all those conclusions. The source links below use the book's inspected revision; the paper's historical links are preserved.

- [Semisimple classification](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/SemisimpleDerivationClassification.lean#L277).
- [Universal full-functor refutation](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/AlgebraicGroupRealizationRefutation.lean#L246).
- [SL₃ tangent bridge](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/EvolutionAutomorphismTangentBridge.lean).
- [Nonzero natural squares](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/DerivationAnnihilatorObstruction.lean#L301).
- [Square-block decomposition](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/NondegenerateDerivationBlocks.lean#L712).
- [Natural-basis existence](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/FiniteAutomorphismsInfiniteNaturalBases.lean#L210).

## Finite checks are illustrations

The source reports finite calculations for orthogonal examples with $1\le m\le7$, sums of orthogonal dimensions up to eight, rank/dimension comparisons through $n=100$, and basis parameters $1\le t\le25$. These are not proofs of unbounded conclusions; the arguments in the preceding chapters establish those conclusions.

## Contribute to the remaining formalization

The shared requests below track the remaining scope of individual complete source results. Some need only composition of existing lemmas; the classification should not be reproved. Coordinate on the corresponding request, work on a focused branch in your own fork, and submit directly to upstream `dev` under its [current contribution rules](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). Keep the original authors, earlier literature and proof contributors separately credited. Issue closure or CI success does not by itself establish whole-paper statement correspondence.

- [Theorem 1 — Complete SL3 derivation and full-group obstruction](https://github.com/the-omega-institute/trureturing-requests/issues/101).
- [Lemma 2 — Semisimplicity forces zero annihilator](https://github.com/the-omega-institute/trureturing-requests/issues/102).
- [Lemma 3 — Orthogonal pointwise-stabilizer decomposition](https://github.com/the-omega-institute/trureturing-requests/issues/103).
- [Lemma 4 — Semisimple pointwise stabilizers are orthogonal](https://github.com/the-omega-institute/trureturing-requests/issues/104).
- [Corollary 6 — Orthogonal realization by evolution algebras](https://github.com/the-omega-institute/trureturing-requests/issues/105).
- [Corollary 7 — Two automorphisms and infinitely many natural basis classes](https://github.com/the-omega-institute/trureturing-requests/issues/106).
- [Corollary 8 — Orthogonal semisimple quotient and simple ideals](https://github.com/the-omega-institute/trureturing-requests/issues/107).
- [Corollary 9 — Special linear realization obstruction and two Lie exceptions](https://github.com/the-omega-institute/trureturing-requests/issues/108).
- [Corollary 10 — Annihilator necessity and faithful SL3 Lie actions](https://github.com/the-omega-institute/trureturing-requests/issues/109).
- [Corollary 11 — Characteristic-zero smoothness of algebra automorphism schemes](https://github.com/the-omega-institute/trureturing-requests/issues/110).

## References

- Haobo Ma and Wenlin Zhang. *A negative answer to Question 31 (section 2.2.5, page 24, arXiv:2610.22248v1): special linear obstructions for evolution algebras*, version 2. [10.5281/zenodo.23957573](https://doi.org/10.5281/zenodo.23957573). CC-BY-4.0.
- I. Kaygorodov, C. Martín González and A. Viruel. *Evolution algebras: a survey of results and a list of open problems*, [arXiv:2610.22248v1](https://arxiv.org/abs/2610.22248v1), 2026. Question 31: §2.2.5, p.24; Question 36 and Question 37: p.25; Conjecture 5: §2.3, p.28; Question 14: §2.2.2, p.22; Proposition 14 and Remark 15: §2.1.2, pp.13–14.
- A. J. Calderón Martín, A. Fernández Ouaridi and I. Kaygorodov. *Non-degenerate evolution algebras*. J. Pure Appl. Algebra **228** (2024), 107594. [10.1016/j.jpaa.2023.107594](https://doi.org/10.1016/j.jpaa.2023.107594). Derivation equations: §5 of [arXiv:2303.00862v1](https://arxiv.org/abs/2303.00862v1); the group ingredient: Theorem 26 and Remark 29.
- A. Elduque and A. Labra. *Evolution algebras, automorphisms, and graphs*. Linear Multilinear Algebra **69** (2021), 331–342. [10.1080/03081087.2019.1598931](https://doi.org/10.1080/03081087.2019.1598931); [arXiv:1902.02191v1](https://arxiv.org/abs/1902.02191v1). Introduction and §4.
- J. S. Milne. *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*. Cambridge University Press, 2017. [Author's text](https://www.jmilne.org/math/Books/iAG2017.pdf), Theorem 3.23 and Corollary 11.31(a).
- J. S. Milne. *Lie Algebras, Algebraic Groups, and Lie Groups*, version 2.00, 5 May 2013. [Author's text](https://www.jmilne.org/math/CourseNotes/LAG.pdf), Chapter I, §§3–4, 7–8; classical ranks and dimensions on pp.92–96.
- M. I. Cardoso Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González and M. Siles Molina. *Squares and associative representations of two dimensional evolution algebras*. J. Algebra Appl. **20** (2021), 2150090. [10.1142/S0219498821500900](https://doi.org/10.1142/S0219498821500900); [arXiv:1807.02362v1](https://arxiv.org/abs/1807.02362v1), first posted 6 July 2018. Lemma 3.15 and §5.1, $A_{8,1}$.
- N. Boudi, Y. Cabrera Casado and M. Siles Molina. *Natural families in evolution algebras*. Publ. Mat. **66** (2022), 159–181. [10.5565/PUBLMAT6612206](https://doi.org/10.5565/PUBLMAT6612206); [arXiv:2006.14460v1](https://arxiv.org/abs/2006.14460v1), first posted 25 June 2020. Corollary 2.13 and Proposition 2.16.
- Y. Cabrera Casado, M. I. Cardoso Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González and I. Ruiz Campos. *Solenoids in automorphism groups of evolution algebras*. [arXiv:2505.14584v1](https://arxiv.org/abs/2505.14584v1), first posted 20 May 2025. Example 6.3.

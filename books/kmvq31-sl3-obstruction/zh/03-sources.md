# 文献、形式化范围与贡献

本说明依据 Haobo Ma 与 Wenlin Zhang 的原论文第2版及同版本公开阅读文本展开。这里的原文 Theorem、Lemma、Corollary 编号只用于定位原论文；正文交叉引用使用描述性名称，以免与本书的重新编号混淆。

## 谁提出问题，哪些结果已有先行来源？

综述由 Kaygorodov、Martín González 与 Viruel 撰写；Question 31 在那里归于 Costoya 与 Viruel。Elduque–Labra 已使用自同构群概形及其导子切空间；Calderón Martín、Fernández Ouaridi 与 Kaygorodov 已写出比例平方块及导子方程。正交构造在综述 Proposition 14 与 Remark 15 中已有；二维代数及其完整自同构群也有更早研究。这里将这些来源与本文的半单归约、群障碍、半单商和自然基商论证分别署名。光滑性是 Cartier 定理的应用，经典李代数的秩、维数与偶然同构不是本文的新定理。

## Lean 具体检查了什么？

[半单分类](01-proof.md#classification)与所引公开声明完整一致：任意特征零代数闭域、有限维演化乘法、半单导子代数、允许空直和。这并不包含逆向实现。

SL₃ 文件的公开主结论否定“每个线性代数群都能由全部自然自同构函子实现”，使用 SL₃ 作反例。它的导子障碍在私有引理内；完整原文主定理还明确陈述每个代数的导子障碍及代数群比较。切空间文件针对 SL₃。自然基文件证明二维、零化子为零、群有限和全部自然基商无限，没有在主声明中给出“恰好两个”及最小性。非零平方、块分解及稳定子商有公开形式化成分；将其组合成原文各引理的完整表述仍在贡献任务中。

因此本书将完整匹配的分类与其余书面证明区分。半单商、高阶特殊线性障碍、正交函子性实现与理想/作用例子保留纸面论证，不借用邻近声明声称整条结论已经形式化。以下源码链接固定在本书所用版本；原论文的历史链接保持原样。

- [Semisimple classification](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/SemisimpleDerivationClassification.lean#L277).
- [Universal full-functor refutation](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/AlgebraicGroupRealizationRefutation.lean#L246).
- [SL₃ tangent bridge](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/EvolutionAutomorphismTangentBridge.lean).
- [Nonzero natural squares](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/DerivationAnnihilatorObstruction.lean#L301).
- [Square-block decomposition](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/NondegenerateDerivationBlocks.lean#L712).
- [Natural-basis existence](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/QuadraticForms/EvolutionAlgebras/FiniteAutomorphismsInfiniteNaturalBases.lean#L210).

## 有限检查只是例子

原文附带的有限计算涉及正交例子 $1\le m\le7$、不超过八维的正交维数之和、$n\le100$ 的秩维数比较及 $1\le t\le25$ 的基参数。这些不是无界结论的证明；无界结论由前面的论证给出。

## 如何贡献尚未形式化的部分

以下共享请求分别追踪完整原文结果的剩余范围。其中若干只需组合已有引理，不应重新证明已有分类。先在相应请求中协调，再在贡献者自己的 fork 中开聚焦分支，直接向上游 `dev` 提交 PR，遵守[现行贡献规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)。保留原作者、先行工作与形式化贡献者的分别署名；任务关闭或 CI 成功不自动意味着整篇论文的陈述已匹配。

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

## 文献

- Haobo Ma and Wenlin Zhang. *A negative answer to Question 31 (section 2.2.5, page 24, arXiv:2610.22248v1): special linear obstructions for evolution algebras*, version 2. [10.5281/zenodo.23957573](https://doi.org/10.5281/zenodo.23957573). CC-BY-4.0.
- I. Kaygorodov, C. Martín González and A. Viruel. *Evolution algebras: a survey of results and a list of open problems*, [arXiv:2610.22248v1](https://arxiv.org/abs/2610.22248v1), 2026. Question 31: §2.2.5, p.24; Question 36 and Question 37: p.25; Conjecture 5: §2.3, p.28; Question 14: §2.2.2, p.22; Proposition 14 and Remark 15: §2.1.2, pp.13–14.
- A. J. Calderón Martín, A. Fernández Ouaridi and I. Kaygorodov. *Non-degenerate evolution algebras*. J. Pure Appl. Algebra **228** (2024), 107594. [10.1016/j.jpaa.2023.107594](https://doi.org/10.1016/j.jpaa.2023.107594). Derivation equations: §5 of [arXiv:2303.00862v1](https://arxiv.org/abs/2303.00862v1); the group ingredient: Theorem 26 and Remark 29.
- A. Elduque and A. Labra. *Evolution algebras, automorphisms, and graphs*. Linear Multilinear Algebra **69** (2021), 331–342. [10.1080/03081087.2019.1598931](https://doi.org/10.1080/03081087.2019.1598931); [arXiv:1902.02191v1](https://arxiv.org/abs/1902.02191v1). Introduction and §4.
- J. S. Milne. *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*. Cambridge University Press, 2017. [Author's text](https://www.jmilne.org/math/Books/iAG2017.pdf), Theorem 3.23 and Corollary 11.31(a).
- J. S. Milne. *Lie Algebras, Algebraic Groups, and Lie Groups*, version 2.00, 5 May 2013. [Author's text](https://www.jmilne.org/math/CourseNotes/LAG.pdf), Chapter I, §§3–4, 7–8; classical ranks and dimensions on pp.92–96.
- M. I. Cardoso Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González and M. Siles Molina. *Squares and associative representations of two dimensional evolution algebras*. J. Algebra Appl. **20** (2021), 2150090. [10.1142/S0219498821500900](https://doi.org/10.1142/S0219498821500900); [arXiv:1807.02362v1](https://arxiv.org/abs/1807.02362v1), first posted 6 July 2018. Lemma 3.15 and §5.1, $A_{8,1}$.
- N. Boudi, Y. Cabrera Casado and M. Siles Molina. *Natural families in evolution algebras*. Publ. Mat. **66** (2022), 159–181. [10.5565/PUBLMAT6612206](https://doi.org/10.5565/PUBLMAT6612206); [arXiv:2006.14460v1](https://arxiv.org/abs/2006.14460v1), first posted 25 June 2020. Corollary 2.13 and Proposition 2.16.
- Y. Cabrera Casado, M. I. Cardoso Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González and I. Ruiz Campos. *Solenoids in automorphism groups of evolution algebras*. [arXiv:2505.14584v1](https://arxiv.org/abs/2505.14584v1), first posted 20 May 2025. Example 6.3.

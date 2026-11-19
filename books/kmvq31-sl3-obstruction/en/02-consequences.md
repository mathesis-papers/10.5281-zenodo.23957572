# Realizations, obstructions, and the boundaries between them

Unless a statement says otherwise, $k$ is algebraically closed of characteristic zero and $A$ is a finite-dimensional evolution algebra. The wider fields allowed by the orthogonal construction and by smoothness are stated explicitly.

## Build the orthogonal examples

The classification would be only a restriction if its permitted blocks never occurred. Here is an explicit construction, already present in the survey's Proposition 14 and Remark 15. Start with a nondegenerate symmetric pairing $b$ on $V$, adjoin one vector $u$, and define

$$
\begin{gathered}
E(b)=ku\oplus V,\qquad u^2=u,\\
uV=0,\qquad vw=b(v,w)u.
\end{gathered}
$$

A diagonal basis of $b$, together with $u$, is natural. For the standard form, all those basis vectors square to $u$. The opening two-dimensional example is the case $\dim V=1$.

::: {.corollary #orthogonal-realization title="Orthogonal realizations" mathesis="collected:kmvq31-sl3-obstruction:2:s6" status="written-proof" proof="pf-orthogonal-realization" doi="10.5281/zenodo.23957573" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/105"}
Every finite direct sum $\bigoplus_a\mathfrak{so}_{m_a}(k)$ with $m_a\ge3$ is the derivation algebra of an evolution algebra, including the empty sum. Together with the classification this answers exactly the semisimple clause of Question 36. More generally, over any field of characteristic different from two, every nondegenerate symmetric space $(V,b)$ has an evolution algebra $E(b)$ with full group scheme $\mathbf{Aut}(E(b))\cong O(b)$ and $\operatorname{Der}(E(b))\cong\mathfrak{so}(V,b)$.
:::


::: {.proof #pf-orthogonal-realization}
This is source Corollary 6, extending the earlier construction functorially. Over any commutative coefficient algebra $R$, $E(b)_R^2=Ru$. An automorphism therefore sends $u$ to $cu$, where $c$ is a unit. Since $u$ is idempotent, $c^2=c$, hence $c=1$. It preserves $V_R=\{x:xu=0\}$. Multiplication of two vectors in $V_R$ then says precisely that its restriction preserves $b_R$. Conversely any isometry extends by fixing $u$. These inverse correspondences commute with change of $R$, proving the group-scheme assertion, not just an assertion about field-valued points.

For derivations, $D(u)=D(u^2)=2uD(u)$ forces $D(u)=0$ by comparing the $ku$ and $V$ components. The equations for $uV=0$ force $D(V)\subseteq V$. Those for $vw=b(v,w)u$ give $b(Dv,w)+b(v,Dw)=0$. Conversely these conditions imply the product rule. Thus $\operatorname{Der}(E(b))\cong\mathfrak{so}(V,b)$. Nondegeneracy of $b$ also gives $\operatorname{Ann}(E(b))=0$.

Let $A_m$ denote this construction for the identity form of dimension $m$. Take $A=\bigoplus_a A_{m_a}$. A derivation cannot mix the summands: for $x$ in one and $y$ in another, projecting $D(x)y+xD(y)=0$ to the latter puts the corresponding component of $D(x)$ in that summand's zero annihilator. Therefore $\operatorname{Der}(A)=\bigoplus_a\operatorname{Der}(A_{m_a})$. The zero vector space gives the empty sum. In characteristic zero the algebras $\mathfrak{so}_m$ for $m\ge3$ are semisimple, including $\mathfrak{so}_4\cong\mathfrak{sl}_2\oplus\mathfrak{sl}_2$. This proves sufficiency as well as necessity.
:::

## Finish the eight-dimensional obstruction

::: {.proof #pf-sl3-obstruction}
We prove the headline theorem, source Theorem 1. First $\mathfrak{sl}_3(\mathbb C)$ is simple, hence semisimple. One direct argument uses $H=\operatorname{diag}(1,3,-4)$. Its six nonzero ordered diagonal differences are distinct. Polynomial projections in $\operatorname{ad}H$ isolate a nonzero off-diagonal coefficient of any ideal, giving a matrix unit $E_{ij}$. If a nonzero ideal initially supplies only a diagonal element, it is nonscalar because its trace is zero; a bracket with a suitable $E_{ij}$ produces an off-diagonal element. From $E_{ij}$, brackets with $E_{ji}$ give $E_{ii}-E_{jj}$ and then $E_{ji}$. Brackets with the remaining matrix units generate all off-diagonal units and diagonal differences, so the ideal is the whole algebra.

Its dimension is $3^2-1=8$. If it were $\operatorname{Der}(A)$, the classification would write eight as a sum of $m(m-1)/2$ with $m\ge3$. Each summand is nonnegative and at most eight, hence $m=3$ or $4$, contributing three or six. Their sum is divisible by three; eight is not. This proves the derivation obstruction with no assumption on $A^2$ or $\operatorname{Ann}(A)$.

For the group-scheme conclusion, the full automorphism functor on commutative unital $k$-algebras is $\mathbf{Aut}(A)(R)=\operatorname{Aut}_R(A\otimes_k R)$. Over the dual numbers $k[\epsilon]/(\epsilon^2)$, the kernel at the identity consists exactly of $I+\epsilon D$ satisfying the product rule. Multiplying tangent elements recovers addition; substitution $\epsilon\mapsto a\epsilon$ recovers scalar multiplication. Over $k[s,t]/(s^2,t^2)$, their commutator is $I+st[D,E]$. Thus a natural isomorphism of full automorphism functors induces a Lie isomorphism on derivations. For $\mathrm{SL}_3$, the identity $\det(I+\epsilon X)=1+\epsilon\operatorname{tr}X$ identifies that Lie algebra as $\mathfrak{sl}_3$. This is impossible by the first part.

Finally multiplication preservation defines a finite-type closed subgroup scheme of $\mathrm{GL}(A)$. Cartier's theorem makes it smooth in characteristic zero (Milne, *Algebraic Groups*, Theorem 3.23 and Corollary 11.31(a)). Its algebraic-group formulation has the same tangent Lie algebra, so it too cannot be $\mathrm{SL}_3$. An abstract isomorphism of groups of complex points supplies none of this tangent compatibility, and no abstract-group conclusion follows here.
:::

## Only two special linear Lie algebras survive

Dimension alone excluded $\mathfrak{sl}_3$. For the whole family we also compare **rank**, the dimension of a maximal toral subalgebra. These ranks are standard Lie-theoretic invariants, not ranks of individual matrices.

::: {.corollary #special-linear title="Special linear obstructions and Lie algebra exceptions" mathesis="collected:kmvq31-sl3-obstruction:2:s9" status="written-proof" proof="pf-special-linear" doi="10.5281/zenodo.23957573" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/108"}
Over an algebraically closed field of characteristic zero, $\operatorname{Der}(A)\cong\mathfrak{sl}_n$ with $n\ge2$ is possible exactly when $n=2,4$. Over $\mathbb C$, the full automorphism group scheme or algebraic group of an evolution algebra cannot be $\mathrm{SL}_n$ when $n=3$ or $n\ge5$.
:::


::: {.proof #pf-special-linear}
Source Corollary 9 uses simplicity of $\mathfrak{sl}_n$ for $n\ge2$. The classification forces it to be a single simple orthogonal factor $\mathfrak{so}_m$; $m=4$ is not simple and cannot occur. Compare ranks and dimensions:

$$
\begin{aligned}
\operatorname{rank}\mathfrak{sl}_n&=n-1,\\
\operatorname{rank}\mathfrak{so}_m&=\lfloor m/2\rfloor,\\
\dim\mathfrak{sl}_n&=n^2-1,\\
\dim\mathfrak{so}_m&=m(m-1)/2.
\end{aligned}
$$

If $m=2r+1$, rank equality gives $r=n-1$. Dimension equality, after dividing by $n-1\ne0$, gives $n+1=2n-1$, hence $n=2$. If $m=2r$, the same steps give $n+1=2n-3$, hence $n=4$. Conversely the classical identifications $\mathfrak{sl}_2\cong\mathfrak{so}_3$ and $\mathfrak{sl}_4\cong\mathfrak{so}_6$ (root systems $A_1=B_1$, $A_3=D_3$) and the orthogonal construction realize both. The dual-number argument works for every $n$, and Cartier smoothness supplies the algebraic-group comparison. This excludes the stated full groups. It does not positively realize $\mathrm{SL}_2$ or $\mathrm{SL}_4$ as full groups. The rank, dimension and classical identifications are standard results cited in Milne's *Lie Algebras, Algebraic Groups, and Lie Groups*, Chapter I, §8.
:::

## Two automorphisms, infinitely many natural coordinates

::: {.corollary #natural-bases title="Finite automorphisms and infinitely many natural bases" mathesis="collected:kmvq31-sl3-obstruction:2:s7" status="written-proof" proof="pf-natural-bases" doi="10.5281/zenodo.23957573" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/106"}
There is a two-dimensional nondegenerate complex evolution algebra with exactly two automorphisms and infinitely many natural bases modulo permutations and independent nonzero scalings. Dimension two is minimal. Here nondegenerate means zero annihilator.
:::


::: {.proof #pf-natural-bases}
Use $A=\mathbb C u\oplus\mathbb C e$ with $u^2=e^2=u$ and $ue=0$, as in source Corollary 7. The orthogonal construction gives zero annihilator and $\operatorname{Aut}(A)=O_1(\mathbb C)=\{1,-1\}$ on the $e$ coordinate, so there are exactly two automorphisms. For every positive integer $t$, put $v_t=u+te$ and $w_t=-tu+e$. Their mixed product is $-tu+tu=0$, and their coordinate determinant is $1+t^2\ne0$, so they form a natural basis.

Suppose the bases for $t$ and $s$ are related by independent nonzero scalings and a permutation. Without a swap, proportionality of $u+te$ and $u+se$ forces $t=s$ by their $u$ coefficients. With a swap, proportionality of $u+te$ and $-su+e$ forces $ts=-1$, impossible for positive integers. Thus all these basis classes are different. In dimensions zero and one all bases differ only by scaling (or there is only the empty basis), so two is minimal.
:::

The algebra and its group were already studied by Cardoso Gonçalves and collaborators (2018 preprint; 2021 publication, Lemma 3.15 and §5.1, $A_{8,1}$), and also by Calderón Martín and collaborators. Boudi–Cabrera Casado–Siles Molina study natural-family structure. The solenoid example of Cabrera Casado and collaborators has nonzero annihilator and an infinite group; the present conclusion treats the zero-annihilator, finite-group existence clause of Question 14, not its general classification or finiteness criteria.

## Remove the solvable part, rather than assuming it absent

The **radical** $\operatorname{rad}L$ is the largest solvable ideal. Passing to $L/\operatorname{rad}L$ removes that part; it does not require $L$ itself to be semisimple.

::: {.corollary #semisimple-quotient title="The orthogonal semisimple quotient and simple ideals" mathesis="collected:kmvq31-sl3-obstruction:2:s8" status="written-proof" proof="pf-semisimple-quotient" doi="10.5281/zenodo.23957573" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/107"}
Over an algebraically closed field of characteristic zero, if $\operatorname{Ann}(A)=0$ and $L=\operatorname{Der}(A)$, then $L/\operatorname{rad}L\cong\bigoplus_a\mathfrak{so}_{m_a}(k)$ with $m_a\ge3$. Every simple ideal of $L$ is an orthogonal simple Lie algebra. Neither $\mathfrak{sl}_3$ nor $\mathfrak g_2$ can be such an ideal, regardless of $\dim A^2$ and without assuming $L$ semisimple.
:::


::: {.proof #pf-semisimple-quotient}
This is source Corollary 8. With zero annihilator, all natural squares are nonzero and can be normalized in proportional-square blocks as before. The basis equations still give $D|_{V_a}=\lambda_a(D)I+X_a$ with $X_a$ skew, without assuming semisimplicity. Now $\lambda_a(D)=\operatorname{tr}(D|_{V_a})/\dim V_a$. Traces of commutators vanish, so $\lambda:L\to k^{\{a\}}$ is a Lie homomorphism to an abelian algebra. Its kernel $K$ is exactly the direct sum of the earlier pointwise stabilizers: zero diagonal scalars are equivalent to all $D(w_b)=0$, and the converse basis-equation calculation still applies.

Each stabilizer has the nilpotent kernel $N$ of the matrix argument and quotient $\mathfrak{so}_m$. For $m\ge3$ the quotient is semisimple, so $N$ equals the radical. For $m\le2$ the entire stabilizer is solvable. Hence $K/\operatorname{rad}K$ is the asserted orthogonal sum.

The radical of $K$ is characteristic, hence invariant under the derivations induced by $L$ and an ideal of $L$; it lies in $\operatorname{rad}L$. Conversely $K\cap\operatorname{rad}L$ is a solvable ideal of $K$, so $\operatorname{rad}K=K\cap\operatorname{rad}L$. The image of $K$ in $L/\operatorname{rad}L$ is therefore semisimple. The quotient by that image is abelian because $L/K$ is abelian, and is also semisimple as a quotient of a semisimple Lie algebra. It is zero. This proves the formula.

A simple ideal of $L$ meets its radical trivially, since that intersection is a solvable ideal in a simple nonabelian algebra. It injects as an ideal in the orthogonal sum. Ideals of a semisimple algebra are sums of simple factors. The only nonsimple $\mathfrak{so}_m$ for $m\ge3$ is $\mathfrak{so}_4\cong\mathfrak{so}_3\oplus\mathfrak{so}_3$. Thus a simple ideal is $\mathfrak{so}_m$ with $m=3$ or $m\ge5$. Neither eight nor fourteen is of the form $m(m-1)/2$, excluding $\mathfrak{sl}_3$ and $\mathfrak g_2$. The latter has rank two and twelve roots, hence dimension fourteen. The radical and ideal facts, and these standard root data, are cited in Milne's Lie theory notes, Chapter I, §§3–4, 7–8.
:::

## An ideal is more restrictive than an action

::: {.corollary #ideals-actions title="Annihilators, ideals, and faithful actions" mathesis="collected:kmvq31-sl3-obstruction:2:s10" status="written-proof" proof="pf-ideals-actions" doi="10.5281/zenodo.23957573" source="Corollary 10" request="https://github.com/the-omega-institute/trureturing-requests/issues/109"}
The zero-annihilator hypothesis in the semisimple-quotient result is essential. Moreover, absence of a simple ideal $\mathfrak{sl}_3$ does not exclude a faithful $\mathfrak{sl}_3$ action by derivations, even when $\operatorname{Ann}(A)=0$ and $\dim A^2>1$.
:::


::: {.proof #pf-ideals-actions}
For the first clause of source Corollary 10, use the zero-product algebra on $k^3$. Every linear map satisfies the product rule, so its derivation algebra is $\mathfrak{gl}_3$, containing the simple ideal $\mathfrak{sl}_3$. Its annihilator is all of $A$, showing why the earlier hypothesis matters.

For the second clause, take $V=k^3\oplus(k^3)^*$ with

$$
b((v,f),(w,g))=f(w)+g(v).
$$

This form is symmetric and nondegenerate. The injective Lie map $X\mapsto\operatorname{diag}(X,-X^t)$ takes $\mathfrak{sl}_3$ into $\mathfrak{so}(V,b)$: substituting into the form cancels the two terms. The orthogonal construction and its direct-sum argument give $A=E(b)\oplus k$, with the ordinary idempotent multiplication on $k$. Its annihilator is zero, $\dim A^2=2$, and $\operatorname{Der}(A)\cong\mathfrak{so}_6$ (the last summand has zero derivations). Thus $\mathfrak{sl}_3$ acts faithfully by derivations. It is a proper subalgebra, not an ideal, because $\mathfrak{so}_6$ is simple.
:::

## Smoothness is a prior theorem applied here

::: {.corollary #smoothness title="Smoothness in characteristic zero" mathesis="collected:kmvq31-sl3-obstruction:2:s11" status="written-proof" proof="pf-smoothness" doi="10.5281/zenodo.23957573" source="Corollary 11" request="https://github.com/the-omega-institute/trureturing-requests/issues/110"}
The full automorphism group scheme of every finite-dimensional algebra over a characteristic-zero field is smooth. Thus the smoothness clause of Question 37 has an affirmative answer in characteristic zero.
:::


::: {.proof #pf-smoothness}
As in source Corollary 11, write multiplication preservation as polynomial equations in the entries of an invertible linear map. They define a closed subgroup scheme of a finite general linear group, hence a group scheme of finite type. Cartier's characteristic-zero smoothness theorem applies (Milne, *Algebraic Groups*, Theorem 3.23 and Corollary 11.31(a)). This argument works for every finite-dimensional algebra; it needs neither an evolution basis nor algebraic closure. It says nothing here about positive characteristic, identity components or generation by exponentials.
:::

## What remains beyond these conclusions?

The survey's Question 31 has separate abstract-group, algebraic-group and group-scheme formulations. Only the latter two are refuted here. Question 36 is answered exactly in its semisimple clause; the nilpotent and solvable clauses are not answered. Question 14 receives the finite-group, zero-annihilator existence example in minimal dimension two; no general classification or finiteness criterion is claimed. For Question 37 only characteristic-zero smoothness is addressed. Questions 32–35 and 38, and other conjectures, are not resolved by this paper. In the perfect case $A^2=A$, the earlier result of Elduque–Labra gives $\operatorname{Der}(A)=0$ in characteristic zero, so it creates no additional nonzero semisimple possibilities.

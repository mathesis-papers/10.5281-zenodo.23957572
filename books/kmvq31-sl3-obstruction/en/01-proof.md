# Why orthogonal blocks appear

This chapter proves the structural result used in the opening story. Throughout it, $k$ is algebraically closed of characteristic zero, $A$ is a finite-dimensional evolution algebra, and $L=\operatorname{Der}(A)$. Algebraic closure lets us take square roots when normalizing a basis; characteristic zero lets us divide by positive integers and by two. These are hypotheses, not cosmetic choices.

For a first pass, follow the three steps: remove vectors that multiply everything to zero; group basis vectors with proportional squares; remove a nilpotent part of each resulting stabilizer. The formulas make those steps precise.

## A zero square would leave a forbidden ideal

Write $P=A^2$ for the span of all products and $Z=\operatorname{Ann}(A)=\{x:xA=0\}$. Thus $P$ measures what multiplication produces, whereas $Z$ measures what multiplication cannot detect. For a natural basis $(e_i)$,

$$
\left(\sum_i x_i e_i\right)e_j=x_j e_j^2.
$$

Consequently $Z$ is exactly the span of natural basis vectors whose squares are zero.

::: {.lemma #annihilator title="Semisimplicity removes the annihilator" mathesis="collected:kmvq31-sl3-obstruction:2:s2" status="written-proof" proof="pf-annihilator" doi="10.5281/zenodo.23957573" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/102"}
If $\operatorname{Der}(A)$ is semisimple, then $\operatorname{Ann}(A)=0$.
:::


::: {.proof #pf-annihilator}
This is the argument of source Lemma 2. Both $Z$ and $P$ are invariant under derivations: the product rule preserves $P$, and $zx=0$ gives $D(z)x=-zD(x)=0$ for $z\in Z$. Consider

$$
\begin{aligned}
J&=\{D\in\operatorname{End}(A):\\
 &\quad D(A)\subseteq Z,\ D(P)=0\}\\
 &\cong\operatorname{Hom}(A/P,Z).
\end{aligned}
$$

Every such map is a derivation because both sides of the product rule are zero. Invariance of $P$ and $Z$ makes $J$ an ideal of $L$. If $Z\subseteq P$, any composite of two maps in $J$ vanishes, so $J$ is abelian. If also $Z\ne0$ and $P\ne A$, the displayed Hom space is nonzero, contradicting semisimplicity.

If $Z\not\subseteq P$, choose $z\in Z\setminus P$ and a functional $\phi$ with $\phi(P)=0$ and $\phi(z)=1$. Then $D(x)=\phi(x)z$ lies in $J$ and has trace one on $Z$. But a semisimple Lie algebra is perfect, $L=[L,L]$, and the trace of every represented commutator is zero. Its representation on $Z$ therefore has trace zero for every element, another contradiction. We have proved $Z=0$ or $P=A$.

Finally, if $Z\ne0$, some natural basis square is zero. The space $P$ is then spanned by fewer than $\dim A$ nonzero squares, so $P\ne A$. This rules out the remaining possibility and proves $Z=0$.
:::

The trace fact used here is standard: nondegeneracy and invariance of the Killing form give $[L,L]^\perp=Z(L)=0$, hence perfectness. This concerns the center of the Lie algebra, not the annihilator $Z$ of our multiplication.

## Equal square directions force skew matrices

We can now group the basis by the lines $ke_i^2$. No square is zero. In a class $a$, choose a nonzero representative $w_a$ and rescale the basis vectors so that every square in the class is exactly $w_a$. Square roots exist in $k$. Give their span $V_a$ the symmetric form $b_a(e_i,e_j)=\delta_{ij}$.

For $D(e_j)=\sum_i d_{ij}e_i$, the product rule on $e_i e_j=0$ says

$$
d_{ji}e_j^2+d_{ij}e_i^2=0\quad(i\ne j).
$$

For different square lines, two nonproportional vectors are linearly independent, forcing both coefficients to vanish. Within one class, the equation becomes $d_{ji}=-d_{ij}$. This is the source of orthogonal geometry: opposite off-diagonal entries cancel because mixed products vanish.

::: {.lemma #square-blocks title="The square-block decomposition" mathesis="collected:kmvq31-sl3-obstruction:2:s3" status="written-proof" proof="pf-square-blocks" doi="10.5281/zenodo.23957573" source="Lemma 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/103"}
If $L=\operatorname{Der}(A)$ is semisimple, there are nondegenerate symmetric spaces $(V_a,b_a)$ and subspaces $W_a\subseteq V_a$ with $L\cong\bigoplus_a\{X\in\mathfrak{so}(V_a,b_a):XW_a=0\}$.
:::


::: {.proof #pf-square-blocks}
Continue the calculation, as in source Lemma 3. Each $V_a$ is invariant. From $D(w_a)=D(e_i^2)=2d_{ii}w_a$, its diagonal coefficients have one common value $\lambda_a$. Perfectness gives $\operatorname{tr}(D|_{V_a})=0$. This trace is $(\dim V_a)\lambda_a$, so $\lambda_a=0$. Thus $D|_{V_a}$ is skew and $D(w_a)=0$.

Let $\pi_a:A\to V_a$ be the block projection and set

$$
W_a=\operatorname{span}\{\pi_a(w_b):b\}.
$$

For block-diagonal $D$, the condition $D(w_b)=0$ for every $b$ is equivalent to $D|_{V_a}$ killing $W_a$ for every $a$. Conversely, take arbitrary skew operators on the $V_a$ killing these $W_a$. They satisfy the mixed-product equations, and the square equations read $D(e_i^2)=D(w_a)=0=2d_{ii}w_a$. These are all basis-product equations, hence the full product rule by bilinearity. Restriction and assembly are inverse Lie maps; distinct blocks commute. This proves the stated direct sum, not merely an inclusion in it.
:::

## A stabilizer has only an orthogonal part and a nilpotent part

A form is nondegenerate when a vector pairing to zero with every vector must itself be zero. Even when $b$ is nondegenerate on $V$, its restriction to $W$ may be degenerate. That is why simply writing “take the perpendicular complement of $W$” is not a sufficient proof.

::: {.lemma #stabilizer title="Semisimple pointwise stabilizers" mathesis="collected:kmvq31-sl3-obstruction:2:s4" status="written-proof" proof="pf-stabilizer" doi="10.5281/zenodo.23957573" source="Lemma 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/104"}
Let $(V,b)$ be a nondegenerate symmetric space. If its pointwise stabilizer $\mathfrak h=\{X\in\mathfrak{so}(V,b):XW=0\}$ is semisimple, then $\mathfrak h\cong\mathfrak{so}_m(k)$ for some $m\ge0$.
:::


::: {.proof #pf-stabilizer}
We give the matrix argument of source Lemma 4. Put $R=W\cap W^\perp$ and choose $W=W_0\oplus R$. The restricted form on $W_0$ is nondegenerate: a vector of $W_0$ perpendicular to $W_0$ is perpendicular to all of $W$, hence lies in $R$ and is zero. Operators in $\mathfrak h$ vanish on $W_0$ and preserve $U=W_0^\perp$.

In $U$ choose $U=R\oplus H\oplus R'$, where $R,R'$ are totally isotropic and dually paired, while $H$ is nondegenerate and perpendicular to both. To construct $R'$, first choose vectors dual to a basis of $R$, then subtract half their Gram matrix in the $R$ directions. Their new pairings with one another vanish. Take the orthogonal complement of $R\oplus R'$ as $H$.

Writing $r=\dim R$ and letting $B$ be the Gram matrix on $H$, the form and its pointwise-stabilizing skew operators have matrices

$$
G=\begin{pmatrix}0&0&I_r\\0&B&0\\I_r&0&0\end{pmatrix},
$$

$$
X=\begin{pmatrix}0&-P^tB&C\\0&T&P\\0&0&0\end{pmatrix},
$$

with $T^tB+BT=0$ and $C^t=-C$. These follow by solving $XR=0$ and $X^tG+GX=0$.

The projection $X\mapsto T$ is a surjective Lie homomorphism onto $\mathfrak{so}(H,b|_H)$, since any $T$ extends by zero. Its kernel $N$ has $T=0$. Multiplying these block matrices shows that a bracket of two kernel elements has only the $C$ block; this block commutes with every element of $N$. Thus $[N,[N,N]]=0$: $N$ is a nilpotent, hence solvable, ideal. Semisimplicity forces $N=0$. Finally diagonalize and rescale the nondegenerate symmetric form on $H$ over the algebraically closed field to obtain the identity form. For $m=\dim H$, this gives $\mathfrak h\cong\mathfrak{so}_m(k)$, including $m=0$.
:::

## The classification, including the zero case

::: {.theorem #classification title="The semisimple derivation classification" mathesis="collected:kmvq31-sl3-obstruction:2:s5" lean="D5/S3/QuadraticForms/EvolutionAlgebras/SemisimpleDerivationClassification.result"}
If $\operatorname{Der}(A)$ is semisimple, then $\operatorname{Der}(A)\cong\bigoplus_{a=1}^s\mathfrak{so}_{m_a}(k)$ with every $m_a\ge3$. The empty direct sum, giving the zero Lie algebra, is allowed.
:::


::: proof
Apply the square-block decomposition. Each factor is semisimple, since a solvable ideal in one factor would be a solvable ideal in the direct sum. The stabilizer argument identifies each factor with $\mathfrak{so}_m$. The cases $m=0,1$ give zero and can be omitted. The case $m=2$ is a nonzero one-dimensional abelian Lie algebra, so semisimplicity excludes it. Every remaining $m$ is at least three. If none remain, the sum is empty. This is source Theorem 5, proving Conjecture 5 of the survey; the cited Lean theorem has exactly these hypotheses and conclusion.
:::

The familiar three-dimensional algebra of infinitesimal rotations is one allowed block. The six-dimensional $\mathfrak{so}_4$ is also allowed, although it is not simple: it splits as two copies of $\mathfrak{sl}_2$. Semisimple is not the same as simple. The [realization construction](02-consequences.md#orthogonal-realization) supplies the converse and therefore the exact answer to the semisimple clause of the survey's Question 36.

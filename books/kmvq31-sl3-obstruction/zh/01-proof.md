# 为什么出现正交块

本章证明开篇使用的结构结论。全章设 $k$ 为特征零的代数闭域，$A$ 为有限维演化代数，$L=\operatorname{Der}(A)$。代数闭性让我们在规范化基时取平方根；特征零让我们除以正整数和二。这些都是证明假设。

初读时抓住三个步骤：去掉与所有元素相乘都为零的方向；把平方成比例的基向量归到一组；从每个稳定子中去掉幂零部分。下面用公式说明每一步。

## 零平方会产生不允许的理想

记 $P=A^2$ 为所有乘积的线性包，$Z=\operatorname{Ann}(A)=\{x:xA=0\}$。$P$ 衡量乘法能产生什么，$Z$ 衡量乘法无法探测什么。对自然基 $(e_i)$，有

$$
\left(\sum_i x_i e_i\right)e_j=x_j e_j^2.
$$

所以 $Z$ 恰好由平方为零的自然基向量张成。

::: {.lemma #annihilator title="半单性排除零化子" mathesis="collected:kmvq31-sl3-obstruction:2:s2" status="written-proof" proof="pf-annihilator" doi="10.5281/zenodo.23957573" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/102"}
若 $\operatorname{Der}(A)$ 半单，则 $\operatorname{Ann}(A)=0$。
:::


::: {.proof #pf-annihilator}
这是原文 Lemma 2 的论证。乘积法则说明 $P$ 在导子下不变；若 $z\in Z$，则 $D(z)x=-zD(x)=0$，所以 $Z$ 也不变。考虑

$$
\begin{aligned}
J&=\{D\in\operatorname{End}(A):\\
 &\quad D(A)\subseteq Z,\ D(P)=0\}\\
 &\cong\operatorname{Hom}(A/P,Z).
\end{aligned}
$$

每个这样的映射都满足乘积法则，因为两边全为零。由 $P,Z$ 的不变性，$J$ 是 $L$ 的理想。若 $Z\subseteq P$，任意两个 $J$ 中映射的复合为零，所以 $J$ 交换。若还有 $Z\ne0$、$P\ne A$，上述 Hom 空间非零，与半单性矛盾。

若 $Z\not\subseteq P$，取 $z\in Z\setminus P$，再取线性泛函 $\phi$ 使 $\phi(P)=0$、$\phi(z)=1$。映射 $D(x)=\phi(x)z$ 属于 $J$，且在 $Z$ 上的迹为一。但半单李代数是完美的，即 $L=[L,L]$；每个表示中交换子的迹都是零。因此 $L$ 在 $Z$ 上的表示中每个元素的迹都应为零，再次矛盾。至此得到 $Z=0$ 或 $P=A$。

最后，若 $Z\ne0$，就有一个自然基向量的平方为零。于是 $P$ 由少于 $\dim A$ 个非零平方张成，故 $P\ne A$。这排除了剩余情况，得到 $Z=0$。
:::

这里用到的迹性质是标准李理论：Killing 形式的不变性与非退化性给出 $[L,L]^\perp=Z(L)=0$，故 $L$ 完美。此处 $Z(L)$ 是李代数的中心，与乘法的零化子 $Z$ 不同。

## 相同的平方方向迫使矩阵反对称

现在可按直线 $ke_i^2$ 给基分组，且没有零平方。每组 $a$ 取非零代表 $w_a$，利用域中的平方根缩放各基向量，使组内每个平方都恰好等于 $w_a$。在该组的线性包 $V_a$ 上取对称形式 $b_a(e_i,e_j)=\delta_{ij}$。

写 $D(e_j)=\sum_i d_{ij}e_i$。将乘积法则用于 $e_ie_j=0$，得

$$
d_{ji}e_j^2+d_{ij}e_i^2=0\quad(i\ne j).
$$

不同组的两个平方不成比例，故线性无关，两个系数都为零。同组则得到 $d_{ji}=-d_{ij}$。这就是正交几何的来源：混合乘积为零，迫使相反位置的系数相消。

::: {.lemma #square-blocks title="平方块分解" mathesis="collected:kmvq31-sl3-obstruction:2:s3" status="written-proof" proof="pf-square-blocks" doi="10.5281/zenodo.23957573" source="Lemma 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/103"}
若 $L=\operatorname{Der}(A)$ 半单，则存在非退化对称空间 $(V_a,b_a)$ 与子空间 $W_a\subseteq V_a$，使 $L\cong\bigoplus_a\{X\in\mathfrak{so}(V_a,b_a):XW_a=0\}$。
:::


::: {.proof #pf-square-blocks}
继续原文 Lemma 3 的计算。每个 $V_a$ 都在 $D$ 下不变。等式 $D(w_a)=D(e_i^2)=2d_{ii}w_a$ 说明组内所有对角系数相同，记为 $\lambda_a$。由完美性，$\operatorname{tr}(D|_{V_a})=0$；而这个迹是 $(\dim V_a)\lambda_a$，故 $\lambda_a=0$。因此 $D|_{V_a}$ 反对称，且 $D(w_a)=0$。

设 $\pi_a:A\to V_a$ 为块投影，并置

$$
W_a=\operatorname{span}\{\pi_a(w_b):b\}.
$$

对块对角的 $D$，所有 $D(w_b)=0$ 当且仅当每个 $D|_{V_a}$ 都消去 $W_a$。反之，在每块上任取消去 $W_a$ 的反对称算子。它们满足混合乘积方程；平方方程则是 $D(e_i^2)=D(w_a)=0=2d_{ii}w_a$。这些就是全部基乘积方程，由双线性性推出完整乘积法则。限制与拼装互为逆李映射，不同块彼此交换。因此得到的是所述直和，而不仅是嵌入。
:::

## 稳定子只有正交部分与幂零部分

非退化表示：若向量与每个向量的配对都为零，它本身只能为零。即使 $b$ 在 $V$ 上非退化，它在 $W$ 上的限制仍可能退化。因此，只说“取 $W$ 的正交补”并不足以完成证明。

::: {.lemma #stabilizer title="半单逐点稳定子" mathesis="collected:kmvq31-sl3-obstruction:2:s4" status="written-proof" proof="pf-stabilizer" doi="10.5281/zenodo.23957573" source="Lemma 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/104"}
设 $(V,b)$ 为非退化对称空间。若逐点稳定子 $\mathfrak h=\{X\in\mathfrak{so}(V,b):XW=0\}$ 半单，则对某个 $m\ge0$ 有 $\mathfrak h\cong\mathfrak{so}_m(k)$。
:::


::: {.proof #pf-stabilizer}
采用原文 Lemma 4 的矩阵论证。令 $R=W\cap W^\perp$，选补空间 $W=W_0\oplus R$。$b$ 在 $W_0$ 上非退化：若 $W_0$ 中的向量与 $W_0$ 正交，它也与整个 $W$ 正交，因而在 $R$ 中，只能为零。$\mathfrak h$ 中的算子消去 $W_0$ 并保持 $U=W_0^\perp$。

在 $U$ 中选分解 $U=R\oplus H\oplus R'$，其中 $R,R'$ 全迷向且互为对偶，$H$ 非退化并与二者正交。构造时，先选与 $R$ 的基对偶的向量，再沿 $R$ 方向减去它们 Gram 矩阵的一半，使这些新向量彼此配对为零；其张成空间为 $R'$。取 $R\oplus R'$ 的正交补为 $H$。

令 $r=\dim R$，$B$ 为 $H$ 上的 Gram 矩阵。形式及逐点稳定的反对称算子在 $U$ 上分别为

$$
G=\begin{pmatrix}0&0&I_r\\0&B&0\\I_r&0&0\end{pmatrix},
$$

$$
X=\begin{pmatrix}0&-P^tB&C\\0&T&P\\0&0&0\end{pmatrix},
$$

其中 $T^tB+BT=0$、$C^t=-C$。直接解 $XR=0$ 与 $X^tG+GX=0$ 就得到这些条件。

投影 $X\mapsto T$ 是到 $\mathfrak{so}(H,b|_H)$ 的满李同态，因为每个 $T$ 都可延拓为其他位置为零的算子。其核 $N$ 满足 $T=0$。块矩阵相乘说明两个核元素的括号仅剩 $C$ 块，而该块与整个 $N$ 交换。因此 $[N,[N,N]]=0$，$N$ 是幂零、从而可解的理想。半单性迫使 $N=0$。最后在代数闭域上将 $H$ 的非退化对称形式对角化并缩放成单位形式。取 $m=\dim H$，得到 $\mathfrak h\cong\mathfrak{so}_m(k)$，包括 $m=0$。
:::

## 分类也包括零代数

::: {.theorem #classification title="半单导子分类" mathesis="collected:kmvq31-sl3-obstruction:2:s5" lean="D5/S3/QuadraticForms/EvolutionAlgebras/SemisimpleDerivationClassification.result"}
若 $\operatorname{Der}(A)$ 半单，则 $\operatorname{Der}(A)\cong\bigoplus_{a=1}^s\mathfrak{so}_{m_a}(k)$，每个 $m_a\ge3$。允许空直和，即零李代数。
:::


::: proof
应用平方块分解。每个因子都半单，因为任一因子中的可解理想也是整个直和的可解理想。稳定子论证将每个因子识别为 $\mathfrak{so}_m$。$m=0,1$ 时为零，可略去；$m=2$ 时为非零一维交换李代数，与半单性矛盾。因此余下所有 $m\ge3$。若没有余下因子，就得到空直和。这是原文 Theorem 5，证明综述的 Conjecture 5；所引 Lean 定理具有完全相同的假设与结论。
:::

熟悉的三维无穷小旋转代数是允许的一块。六维的 $\mathfrak{so}_4$ 也允许出现，尽管它并不简单，而是两个 $\mathfrak{sl}_2$ 的直和。半单与简单不是同一个概念。[正交实现构造](02-consequences.md#orthogonal-realization)给出逆向存在性，从而准确回答综述 Question 36 的半单部分。

# 实现、障碍，以及它们之间的边界

除非陈述另作说明，设 $k$ 为特征零的代数闭域，$A$ 为有限维演化代数。正交构造与光滑性结论允许更广的域，将在相应陈述中明确指出。

## 构造正交例子

若分类允许的块全都无法出现，那就只有限制而没有分类。下面是综述 Proposition 14 与 Remark 15 已有的明确构造。在带非退化对称配对 $b$ 的空间 $V$ 上添一个向量 $u$，规定

$$
\begin{gathered}
E(b)=ku\oplus V,\qquad u^2=u,\\
uV=0,\qquad vw=b(v,w)u.
\end{gathered}
$$

$b$ 的对角基连同 $u$ 构成自然基。标准形式下这些基向量的平方全是 $u$。开篇的二维例子正是 $\dim V=1$ 的情形。

::: {.corollary #orthogonal-realization title="正交实现" mathesis="collected:kmvq31-sl3-obstruction:2:s6" status="written-proof" proof="pf-orthogonal-realization" doi="10.5281/zenodo.23957573" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/105"}
每个有限直和 $\bigoplus_a\mathfrak{so}_{m_a}(k)$（$m_a\ge3$）都是某个演化代数的导子代数，包括空直和。因此分类准确回答 Question 36 的半单部分。更一般地，在任意特征不为二的域上，每个非退化对称空间 $(V,b)$ 都有演化代数 $E(b)$，满足全部群概形 $\mathbf{Aut}(E(b))\cong O(b)$ 与 $\operatorname{Der}(E(b))\cong\mathfrak{so}(V,b)$。
:::


::: {.proof #pf-orthogonal-realization}
这是原文 Corollary 6 对已有构造的函子性论证。在任意交换系数代数 $R$ 上，$E(b)_R^2=Ru$。自同构将 $u$ 送到 $cu$，其中 $c$ 可逆。由幂等关系得 $c^2=c$，所以 $c=1$。它保持 $V_R=\{x:xu=0\}$，而 $V_R$ 中两向量的乘法说明其限制恰好保持 $b_R$。反过来每个等距变换都可通过固定 $u$ 延拓。这两个对应互为逆且与更换 $R$ 相容，因此得到群概形结论，而不仅是域值点的结论。

对导子，由 $D(u)=D(u^2)=2uD(u)$，比较 $ku$ 与 $V$ 分量得 $D(u)=0$。$uV=0$ 的导子方程给出 $D(V)\subseteq V$。$vw=b(v,w)u$ 的方程则给出 $b(Dv,w)+b(v,Dw)=0$。反之这些条件保证完整乘积法则。因此 $\operatorname{Der}(E(b))\cong\mathfrak{so}(V,b)$。$b$ 非退化还保证 $\operatorname{Ann}(E(b))=0$。

记 $A_m$ 为 $m$ 维单位形式的构造，取 $A=\bigoplus_a A_{m_a}$。导子不能混合直和因子：若 $x,y$ 分属两因子，将 $D(x)y+xD(y)=0$ 投影到后一因子，发现 $D(x)$ 的相应分量在后一因子的零化子中，只能为零。因此 $\operatorname{Der}(A)=\bigoplus_a\operatorname{Der}(A_{m_a})$。零向量空间给出空直和。在特征零时，所有 $m\ge3$ 的 $\mathfrak{so}_m$ 都半单，包括 $\mathfrak{so}_4\cong\mathfrak{sl}_2\oplus\mathfrak{sl}_2$。这就同时证明了充分性与必要性。
:::

## 完成八维障碍的证明

::: {.proof #pf-sl3-obstruction}
证明主结论，即原文 Theorem 1。首先 $\mathfrak{sl}_3(\mathbb C)$ 简单，因而半单。一个直接证明取 $H=\operatorname{diag}(1,3,-4)$：其六个非零有序对角差各不相同。在 $\operatorname{ad}H$ 上取多项式投影，可以从理想中任一非零的非对角系数分离出矩阵单位 $E_{ij}$。若非零理想最初只给出对角元素，由迹为零可知它不是非零标量矩阵；与合适的 $E_{ij}$ 取括号便得到非对角元素。由 $E_{ij}$ 与 $E_{ji}$ 的括号得到 $E_{ii}-E_{jj}$，再得到 $E_{ji}$。继续与其余矩阵单位取括号，生成所有非对角单位和对角差，故理想是整个代数。

其维数为 $3^2-1=8$。若它是 $\operatorname{Der}(A)$，分类就将八写成若干 $m(m-1)/2$ 的和，每个 $m\ge3$。每项都非负且至多为八，所以只能有 $m=3,4$，贡献三或六。其和被三整除，而八不被三整除，矛盾。这个导子障碍不需要对 $A^2$ 或 $\operatorname{Ann}(A)$ 作任何额外假设。

对群概形结论，全部自同构函子在交换含幺 $k$-代数上为 $\mathbf{Aut}(A)(R)=\operatorname{Aut}_R(A\otimes_k R)$。在对偶数 $k[\epsilon]/(\epsilon^2)$ 上，单位元处的核恰由满足乘积法则的 $I+\epsilon D$ 组成。相乘切向元素恢复加法；代入 $\epsilon\mapsto a\epsilon$ 恢复数乘。在 $k[s,t]/(s^2,t^2)$ 上，其交换子为 $I+st[D,E]$。所以全部自同构函子的自然同构诱导导子间的李同构。对 $\mathrm{SL}_3$，由 $\det(I+\epsilon X)=1+\epsilon\operatorname{tr}X$，其切李代数为 $\mathfrak{sl}_3$，与前面矛盾。

最后，乘法保持方程定义 $\mathrm{GL}(A)$ 的有限型闭子群概形。由 Cartier 定理，它在特征零时光滑（Milne《Algebraic Groups》Theorem 3.23 与 Corollary 11.31(a)）。其代数群表述具有相同切李代数，因此也不能是 $\mathrm{SL}_3$。复点群之间的抽象同构不提供上述切结构相容性，所以这里没有抽象群结论。
:::

## 只有两个特殊线性李代数例外

维数已经排除 $\mathfrak{sl}_3$。对整个族，还比较**秩**，即极大环面子代数的维数。这是李代数的标准不变量，不是某个矩阵的秩。

::: {.corollary #special-linear title="特殊线性障碍与李代数例外" mathesis="collected:kmvq31-sl3-obstruction:2:s9" status="written-proof" proof="pf-special-linear" doi="10.5281/zenodo.23957573" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/108"}
在特征零的代数闭域上，对 $n\ge2$，$\operatorname{Der}(A)\cong\mathfrak{sl}_n$ 可以实现当且仅当 $n=2,4$。在 $\mathbb C$ 上，当 $n=3$ 或 $n\ge5$ 时，演化代数的全部自同构群概形或全部自同构代数群不能是 $\mathrm{SL}_n$。
:::


::: {.proof #pf-special-linear}
原文 Corollary 9 使用 $n\ge2$ 时 $\mathfrak{sl}_n$ 的简单性。分类迫使它等于单个简单正交因子 $\mathfrak{so}_m$；$m=4$ 不简单，不能出现。比较秩与维数：

$$
\begin{aligned}
\operatorname{rank}\mathfrak{sl}_n&=n-1,\\
\operatorname{rank}\mathfrak{so}_m&=\lfloor m/2\rfloor,\\
\dim\mathfrak{sl}_n&=n^2-1,\\
\dim\mathfrak{so}_m&=m(m-1)/2.
\end{aligned}
$$

若 $m=2r+1$，秩相等给出 $r=n-1$，维数相等后除以非零的 $n-1$，得到 $n+1=2n-1$，故 $n=2$。若 $m=2r$，同样得到 $n+1=2n-3$，故 $n=4$。反之，经典同构 $\mathfrak{sl}_2\cong\mathfrak{so}_3$、$\mathfrak{sl}_4\cong\mathfrak{so}_6$（根系 $A_1=B_1$、$A_3=D_3$）配合正交构造实现了二者。对偶数论证适用于每个 $n$，Cartier 光滑性给出代数群比较，于是排除所述全部群。但这并没有正面实现全部群 $\mathrm{SL}_2$ 或 $\mathrm{SL}_4$。秩、维数及经典同构见 Milne 的李理论讲义 Chapter I, §8。
:::

## 两个自同构，无穷多种自然坐标

::: {.corollary #natural-bases title="有限自同构与无限自然基" mathesis="collected:kmvq31-sl3-obstruction:2:s7" status="written-proof" proof="pf-natural-bases" doi="10.5281/zenodo.23957573" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/106"}
存在二维非退化复演化代数，恰好有两个自同构，但自然基模排列与独立非零缩放后仍有无穷多个等价类。二维是最小维数。这里非退化指零化子为零。
:::


::: {.proof #pf-natural-bases}
取开篇的 $A=\mathbb C u\oplus\mathbb C e$，其中 $u^2=e^2=u$、$ue=0$，即原文 Corollary 7。正交构造给出零化子为零，且 $\operatorname{Aut}(A)=O_1(\mathbb C)=\{1,-1\}$，作用于 $e$ 坐标，所以恰有两个自同构。对每个正整数 $t$，令 $v_t=u+te$、$w_t=-tu+e$。混合乘积为 $-tu+tu=0$，坐标行列式为 $1+t^2\ne0$，故构成自然基。

若参数 $t,s$ 对应的基经独立非零缩放与排列等价，不交换时，比较 $u+te$ 与 $u+se$ 的 $u$ 系数迫使 $t=s$；交换时，$u+te$ 与 $-su+e$ 成比例会迫使 $ts=-1$，对正整数不可能。所以所有这些基类互不相同。零维只有空基，一维所有基仅差缩放，因此二维最小。
:::

该代数与自同构群已有 Cardoso Gonçalves 等人的研究（2018年预印本，2021年发表，Lemma 3.15 与 §5.1 的 $A_{8,1}$），也见 Calderón Martín 等人的工作。Boudi、Cabrera Casado 与 Siles Molina 研究自然族结构。Cabrera Casado 等人的 solenoid 例子具有非零零化子及无限自同构群；这里处理的是 Question 14 中零化子为零、群有限的存在性部分，不是一般分类或有限性准则。

## 去掉可解部分，而不先假设它不存在

**根基** $\operatorname{rad}L$ 是最大的可解理想。取商 $L/\operatorname{rad}L$ 去掉这一部分，并不要求 $L$ 自身半单。

::: {.corollary #semisimple-quotient title="正交半单商与简单理想" mathesis="collected:kmvq31-sl3-obstruction:2:s8" status="written-proof" proof="pf-semisimple-quotient" doi="10.5281/zenodo.23957573" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/107"}
在特征零的代数闭域上，若 $\operatorname{Ann}(A)=0$，则 $L=\operatorname{Der}(A)$ 满足 $L/\operatorname{rad}L\cong\bigoplus_a\mathfrak{so}_{m_a}(k)$，其中 $m_a\ge3$。特别地，$L$ 的每个简单理想都是正交简单李代数；$\mathfrak{sl}_3$ 与 $\mathfrak g_2$ 都不能是这样的理想，无论 $\dim A^2$ 多大，也无需假设 $L$ 半单。
:::


::: {.proof #pf-semisimple-quotient}
这是原文 Corollary 8。零化子为零保证所有自然平方非零，可仍按比例平方块规范化。不假设半单，基方程仍给出 $D|_{V_a}=\lambda_a(D)I+X_a$，其中 $X_a$ 反对称。现在 $\lambda_a(D)=\operatorname{tr}(D|_{V_a})/\dim V_a$。交换子的迹为零，所以 $\lambda:L\to k^{\{a\}}$ 是到交换李代数的同态。其核 $K$ 恰好是先前逐点稳定子的直和：对角标量全零等价于所有 $D(w_b)=0$，逆向的基方程论证依然适用。

每个稳定子都有矩阵论证中的幂零核 $N$ 与商 $\mathfrak{so}_m$。当 $m\ge3$ 时商半单，故 $N$ 正是根基；当 $m\le2$ 时整个稳定子可解。因此 $K/\operatorname{rad}K$ 是所述正交直和。

$K$ 的根基是特征理想，在 $L$ 诱导的导子下不变，故是 $L$ 的理想并包含于 $\operatorname{rad}L$。反之，$K\cap\operatorname{rad}L$ 是 $K$ 的可解理想，因此 $\operatorname{rad}K=K\cap\operatorname{rad}L$。所以 $K$ 在 $L/\operatorname{rad}L$ 中的像半单。再对此像取商，所得既交换（因为 $L/K$ 交换）又半单（因为它是半单李代数的商），故为零。这证明所需公式。

$L$ 的简单理想与根基的交为零，否则交会是简单非交换李代数中的非零可解理想。它因而嵌入上述正交直和成为理想。半单代数的理想是简单因子的直和；$m\ge3$ 时唯一不简单的 $\mathfrak{so}_m$ 是 $\mathfrak{so}_4\cong\mathfrak{so}_3\oplus\mathfrak{so}_3$。因此简单理想是 $m=3$ 或 $m\ge5$ 的 $\mathfrak{so}_m$。八与十四都不是 $m(m-1)/2$，故排除 $\mathfrak{sl}_3$ 与 $\mathfrak g_2$；后者秩二且有十二个根，故维数十四。所用根基、理想性质及标准根系数据见 Milne 李理论讲义 Chapter I, §§3–4, 7–8。
:::

## 理想比作用要求更强

::: {.corollary #ideals-actions title="零化子、理想与忠实作用" mathesis="collected:kmvq31-sl3-obstruction:2:s10" status="written-proof" proof="pf-ideals-actions" doi="10.5281/zenodo.23957573" source="Corollary 10" request="https://github.com/the-omega-institute/trureturing-requests/issues/109"}
半单商结论的零化子为零假设不可去掉。而且，即使 $\operatorname{Ann}(A)=0$ 且 $\dim A^2>1$，没有简单理想 $\mathfrak{sl}_3$ 也不排除 $\mathfrak{sl}_3$ 通过导子忠实作用。
:::


::: {.proof #pf-ideals-actions}
原文 Corollary 10 的第一部分取 $k^3$ 上的零乘法代数。每个线性映射都满足乘积法则，所以导子代数为 $\mathfrak{gl}_3$，其中有简单理想 $\mathfrak{sl}_3$。其零化子是整个 $A$，说明前述假设不可去掉。

对第二部分，取 $V=k^3\oplus(k^3)^*$，配上

$$
b((v,f),(w,g))=f(w)+g(v).
$$

该形式对称且非退化。单射李映射 $X\mapsto\operatorname{diag}(X,-X^t)$ 将 $\mathfrak{sl}_3$ 嵌入 $\mathfrak{so}(V,b)$，因为代入配对后两项相消。正交构造及其直和论证给出 $A=E(b)\oplus k$，其中最后一个因子使用通常的幂等乘法。它的零化子为零，$\dim A^2=2$，并且 $\operatorname{Der}(A)\cong\mathfrak{so}_6$（最后因子的导子为零）。因此 $\mathfrak{sl}_3$ 通过导子忠实作用。但它是严格子代数而非理想，因为 $\mathfrak{so}_6$ 简单。
:::

## 光滑性是对先行定理的应用

::: {.corollary #smoothness title="特征零的光滑性" mathesis="collected:kmvq31-sl3-obstruction:2:s11" status="written-proof" proof="pf-smoothness" doi="10.5281/zenodo.23957573" source="Corollary 11" request="https://github.com/the-omega-institute/trureturing-requests/issues/110"}
任意特征零域上的每个有限维代数，其全部自同构群概形都是光滑的。因此 Question 37 的光滑性部分在特征零时有肯定答案。
:::


::: {.proof #pf-smoothness}
与原文 Corollary 11 一样，将可逆线性映射保持乘法的条件写成矩阵元的多项式方程。这定义有限一般线性群的闭子群概形，因而为有限型。应用 Cartier 的特征零光滑性定理（Milne《Algebraic Groups》Theorem 3.23 与 Corollary 11.31(a)）即可。此论证适用于每个有限维代数，不需要自然基，也不需要代数闭性。这里没有关于正特征、单位连通分支或指数生成的结论。
:::

## 哪些问题仍在结论之外？

综述 Question 31 分别询问抽象群、代数群与群概形；这里只否定后两种普遍实现。Question 36 只回答半单部分，不回答幂零与可解部分。Question 14 得到零化子为零、群有限且维数最小的存在性例子，而不是一般分类或有限性准则。Question 37 只涉及特征零光滑性。Questions 32–35 与 38 及其他猜想不由本文解决。在完美情形 $A^2=A$，Elduque–Labra 的先行结果在特征零给出 $\operatorname{Der}(A)=0$，不会增加非零半单的可能性。

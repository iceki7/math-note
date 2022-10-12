**奇异值分解**
$$
m>n,\\
A_{mn}=U_{mm}\Sigma_{mn}V^T_{nn}\\
=[\sigma_1 u_1,...,\sigma_n u_n]V^T_{nn}
=\sum_i^n \sigma_i u_i v_i^T
$$
U,V都是酉矩阵。在实数域下，则等同于正交矩阵。
方阵$A^TA$的特征向量就是$V$中的向量。

$\Sigma$除了对角线的元素(奇异值)都是0。
我们只保留最大的几个奇异值来压缩描述矩阵A。


**特征值分解**
方阵A，
$$
S=Q\Sigma Q^{-1}
$$

Q是A的特征向量组成的矩阵$\begin{bmatrix}
w_1 & ... & w_n
\end{bmatrix}$

Σ是一个对角阵，每一个对角线上的元素就是一个特征值。
这是因为：
$
A=Q\Sigma Q^{-1}\Leftrightarrow AQ=Q\Sigma\Leftrightarrow Av_i=\lambda_i v_i
$

让W标准化，即$||w_i||_2=1$后，$Q^{-1}=Q^T$

**矩阵变换**
对角方阵实现横纵方向的拉伸变换：$\Lambda \vec{v}=\vec{v}'$

**奇异值分解**
对矩阵$A_{mn}$，对矩阵$A^TA$做分解：$$A^TA=V\Sigma'_{nn}V^T$$
把$\Sigma'$拆分成$\Sigma^T\Sigma,\Sigma=\Sigma_{mn}$，则
$$A^TA=V\Sigma^T\Sigma V^T$$
对$AA^T$做分解得到的特征向量矩阵为$U_{mm}$，则
$A^TA=V\Sigma^TU^TU\Sigma V^T=(U\Sigma V^T)^TU\Sigma V^T$

由于$AA^T、A^TA$的非零特征值相同，因此
$AA^T=U\Sigma''_{mm} U^T=U\Sigma\Sigma^T U^T=U\Sigma V^T V\Sigma^T U^T=(V\Sigma^TU^T)^TV\Sigma^TU^T$

因此，$AA^T=BB^T,A^TA=B^TB$

**例**

$A=U\Sigma V^T$，因为V中列向量正交，对任意向量$\vec{x}$，存在$\vec{\zeta}$,
$\vec{x}=V\vec{\zeta}$
则$A\vec{x}=U\Sigma V^T V\vec{\zeta}$=$A\vec{x}=U\Sigma \vec{\zeta}=\sum \zeta_i \sigma_i \vec{u}_i$，即将它分解为了若干正交的向量。
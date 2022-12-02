



**特征值分解**
方阵$A$的n个特征向量$w$线性独立，则可做分解：
$$
A=Q\Sigma Q^{-1}
$$

$Q=\begin{bmatrix}
w_1 & ... & w_n
\end{bmatrix}$

Σ是对角阵，角上的元素是对应的特征值。
这是因为：
$
A=Q\Sigma Q^{-1}\Leftrightarrow AQ=Q\Sigma\Leftrightarrow Aw_i=\lambda_i w_i
$

如果$A^T=A$，正交化后，并使$||w||_2=1$，$Q^{-1}=Q^{T}$



**奇异值分解**

$$
m>n,\\
A_{mn}=U_{mm}\Sigma_{mn}V^T_{nn}\\
=[\sigma_1 u_1,...,\sigma_n u_n]V^T_{nn}
=\sum_i^n \sigma_i u_i v_i^T
$$
U,V都是正交矩阵。

$\Sigma$为对角阵，对角线上为奇异值。
通过丢弃奇异值来压缩/提取特征。


**SVD推导**
设$A^TAv=\lambda v,$则$(Av)^TAv=\lambda v^Tv$，令$|v|=1$，则$|Av|=\sqrt{\lambda}$

设$$u=\frac{Av}{\sqrt{\lambda}}$$

则$|u|=1$，因此
$$
AV=\begin{bmatrix}
    Av_1,Av_2,...
\end{bmatrix}=\begin{bmatrix}
    \sqrt{\lambda_1}u_1,\sqrt{\lambda_2}u_2...
\end{bmatrix}=U \Sigma
$$

特征值分解：
$A^TA=V \Sigma^T\Sigma V^T$
$A^TA^T=U \Sigma\Sigma^T U^T$
**例**

$A=U\Sigma V^T$
V中列向量正交，对n维向量$\vec{x}$，存在$\vec{\zeta}$,
$\vec{x}=V\vec{\zeta}$
则$A\vec{x}=U\Sigma V^T V\vec{\zeta}$=$A\vec{x}=U\Sigma \vec{\zeta}=\sum \zeta_i \sigma_i \vec{u}_i$，即将它分解为了若干正交的向量。

**Polar Decomposition**
矩阵A的极分解；
$A=SQ$,$S$是对称阵,$Q$是正交阵

右极分解:$A=U\Sigma V^T=(UV^T)(V\Sigma V^T)=QS$

力学应用：物体的变形梯度$F=RU$,对称阵$U$表征变形（stretch），正交阵$R$表征旋转(rotation)。
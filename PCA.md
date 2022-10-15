**MDS**
给定数据样本：$$X_{d\times n}=\begin{bmatrix}
    x_1,...x_n
\end{bmatrix}$$

将它压缩到低维：$Z=W^TX$
W中是基向量，且W列向量正交。
X与基向量做点积，可以得到X在新的坐标系中的坐标。

**PCA**
PCA要让样本的投影最大可分(最近重构)，
即最大化d个特征的方差之和。
假设数据已经中心化，即$\sum x=\vec{0}$，则对$x$中任意一个特征k，k的方差为$$\frac{1}{n}\sum^n k^2$$
投影后协方差为矩阵为$ZZ^T$,因此目标为：
$$
\max_W tr(ZZ^T),s.t. W^TW=I
$$

**求解**
对上式使用拉格朗日乘子法:$$XX^Tw_i=\lambda_i w_i$$
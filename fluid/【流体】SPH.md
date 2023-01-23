**material  derivative**
$$
\frac{D A^E}{D t}=\frac{\partial A^E}{\partial t}+\mathbf{v} \cdot \nabla_{\mathbf{x}} A^E \quad(对流项) \text { and } \quad \frac{D A^L}{D t}=\frac{\partial A^L}{\partial t} \text {. }
$$




$$
\frac{DA}{D t}=\frac{\partial A}{\partial t}+\frac{\partial A}{\partial x}\frac{dx}{dt}+...=\frac{\partial A}{\partial t}+\nabla A \cdot \mathbf{v}
$$


**2 motion eq.**


$$
\rho \frac{D \mathbf{v}}{D t}=\nabla \cdot \mathbf{T}+\mathbf{f}_{\mathrm{ext}}
$$
**3 constitutive relation for incomp. flow**
$$
T=-p\mathbb{I} + \mu(\nabla\mathbf{v} + (\nabla\mathbf{v})^T )
$$

2 3 推导出NS：

$$
\rho \frac{Dv}{Dt}=\mathbf{f}_{ext}+\mu \nabla^2 \mathbf{v}-\nabla p
$$


**continuity eq.**


$$
\frac{D\rho}{Dt}=-\rho(\nabla \cdot \mathbf{v})
$$
---
非压力加速度带来密度偏差（连续性方程）。

用压力加速度抵消。

两种方法：解PPE/状态方程。带来的压缩性不同。

显式计算体积(密度)偏差：核函数计算，过度修正导致oscillation

隐式：计算$\rho^*-\rho_0$，volume drift

---



**State eq.**

弱（可）压缩，$p(\rho)$
用密度偏差控制压力大小。


**PPE**

不可压缩

$a^p$引起的密度变化与$a^{nonp}$引起的密度变化相等：
$$
\Rightarrow \nabla^2 p \Delta t=\frac{\rho_0-\rho^*}{\Delta t}
$$

$$\mathbf{v}^*=\mathbf{v}+a^{nonp}\Delta t $$
$$\rho^*=\rho-\rho(\nabla \cdot \mathbf{v}^*)$$


**Pressure Solver**

显式计算体积(密度)偏差：过度修正，oscillation
隐式：volume drift

压力求解：State eq. / PPE



**Implicit Incomp. SPH**

基于PPE的思路，隐式求解$p$。


---
离散化

**kernel**

$$
A(\mathbf{x_i})=\sum_j A_j\frac{m_j}{\rho_j}W(\mathbf{x_i}-\mathbf{x_j},h)
$$



差分、对称形式

---
具体方法

---
**viscosity**

---
**boundary**





HC:
$$p=k(\rho-\rho_0)$$
WC(tait eq):
$$p=\frac{\kappa \rho_0}{\gamma}((\frac{\rho}{\rho_0})^\gamma-1)$$



**粘性力计算**
显式：direct SPH($\nabla^2 \vec{v}$)；SPH确定一阶导，有限元方法确定二阶导；XSPH、SE、II、PCISPH、DFSPH。
隐式：$\nabla \cdot E$(需速度场无散度，避免bulk viscosity)

**边界**
n是边界法向量，在边界上：
$$
\vec{v}\cdot \vec{n}\geq 0
$$
用固体粒子描述。
若在边界流体粒子的核半径内，贡献$p$和$\rho$。
固体粒子的$p$：mirroring




**邻域搜索**
假设邻域内的平均粒子数。
划分网格。保存每个粒子所在的网格。只计算相邻网格内的粒子（存储空网格的空间）


TODODO
Continuum Theorem + 欧拉假设 + 斯托克斯假设

bulk viscosity
sheer viscosity

核函数的展开不具有左右侧连续性，会产生误差：

欧拉法：水中的立柱，测量同一个空间位置上的点的情况。
粒子法：追踪parcel。


**Weakly Compressible SPH**
直接的显式求解。
允许用户定义的小密度波动($\frac{d\rho}{dt}$)，而不是严格执行不可压缩性，以节省求解泊松方程的时间。
根据$\rho$误差计算$p$(tait eq)


*要设定状态方程中的压力常数$k$，$k$过小流体压缩性会变大，过大会限制计算步长*



**PCISPH**（predictive-corrective incompressible）
压力是通过持续校正而非解决PPE获得的

*预测矫正循环*
根据$p$预测粒子的$v$和$x$;
更新$\rho$:$\frac{d\rho}{dt}=\sum_j m_j \mathbf{v_{ij}}\nabla W $
计算$\rho$误差，矫正$p$以控制$\rho$偏差在threshold内，以控制不可压缩性，重复。

*比WCSPH更大的时间步长。*
*允许像WCSPH这样的小密度波动。*

<!-- ![pic](WCSPH_PCISPH.png) -->

**implicit incompressible SPH(IISPH)**
隐式方法。求解$\rho$恒定、未知量为$p$的线性方程组.
relaxed Jacobi方法求解。

<!-- ![pic](IISPH_alg.png) -->

**DFSPH（divergence-free）**
恒定密度+速度无散
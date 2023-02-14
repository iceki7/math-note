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
\rho \frac{Dv}{Dt}=\mathbf{f}_{ext}+\mu \nabla^2 \mathbf{v}-\nabla p[\rho a]
$$


**continuity eq.**


$$
\frac{D\rho}{Dt}=-\rho(\nabla \cdot \mathbf{v})
$$
---





---

不可压缩对于真实流体模拟至关重要。不适当的压缩会导致如体积振荡或体积损失。

【不可压缩】用【密度恒定】来衡量，即减小【Δρ】

用p矫正nonp产生的【Δρ】

【求解Δρ】：可以通过密度显式计算/速度散度计算体积偏差的微分。显式计算体积(密度)偏差：核函数计算，过度修正导致oscillation；隐式：计算$D\rho /Dt$，continuity eq.,volume drift



【求解p】：通过state eq.局部计算/PPE全局计算。

---
**State eq.**



弱（可）压缩，$p(\rho)$
用密度偏差控制压力大小。

WC:tait eq.

---
**PPE**

不可压缩

$a^p$引起的密度变化与$a^{nonp}$引起的密度变化相等，continuity eq.：
$$
\Rightarrow \nabla^2 p \Delta t=\frac{\rho_0-\rho^*}{\Delta t}
$$
两种矫正方式：矫正密度，和矫正密度偏差，
例如1000→1001→1000
和1→0→1

$$\mathbf{v}^*=\mathbf{v}+a^{nonp}\Delta t $$
$$\rho^*=\rho-\rho(\nabla \cdot \mathbf{v}^*)$$
vel-div source term形式的PPE：
$$
\nabla^2 p \Delta t^2=\Delta t\rho_0 \nabla \cdot \mathbf{v}^*
$$
IISPH方法使用松弛雅各比法迭代求解压力泊松方程。

隐式求解：$Mp=\Delta \rho$


**Pressure Solver**

显式计算体积(密度)偏差：过度修正，oscillation（即1000→1001→1000）
微分形式：volume drift
（即1→0→1）

如果压力加速度是从密度偏差的显式形式导出的，则流体体积会由于压力加速度的过度矫正而振荡，这些振荡必须最小化，至少是不可感知的(综述)。如果是使用微分形式计算密度偏差，那么会导致流体体积的漂移，通常是体积损失，需要最小化体积漂移。




**Implicit Incomp. SPH**

基于PPE的思路，隐式求解$p$。


---
离散化

**kernel**

$$
A(\mathbf{x_i})=\sum_j A_j\frac{m_j}{\rho_j}W(\mathbf{x_i}-\mathbf{x_j},h)
$$


$$
\nabla A_i \approx\left\langle\nabla A_i\right\rangle-A_i\langle\nabla 1\rangle=\sum_j \frac{m_j}{\rho_j}\left(A_j-A_i\right) \nabla_i W_{i j}
$$

$$
\begin{aligned}
\nabla A_i & \approx \rho_i\left(\frac{A_i}{\rho_i^2}\langle\nabla \rho\rangle+\left\langle\nabla\left(\frac{A_i}{\rho_i}\right)\right\rangle\right) \\
& =\rho_i \sum_j m_j\left(\frac{A_i}{\rho_i^2}+\frac{A_j}{\rho_j^2}\right) \nabla_i W_{i j} .
\end{aligned}
$$

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
**物质导数**
$$
\frac{DA}{D t}=\frac{\partial A}{\partial t}+\frac{\partial A}{\partial x}\frac{dx}{dt}+...=\frac{\partial A}{\partial t}+\mathbf{v}\cdot \nabla A
$$
在拉格朗日法下，由于相当于追踪某个物质微元，因此式子退化为：$$\frac{D A}{Dt}=\frac{\partial A}{\partial t}$$

**Linear Momentum Conservation**
牛二在连续体上的推广。material-independenth
T是应力张量，f是力密度.
$$
\rho\frac{D\vec{v}}{Dt}=\nabla\cdot T+\vec{f}
$$
**Fluid Stress Tensor**
$$
T=-p\mathbb{I} +2 \mu E=-p\mathbb{I} + \mu(\nabla\vec{v} + \nabla\vec{v}^T )
$$
E：应变率张量。p衡量抗压缩性。
以上可得出NS方程。


**continuity equation**
物体密度随时间的变化。不可压缩流体该项为零.
$$
\frac{D\rho}{Dt}=-\rho(\nabla \cdot \mathbf{v})
$$

**Pressure Poission Eq.**
从momentum equation and continuity equation推出
描述$p$和$\rho$的关系：
Incompressible:
$$\nabla^2 p=\rho\frac{\nabla \cdot \mathbf{v}}{\Delta t}
$$
HC:
$$p=k(\rho-\rho_0)$$
WC(tait eq):
$$p=\frac{\kappa \rho_0}{\gamma}((\frac{\rho}{\rho_0})^\gamma-1)$$
**NS方程**
描述不可压缩牛顿流体
$$
\rho\frac{D\mathbf{v}}{Dt}=\rho(\frac{\partial \mathbf{v}}{\partial t}+\mathbf{v}\cdot \nabla\mathbf{v})=\mathbf{g}-\nabla p+\mu \nabla^2 \mathbf{v}
$$

$\rho$是密度。
p是压力。
SESPH：state equation计算：$p=k(\rho-\rho_0)$，密度差（适用于可压缩流体）。
$\mu$是动力粘度。

最后一项是不可压缩流体的粘性力。


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

**kernel**
对Dirac-$\delta$的近似。
$$
A(\mathbf{x_i})=\sum_j A_j\frac{m_j}{\rho_j}W(\mathbf{x_i}-\mathbf{x_j})
$$

差分形式、对称形式
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
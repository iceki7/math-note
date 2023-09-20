


**gradient**
$$
\nabla  p=
(
  p_x, p_y, p_z )

$$
显然，函数极值点处 $\nabla f=\vec{0}$，但反过来则不然，该点有可能是鞍点，因此还需要雅可比矩阵和海森矩阵用于判断。

**divergence**
$$
\nabla \cdot \bold{v}=u_x+v_y+w_z
$$

$$
\nabla \cdot (k\mathbb{I})=\nabla k
$$

**旋度**

向量场$\vec{F}(x,y,z)=(a,b,c)$
$$
\nabla \times (a,b,c)=\begin{vmatrix}
 \vec{i} & \vec{j} &\vec{k} \\ 
 \frac{\partial }{\partial x} &\frac{\partial }{\partial y} &\frac{\partial }{\partial z}
  \\ a&b&c \end{vmatrix}
$$
**Laplace operator**
$$
\nabla^2 f=\nabla\cdot (\nabla f)
$$
如果是标量，拉普拉斯运算后仍然是标量。

其他规则：
$$
\nabla (uv)=u\nabla v+v \nabla u \\
\nabla \cdot (\nabla \times \vec{F})=0
$$


---

如果变量不是解析的，而是一些统计量，还能不能求梯度呢？
当然我们知道对一个完全随机分布的数据，求出梯度也没有意义。

所以不妨假设这里的数据虽然没有解析式，仍然可以认为是某种意义上连续的。
比如说，假设数据一个二维的标量场，在一个足够小的区域内是单调的。

另一个思路是对数据进行插值得到解析式。
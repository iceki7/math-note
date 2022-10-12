$$
\nabla=(\frac{\partial }{\partial x},\frac{\partial }{\partial y},...) 
$$

**梯度**
$$
\nabla f(x,y)=(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y})
$$

显然，函数极值点处 $\nabla f=\vec{0}$，但反过来则不然，该点有可能是鞍点，因此还需要雅可比矩阵和海森矩阵用于判断。

**散度**
$$
\nabla \cdot \vec{F}(x,y)=\frac{\partial {F_x}}{\partial x}+\frac{\partial {F_y}}{\partial y}
$$

**旋度**
就是叉积.
$$
\nabla \times \vec{F}(x,y,z)=\begin{vmatrix}
 \vec{i} & \vec{j} &\vec{k} \\ 
 \frac{\partial }{\partial x} &\frac{\partial }{\partial y} &\frac{\partial }{\partial z}
  \\ F_x & F_y & F_z \end{vmatrix}
$$
**Laplace算子**
$$
\nabla\cdot (\nabla f)=\nabla^2 f
$$
场的二阶偏导的和，可以是向量场。




$$
a\times b=ab^T
$$
$$
\nabla=(\frac{\partial }{\partial x},\frac{\partial }{\partial y},...) 
$$

**梯度**
$$
\nabla  \begin{bmatrix}
  u \\
  v \\
  w \\
\end{bmatrix}=
 \begin{bmatrix}
  u_x & u_y & u_z \\ 
  v_x & v_y & v_z \\ 
  w_x & w_y & w_z \\ 
\end{bmatrix}

$$
显然，函数极值点处 $\nabla f=\vec{0}$，但反过来则不然，该点有可能是鞍点，因此还需要雅可比矩阵和海森矩阵用于判断。

**散度**
$$
\nabla \cdot \begin{bmatrix}
  u \\
  v \\
  w \\
\end{bmatrix}=u_x+v_y+w_z
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
**Laplace算子**
$$
\nabla^2 f=\nabla\cdot (\nabla f)=
\nabla \cdot \begin{bmatrix}
  u_x & u_y & u_z \\ 
  v_x & v_y & v_z \\ 
  w_x & w_y & w_z \\ 
\end{bmatrix}=
 \begin{bmatrix}
  u_{xx} + u_{yy} + u_{zz} \\ 
v_{xx} + v_{yy} + v_{zz} \\ 
w_{xx} + w_{yy} + w_{zz} \\ 
\end{bmatrix}
$$

其他规则：
$$
\nabla (uv)=u\nabla v+v \nabla u \\
\nabla \cdot (\nabla \times \vec{F})=0
$$


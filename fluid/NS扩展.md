PINN 


3D-NS扩展：

$$
\rho(\mathbf{v}_t+\nabla \mathbf{v}\cdot \mathbf{v})=f_{ext}+\mu \nabla^2 \mathbf{v}-\nabla p\\
\begin{aligned}
\rho(u_t+(u u_x+v u_y+wu_z)) & =0+\mu\left(u_{x x}+u_{y y}+u_{zz}\right)-p_x \\
\rho(v_t+\left(u v_x+v v_y+wv_z\right)) & =g+\mu\left(v_{x x}+v_{y y}+v_{zz}\right)-p_y \\
\rho(w_t+\left(u w_x+v w_y+ww_z\right)) & =0+\mu\left(w_{x x}+w_{y y}+w_{zz}\right)-p_z \\

\end{aligned}





$$

不考虑粘度，增加重力后的修正公式:
$$
...=-g-p_x
$$
Divergence-free：

$$
\nabla \cdot \mathbf{v}=0\\
u_x+v_y+w_z=0
$$

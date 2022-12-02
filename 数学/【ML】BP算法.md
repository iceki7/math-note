在MLP上，输出误差是参数k的函数。

$$
E=f_x(k)
$$
x是样本集，E是样本集的平均误差。
因此，让f在E的负梯度方向上移动，即可降低平均误差。
$$
E=\frac{1}{m}\sum_s^m (\vec{\hat{y}}_s-\vec{y}_s)
$$
假设网络有2层，
$$
f(W\vec{z}-\vec{\theta})=\vec{\hat{y}}\\
f(V\vec{x}-\vec{\gamma})=\vec{\hat{z}}
$$
调整W：
$$
\frac{\partial E}{\partial w_{pq}}=\frac{\partial \frac{1}{m}\sum_s\sum_i(f(\sum_j z_{sj}w_{ji}-{\theta}_i)-y_i)^2}{w_{pq}}\\
=\frac{1}{m}\sum_s(\sum_i(f-y_i)^2)' 
=\frac{1}{m}\sum_s(\sum_i(f^2)'-2(fy_i)')\\
=\frac{2}{m}\sum_s f'(f-y_i)
$$
令:$f=sigmoid(x),则f'=f(1-f)$
因此，
$$
\frac{\partial E}{\partial w_{pq}}=\frac{2}{m}\sum_s f(1-f)(f-y_i)
$$
其中$f=f(z_{sp}w_{pq}-\theta_q)$

类似地，可求出 $\frac{\partial E}{\partial \theta_{p}},\frac{\partial E}{\partial v_{pq}}$等。

最后参数：$k+=-\eta \nabla E$。
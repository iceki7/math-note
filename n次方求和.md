知乎上看到的一个方法：

zhihu.com/question/369313777/answer/998250791

觉得很有意思，用自己的语言重新写一下。

设：
$$
f(k,n)=\sum_{i=0}^n  i^k,n\geq 0,k\geq 1
$$
则：
$$
f(k,n+1)=f(k,n)+(n+1)^k\quad(*)
$$


假设$f(k,n)$其实是一个关于n的初等函数 $g(k,n)$ $ 在n取整数时的特例，而g就是我们要得到的通项公式。

假设$g(k,n)$关于n可导，
​
则$k\geq 2$时，
$$
\frac{\partial g(k,n)}{\partial n}=\frac{\partial g(k,n-1)}{\partial n}+kn^{k-1}
\\ . \\
=\frac{\partial g(k,n-2)}{\partial n}+k(n-1)^{k-1}+kn^{k-1}
$$
n取多少，就将以上过程重复多少次，之后：
$$
=...=\frac{\partial g(k,n)}{\partial n}|_{n=0}+k(1^{k-1}+2^{k-1}+...+n^{k-1})
\\
=c(k)+kg(k-1,n)
$$
​其中，c(k)是$g(k,n)$对n的导数在n=0处的值.

​因此，
$$
\large g(k,n)=nc(k)+\int_0^n kg(k-1,x)dx+C
$$
分别取n=0，n=1，得到：
$$
g(k,n)=n\cdot (1-\int^1_0kg(k-1,x)dx)+\int_0^n kg(k-1,x)dx
$$
在$k\geq 2$时成立。
​
进行验证。我们已经知道g(1,n)存在：
$$
g(1,n)=\frac{n^2}{2}+\frac{n}{2}
$$

因此，
$$
g(2,n)=\int_0^nx^2+xdx+n(1-\int_0^1x^2+xdx)=\frac{n^3}{3}+\frac{n^2}{2}+\frac{n}{6}
$$

​
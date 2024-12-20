思路1


平方和公式。
是二维的类加，可以换一个方向去给它“切丝”：
$$
\sum i^2
\\=n+(2*2-1)(n-1)+(2*3-1)(n-2)+...(2*n-1)*1
$$
这是两个等差数列的积数列求和。

积数列：$(a+ix)(b+iy)=ab+ay i+bx i +iixy，其中a=1 , x=2 ,b=n , y= -1$
	
所以，积数列是一个等差数列 + iixy，如果对它求和，后者又是一个平方和
所以：
$$
\sum_{i=1}^n i^2 = (n+ (n+(n-1)(-1+2n))n/2 +(-2) \sum_{0}^{n-1}i^2
\\=...+(-2)\sum_{i=1}^n i^2 +2n^2

\\ \Rightarrow \sum_{i=1}^n i^2=(2n^3+3n^2+n)/6=n(n+1)(2n+1)/6
$$




或者一个卷积。
F= Σ_i (2*i-1)(n+1-i)


思考1：在整除视角下来看，它永远是个整数，探究原因

由于考虑到推广到别的式子时它不一定能因式分解，因此这里不展开了


首先$n^3\equiv n \mod 6$是显然的，因为$n^3-n=n(n+1)(n-1)$


$$
2n^3+3n^2+n\equiv 3n+3n^2=3n(n+1)\equiv 0 \mod 6
$$

---

知乎上看到的一个方法：

zhihu.com/question/369313777/answer/998250791

觉得很有意思，用自己的语言重新写一下。

设：
$$
f_k(n)=\sum_{i=0}^n  i^k,n\geq 0,k\geq 1
$$
则：
$$
f_k(n+1)=f_k(n)+(n+1)^k\quad(*)
$$


假设$f_k(n)$其实是一个初等函数$g_k(n)$ 在n取整数时的特例，而g就是我们要得到的通项公式。注意，虽然我们连g存不存在都不知道，但是我们仍然可以利用解方程的一般思想——先假设它存在，然后推断下去，最起码得到g如果存在则必须满足的一些性质。




假设$g_k(n)$关于n可导，则
$$
g_k'(n)= g_k'(n-1)+kn^{k-1}
\\ . \\
= g_k'(n-2)+k(n-1)^{k-1}+kn^{k-1}
$$
n取多少，就将以上过程重复多少次，之后：
$$
=...= g_k'(0)+k(1^{k-1}+...+n^{k-1})
\\
=g_k'(0)+kg_{k-1}(n)
$$


​因此，
$$
 g_k(n)=ng_k'(0)+k\int_0^n g_{k-1}(x)dx+C
$$
分别取n=0，n=1，得到：
$$
g_k(n)=n\cdot (1-k\int^1_0 g_{k-1}(x)dx)+k\int_0^n g_{k-1}(x)dx
$$

进行验证。我们已经知道$g_1(n)$存在：
$$
g_1(n)=\frac{n^2}{2}+\frac{n}{2}
$$

为方便，把多项式简写为向量的形式，则：
$$
g_2(n)=[\frac{1}{3},\frac{1}{2},\frac{1}{6},0]
\\-
\\g_3(n)=[\frac{1}{4},\frac{1}{2},\frac{1}{4},0,0]
\\-
\\
g_4(n)=[\frac{1}{5},\frac{1}{2},\frac{1}{3},0,\frac{-1}{30},0]
$$

---

如果直接去算x^k的积分：

$$
s=\frac{D}{n}\sum_{i=0}^{n-1} (id)^k,nd=D，D是常数
\\ \lim_n s=D^{k+1}\lim \frac{g(k,n-1)}{n^{k+1}}=\int_0^D x^kdx=D^{k+1}/k+1
\\ \lim \frac{g(k,n-1)}{n^k}=\frac{1}{k+1}
$$

---
**思考1**

​值得注意的是，对g求导的时候，$g(n)=g(0)+1^k+2^k+...+n^k$，右边的项的【个数】是和n有关系的，是一个类似级数的形式。这种情况下还能不能直接求导，其实有点疑问。

但是，我们其实假设了g(n)是初等函数的表达式的，所以$g(n)=g(n-2)+(n-1)^k+n^k$
等式左右两边是两个等价的函数（但需要约定$n\geq2$），当然可以同时对它们求导得到两个等价的导函数。我们的疑问其实在于，右边导函数有几项，这和$n$的取值也有关系。换句话说，g的公式能不能用取决于我们对于前多少项进行求和。

---
**思考2**

这些多项式在n为整数时，也都是整数。
比如

$30|6n^5+15n^4+10n^3-n$

---
**思考3**

都写成向量以后忽然有个想法

既然求导在希尔伯特空间里也就是一个线性变换，那么，这里的递推公式也是一个线性变换。既然如此，就可以把它的矩阵写出来
能不能找到什么更深层的规律？因为这个积分式实在有点丑 看不出啥


在希尔伯特空间的视角下重写上述的递推式子。
把一些基本的运算的线性变换形式表示出来：

$$
d()/dx=
\begin{bmatrix}
     & 1 &  & .. \\
     &  & 2 & .. \\
     &  &  & .. \\
    .. & .. & .. & .. \\
\end{bmatrix}
\\ - \\
\int()dx =
\begin{bmatrix}
     &  &  & .. \\
    1 &  &  & .. \\
     & 1/2 &  & .. \\
    .. & .. & 1/3 & .. \\
\end{bmatrix}=S
\\-\\

n f(n) =
\begin{bmatrix}
     &  &  & .. \\
    1 &  &  & .. \\
     & 1 &  & .. \\
    .. & .. & 1 & .. \\
\end{bmatrix}f=Nf
\\-\\
M =
\begin{bmatrix}
    1 &  &  & .. \\
     &  &  & .. \\
     &  &  & .. \\
    .. & .. & ..& .. \\
\end{bmatrix}
\\-\\

f(n)+n=f+[0,1,...]^T=f+e_1


\\

函数代入值得到标量:f(C)
=\begin{bmatrix}
    1 & C & C^2 & .. \\

\end{bmatrix}f=v_Cf
$$

所以递推式为：
$$
e_1(I-k(v_1-v_0)Sf)+k(Sf-MSf)
\\=e_1+(-ke_1v_1+ke_1v_0+kI-M)Sf
$$

---
思考4：从向量操作的角度看这个积分迭代。


求导。等价于把各项的次数写到前一项里(写作c)，然后乘以一个平移向量
比如
$[2 3 5 0]'=[0 2 3 5]*[4 3 2 1]=[0 2 3 5]* c$

所以积分运算对多项式向量$p$的意义是：
$$
\int p=(p/c)<<1
$$
而0-1积分的意义是把上述结果再求和（记为$|p|$），
从这个角度化简递推式：
$$
g_k=n(1- k|\int g_{k-1}|)+k(\int g_{k-1})
$$
由于平移不改变求和，所以$|\int g|=|g/c|$，那么
$$
g_k=n(1-|g_{k-1}/c|)+k(\int g_{k-1})
$$
我们猜测|g|是不是在迭代过程中保持稳定？
$$
|g_k|=1-|g_{k-1}/c|+k|g_{k-1}/c|=1+(k-1)|g_{k-1}/c|
$$
并不是。




<!-- <font size=4 color=#0825aa> -->
<!-- <font size=4> -->



由3Blue1Brown的视频启发.
https://www.bilibili.com/video/BV1pW411J7s8
https://www.bilibili.com/video/BV1vt411N7Ti

傅里叶级数将函数$f(t)$表示成不同频率的三角函数的和。


部分和:
$$s_N(t)=\sum_{n=-N}^N c_n e^{ i2\pi n t/P }$$
P是函数在某个可积区间上的长。

n可理解为向量旋转的频率。在DFT中它取等差。


$c_n$是一个系数：

$$
c_n=\frac{1}{P}\int_P e^{-i\frac{2\pi n t}{P}}f(t)dt
$$


$c_n\in \mathbb{C}$，它控制了每个向量的模长和初始相位。
右边的式子的一个可视化的理解方式为：将g(t)按某个频率f缠绕在复平面的原点周围，并求取了整个图像的“质心”的位置。


如果$f(t)\in \mathbb{C}$，这种表示仍然可以成立（此时$f(t)$是一个二维的图案，意味着用傅里叶级数可以逼近闭合的曲线图案，或者压缩图像）


直观来看，它表示许多个首尾相接的向量，每一个都在做角速度不同的圆周运动（类似地心说中的本轮和均轮）


$f(t)\in \mathbb{R}$时，频率分别为 $\pm n$ 的两个向量在竖直方向上的分量总是互相抵消，向量的和总是落在实轴上形成一个震荡的正弦波，这是后者的特例。

正交基==


---

**Hilbert空间**
函数集合
$$E=
\begin{bmatrix}
    e_n:=e^{inx},n\in \mathbb{Z}
\end{bmatrix}
$$
E是平方可积函数的正交基。

内积
$$<f,g>=\int f\cdot \overline{g} dx 
$$
并且$<sin(nx),sin(mx)>=0,n\neq m$（正交性）

$<sin(nx),cos(mx)>=0,n\neq m$

$<sin(nx),sin(nx)>=\pi$

范数$||f||=\sqrt{<f,f>}$


部分和$\hat{s}=\sum_{n=-N}^N \hat{f}(n)e_n$


勾股定理的扩展：
$$
\sum_n |<v,e_n>|^2=||v||^2
$$
$$
||f||^2=||f-\sum\hat{f}e_n||^2+||\sum \hat{f}e_n||^2
$$
对于第二项，由基的正交性可知：
$$
||\sum \hat{f}e_n||^2=\sum |\hat{f}|^2（Parseval's定理）
$$
每个实数都是一个维度，空间中的点实际上是函数。


以实轴为无穷多个维度，则$\mathbb{H}$中的一点可表示为f(x)
内积：$$\int_{-\infty}^{+\infty} f(t)g(t) dt$$

从而，傅里叶变换是$\mathbb{H}$中的一个坐标变换：
$$
F(\omega)=\int_{-\infty}^{+\infty} f(t)e^{-i\omega t} dt
$$

而$e^{-i\omega t}$是正交基。

---

**DFT**



求分量：选取一个正弦波与信号相乘：
$A=\int sin(2\pi f x)f(x),A'=\int cos(2\pi f x)f(x)$


A就是频率强度。

那么构成它的强度就是：
$$
Asin(x)+A'cos(x)
$$
离散情况下，信号采样的频率f决定它能分析出的分量的最大频率的大小L；采样长度L'决定了频率的分辨率f。（分辨率决定长度，长度决定分辨率）

---
例如，假设信号长度$L$，正弦曲线周期$T$

采样$n$个点，那么频率个数也只有$n$个。
信号函数$s(x)$


频率$F=0$时，计算方法为：$\sum Cf(t)$


$频谱图频率F=m$时，
$$T=\frac{L}{m}=\frac{2\pi }{\omega},\Delta =\frac{L}{n}$$

计算 
$$A_m=\sum_{j=0}^{n-1} cos(2\pi f j\Delta )s(j\Delta)$$
$$B_m=\sum sin(2\pi f j\Delta)s(j\Delta)$$
$$f=\frac{1}{T}=\frac{m}{L}$$



还原：
$$
\hat{s}=A_0+\sum_{m=1}^{n-1} A_m cos(2\pi fx)+B_m sin(2\pi f x)
$$

写成复数，合并正余弦强度：

$$
\hat{s}=A_0+\frac{1}{2}\sum_{t=1}^{n-1} (a-ib)e^{i2\pi f t}+ (a+ib)e^{-i2\pi f t}\\=\sum_{t=-(n-1)}^{n-1}c_ne^{i2\pi ft}
$$
---
**收敛性**

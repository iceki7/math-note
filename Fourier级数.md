

<!-- <font size=4 color=#0825aa> -->
<!-- <font size=4> -->
通俗解释傅里叶级数


本文由3Blue1Brown的视频启发。
https://www.bilibili.com/video/BV1pW411J7s8
https://www.bilibili.com/video/BV1vt411N7Ti

傅里叶级数用来将一个函数$f(t)$表示成无数个不同频率的三角函数的和。

部分和:
$$s_N(t)=\sum_{n=-N}^N c_n e^{ i\frac{2\pi n t}{P} }$$
P是函数在某个可积区间上的长。

n可理解为向量旋转的频率，$c_n$是一个系数：

$$
c_n=\frac{1}{P}\int_P e^{-i\frac{2\pi n t}{P}}f(t)dt
$$


$c_n\in \mathbb{C}$，它控制了每个向量的模长和初始相位。
右边的式子的一个可视化的理解方式为：将g(t)按某个频率f缠绕在复平面的原点周围，并求取了整个图像的“质心”的位置。


如果$f(t)\in \mathbb{C}$，这种表示仍然可以成立（此时$f(t)$是一个二维的图案，意味着用傅里叶级数可以逼近闭合的曲线图案，或者压缩图像）


直观来看，它表示许多个首尾相接的向量，每一个都在做角速度不同的圆周运动（类似地心说中的本轮和均轮）


如果回到一开始的情况，即$f(t)\in \mathbb{R}$时，实际上就是对应着频率分别为 $\pm n$ 的两个向量在竖直方向上的分量总是互相抵消，因而向量的和总是落在实轴上形成一个震荡的正弦波，这是后者的一个特例。

正交基==


**Hilbert空间**

以实轴为无穷多个维度，则$\mathbb{H}$中的一点可表示为f(x)
内积：$$\int_{-\infty}^{+\infty} f(t)g(t) dt$$

从而，傅里叶变换是$\mathbb{H}$中的一个坐标变换：
$$
F(\omega)=\int_{-\infty}^{+\infty} f(t)e^{-i\omega t} dt
$$

而$e^{-i\omega t}$是正交基。
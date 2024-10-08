**机器学习的一般形式**

在限定了某个样本空间D（数据集）的情况下，损失函数是参数$\theta$的函数。


$$
L=L(\hat{y},y),\hat{y}=f(\theta,x)
$$
f代表预测网络。(x,y)是数据集中的点，也就是通过在这些点之间构建拟合的“曲线”，来构建映射关系，实现对未知输入的推测。


在D被限定在某个范围的情况下，L可视为$\theta$的函数。

$$
L=g(\theta)
$$

让参数在负梯度方向上移动以降低损失：
$$
\theta-=\nabla_\theta L
$$


由于网络是函数的迭代$f(..f()...)$，如果其中每一个部分都是解析的，根据链式法则可以写出L对任何一个参数的导数
$L'_{\theta}$


----
为了评估网络在一些没有训练过的点上的准确性，取一些从未输入过的数据$(x_t,y_t)$作为测试集。如果准确率很高，说明网络对于这些数据的拟合是足够有效的。此时可以认为网络的参数中存储了空间到目标的映射过程。是有信息的。当然，测试集和训练集是同一类型的数据。


网络具有**连续性**，输入的小范围变动也只会引起输出的小范围变动。

这与现实世界人们的认知方式一致。（比如一副数字2的图像，改变其中的一个像素点并不会让人觉得这因此就不是数字2了，想要变成另一个数字需要经过很大范围的变动）。

另一个例子就是AI作画中，可以通过控制输入，将一种物体渐变为另外一种物体。（由此，也可以研究输入对于输出是**如何进行控制**的，也就是提取出输入中存在着的**语义**信息），比如如果我构造了一个网络，输入一个向量，输出一张动物的图片（先不管它是怎么做到的），
那么，我们就会想知道输入中的哪个分量在控制着输出动物的品种（如果它刚好能对应一个分量的话），如果能捕捉到语义，那么就能实现定制化地生成而非随机生成。


---

激活函数赋予非线性拟合能力.因为全连接网络（Wx+b）无论叠加多少层，都仍然是线性变换。线性变换的拟合能力有局限（比如，异或分类问题）


为避免局部最小，发明了很多梯度下降的方法。


为捕捉整体特征防止过拟合，提出了批训练的概念。也就是$g(\theta)$是关于许多个数据点的平均损失。根据这些平均损失执行梯度回传。所以g实际上不是某个特定的函数（除了全批量训练时，也就是一次性计算所有数据点的平均最低loss，此时的全局最优点理论上就是网络的最优解，但是全批量可能很难找到这个点）



卷积：捕捉邻域特征。


pooling：改变分辨率。例如图像的分类问题。


特征。存在一个抽象层次的区别。低层的特征比如物体的边缘，高层的特征比如物品的种类。越往高层走，所需要牺牲的细节就越多，而越往底层走，就越具体，当然具体到极致就是每一个像素点的RGB值了。

这让人联想到《博闻强记的富内斯》所述那样，一个人因为生了场怪病获得了超强的记忆力，但是也失去了高层次抽象的能力。他眼里看到的马都不再是马了，而是一缕缕的鬃毛，诸如此类的细节，过目不忘，由于对于细节的强烈敏感和超强记忆，使得他无法再把任意两匹马视作是马，对他来说每一匹马都完全不同，这使得马的这个概念在他脑海中彻底瓦解了。他无法再给任何物品进行分类。

这也可以和信息的鲁棒性联系起来。什么叫信息呢？信息就是鲁棒。我们判断一幅画里画的是一只猫，不是对那幅画的某个像素做if else判断得到的，猫的信息不存在于这幅画的任何一个像素中，而是存在于整体之中。所以信息是有鲁棒性的。

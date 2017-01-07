<h1 align = "center">Final Project——Start with random walk</h1>

<div align=center>
物基一班 倪世杰 2014301020001
</div>

---

**[摘要]**本文从随机游走出发，先研究了随机游走的一些性质，而后探究了扩散过程和随机游走的联系，并粗略探讨了扩散过程中的熵变。

**[关键词]**随机游走；SAW；SAP；扩散；菲克定律；熵

###1. 引言

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在之前计算物理的学习中，我们所讨论的所有系统都是确定性的（即使是混沌系统，我们使用的动力学方程也是确定性的）。然而，在现实中，随机系统广泛存在，而且许多问题的解决离不开对随机系统的研究。其中，一类最简单的随机系统和问题就是随机游走和扩散现象。


###2. 背景介绍

* **随机游走**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;随机游走是描述由一系列随机步骤组成的路线的数学对象。例如，一个分子在液体或气体中前进的路线，动物的觅食路线，超弦行为，一支波动的股票的价格以及一个赌徒的财务状况都可以通过随机游走模型近似,，即使事实上他们可能不是随机的。如这些例子所示，随机游走在许多科学领域都有应用，包括生态学、心理学、计算科学、物理学、化学和生物学，同时也有经济学。随机游走揭示了这些领域中许多过程中被观测到的行为，因此它作为一个已记录的随机活动的基础模型。作为一个更偏数学的应用， 在基于主体的建模环境中，π的值可以通过使用随机行走近似得出。随机行走这个术语最早被英国数学家、生物统计学家卡尔·皮尔逊于1905年提出。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在很多系统都存在不同类型的随机游走，他们都具有相似结构。单个的随机事件我们不可预测，但随机大量的群体行为，却是精确可知的，这就是概率世界的魅力，在偶然中隐含着必然。随机性造成了低尺度下的差异性，但在高尺度下又表现为共同的特征的相似性。按照概率的观点“宇宙即是所有随机事件概率的总和”。

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/quantum_cloud_front_775.jpg?raw=true" /></div>

<div align=center>雕塑家安东尼·葛姆雷使用随机游走算法创作的雕塑——《量子云》</div>

* **自回避随机游走**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在数学上，自回避随机游走（SAW）是指在网格上一系列重复经过同一个点的一系列移动。自回避多边形（SAP） 则是指网格上一个封闭的自回避随机游走的路径。自回避随机游走最早被保罗·弗洛里提出用来模拟链状实体比如溶剂和聚合物的真实行为，它们拥有的体积禁止在空间同一个点上有多个物体。尽管物理学家提出了许多有数值模拟强力支持并被认为是正确的猜想，但是从数学角度来说，我们对自回避随机游走了解非常少。

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/knot_3a_blog.jpg?raw=true" /></div>

<div align=center>一种自回避多边形</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在计算物理中，自回避随机游走是一个二维或三维欧几里得空间中有固定节点数和步长的链状路线，并且其被禁止穿过自身或其他路线。一个自回避随机游走系统满足所谓的排斥体积条件。在更高维度中，自回避随机游走被认为行为更像原本的随机游走。自回避随机游走和自回避多边形在模型化如蛋白质的线状或环状分子的拓扑和纽结理论行为时起到核心作用。自回避随机游走是分形的。例如，在二维空间中，分形维数是<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{4}{3}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{4}{3}" title="\frac{4}{3}" /></a>，三维空间中，分形维数接近<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{5}{3}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{5}{3}" title="\frac{5}{3}" /></a>，在四维和更高维空间中，分形维数为<a href="http://www.codecogs.com/eqnedit.php?latex=2" target="_blank"><img src="http://latex.codecogs.com/gif.latex?2" title="2" /></a>。这个维数被称为上临界维数，当超过这个维数时排斥体积是微不足道的。

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/HK4nV.jpg?raw=true" /></div>

<div align=center>三维点阵自回避随机游走</div>

* **扩散**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分子扩散，通常简称为扩散，是分子通过随机分子运动从高浓度（或高化学势）区域向低浓度（或低化学势）区域的网状的传播。扩散的结果是物质缓慢地混合起来。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;扩散现象是分子的内迁移现象。从微观上分析是大量分子做无规则热运动时，分子之间发生相互碰撞的结果。由于不同空间区域的分子密度分布不均匀，分子发生碰撞的情况也不同。这种碰撞迫使密度大的区域的分子向密度小的区域转移，最后达到均匀的密度分布。</font>

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Blausen_0315_Diffusion.png?raw=true" /></div>

<div align=center>颜料在水中的扩散</div>

* **扩散定律**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;扩散以一个初始分布释放大量的无规则行走，观察他们的密度就会得到分布函数。1855年法国生理学家阿道夫·菲克提出了描述扩散规律的基本公式——菲克定律。

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/DiffusionMicroMacro.gif?raw=true" /></div>

<div align=center>不同尺度下观察到的扩散过程</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;菲克第一定律假设从高浓度区域往低浓度流的通量大小与浓度梯度（空间导数）成正比，通过这个假设，菲克第一定律把扩散通量与浓度联系起来。在一维空间下的菲克第一定律如下：

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=J=-D\frac{\partial&space;\phi&space;}{\partial&space;x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?J=-D\frac{\partial&space;\phi&space;}{\partial&space;x}" title="J=-D\frac{\partial \phi }{\partial x}" /></a></div>

其中，<a href="http://www.codecogs.com/eqnedit.php?latex=J" target="_blank"><img src="http://latex.codecogs.com/gif.latex?J" title="J" /></a>为“扩散通量”（于某单位时间内通过某单位面积的物质量），<a href="http://www.codecogs.com/eqnedit.php?latex=J" target="_blank"><img src="http://latex.codecogs.com/gif.latex?J" title="J" /></a>为扩散系数或扩散度，<a href="http://www.codecogs.com/eqnedit.php?latex=\phi" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\phi" title="\phi" /></a>为浓度（假设为理想混合物）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据斯托克斯-爱因斯坦关系，<a href="http://www.codecogs.com/eqnedit.php?latex=D" target="_blank"><img src="http://latex.codecogs.com/gif.latex?D" title="D" /></a>的大小取决于温度、流体黏度与分子大小，并与扩散分子流动的平均速度平方成正比。

在二维或以上的情况下，我们必须使用<a href="http://www.codecogs.com/eqnedit.php?latex=\nabla" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\nabla" title="\nabla" /></a>来把第一导数通用化，得

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=J=-D\nabla\phi" target="_blank"><img src="http://latex.codecogs.com/gif.latex?J=-D\nabla\phi" title="J=-D\nabla\phi" /></a></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;菲克第二定律预测扩散会如何使得浓度随时间改变：

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\phi&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\varphi&space;}{\partial&space;x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\phi&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\varphi&space;}{\partial&space;x^{2}}" title="\frac{\partial \phi }{\partial t}=D\frac{\partial ^{2}\varphi }{\partial x^{2}}" /></a></div>

对于二维或以上的扩散，其菲克第二定律为：

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\phi&space;}{\partial&space;t}=D\nabla^{2}\varphi" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\phi&space;}{\partial&space;t}=D\nabla^{2}\varphi" title="\frac{\partial \phi }{\partial t}=D\nabla^{2}\varphi" /></a></div>

其形式跟热传导方程类似。

* **熵**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;化学及热力学中所指的熵，是一种测量在动力学方面不能做功的能量总数，也就是当总体的熵增加，其做功能力也下降，熵的量度正是能量退化的指标。熵亦被用于计算一个系统中的失序现象，也就是计算该系统混乱的程度。熵是一个描述系统状态的函数，但是经常用熵的参考值和变化量进行分析比较，它在控制论、概率论、数论、天体物理、生命科学等领域都有重要应用，在不同的学科中也有引申出的更为具体的定义，是各领域十分重要的参量。

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/entropy.jpg?raw=true" /></div>

<div align=center>熵增过程</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1877年，玻尔兹曼发现单一系统中的熵跟构成热力学性质的微观状态数量相关。可以考虑情况如：一个容器内的理想气体。微观状态可以以每个组成的原子的位置及动量予以表达。为了一致性起见，我们只需考虑包含以下条件的微观状态：（i）所有粒子的位置皆在容器的体积范围内；（ii）所有原子的动能总和等于该气体的总能量值。玻尔兹曼提出一个系统的熵和所有可能微观状态的数目满足以下简单关系：

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=S=k\ln\Omega" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S=k\ln\Omega" title="S=k\ln\Omega" /></a></div>

这个公式称为“玻尔兹曼公式”，其中<a href="http://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="http://latex.codecogs.com/gif.latex?k" title="k" /></a>是玻尔兹曼常数，<a href="http://www.codecogs.com/eqnedit.php?latex=\Omega" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /></a>则为系统宏观状态中所包含的微观状态总数。根据玻尔兹曼的定义，熵是一则关于状态的函数。并且因为<a href="http://www.codecogs.com/eqnedit.php?latex=\Omega" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /></a>是一个自然数（1,2,3,...），熵必定是个非负数。根据这个公式，我们可以将熵看作是一个系统“混乱程度”的度量，因为一个系统越混乱，可以看作是微观状态分布越均匀。根据熵的统计学定义，热力学第二定律说明一个孤立系统的倾向于增加混乱程度。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以严格证明，玻尔兹曼公式的另一种等价表述形式是

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=S=-k\sum_{s}^{&space;}P_{s}\ln&space;P_{s}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S=-k\sum_{s}^{&space;}P_{s}\ln&space;P_{s}" title="S=-k\sum_{s}^{ }P_{s}\ln P_{s}" /></a></div>

其中<a href="http://www.codecogs.com/eqnedit.php?latex=s" target="_blank"><img src="http://latex.codecogs.com/gif.latex?s" title="s" /></a>标记所有可能的微观态， <a href="http://www.codecogs.com/eqnedit.php?latex=P_{s}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P_{s}" title="P_{s}" /></a>表示微观态<a href="http://www.codecogs.com/eqnedit.php?latex=s" target="_blank"><img src="http://latex.codecogs.com/gif.latex?s" title="s" /></a>的出现几率。

###3. 正文

#### Ⅰ 点阵随机游走

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个最流行的随机游走模型就是规则点阵上的随机游走，在这个模型中，每一步对象的位置根据某种概率分布从一个阵点跳跃到另一个阵点上。这种简化使问题更易处理又不失一般性，故我们接下来主要研究该种模型。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中最简单的情形就是一个行人以固定步幅在一条直线上等概率地沿两个方向之一行走。为使结果更具普遍性，我们假设同时有若干人在随机游走，研究他们走完每一步后与原点之间的平均距离。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;显然，实现该程序的关键是如何模拟行人们等几率的向两个方向行走。我们可以通过产生一个介于<a href="http://www.codecogs.com/eqnedit.php?latex=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?0" title="0" /></a>和<a href="http://www.codecogs.com/eqnedit.php?latex=1" target="_blank"><img src="http://latex.codecogs.com/gif.latex?1" title="1" /></a>之间的随机数<a href="http://www.codecogs.com/eqnedit.php?latex=r" target="_blank"><img src="http://latex.codecogs.com/gif.latex?r" title="r" /></a>来实现：若<a href="http://www.codecogs.com/eqnedit.php?latex=r<0.5" target="_blank"><img src="http://latex.codecogs.com/gif.latex?r<0.5" title="r<0.5" /></a>，则行人向右走一步，否则行人向左走一步。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-1.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们取行人人数为10000，模拟三次得如下结果

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_1-1.png?raw=true" /></div>

可以看出10000名行人的平均位移<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x}" title="\overline{x}" /></a>在<a href="http://www.codecogs.com/eqnedit.php?latex=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?0" title="0" /></a>附近波动且波动幅度随<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>增大，但<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x}" title="\overline{x}" /></a>的期望值大致为<a href="http://www.codecogs.com/eqnedit.php?latex=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?0" title="0" /></a>，这是由于

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E\left&space;(&space;\overline{x}&space;\right&space;)=E\left&space;(&space;\&space;\frac{1}{N}\sum_{i=1}^{N}x_{i}\right&space;)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E\left&space;(&space;\overline{x}&space;\right&space;)=E\left&space;(&space;\&space;\frac{1}{N}\sum_{i=1}^{N}x_{i}\right&space;)" title="E\left ( \overline{x} \right )=E\left ( \ \frac{1}{N}\sum_{i=1}^{N}x_{i}\right )" /></a><a href="http://www.codecogs.com/eqnedit.php?latex==E\left&space;(&space;\&space;\frac{1}{N}\sum_{i=1}^{N}\sum_{j=1}^{n}s_{ij}\right&space;)=\frac{1}{N}NnE\left&space;(&space;s&space;\right&space;)=n\left&space;[&space;\frac{1}{2}\times&space;1&plus;\frac{1}{2}\times&space;\left&space;(&space;-1&space;\right&space;)&space;\right&space;]=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?=E\left&space;(&space;\&space;\frac{1}{N}\sum_{i=1}^{N}\sum_{j=1}^{n}s_{ij}\right&space;)=\frac{1}{N}NnE\left&space;(&space;s&space;\right&space;)=n\left&space;[&space;\frac{1}{2}\times&space;1&plus;\frac{1}{2}\times&space;\left&space;(&space;-1&space;\right&space;)&space;\right&space;]=0" title="=E\left ( \ \frac{1}{N}\sum_{i=1}^{N}\sum_{j=1}^{n}s_{ij}\right )=\frac{1}{N}NnE\left ( s \right )=n\left [ \frac{1}{2}\times 1+\frac{1}{2}\times \left ( -1 \right ) \right ]=0" /></a></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面我们具体研究<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x}" title="\overline{x}" /></a>的波动幅度与步数<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>的关系。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-2.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下图是一次模拟中<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>随步数的变化

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_1-2.png?raw=true" /></div>

可以看出，<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>的值大致等于步数<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>。接下来我们从理论上具体分析原因：

因为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E\left&space;(&space;\overline{x^{2}}&space;\right&space;)=E\left&space;(&space;\&space;\frac{1}{N}\sum_{i=1}^{N}x_{i}^{2}\right&space;)=\frac{1}{N}\sum_{i=1}^{N}E\left&space;(&space;\&space;x_{i}^{2}\right&space;)=E\left&space;(&space;\&space;x_{i}^{2}\right&space;)=E\left&space;[\left&space;(&space;\sum_{j=1}^{n}s_{ij}&space;\right&space;)^{2}&space;\right&space;]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E\left&space;(&space;\overline{x^{2}}&space;\right&space;)=E\left&space;(&space;\&space;\frac{1}{N}\sum_{i=1}^{N}x_{i}^{2}\right&space;)=\frac{1}{N}\sum_{i=1}^{N}E\left&space;(&space;\&space;x_{i}^{2}\right&space;)=E\left&space;(&space;\&space;x_{i}^{2}\right&space;)=E\left&space;[\left&space;(&space;\sum_{j=1}^{n}s_{ij}&space;\right&space;)^{2}&space;\right&space;]" title="E\left ( \overline{x^{2}} \right )=E\left ( \ \frac{1}{N}\sum_{i=1}^{N}x_{i}^{2}\right )=\frac{1}{N}\sum_{i=1}^{N}E\left ( \ x_{i}^{2}\right )=E\left ( \ x_{i}^{2}\right )=E\left [\left ( \sum_{j=1}^{n}s_{ij} \right )^{2} \right ]" /></a></div>

而<a href="http://www.codecogs.com/eqnedit.php?latex=s_{ij_{1}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?s_{ij_{1}}" title="s_{ij_{1}}" /></a>与<a href="http://www.codecogs.com/eqnedit.php?latex=s_{ij_{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?s_{ij_{2}}" title="s_{ij_{2}}" /></a>是相互独立的随机变量，故有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E\left&space;(s_{ij_{1}}s_{ij_{2}}&space;\right&space;)=E\left&space;(&space;s_{ij_{1}}&space;\right&space;)E\left&space;(&space;s_{ij_{2}}&space;\right&space;)=\left&space;[&space;\frac{1}{2}\times&space;1&plus;\frac{1}{2}\times&space;\left&space;(&space;-1&space;\right&space;)&space;\right&space;]^{2}=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E\left&space;(s_{ij_{1}}s_{ij_{2}}&space;\right&space;)=E\left&space;(&space;s_{ij_{1}}&space;\right&space;)E\left&space;(&space;s_{ij_{2}}&space;\right&space;)=\left&space;[&space;\frac{1}{2}\times&space;1&plus;\frac{1}{2}\times&space;\left&space;(&space;-1&space;\right&space;)&space;\right&space;]^{2}=0" title="E\left (s_{ij_{1}}s_{ij_{2}} \right )=E\left ( s_{ij_{1}} \right )E\left ( s_{ij_{2}} \right )=\left [ \frac{1}{2}\times 1+\frac{1}{2}\times \left ( -1 \right ) \right ]^{2}=0" /></a></div>

从而有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E\left&space;[\left&space;(&space;\sum_{j=1}^{n}s_{ij}&space;\right&space;)^{2}&space;\right&space;]=\sum_{j=1}^{n}E\left&space;(&space;s_{ij}^{2}&space;\right&space;)=nE\left&space;(&space;s_{ij}^{2}&space;\right&space;)=n\left&space;[&space;\frac{1}{2}\times&space;1^{2}&plus;&space;\frac{1}{2}\times&space;\left&space;(-1&space;\right&space;)^{2}&space;\right&space;]=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E\left&space;[\left&space;(&space;\sum_{j=1}^{n}s_{ij}&space;\right&space;)^{2}&space;\right&space;]=\sum_{j=1}^{n}E\left&space;(&space;s_{ij}^{2}&space;\right&space;)=nE\left&space;(&space;s_{ij}^{2}&space;\right&space;)=n\left&space;[&space;\frac{1}{2}\times&space;1^{2}&plus;&space;\frac{1}{2}\times&space;\left&space;(-1&space;\right&space;)^{2}&space;\right&space;]=n" title="E\left [\left ( \sum_{j=1}^{n}s_{ij} \right )^{2} \right ]=\sum_{j=1}^{n}E\left ( s_{ij}^{2} \right )=nE\left ( s_{ij}^{2} \right )=n\left [ \frac{1}{2}\times 1^{2}+ \frac{1}{2}\times \left (-1 \right )^{2} \right ]=n" /></a></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接下来，我们取消步长为固定值的限制，使每步的位移在<a href="http://www.codecogs.com/eqnedit.php?latex=\left&space;[&space;-1,1&space;\right&space;]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\left&space;[&space;-1,1&space;\right&space;]" title="\left [ -1,1 \right ]" /></a>间等概率随机取值。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-3.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们同样取行人人数为10000，模拟三次得如下结果

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_2-1.png?raw=true" /></div>

同样我们可以看出<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x}" title="\overline{x}" /></a>在<a href="http://www.codecogs.com/eqnedit.php?latex=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?0" title="0" /></a>附近波动，但波动幅度却明显比之前要小。

显然，由于每步的位移<a href="http://www.codecogs.com/eqnedit.php?latex=s" target="_blank"><img src="http://latex.codecogs.com/gif.latex?s" title="s" /></a>服从均匀分布<a href="http://www.codecogs.com/eqnedit.php?latex=U[-1,1]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?U[-1,1]" title="U[-1,1]" /></a>，有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E(s)=\frac{1}{2}\left&space;[&space;1&plus;\left&space;(&space;-1&space;\right&space;)&space;\right&space;]=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(s)=\frac{1}{2}\left&space;[&space;1&plus;\left&space;(&space;-1&space;\right&space;)&space;\right&space;]=0" title="E(s)=\frac{1}{2}\left [ 1+\left ( -1 \right ) \right ]=0" /></a></div>

从而由之前讨论知

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E(\bar{x})=nE(s)=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(\bar{x})=nE(s)=0" title="E(\bar{x})=nE(s)=0" /></a></div>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面我们具体研究<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x}" title="\overline{x}" /></a>的波动幅度与步数<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>的关系。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-4.py)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下图是一次模拟中<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>随步数的变化

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_2-2.png?raw=true" /></div>

可以看出，<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>的值仍然与步数<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>成正比，但其值要比之前小很多。下面我们从理论上给出解释：

由<a href="http://www.codecogs.com/eqnedit.php?latex=s\sim&space;U[-1,1]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?s\sim&space;U[-1,1]" title="s\sim U[-1,1]" /></a>，有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E(s^{2})=D(s)&plus;[E(s)]^{2}=\frac{[1-(-1)]^{2}}{12}&plus;0^{2}=\frac{1}{3}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(s^{2})=D(s)&plus;[E(s)]^{2}=\frac{[1-(-1)]^{2}}{12}&plus;0^{2}=\frac{1}{3}" title="E(s^{2})=D(s)+[E(s)]^{2}=\frac{[1-(-1)]^{2}}{12}+0^{2}=\frac{1}{3}" /></a></div>

故而由前讨论有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E(\overline{x^{2}})=nE(s^{2})=\frac{n}{3}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(\overline{x^{2}})=nE(s^{2})=\frac{n}{3}" title="E(\overline{x^{2}})=nE(s^{2})=\frac{n}{3}" /></a></div>

显然，这与模拟所得图像高度一致。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面，我们按照**习题7.3**所说，研究当行人向两个方向移动的概率不等时的情况，我们取向左移动的概率<a href="http://www.codecogs.com/eqnedit.php?latex=p_{left}=0.25" target="_blank"><img src="http://latex.codecogs.com/gif.latex?p_{left}=0.25" title="p_{left}=0.25" /></a>，从而向右移动的概率<a href="http://www.codecogs.com/eqnedit.php?latex=p_{right}=0.75" target="_blank"><img src="http://latex.codecogs.com/gif.latex?p_{right}=0.75" title="p_{right}=0.75" /></a>。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-5.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们同样取行人人数为10000，模拟三次得如下结果

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_3-1.png?raw=true" /></div>

不难看出，<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>的值约为步数<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>的<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{1}{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{1}{2}" title="\frac{1}{2}" /></a>。

又由之前讨论有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E(\overline{x})=nE(s)=n[0.75\times&space;1&plus;0.25\times&space;(-1)]=\frac{1}{2}n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(\overline{x})=nE(s)=n[0.75\times&space;1&plus;0.25\times&space;(-1)]=\frac{1}{2}n" title="E(\overline{x})=nE(s)=n[0.75\times 1+0.25\times (-1)]=\frac{1}{2}n" /></a></div>

显然，这与模拟结果一致。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接着我们具体研究<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>与步数<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>的关系。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-6.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下图是一次模拟中<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>随步数的变化

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_3-2.png?raw=true" /></div>


从拟合曲线可知，<a href="http://www.codecogs.com/eqnedit.php?latex=\overline{x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overline{x^{2}}" title="\overline{x^{2}}" /></a>大致是<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>的二次函数。

由于该种情况下，<a href="http://www.codecogs.com/eqnedit.php?latex=E(s)=0.75\times&space;1&plus;0.25\times&space;(-1)=\frac{1}{2}\neq&space;0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(s)=0.75\times&space;1&plus;0.25\times&space;(-1)=\frac{1}{2}\neq&space;0" title="E(s)=0.75\times 1+0.25\times (-1)=\frac{1}{2}\neq 0" /></a>，<a href="http://www.codecogs.com/eqnedit.php?latex=E(s^{2})=0.75\times&space;1^{2}&plus;0.25\times&space;(-1)^{2}=1" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(s^{2})=0.75\times&space;1^{2}&plus;0.25\times&space;(-1)^{2}=1" title="E(s^{2})=0.75\times 1^{2}+0.25\times (-1)^{2}=1" /></a>，则有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=E(\overline{x^{2}})=E[(\sum_{i=1}^{n}s_{i})^{2}]=\sum_{i=1}^{n}E(s_{i}^{2})&plus;\sum_{i\neq&space;j,1\leq&space;i,j\leq&space;n}^{&space;}E(s_{i})E(s_{j})&space;\\=nE(s^{2})&plus;n(n-1)[E(s)]^{2}=n&plus;\frac{1}{4}n(n-1)=\frac{1}{4}n(n&plus;3)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?E(\overline{x^{2}})=E[(\sum_{i=1}^{n}s_{i})^{2}]=\sum_{i=1}^{n}E(s_{i}^{2})&plus;\sum_{i\neq&space;j,1\leq&space;i,j\leq&space;n}^{&space;}E(s_{i})E(s_{j})&space;\\=nE(s^{2})&plus;n(n-1)[E(s)]^{2}=n&plus;\frac{1}{4}n(n-1)=\frac{1}{4}n(n&plus;3)" title="E(\overline{x^{2}})=E[(\sum_{i=1}^{n}s_{i})^{2}]=\sum_{i=1}^{n}E(s_{i}^{2})+\sum_{i\neq j,1\leq i,j\leq n}^{ }E(s_{i})E(s_{j}) \\=nE(s^{2})+n(n-1)[E(s)]^{2}=n+\frac{1}{4}n(n-1)=\frac{1}{4}n(n+3)" /></a></div>

经验算，所得曲线和该式符合很好。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了更直观地理解随机行走的过程，我们可以使用python中的turtle模块绘制二维点阵随机游走示意动画。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-1.py)

这是<a href="http://www.codecogs.com/eqnedit.php?latex=17\times&space;17" target="_blank"><img src="http://latex.codecogs.com/gif.latex?17\times&space;17" title="17\times 17" /></a>网格上的随机游走动画

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/GIF0.gif?raw=true" /></div>

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-2.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这是<a href="http://www.codecogs.com/eqnedit.php?latex=33\times&space;33" target="_blank"><img src="http://latex.codecogs.com/gif.latex?33\times&space;33" title="33\times 33" /></a>网格上的随机游走动画

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/GIF1.gif?raw=true" /></div>

我们可以看出红色箭头会在出发点附近一定大小的区域内游走相当长的时间。事实上，对于一维和二维点阵随机游走，只要步数足够大，任意游动的点必定能返回它的出发点，该定理是著名数学家波利亚在1921年证明的。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接着，我们模拟在每一步的方向和步幅都随机的情况下的二维随机游走轨迹。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-3.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面是三次模拟的轨迹图

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_4-1.png?raw=true" /></div>

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_4-2.png?raw=true" /></div>

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_4-3.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此外，我们还可以较为容易地模拟三维点阵随机游走的轨迹。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-4.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面是三次模拟的轨迹图

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_5-1.png?raw=true" /></div>

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_5-2.png?raw=true" /></div>

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_5-3.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们可以看出多数情况下，动点出发后离原点越来越远，没有返回出发点的迹象。实际上，波利亚也证明了在三维网格中随机游走，最终能回到出发点的概率只有大约 34% ，而且随着维度的增 加，回到出发点的概率将变得越来越低。在四维网格中随机游走，最终能回到出发点 的概率是 19.3% ，而在八维空间中，这个概率只有 7.3% 。 

#### Ⅱ 从随机游走到扩散

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们之前曾提到，随机游走和扩散是等价的，宏观上观测到的扩散现象其实就是大量粒子的随机游走行为。下面为了研究扩散问题的处理方法，我们讨论单个粒子在简单立方点阵中的随机游走。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;记<a href="http://www.codecogs.com/eqnedit.php?latex=P(i,j,k,n)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P(i,j,k,n)" title="P(i,j,k,n)" /></a>为粒子在<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>时刻（即第<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>步）出现在点<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>处的概率。要使粒子在<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>时刻出现在点<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>，则在<a href="http://www.codecogs.com/eqnedit.php?latex=n-1" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n-1" title="n-1" /></a>时刻，粒子必须在与<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>相邻的六个阵点上，又从每个相邻阵点运动到<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>的概率为<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{1}{6}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{1}{6}" title="\frac{1}{6}" /></a>，则有如下递推式


<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=P(i,j,k,n)=\frac{1}{6}[P(i&plus;1,j,k,n-1)&plus;P(i-1,j,k,n-1)&plus;P(i,j&plus;1,k,n-1)\\&plus;P(i,j-1,k,n-1)&plus;P(i,j,k&plus;1,n-1)&plus;P(i,j,k-1,n-1)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P(i,j,k,n)=\frac{1}{6}[P(i&plus;1,j,k,n-1)&plus;P(i-1,j,k,n-1)&plus;P(i,j&plus;1,k,n-1)\\&plus;P(i,j-1,k,n-1)&plus;P(i,j,k&plus;1,n-1)&plus;P(i,j,k-1,n-1)]" title="P(i,j,k,n)=\frac{1}{6}[P(i+1,j,k,n-1)+P(i-1,j,k,n-1)+P(i,j+1,k,n-1)\\+P(i,j-1,k,n-1)+P(i,j,k+1,n-1)+P(i,j,k-1,n-1)]" /></a></div>

改写上式，可得

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=P(i,j,k,n)-P(i,j,k,n-1)\\=\frac{1}{6}[P(i&plus;1,j,k,n-1)-2P(i,j,k,n-1)&plus;P(i-1,j,k,n-1)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P(i,j,k,n)-P(i,j,k,n-1)\\=\frac{1}{6}[P(i&plus;1,j,k,n-1)-2P(i,j,k,n-1)&plus;P(i-1,j,k,n-1)]" title="P(i,j,k,n)-P(i,j,k,n-1)\\=\frac{1}{6}[P(i+1,j,k,n-1)-2P(i,j,k,n-1)+P(i-1,j,k,n-1)]" /></a></div>

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=&plus;\frac{1}{6}[P(i,j&plus;1,k,n-1)-2P(i,j,k,n-1)&plus;P(i,j-1,k,n-1)]\\&plus;\frac{1}{6}[P(i,j,k&plus;1,n-1)-2P(i,j,k,n-1)&plus;P(i,j,k-1,n-1)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?&plus;\frac{1}{6}[P(i,j&plus;1,k,n-1)-2P(i,j,k,n-1)&plus;P(i,j-1,k,n-1)]\\&plus;\frac{1}{6}[P(i,j,k&plus;1,n-1)-2P(i,j,k,n-1)&plus;P(i,j,k-1,n-1)]" title="+\frac{1}{6}[P(i,j+1,k,n-1)-2P(i,j,k,n-1)+P(i,j-1,k,n-1)]\\+\frac{1}{6}[P(i,j,k+1,n-1)-2P(i,j,k,n-1)+P(i,j,k-1,n-1)]" /></a></div>

等式两边同乘常量<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{1}{\Delta&space;t}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{1}{\Delta&space;t}" title="\frac{1}{\Delta t}" /></a>，由之前章节对拉普拉斯算子的讨论，可将等式化为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;P(x,y,z,t)}{\partial&space;t}=D\nabla^{2}P(x,y,z,t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;P(x,y,z,t)}{\partial&space;t}=D\nabla^{2}P(x,y,z,t)" title="\frac{\partial P(x,y,z,t)}{\partial t}=D\nabla^{2}P(x,y,z,t)" /></a></div>

其中<a href="http://www.codecogs.com/eqnedit.php?latex=D=\frac{1}{6}\frac{(\Delta&space;x)^{2}}{\Delta&space;t}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?D=\frac{1}{6}\frac{(\Delta&space;x)^{2}}{\Delta&space;t}" title="D=\frac{1}{6}\frac{(\Delta x)^{2}}{\Delta t}" /></a>

我们发现上式与我们之前提到的扩散方程形式完全一样

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\rho&space;}{\partial&space;t}=D\nabla^{2}\rho" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\rho&space;}{\partial&space;t}=D\nabla^{2}\rho" title="\frac{\partial \rho }{\partial t}=D\nabla^{2}\rho" /></a></div>

其实，当体系有大量粒子时，他们某一时刻出现在某一位置的概率<a href="http://www.codecogs.com/eqnedit.php?latex=P" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P" title="P" /></a>之和即为该时刻该位置的粒子数密度<a href="http://www.codecogs.com/eqnedit.php?latex=\rho" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho" title="\rho" /></a>。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在一维情况下，我们将粒子数密度函数写为<a href="http://www.codecogs.com/eqnedit.php?latex=\rho&space;(x,t)=\rho&space;(i\Delta&space;x,n\Delta&space;t)=\rho&space;(i,n)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho&space;(x,t)=\rho&space;(i\Delta&space;x,n\Delta&space;t)=\rho&space;(i,n)" title="\rho (x,t)=\rho (i\Delta x,n\Delta t)=\rho (i,n)" /></a>，则对应的扩散方程为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\rho&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\rho&space;}{\partial&space;x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\rho&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\rho&space;}{\partial&space;x^{2}}" title="\frac{\partial \rho }{\partial t}=D\frac{\partial ^{2}\rho }{\partial x^{2}}" /></a></div>

其有限差分形式如下

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\rho&space;(i,n&plus;1)-\rho&space;(i,n)}{\Delta&space;t}=D\frac{\rho&space;(i&plus;1,n)-2\rho&space;(i,n)&plus;\rho&space;(i-1,n)}{(\Delta&space;x)^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\rho&space;(i,n&plus;1)-\rho&space;(i,n)}{\Delta&space;t}=D\frac{\rho&space;(i&plus;1,n)-2\rho&space;(i,n)&plus;\rho&space;(i-1,n)}{(\Delta&space;x)^{2}}" title="\frac{\rho (i,n+1)-\rho (i,n)}{\Delta t}=D\frac{\rho (i+1,n)-2\rho (i,n)+\rho (i-1,n)}{(\Delta x)^{2}}" /></a></div>

改写为递推形式有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\rho&space;(i,n&plus;1)=\rho&space;(i,n)&plus;\frac{D\Delta&space;t}{(\Delta&space;x)^{2}}[\rho&space;(i&plus;1,n)&plus;\rho&space;(i-1,n)-2\rho&space;(i,n)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho&space;(i,n&plus;1)=\rho&space;(i,n)&plus;\frac{D\Delta&space;t}{(\Delta&space;x)^{2}}[\rho&space;(i&plus;1,n)&plus;\rho&space;(i-1,n)-2\rho&space;(i,n)]" title="\rho (i,n+1)=\rho (i,n)+\frac{D\Delta t}{(\Delta x)^{2}}[\rho (i+1,n)+\rho (i-1,n)-2\rho (i,n)]" /></a></div>

可见，如果我们知道粒子的初始分布，就可求得他们之后时刻的分布。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们首先用以上由扩散方程得到的递推式模拟初始时刻粒子全部聚集在原点的情况。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project3-1.py)

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_6-2.png?raw=true" /></div>

如习题**7.9**所说，扩散进行一段时间后，粒子呈正态分布（高斯分布）

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\rho&space;(x,t)=\frac{1}{\sigma&space;}e^{-\frac{x^{2}}{2\sigma&space;^{2}}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho&space;(x,t)=\frac{1}{\sigma&space;}e^{-\frac{x^{2}}{2\sigma&space;^{2}}}" title="\rho (x,t)=\frac{1}{\sigma }e^{-\frac{x^{2}}{2\sigma ^{2}}}" /></a></div>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;既然扩散方程可以由大量粒子的格点随机游走得到，那我们不妨试试模拟初始时刻大量粒子聚集在原点的格点随机游走。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project3-2.py)

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_6-1.png?raw=true" /></div>

可见两种方法所得的粒子分布吻合程度相当高，这恰好印证了两种方法的一致性。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们接下来研究教材提到的奶油在咖啡中溶解的问题。该问题可合理简化为初始时刻在一个正方形区域内均匀分布的粒子的二维扩散问题。我们首先用扩散方程所得递推式进行模拟。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project4-1.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们用高度表示某一位置的粒子数密度，初始时刻的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-1%200.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=50" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=50" title="n=50" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-2%2050.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=200" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=200" title="n=200" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-3%20200.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=500" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=500" title="n=500" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-4%20500.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=1000" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=1000" title="n=1000" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-5%201000.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=2000" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=2000" title="n=2000" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-6%202000.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=4000" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=4000" title="n=4000" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-7%204000.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了更清楚地理解扩散方程和随机游走的联系，我们再用随机游走的方法模拟这个问题

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project4-2.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模拟所得不同时刻的粒子分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_1-3.png?raw=true" /></div>

可以看出，两种方法所得的粒子分布情况是一致的。

#### Ⅲ 扩散过程中的熵

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如之前所说，熵的统计学定义为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=S=-k\sum_{s}^{&space;}P_{s}\ln&space;P_{s}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S=-k\sum_{s}^{&space;}P_{s}\ln&space;P_{s}" title="S=-k\sum_{s}^{ }P_{s}\ln P_{s}" /></a></div>

运用该式，我们就可计算各种过程中的熵。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面我们就按习题**7.12**的要求来模拟计算奶油在咖啡中溶解过程中的熵随时间的变化。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project5-1.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模拟所得扩散过程中不同时刻的熵如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_7-1.png?raw=true" /></div>

可以看出，在奶油溶解的过程中，体系的熵一直在增加，且熵随时间（步数）变化的函数图像大致为一个向左平移后的对数函数。

###4. 结果讨论

* 扩散过程的本质是大量粒子的随机游走，但扩散方程本身却是确定性的。

* 用确定性的扩散方程和大量粒子随机游走模拟得到相同的结果，这昭示了大量在微观上行为服从一定概率分布的粒子在宏观上有确定性的规律来描述其行为。

* 扩散是一个自发行为，而伴随着这个自发行为，系统的熵自发地增加。

---

<h4 align="center">参考文献</h4>

**[1]**Nicholas J. Giordano，Hisao Nakanishi. 计算物理（第2版）[M]. 北京：清华大学出版社，2007.181-206.

**[2]**Y. Daniel Liang.RandomWalk[EB/OL].http://www.cs.armstrong.edu/liang/py/html/RandomWalk.html ，2016.

**[3]**tacaswell.Problems plotting a 2D random walk with Python[EB/OL].http://stackoverflow.com/questions/27282835/problems-plotting-a-2d-random-walk-with-python ，2014.

**[4]**Martin Evans.Plotting 3D random walk in Python[EB/OL].http://stackoverflow.com/questions/34920680/plotting-3d-random-walk-in-python ，2016. 

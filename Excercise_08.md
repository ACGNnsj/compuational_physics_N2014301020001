# Excercise_08


---
###1. 摘要
* **EXERCISES**

3.18. Calculate Poincaré sections for the pendulum as it undergoes the period-doubling route to chaos. Plot ω versus θ, with one point plotted for each drive cycle, as in Figure 3.9. Do this for <a href="http://www.codecogs.com/eqnedit.php?latex=F_{D}=1.4,&space;\:&space;1.44\:&space;and\:&space;1.465" target="_blank"><img src="http://latex.codecogs.com/gif.latex?F_{D}=1.4,&space;\:&space;1.44\:&space;and\:&space;1.465" title="F_{D}=1.4, \: 1.44\: and\: 1.465" /></a>, using the other parameters as given in connection with Figure 3.10. You should find that after removing the points corresponding to the initial transient the attractor in the period-1 regime will contain only a single point. Likewise, if the behavior is period n, the attractor will contain n discrete points.


---
###2. 背景
* **庞加莱映射**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在数学领域中，尤其是对动态系统的研究中，庞加莱映射，或第一次回归映射是连续动力系统的状态空间中的周期轨道与确定的低维子空间的横向交点，其中的低维子空间被称作庞加莱截面。更精确的说，对于具有初值位于庞加莱截面上的周期轨道，轨道第一次回到庞加莱截面上的交点就定义了初值的庞加莱映射，这就是第一次回归映射的由来。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;任何粒子在经历一个漫长的时间之后必然能回到其无限接近其初始位置的位置（但是不能回到原来位置，只能无限接近），尽管这个时间的长度远远超出我们所能想象，但是它必然会实现，这样一个周期就称为一个庞加莱回归。

* **单峰映象**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;单峰映象（logistic map）是种二次的多项式映射（递推关系式），是一个由简单非线性方程式产生混沌现象的经典范例。这种映射因生物学家Robert May在1976年发表的一篇论文而著名。单峰映象原本被Pierre François Verhulst用作一个人口学模型，后来应用在物种受到限制因素之下的数目。数学上可写成<a href="http://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}=rx_{n}(1-x_{n})" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{n&plus;1}=rx_{n}(1-x_{n})" title="x_{n+1}=rx_{n}(1-x_{n})" /></a>

其中

* <a href="http://www.codecogs.com/eqnedit.php?latex=x_{n}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{n}" title="x_{n}" /></a>是介于0和1之间的数，<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>表示在第年的物种数目。

* <a href="http://www.codecogs.com/eqnedit.php?latex=r" target="_blank"><img src="http://latex.codecogs.com/gif.latex?r" title="r" /></a>是正整数，是根据繁殖和饿死率而得出的数。

单峰映象是根据以下两个现象：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.当人口少时，繁殖增加的人口大致跟物种的原本总数目成正比；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.环境资源有一“最大容量”，当人口接近最大容量时，人口可能会下降。

可是在特定初始条件及参数时，单峰映象的人口模型会出现负的人口数，较早期使用的Ricker模型也有混沌现象，但没有这种问题。

r=4的单峰映象是位元移动映射及参数μ=2的帐篷映射的非线性变换。

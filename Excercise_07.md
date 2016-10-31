# Excercise_07
***

#### Exercise 3.12
In constructing the Poincaré section in Figure 3.9 we plotted points only at times that were in phase with the drive force; that is, at times <img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn.gif?raw=true" alt="" title="" />, where <img src="http://latex.codecogs.com/gif.latex?n" alt="" title="" /> is an integer. At these values of <img src="http://latex.codecogs.com/gif.latex?t" alt="" title="" /> the driving force passed through zero [see(3.18)]. However, we could jusi as easily have chosen to make the plot at times corresponding to a maximum of the drive force, or at times <img src="http://latex.codecogs.com/gif.latex?\pi/4" alt="" title="" /> out-of-phase with this force, etc. Construct the Poincaré sections for these cases and compare them with Figure 3.9.

#### Exercise 3.13
Write a program to calculate and compare the behavior of two, nearly identical pendulums. Use it to calculate the divergence of two nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent from the slope of a plot of <img src="http://latex.codecogs.com/gif.latex?log(\Delta\theta)" alt="" title="" /> as a function of <img src="http://latex.codecogs.com/gif.latex?t" alt="" title="" />.

#### Exercise 3.14
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent compare with that found in Figure 3.7?
***

###1. 理论推导
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;过去我们已经学习了一些单摆的基础知识，在无阻尼和驱动力且摆角很小的情况下单摆的动力学方程近似为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(1).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;显然， 这种情况下单摆近似地做简谐运动，有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(3).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果我们考虑阻尼，单摆的动力学方程会变为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(2).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这时，单摆将会做阻尼振动，有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(4).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此时单摆将做振幅逐渐减小的周期性阻尼振动，经过较长时间后，振幅几乎为零，可以认为振动停止。然而，如果有驱动力，情况又将大不一样，单摆的运动学方程变为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(5).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这时单摆做受迫振动，有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(6).gif?raw=true" alt="" title="" />
</div>
其中<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(7).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;然而，在摆角较大时，近似<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(8).gif?raw=true" alt="" title="" />不再成立，我们必须设法求解如下非线性方程

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(9).gif?raw=true" alt="" title="" />
</div>

###2.算法探讨
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们如果依然采用欧拉法，将得到发散的解，显然这与实际不符，在此我们采用欧拉-克罗默方法求数值解，步骤如下

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(10).gif?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(11).gif?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(12).gif?raw=true" alt="" title="" />
</div>

注意，若<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(13).gif?raw=true" alt="" title="" />不在区间<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(14).gif?raw=true" alt="" title="" />内，我们须通过加或减<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(15).gif?raw=true" alt="" title="" />使其落入区间内。

###3.程序模拟
**1.我们先研究比较不同参数下，摆角及角速度随时间的变化关系**

[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/Excercise_07.py)

我们取参数![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(16).gif?raw=true)

结果如下
![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/figure_1-1.png?raw=true)

* 可见，图1和图6是无驱动力的情况，单摆做欠阻尼振动，运动很快停止

* 但如果加上一定的驱动力，你会发现单摆的振动频率变得和驱动力一样，如图2和图7所示

* 当驱动力超过某一范围时，单摆进行大角摆动，其动力学方程不再能近似为线性微分方程，它的解不具有稳定性，初始条件做出微小的改变，会得到完全不同的解，如剩下的图所示，这是混沌现象的体现

**2.我们先来解决问题3.13和3.14**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在此我们研究两个单摆系统，参数与之前相同，但它们的初始摆角相差0.001rad

这里我们采用龙格-库塔法

[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/Excercise_07(1).py)

它们的摆角差取常用对数随时间的变化如下
![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/figure_1-2.png?raw=true)

根据![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(17).gif?raw=true)
观察得q=0.5时， 不同驱动力下对应的李雅普诺夫指数分别约为-0.25和0.1

而q=0.56时，不同驱动力下对应的李雅普诺夫指数均减小

**3.接着我们来解决问题3.12**

首先，我们画出一般的庞加莱截面图

[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/Excercise_07(2).py)

结果如下

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/figure_1-3.png?raw=true)

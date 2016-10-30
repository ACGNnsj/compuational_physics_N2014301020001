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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;然而我们如果采用欧拉法，将得到发散的解，显然与事实不符，在此我们采用欧拉-克罗默方法求数值解，步骤如下

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(10).gif?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(11).gif?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(12).gif?raw=true" alt="" title="" />
</div>

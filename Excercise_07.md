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
过去我们已经学习了一些单摆的基础知识，在无阻尼和驱动力且摆角很小的情况下单摆的动力学方程近似为
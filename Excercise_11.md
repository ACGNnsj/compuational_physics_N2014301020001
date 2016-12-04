# Excercise_11


---
###1. 摘要
* **EXERCISES**

4.19. Study the behavior of our model for Hyperion for different initial conditions. Estimate the Lyapunov exponent from calculations of Δθ, such as those shown in Figure 4.19. Examine how this exponent varies as a function of the eccentricity of the orbit. 

4.20. Our results for the divergence of the two trajectories θ1(t) and θ2(t) in the chaotic regime, shown on the right in Figure 4.19, are complicated by the way we dealt with the angle θ. In Figure 4.19 we followed the practice employed in Chapter 3 and restricted θ to the range -π to +π, since angles ouside this range are equivalent to angles within it. However, when during the course of a calculation the angle passes out of this range and is then 'reset' (by adding or subtracting 2π), this shows up in the results for Δθ as a discontinuous (and distrcting) jump. Repeat the calculation of Δθ as in Figure 4.19, but do not restrict the value of θ. This should remove the large (Δθ ～ 2π) jumps in Δθ in Figure 4.19, but the smaller and more frequent dips will remain. What is the origin of these dips? Hint: Consider the behavior of a pendulum near one of its turning points.

---
###2. 背景
* **三体问题**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;它是指三个质量、初始位置和初始速度都是任意的可视为质点的天体，在相互之间万有引力的作用下的运动规律问题。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;现在已知，三体问题不能精确求解，即无法预测所有三体问题的数学情景，只有几种特殊情况已研究。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;三体问题（three-body problem）最简单的一个例子就是太阳系中太阳、地球和月球的运动。在浩瀚的宇宙中，星球的大小可以忽略不记，所以我们可以把它们看成质点。如果不计太阳系其他星球的影响，那么它们的运动就只是在引力的作用下产生的，所以我们就可以把它们的运动看成一个三体问题。

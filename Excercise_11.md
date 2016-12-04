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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在1887年，为了祝贺自己的60岁寿诞，瑞典国王奥斯卡二世赞助了一项现金奖励的竞赛，征求太阳系的稳定性问题的解答，这是三体问题的一个变种。法国数学家庞加莱简化了问题，提出了限制性三体问题，即三体中其中两体的质量是如此之大，以至于第三体的质量完全不能对其造成任何扰动。面对这个问题，庞加莱运用了他发明的相图理论，并且最终发现了混沌理论。虽然庞加莱没有成功给出一个完整的解答，他的工作令人印象深刻，以至于他还是在1888年赢得了奖金。庞加莱发现这个系统的演变经常是混沌的，意思是说如果初始状态有一个小的扰动，例如一个体的初始位置有一个小的变动，则后来的状态可能会有极大的不同。如果该小变动不能被我们的测量仪器所探测，则我们不能预测最终状态为何。裁判之一，著名的数学家卡尔·魏尔施特拉斯说：“这个工作不能真正视为对所求的问题的完善解答，但是它的重要性使得它的出版将标志着天体力学的一个新时代的诞生。”

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;魏尔斯特拉斯并不知道他自己的预测有多准确。在庞加莱的论文中，他描述了例如同宿点（homoclinic points）之类的新思想。这些概念在1890年的Acta Mathematica备忘录中出版，后来该书在编辑途中被发现一个理论上的错误，然而该错误实际上导致了庞加莱一些进一步的发现，它们现在被视为混沌理论的开端。

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/sleptir.gif?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/rleptir.jpg?raw=true)

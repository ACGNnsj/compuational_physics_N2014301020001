# Exercise_11


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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;三体问题周期解在欧拉与拉格朗日之后就就进展很少。20世纪70年代，Roger Broucke和Michel Hénon用计算机进行模拟，得到了更多结果。现在，这些周期解上被分为3族。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2013年，这方面的研究获得又一个突破性进展，物理学家Milovan Suvakov和Veljko DmitraSinovic在《物理评论快报》（[Phys. Rev. Lett. 110, 114301 (2013)](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.114301)）上发表文章，宣布发现13族新的特解，三体问题特解的族数直接从3族扩充到16族。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面展示了三体运动特解中的3族曲线，左侧为抽象空间中的轨迹，右侧为对应的在真实空间中的轨迹。

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/sleptir.gif?raw=true)![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/rleptir.jpg?raw=true)

<div align=center>
蝴蝶类Ⅰ
</div>

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/skonjic.gif?raw=true)![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/rkonjic.jpg?raw=true)

<div align=center>
蜻蜓类
</div>

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/sleptir4.gif?raw=true)![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/rleptir4.jpg?raw=true)

<div align=center>
蝴蝶类Ⅳ
</div>

* **土卫七（Hyperion）**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;土卫七（Hyperion）是环绕土星运行的一颗卫星。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1848年美国天文学家邦德（G. Bond）和英国的拉塞尔（W. Lassell）各自独立发现土卫七，距土星1482000公里，像大星体的碎片，表面有如海绵，是目前所发现太阳系中最大的一颗非球形天体，也是太阳系中已知星体中极其罕见的自转会混沌的星体，每21.3天绕土星旋转一周。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;旅行者2号的照片以及随后的地面测光表明土卫七的自转是混沌的，更确切地说，它的自转轴大幅摆动以致于它在空间中的方向是不可预测的。它自转的李雅普诺夫时间为36天左右。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;土卫七以及冥卫二和冥卫三是太阳系中已知的少数几个自转是混沌的卫星，不过这种现象在双小行星中会比较常见。土卫七还是太阳系中唯一已知的未被潮汐锁定的规则卫星。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;土卫七在大行星中非常独特，因为它形状非常不规则，有一个离心率相当大的轨道，并且靠近一个比它大得多的卫星土卫六。这些因素共同作用导致了土卫七不能稳定自转。

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/Moons_of_solar_system-zh.svg.png?raw=true" alt="" title="" />
</div>

<div align=center>
太阳系部分卫星较诸地球大小图
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/hyperion2_cassini_big.jpg?raw=true" alt="" title="" />
</div>

<div align=center>
Authors & editors: Robert Nemiroff (MTU) & Jerry Bonnell (USRA)
</div>

---
###3. 正文

* **理论推导**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了模拟土卫七的运动，我们需要先对问题做一些简化：土卫七由两个被无质量杠固连的质点组成。每一质点所受引力为

<div align=center>
<a href="http://www.codecogs.com/eqnedit.php?latex=\vec{F_{i}}=-\frac{GM_{Sat}m_{i}}{r_{i}^{3}}\left&space;(&space;x_{i}\hat{i}&plus;y_{i}\hat{j}&space;\right&space;)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\vec{F_{i}}=-\frac{GM_{Sat}m_{i}}{r_{i}^{3}}\left&space;(&space;x_{i}\hat{i}&plus;y_{i}\hat{j}&space;\right&space;)" title="\vec{F_{i}}=-\frac{GM_{Sat}m_{i}}{r_{i}^{3}}\left ( x_{i}\hat{i}+y_{i}\hat{j} \right )" /></a>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;质点所受引力相对系统质心的力矩为

<div align=center>
<a href="http://www.codecogs.com/eqnedit.php?latex=\vec{\tau&space;_{i}}=\left&space;[&space;\left&space;(&space;x_{i}-x_{c}&space;\right&space;)\hat{i}&plus;\left&space;(&space;y_{i}-y_{c}&space;\right&space;)\hat{j}&space;\right&space;]\times&space;\vec{F_{i}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\vec{\tau&space;_{i}}=\left&space;[&space;\left&space;(&space;x_{i}-x_{c}&space;\right&space;)\hat{i}&plus;\left&space;(&space;y_{i}-y_{c}&space;\right&space;)\hat{j}&space;\right&space;]\times&space;\vec{F_{i}}" title="\vec{\tau _{i}}=\left [ \left ( x_{i}-x_{c} \right )\hat{i}+\left ( y_{i}-y_{c} \right )\hat{j} \right ]\times \vec{F_{i}}" /></a>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;又有

<div align=center>
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{d\vec{\omega&space;}}{dt}=\frac{\vec{\tau&space;_{1}}&plus;\vec{\tau&space;_{2}}}{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{d\vec{\omega&space;}}{dt}=\frac{\vec{\tau&space;_{1}}&plus;\vec{\tau&space;_{2}}}{2}" title="\frac{d\vec{\omega }}{dt}=\frac{\vec{\tau _{1}}+\vec{\tau _{2}}}{2}" /></a>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;质心系中，质点都绕质心旋转，其相对质心的转动惯量为

<div align=center>
<a href="http://www.codecogs.com/eqnedit.php?latex=I=m_{1}\left&space;|&space;r_{1}&space;\right&space;|^{2}&plus;m_{2}\left&space;|&space;r_{2}&space;\right&space;|^{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?I=m_{1}\left&space;|&space;r_{1}&space;\right&space;|^{2}&plus;m_{2}\left&space;|&space;r_{2}&space;\right&space;|^{2}" title="I=m_{1}\left | r_{1} \right |^{2}+m_{2}\left | r_{2} \right |^{2}" /></a>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代入化简得

<div align=center>
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{d\omega&space;}{dt}\approx&space;-\frac{3GM_{Sat}}{r_{c}^{5}}\left&space;(&space;x_{c}sin\theta&space;-y_{c}cos\theta&space;\right&space;)\left&space;(&space;x_{c}cos\theta&space;&plus;y_{c}sin\theta&space;\right&space;)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{d\omega&space;}{dt}\approx&space;-\frac{3GM_{Sat}}{r_{c}^{5}}\left&space;(&space;x_{c}sin\theta&space;-y_{c}cos\theta&space;\right&space;)\left&space;(&space;x_{c}cos\theta&space;&plus;y_{c}sin\theta&space;\right&space;)" title="\frac{d\omega }{dt}\approx -\frac{3GM_{Sat}}{r_{c}^{5}}\left ( x_{c}sin\theta -y_{c}cos\theta \right )\left ( x_{c}cos\theta +y_{c}sin\theta \right )" /></a>
</div>

该式是我们进行数值模拟的依据

* **算法探讨**

我们采用欧拉—— 克罗姆方法进行数值模拟。

* **程序模拟**

[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/Exercise_11.py)

> 图1: <a href="http://www.codecogs.com/eqnedit.php?latex=v_{0}=2\pi&space;,\theta&space;_{0}=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{0}=2\pi&space;,\theta&space;_{0}=0" title="v_{0}=2\pi ,\theta _{0}=0" /></a>，故而有离心率<a href="http://www.codecogs.com/eqnedit.php?latex=e=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?e=0" title="e=0" /></a>即轨道为圆轨道。

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/figure_1-1.png?raw=true" alt="" title="" />，故而有离心率<a href="http://www.codecogs.com/eqnedit.php?latex=e=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?e=0" title="e=0" /></a>即轨道为圆轨道。
</div>

[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/Exercise_11(1).py)

> 图2: <a href="http://www.codecogs.com/eqnedit.php?latex=v_{0}=2\pi&space;,\omega&space;_{0}=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{0}=2\pi&space;,\omega&space;_{0}=0" title="v_{0}=2\pi ,\omega _{0}=0" /></a>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_11/figure_1-2.png?raw=true" alt="" title="" />
</div>

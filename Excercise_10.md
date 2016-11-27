# Excercise_10


---
###1. 摘要
* **EXERCISES**

4.9. In this section we saw that orbits are unstable for any value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> that is not precisely 2 in (4.12). A related question, which we did not address (until now), is how unstable an orbit might be. That is, how long will it take for an unstable orbit to become obvious. The answer to this question depends on the nature of the orbit. If the intial velocity is chosen so as to make the orbit precisely circular, then the value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> in (4.12) will make absolutely no difference. Of course, in practice it is impossible to construct an orbit that is exactly circular, so the instabilities when <img src="http://latex.codecogs.com/gif.latex?\beta\neq2" alt="" title="" /> will always be apparent given enough time. Even so, orbits that start out as nearly circular will remain almost stable for a longer period than those that are highly elliptical. Investigate this by studying orbits with the same value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> (say, <img src="http://latex.codecogs.com/gif.latex?\beta=2.05" alt="" title="" /> and comparing the behavior with different values of the ellipticity of the orbit. You should find that the orientation of orbits that are more nearly circular will rotate more slowly than those that are highly elliptical.

4.11. Investigate how the precession of the perihelion of a planet's orbit due to general relativity varies as a function of the eccentricity of the orbit. Study the precession of different elliptical orbits with different eccentricities, but with the same value of the perihelion. Let the perihelion have the same value as for Mercury, so that you can compare it with the results shown in this section.


---
###2. 背景
* **伯特兰定理**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在经典力学里，伯特兰定理阐明，只有两种位势<img src="http://latex.codecogs.com/gif.latex?V" alt="" title="" />可以给出闭合轨道：

①平方反比有心力给出的连心势，像引力势或静电势，以方程表示为

<div align=center>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/5edce25c42d4dd1a06c3578ef827db91a7062925" alt="" title="" />
</div>

<div align=center>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/NewtonsLawOfUniversalGravitation.svg/400px-NewtonsLawOfUniversalGravitation.svg.png" alt="" title="" />
</div>

②径向谐振子势：

<div align=center>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e78eabd2ab0a83cea507a587827b3b792a342a24" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/2016112800022516_0.gif?raw=true" alt="" title="" />
</div>

其中， r是径向坐标， k是正值常数。假若物体从某位置移动，经过一段路径后，又回到原先位置，则称此路径为闭合轨道。

这两种情况分别对应β=2和β=-1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1687年，物理泰斗艾萨克·牛顿在巨著《自然哲学的数学原理》里发表的万有引力定律，解释了为什么行星绕着太阳的公转运动会遵守开普勒定律。在这之后，许多科学家开始研究，当行星的运动稍许偏离了这轨道的时候，可能会发生的状况？其中一个问题为：轨道是否仍旧是闭合的？但是，经过多年的探讨，科学家都无法给出合理的解答。一直要等到1873年，法国数学家约瑟·伯特兰发表伯特兰定理，才正确地解析这问题。对于经典天体力学研究，这定理非常的重要；在宇宙遥远的那一边，万有引力的性质是否仍旧保持不变？伯特兰定理给予实验者一个精确的方法，来测试万有引力的平方反比性质。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在现代物理学里，理论物理学家发现，由于广义相对论效应，引力势轨道是非闭合的。天文学家作实验观测到，水星绕着太阳公转的椭圆轨道，其近拱点呈缓慢进动状态。所以，当涉及广义相对论的领域，伯特兰定理不成立。

* **进动**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;进动（precession）是自转物体之自转轴又绕着另一轴旋转的现象，又可称作旋进。在天文学上，又称为“岁差现象”。

常见的例子为陀螺。当其自转轴的轴线不再呈铅直时，即自转轴与对称轴不重合不平行时，会发现自转轴会沿着铅直线作旋转，此即“旋进”现象。另外的例子是地球的自转。

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/axis.precession.jpg?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于量子物体如粒子，其带有自旋特征，常将之类比于陀螺自转的例子。然而实际上自旋是一个内禀性质，并不是真正的自转。粒子在标准的量子力学处理上是视为点粒子，无法说出一个点是怎样自转。若要将粒子视为带质量球状物体来计算，以电子来说，会发现球表面转速超过光速，违反狭义相对论的说法。

自旋的进动现象主要出现在核磁共振与磁振造影上。其中的例子包括了稳定态自由旋进（进动）造影。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;进动是转动中的物体自转轴的指向变化。在物理学中，有两种类型的进动，自由力矩和诱导力矩，此处对后者的讨论会比较详细。在某些文章中，"进动"可能会提到地球经验的岁差，这是进动在天文观测上造成的效应，或是物体在轨道上的进动。

**①岁差** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;岁差是地球自转中的一种大尺度微小变化。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;典型的岁差例子是在公元前若干世纪，3月份的平分点（即春分点）落在白羊宫与双鱼宫的交界处，于是30°的白羊宫便大致与白羊座恒星重合。但是这个框架会经历日积月累的微小变化，这种变化就物理学上称为进动，而天文学上称为岁差，它的一个中等长度的周期是25,868年，在这个时间里，地球极绕黄道极（像陀螺仪那样）缓慢旋转。每年，当太阳返回0°白羊宫时，它相对于背后群星的位置将后移约50弧秒，即约71年移动1°。

<div align=center>
<img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Precession_and_seasons_%28zh%29.jpg" alt="" title="" />
</div>

**②行星轨道的进动** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;行星在轨道上绕行太阳的公转运动也是一种旋转的运动现象，（在这些事件中，行星和太阳结合的系统也是在旋转的。）所以行星轨道平面的转轴会随着时间产生进动。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;每颗行星椭圆轨道的长轴在他的轨道平面内也会发生进动，以回应其他行星的引力改变所施加的摄动，这称为近日点进动或是拱点进动。观察到的水星近日点进动与古典力学理论预测的数值不能吻合，每百年差了43" ，突显了爱因斯坦相对论的正确，消除了观测与理论上的歧异。

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/merc_adv.gif?raw=true" alt="" title="" />
</div>

---
###3. 正文

* **理论推导**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据牛顿万有引力定律，我们有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/1111.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由牛顿第二定律，可得

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/2.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在坐标(x,y)处，我们有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/3.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们将行星受力分解到x方向和y方向上，从而(2)式变为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/4.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在太阳系中，我们可得

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/5.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们将上述方程写成以下形式，以便进行数值求解

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/6.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;实际在太阳系中，行星轨道为椭圆轨道，我们有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/7.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从而半长轴a为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/8.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在近日点和远日点分别有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/9.png?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;广义相对论下万有引力公式近似为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/10.png?raw=true" alt="" title="" />
</div>

* **算法探讨**

根据课本建议，我们采用欧拉—— 克罗姆方法进行数值模拟。

* **程序模拟**

[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_10/Exercise_10.py)

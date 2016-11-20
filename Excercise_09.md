# Excercise_09


---
###1. 摘要
* **EXERCISES**

3.30. Investigate the Lyapunov exponent of the stadium billiard for several values of <a href="http://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a>. You can do this qualitatively by examining the behavior for only one set of initial conditions for each value of  you consider, or more quantitatively by averaging over a range of initial conditions for each value of <a href="http://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a>.

3.31. Study the behavior for other types of tables. One interesting possibility is a square table with a circular interior wall located either in the center, or slightly off-center. Another possibility is an elliptical table.


---
###2. 背景
* **洛伦茨吸引子**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;洛伦茨吸引子是洛伦茨振子（Lorenz oscillator）的长期行为对应的分形结构，以爱德华·诺顿·洛伦茨的姓氏命名。洛伦茨振子是能产生混沌流的三维动力系统，是一种吸引子，以其双纽线形状而著称。映射展示出动力系统（三维系统的三个变量）的状态是如何以一种复杂且不重复的模式，随时间的推移而演变的。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;洛伦茨吸引子及其导出的方程组是由爱德华·诺顿·洛伦茨于1963年发表，最初是发表在《大气科学杂志》（Journal of the Atmospheric Sciences）杂志的论文《Deterministic Nonperiodic Flow》中提出的，是由大气方程中出现的对流卷方程简化得到的。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这一洛伦茨模型不只对非线性数学有重要性，对于气候和天气预报来说也有着重要的含义。行星和恒星大气可能会表现出多种不同的准周期状态，这些准周期状态虽然是完全确定的，但却容易发生突变，看起来似乎是随机变化的，而模型对此现象有明确的表述。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从技术角度看来，洛伦茨振子具有非线性、三维性和确定性。2001年，沃里克·塔克尔（Warwick Tucker）证明出在一组确定的参数下，系统会表现出混沌行为，显示出人们今天所知的奇异吸引子。这样的奇异吸引子是豪斯多夫维数在2与3之间的分形。彼得·格拉斯伯格（Peter Grassberger）已于1983年估算出豪斯多夫维数为2.06 ± 0.01，而关联维数为2.05 ± 0.01。

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/1.gif?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/Free-Converter.com-lorenz_attractor_boxed-12480943.png?raw=true" alt="" title="" />
</div>

<div align=center>
洛伦茨方程的一条轨迹的三维结构
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/1.jpg?raw=true" alt="" title="" />
</div>

<div align=center>
Paul Bourke作出的洛伦兹吸引子的3D图象
</div>

* **蝴蝶效应(台球效应)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;蝴蝶效应是指在一个动态系统中，初始条件下微小的变化能带动整个系统的长期的巨大的连锁反应，是一种混沌的现象。“蝴蝶效应”在混沌学中也常出现。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1961年冬天，美国气象学家爱德华·罗伦兹在使用计算机程序来计算他所设计来模拟大气中空气流动的数学模型，在进行第二次计算时，想要省事，直接从程式的中段开始执行，并输入前一次模拟结果打印出来的数据，计算出来的结果却与第一次完全不同。经检查后发现原因是出在打印的数据是0.506，精准度只有小数后3位，但该数据正确的值为0.506127，到小数后6位。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1963年，罗伦兹发表论文“决定性的非周期流”（Deterministic Nonperiodic Flow），分析了这个效应。这篇论文后来被广泛引用。他也在另一篇期刊文章写道，“一个气象学家提及，如果这个理论被证明正确，一只海鸥扇动翅膀足以永远改变天气变化。”在以后的演讲和论文中他用了更加有诗意的蝴蝶。对于这个效应最常见的阐述是“一只蝴蝶在巴西轻拍翅膀，可以导致一个月后德克萨斯州的一场龙卷风。”

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/Sensitive-dependency.svg.png?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/c5b7fc24b899a901bf7055c61c950a7b0308f505.jpg?raw=true" alt="" title="" />
</div>

---
###3. 正文

* **台球动力系统**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;台球动力系统是一个粒子沿直线匀速运动并在边界发生镜面反射的动力系统。当粒子击中边界发生反射时它不会损失动能。台球动力系统是哈密顿理想化的台球游戏，但其边界可以是矩形等其他形状，甚至可以是多维的。台球动力系统也可以被用于研究非欧几何。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;台球动力系统拥有哈密顿系统从可积性到混沌运动的所有复杂性，无须对运动方程进行困难的积分就可确定其庞加莱截面。乔治·大卫·比尔霍夫证明一个椭圆边界的台球动力系统是可积的。

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/maxresdefault.jpg?raw=true" alt="" title="" />
</div>


<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/longorbit.jpg" alt="" title="" />
</div>

<div align=center>
一个混沌台球动力系统中粒子的轨迹
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_09/4-Figure4-1.png?raw=true" alt="" title="" />
</div>



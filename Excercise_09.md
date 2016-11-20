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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1961年冬天，罗伦兹在使用计算机程序来计算他所设计来模拟大气中空气流动的数学模型，在进行第二次计算时，想要省事，直接从程式的中段开始执行，并输入前一次模拟结果打印出来的数据，计算出来的结果却与第一次完全不同。经检查后发现原因是出在打印的数据是0.506，精准度只有小数后3位，但该数据正确的值为0.506127，到小数后6位。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这一次的经验，罗伦兹发现到他的数学模型，对初期某一个变数的小小变异，会影响到最后的结果，并可能发生很大的差异。他所设计的数学模型，有12个变数，可以发展出非常多发散的气候模型出来，让他得到一个认知，就是天气是不停变动的，根本无法被正确预测。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1963年，罗伦兹将他设计的数学模型，与研究发现写成影响深远的论文“决定性的非周期流”（Deterministic Nonperiodic Flow），该论文可求出无限解的数学模型，被称为“洛伦茨吸引子”（Lorenz attractor）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1972年12月29日，罗伦兹在美国科学促进会举办的第139届年会上，发表了著名的题为“可预测性：一只蝴蝶在巴西扇动翅膀会在德克萨斯引起龙卷风吗？”的演讲。

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

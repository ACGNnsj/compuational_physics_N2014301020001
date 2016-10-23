# Excercise_06
***

作业2.10


#### 2.10 Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher and lower than the cannon. Also investigate how the minimum firing velocity required to hit the target varies as the altitude of the target is varied.

附：在原题的基础上引入迎面风阻

***
#### 为了简化问题，我将固定一些参量，但该方法适用于所有情况
***

**这次我选用棒球的阻力系数来模拟炮弹的情况**

即![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/CodeCogsEqn.gif?raw=true)

其中![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/CodeCogsEqn%20(1).gif?raw=true)

**此外，我们还要引入迎面风阻 **

阻力表达式变为

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/CodeCogsEqn%20(2).gif?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/CodeCogsEqn%20(3).gif?raw=true)

**关于海拔高度的影响和绝热模型和上次作业一致，有 **

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/raw/master/Excercise_05/CodeCogsEqn%20(2).gif?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/raw/master/Excercise_05/CodeCogsEqn%20(1).gif?raw=true)

***
 
### 设计思路

显然，想要找出可以打中目标的最小发射速度，在固定水平距离和竖直高度两个参数的基础上至少需要发射角度和发射速度两个变量。我们可以嵌套循环对两个变量进行双重扫描，从而找到给定的水平距离和竖直高度下 的最小发射速度。

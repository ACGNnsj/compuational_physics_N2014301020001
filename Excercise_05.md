# Excercise_04
***

* 作业2.9


#### 2.9 Calculate the trajectory of our cannon shell including both air drag and the reduced air density at high altitudes so that you can reproduce the results in Figure 2.5. Perform your calculation for different firing angles and determine the value of the angle that gives the maximum range.
***

###1. 理论推导
  
  忽略空气密度变化时的空气阻力近似为 ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn.gif?raw=true)
  
  在绝热的近似处理下空气密度与高度的关系为 ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(2).gif?raw=true)
  
  从而考虑空气密度变化的情况下空气阻力应为 ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(1).gif?raw=true)亦及 ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(3).gif?raw=true)
  
根据牛顿第二定律有 ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(8).gif?raw=true)， ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(9).gif?raw=true)

为方便计算将![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(12).gif?raw=true)正交分解如下（![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(13).gif?raw=true)同理，乘上对应密度系数即可）![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(10).gif?raw=true)，![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(11).gif?raw=true)

###2. 近似计算

  据上述结果运用欧拉法有
  
  ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(4).gif?raw=true)
  
  ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(5).gif?raw=true)
  
  ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(6).gif?raw=true)
  
  ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/CodeCogsEqn%20(7).gif?raw=true)
  
###3.程序模拟


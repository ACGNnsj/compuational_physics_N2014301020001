# Excercise_04
***

## **1.Abstract（摘要）**
* 作业1.5


#### *1.5. Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are

![公式1](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN_B%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_A%7D%7B%5Ctau%7D%2C)

![公式2](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_B%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN_A%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_B%7D%7B%5Ctau%7D%2C)

#### where for simplicity we have assumed that the two types of decay are characterized by the same time constant, <img src="http://latex.codecogs.com/gif.latex?\tau." alt="" title="" /> Solve this system of equations for the numbers of nuclei, <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?N_B" alt="" title="" />, as functions of time. Consider different initial conditions, such as ![公式4](http://latex.codecogs.com/gif.latex?N_A%20%3D%20100%2C) ![公式5](http://latex.codecogs.com/gif.latex?N_B%20%3D%200%2C) etc., and take ![公式6](http://latex.codecogs.com/gif.latex?%5Ctau%20%3D%201) s. Show that your numerical results are consistent with the idea that the system reaches a stteady state in which <img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?N_B" alt="" title="" /> are constant. In such a steady state, the time derivatives <img src="http://latex.codecogs.com/gif.latex?dN_A/dt" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?dN_B/dt" alt="" title="" /> should vanish.
***

## **2.Background（背景介绍）**
* **Double Decay:**

####　ProblemJust as the qustion-stems indicates, a better analogy for this problem would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energys. Although it is a decay problem with two types of nuclei, considering that the total number of two types of nuclei is constant, we can readily solve it in the same way as in the single decay problem.

* **The Euler Method:**

####　Still, I choose to use Euler method to deal with this problem. The principle of it, as we have all learned, is Taylor expansion. And the routine process is to substitute the given ordinary differential equation into the first-order derivative of the Taylor expansion and neglect infinitesimals of hiher order.

***

## **3.Main（正文）**
### 思路
* **求解析解**
观察关系式可知两未知变量地位完全对等且它们的和为一常数，我们不妨设该常数为N并选一个变量进行求解。

![公式7](http://latex.codecogs.com/gif.latex?N%20%3D%20N_A%20&plus;%20N_B%20%3D%20N_A%280%29%20&plus;%20N_B%280%29%20%3D%20N_A%28t%29%20&plus;%20N_B%28t%29)

![公式8](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%28t%29%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN%20-%20N_A%28t%29%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_A%28t%29%7D%7B%5Ctau%7D%20%3D%20%5Cfrac%7BN%20-%202N_A%28t%29%7D%7B%5Ctau%7D)

![公式9](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%28t%29%7D%7BN%20-%202N_A%28t%29%7D%20%3D%20%5Cfrac%7Bdt%7D%7B%5Ctau%7D)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/CodeCogsEqn.gif?raw=true)

显然，当![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/CodeCogsEqn%20(1).gif?raw=true)时，上两式不成立，易知，此时有![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/CodeCogsEqn%20(2).gif?raw=true)。

其他情况下，可以解得![公式14](http://latex.codecogs.com/gif.latex?N_A%28t%29%20%3D%20%5Cfrac%7BN%7D%7B2%7D%20-%20%5Cfrac%7BN%20-%202N_A%280%29%7D%7B2%7De%5E%7B-%20%5Cfrac%7B2t%7D%7B%5Ctau%7D%7D) 

* **求数值解**

首先，我们在t=0附近对<img src="http://latex.codecogs.com/gif.latex?N_A" alt="" title="" />进行泰勒展开：

![公式16](http://latex.codecogs.com/gif.latex?N_A%28%5CDelta%20t%29%20%3D%20N_A%280%29%20&plus;%20%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7Bd%5E2N_A%7D%7Bdt%5E2%7D%20%28%5CDelta%20t%29%5E2%20&plus;%20%5Cdots%20%2C)

如果![公式17](http://latex.codecogs.com/gif.latex?%5CDelta%20t)取得足够小，我们可以略去高阶无穷小项，得到

![公式19](http://latex.codecogs.com/gif.latex?N_A%28%5CDelta%20t%29%20%5Capprox%20N_A%280%29%20&plus;%20%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t)

同样，我们可以通过导数的定义得到该结果

![公式20](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%7D%7Bdt%7D%20%5Cequiv%20%5Clim_%7B%5CDelta%20t%20%5Crightarrow%200%20%7D%5Cfrac%7BN_A%28t%20&plus;%20%5CDelta%20t%29%20-%20N_A%28t%29%7D%7B%5CDelta%20t%7D%20%5Capprox%20%5Cfrac%7BN_A%28t%20&plus;%20%5CDelta%20t%29%20-%20N_A%28t%29%7D%7B%5CDelta%20t%7D)

第二步中我们将![公式17](http://latex.codecogs.com/gif.latex?%5CDelta%20t)取得足够小，但不为0，移项可得

![公式22](http://latex.codecogs.com/gif.latex?N_A%28t%20&plus;%20%5CDelta%20t%29%20%5Capprox%20N_A%28t%29%20&plus;%20%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t)

在该问题中，我们已知![公式8](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%28t%29%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN%20-%20N_A%28t%29%7D%7B%5Ctau%7D%20-%20%5Cfrac%7BN_A%28t%29%7D%7B%5Ctau%7D%20%3D%20%5Cfrac%7BN%20-%202N_A%28t%29%7D%7B%5Ctau%7D)，从而有

 ![公式23](http://latex.codecogs.com/gif.latex?N_A%28t%20&plus;%20%5CDelta%20t%29%20%5Capprox%20N_A%28t%29%20&plus;%20%5Cfrac%7BN%20-%202N_A%7D%7B%5Ctau%7D%5CDelta%20t)
 
### 程序设计和结果分析

**首先，完全按照教案上的模板编写并运行第一个程序**

#### [　　代码](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/Excercise_04(1).py)

#### [　　数据](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/nuclei_decay_data(1).txt)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/figure_1.png?raw=true)

　　***我们可以看到，它确实展示了该初始条件下的变化状况，但光这样还不够。***

***

**因此，我们再在另两种初始条件下进行数值模拟。**

* **情况2:　NA = 75,　NB = 25**

#### [　　代码](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/Excercise_04(2).py)

#### [　　数据](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/nuclei_decay_data(2).txt)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/figure_2.png?raw=true)

* **情况3:　NA = 50,　NB = 50**

#### [　　代码](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/Excercise_04(3).py)

#### [　　数据](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/nuclei_decay_data(3).txt)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/figure_3.png?raw=true)

* **汇总对比图**

#### [　　代码](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/Excercise_04(4).py)

#### [　　数据](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/nuclei_decay_data(4).txt)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_04/figure_4.png?raw=true)

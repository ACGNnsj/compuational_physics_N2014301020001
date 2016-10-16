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

```python
import pylab as pl
import math
pl.ion()
#给定初始条件，计算轨迹
class cannon_shell:
    def __init__(self, init_v = 0, init_theta = 0, time_step = 0):
        self.x = [0]
        self.y = [0]
        self.init_theta = init_theta
        self.vx = [init_v * math.cos(self.init_theta / 180 * math.pi) / 1000]
        self.vy = [init_v * math.sin(self.init_theta / 180 * math.pi) / 1000]
        self.dt = time_step
        self.C = 0
        self.g = 9.8E-3
    def launch(self):
        i = 0
        while(True):
            self.C = 4E-2 * math.pow(1 - 6.5 * self.y[i] / 288.15, 2.5)
            self.x.append(self.x[i] + self.vx[i] * self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i] - self.C * math.hypot(self.vx[i], self.vy[i]) * self.vx[i] * self.dt)
            self.vy.append(self.vy[i] - self.g * self.dt - self.C * math.hypot(self.vx[i], self.vy[i]) * self.vy[i] * self.dt)
            i += 1
            if self.y[i] < 0:
                break
#利用所得x轴两侧最近的两点近似计算曲线与x轴的交点
        self.x[i] = -self.y[i-1] * (self.x[i] - self.x[i-1]) / (self.y[i] - self.y[i-1]) + self.x[i-1]
        self.y[i] = 0
#求给定初速度下的最大落地距离及对应发射角度
class maximum_range(cannon_shell):
    def find(self):
        max_range = 0
        temp_max = 0
        init_theta = 0
        print("\n--------------")
        print("正在计算此初速度下最大落地距离，预计需几十秒，请耐心等待...\n")
        while(True):
            cannon_shell.__init__(self, user_input.init_v, init_theta, user_input.time_step)
            cannon_shell.launch(self)
            temp_max = self.x[-1]
            if (max_range <= temp_max):
                max_range = temp_max
                init_theta += 0.1
            else:
                init_theta -= 0.1
                break
        print("初速度：", user_input.init_v, "m/s")
        print("计算间隔：", user_input.time_step, "s")
        print("在此初速度下最大落地距离为: %.4f km"%max_range)
        print("最大落地距离对应的发射角为: %.1f °"%init_theta)
#绘制运动轨迹
class show_results:
    def show_results_1(self):
        pl.figure(1)
        pl.title('Cannon Shell')
        pl.xlabel('x / $km$')
        pl.ylabel('y / $km$')
        pl.grid()
        pl.show()
    def show_results_2(self):
        pl.figure(1)
        pl.plot(self.x, self.y,label = "angle: %.1f °"%self.init_theta)
        pl.draw()
        pl.legend()
        print("\n初速度：", user_input.init_v, "m/s")
        print("计算间隔：", user_input.time_step, "s")
        print("发射角度：", self.init_theta, "°")
        print("落地距离：%.4f km"%self.x[-1], "\n")
#用户输入初始值
class user_input:
    num_str_in = input("请输入初速度（m/s),计算间隔dt（s）的值,并用空格隔开:\n")
    num = [float(n) for n in num_str_in.split()]
    init_v = num[0]
    time_step = num[1]
#用户输入不同的初始角度值，并输出结果曲线
class user_output:
    start = cannon_shell()
    show_results.show_results_1(start)
    while(True):
        init_theta = float(input("--------------\n输入初始角度（角度制，0~180）（输入999开始计算最大落地距离）:\n"))
        if init_theta != 999:
            start = cannon_shell(user_input.init_v, init_theta, user_input.time_step)
            start.launch()
            show_results.show_results_2(start)
        else:
                break
    start = maximum_range(user_input.init_v, init_theta, user_input.time_step)
    start.find()
#运行程序
user_input()
user_output()
end = input("\n\n\n按下回车结束程序...")
```

###4.结果分析

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/QQ%E6%88%AA%E5%9B%BE20161017013021.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/QQ%E6%88%AA%E5%9B%BE20161017013214.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/QQ%E6%88%AA%E5%9B%BE20161017013546.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/QQ%E6%88%AA%E5%9B%BE20161017013258.png)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/QQ%E6%88%AA%E5%9B%BE20161017013341.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_05/QQ%E6%88%AA%E5%9B%BE20161017013705.png?raw=true)

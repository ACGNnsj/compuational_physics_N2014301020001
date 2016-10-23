# Excercise_06
***

作业2.10


#### 2.10 Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher and lower than the cannon. Also investigate how the minimum firing velocity required to hit the target varies as the altitude of the target is varied.

附：在原题的基础上引入迎面风阻

***

**关于海拔高度的影响和绝热模型和上次作业一致，有**

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/raw/master/Excercise_05/CodeCogsEqn%20(2).gif?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/raw/master/Excercise_05/CodeCogsEqn%20(1).gif?raw=true)

**此外，我们还要引入迎面风阻**

阻力表达式变为

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/CodeCogsEqn%20(2).gif?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/CodeCogsEqn%20(3).gif?raw=true)
***
 
### 解决思路

算法上我们依然和上次作业一样使用欧拉法。

显然，想要找出可以打中目标的最小发射速度，在给定风速、水平距离和竖直高度三个参数的基础上至少需要发射角度和发射速度两个变量。我们可以嵌套循环对两个变量进行双重扫描，从而找到给定的水平距离和竖直高度下的最小发射速度。

此外，找到最小发射速度后，我们以其为中心建立新的扫描区间，并以上次扫描步幅的十分之一进行扫描，如此往复数次。这种末端精确扫描的方法既能节省计算资源，又能获得较精确的结果。

***
 
### 程序模拟

```python
import math
#轨迹计算的基本算法
class cannon_shell:
    def __init__(self, init_v = 0, init_theta = 0, time_step = 0, target_altitude = 0, wind_speeed = 0):
        self.x = [0]
        self.y = [0]
        self.init_v = init_v
        self.init_theta = init_theta
        self.vx = [self.init_v * math.cos(self.init_theta / 180 * math.pi) / 1000]
        self.vy = [self.init_v * math.sin(self.init_theta / 180 * math.pi) / 1000]
        self.v_wind = wind_speeed / 1000
        self.dt = time_step
        self.C = 0
        self.h = target_altitude
    def launch(self):
        i = 0
        j = 0
        global high_enough
        global math_error
        math_error = True
        loop_launch = True
        while(loop_launch):
            if (1 - 6.5 * self.y[i] / 288.15) < 0:
                math_error = False
                break
            self.C = 4E-2 * math.pow(1 - 6.5 * self.y[i] / 288.15, 2.5)
            self.x.append(self.x[i] + self.vx[i] * self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i] - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * abs(self.vx[i] - self.v_wind) * self.dt)
            self.vy.append(self.vy[i] - 9.8E-3 * self.dt - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * self.dt)
            i += 1
            if (self.y[i] < self.y[i-1]) and (self.y[i-1] < self.h):
                high_enough = False
                loop_launch = False
            if (self.y[i] > self.h) or j:
                j += 1
            if (self.y[i] < self.h) and j:
                loop_launch = False
        if self.y[i-1] > self.h:
            self.x[i] = -(self.y[i-1] - self.h) * (self.x[i] - self.x[i-1]) / (self.y[i] - self.y[i-1]) + self.x[i-1]
            self.y[i] = self.h
            high_enough = True
#继承轨迹计算的基本算法
class shoot(cannon_shell):
    #找到初速度一定时炮弹所能达到的最远距离
    def find_maxrange(self):
        self.max_range = 0
        self.max_range_theta = self.theta_begin
        temp_max = 0
        loop_maxrange = True
        while(loop_maxrange):
            cannon_shell.__init__(self, self.v, self.max_range_theta, user_input.time_step, user_input.target_y, user_input.wind_speeed)
            cannon_shell.launch(self)
            temp_max = self.x[-1]
            if high_enough and math_error:
                if self.max_range <= temp_max:
                    self.max_range = temp_max
                    self.max_range_theta += self.theta_step
                else:
                    self.max_range_theta -= self.theta_step
                    loop_maxrange = False
            else:
                self.max_range_theta += self.theta_step
            if self.max_range_theta > self.theta_stop:
                loop_maxrange = False
    #扫描范围及扫描步长
    def detal(self):
        if self.C == 0:
            self.detal_i = 0
            self.v_step = 10
            self.theta_step = 1
            self.v_begin = 0
            self.v_stop = 1000
            self.theta_begin = 0
            self.theta_stop = 90
            print("第一层循环需要的时间比较多，请耐心等待。。。\n\n", [self.v_begin, self.v_stop, self.v_step], [self.theta_begin, self.theta_stop, self.theta_step], "\n")
        else:
            self.v_begin = round(self.temp_v, self.detal_i - 1) - 2 * self.v_step
            self.v_stop = round(self.temp_v, self.detal_i - 1) + 2 * self.v_step
            self.theta_begin = round(self.temp_theta, self.detal_i) - 2 * self.theta_step
            self.theta_stop = round(self.temp_theta, self.detal_i) + 2 * self.theta_step
            self.v_step = round(self.v_step / 10, self.detal_i)
            self.theta_step = round(self.theta_step / 10, self.detal_i + 1)
            print([round(self.v_begin, self.detal_i - 1), round(self.v_stop, self.detal_i - 1), round(self.v_step, self.detal_i)], [round(self.theta_begin, self.detal_i), round(self.theta_stop, self.detal_i), round(self.theta_step, self.detal_i + 1)], "\n")
            self.detal_i += 1
    #找到距离靶点最近落点所对应的初始速度
    def find_close_v(self):
        self.temp_v = 0
        self.temp_theta = 0
        self.d = 0
        self.v = self.v_begin
        loop_v = True
        while(loop_v):
            shoot.find_maxrange(self)
            if high_enough and self.max_range >= user_input.target_x:
                self.temp_v = self.v
                self.temp_theta = self.max_range_theta
                self.d = self.max_range - user_input.target_x
                loop_v = False
            self.v += self.v_step
            if self.v > self.v_stop:
                loop_v = False
    #根据循环层数进行循环计算
    def find(self):
        temp_loop_level = 0
        loop_find = True
        print("\nexpected loop_level: %.i"%user_input.loop_level, "\n---------------------\n")
        while(loop_find):
            shoot.detal(self)
            shoot.find_close_v(self)
            print("最小初速度为：", round(self.temp_v, (self.detal_i - 1)), "m/s")
            print("对应的发射角为：", round(self.temp_theta, (self.detal_i)), "°")
            print("与靶点的横向误差为：", self.d * 1000, "m")
            temp_loop_level +=1
            print("\nloop_level = ", temp_loop_level, "\n---------------------")
            if temp_loop_level >= user_input.loop_level:
                loop_find = False
        print("\n最小初速度为：", round(self.temp_v, (self.detal_i - 1)), "m/s")
        print("对应的发射角为：", round(self.temp_theta, (self.detal_i)), "°")
        print("与靶点的横向误差为：", self.d * 1000, "m")

#用户输入
class user_input:
    num_str_in = input("请输计算间隔dt（s）,横向风速（m/s）,靶点横向距离（km）,靶点纵向高度（km）,计算层数的值,并用空格隔开:\n")
    num = [float(n) for n in num_str_in.split()]
    init_v = 0
    init_theta = 0
    time_step = num[0]
    wind_speeed = num[1]
    target_x = num[2]
    target_y = num[3]
    loop_level = num[4]

#运行程序
user_input()
start = shoot(user_input.init_v, user_input.init_theta, user_input.time_step, user_input.target_y, user_input.wind_speeed)
start.find()
end = input("--------------------\n按下回车结束程序...")
```

***
 
### 结果演示

* **第一组**

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output1.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output2.png?raw=true)

* **第二组**

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output3.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output4.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output5.png?raw=true)

* **第三组**

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output6.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output7.png?raw=true)

![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_06/Output8.png?raw=true)

#### 通过如上几组模拟我们可以看到，当扫描五至六层时结果已足够精确，而加大末端扫描层数的做法无法修正初始步幅过大引起的误差。

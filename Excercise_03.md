# Excercise_03


---
#作业L1
在屏幕上让你的英文名字水平移动起来

---
```python
import os
import time

s1 = ('#######    #      ###   ##   ##')
s2 = ('   #      # #    #   #  ##  ## ')
s3 = ('   #     #   #  #     # ## ##  ')
s4 = ('   #     #   #  #       ###    ')
s5 = ('   #     #####  #     # ## ##  ')
s6 = ('#  #    #     #  #   #  ##  ## ')
s7 = (' ##     #     #   ###   ##   ##')

for j in range(5) :
    os.system("cls")    
    print (s1)
    print (s2)
    print (s3)
    print (s4)
    print (s5)
    print (s6)
    print (s7)
    s1 = " " + s1
    s2 = " " + s2
    s3 = " " + s3
    s4 = " " + s4
    s5 = " " + s5
    s6 = " " + s6
    s7 = " " + s7
    time.sleep(1)
    continue
```
 ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_03(1).gif?raw=true)
 
---
#作业L2 
在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）

---
```python
import time
import os
a=("××××××××××××××××××××\n")
b=("××××\n")
c=("××××        ××××        ××××\n")
d=("                                ××××\n")
e=4*a+4*b
f=4*a+4*d
li=[2*e+4*a,4*a+16*c,2*f+4*a,16*c+4*a]
i=0
while i<20:
    print(li[i%4])
    time.sleep(1)
    i=i+1
    os.system('cls')
```
 ![image](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_03(2).gif?raw=true)

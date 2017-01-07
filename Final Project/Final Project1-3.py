from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave1 = np.zeros(101)
x_ave2 = np.zeros(101)
x_ave3 = np.zeros(101)
x_y0 = np.zeros(101)
x_now1 = np.zeros(10000)
x_now2 = np.zeros(10000)
x_now3 = np.zeros(10000)

for i in range(100):
    for j in range(10000):
        length = 2*np.random.rand() - 1      
        x_now1[j] = x_now1[j] + length
    average = sum(x_now1)/10000
    x_ave1[i+1] = average

for i in range(100):
    for j in range(10000):
        length = 2*np.random.rand() - 1      
        x_now2[j] = x_now2[j] + length
    average = sum(x_now2)/10000
    x_ave2[i+1] = average
    
for i in range(100):
    for j in range(10000):
        length = 2*np.random.rand() - 1      
        x_now3[j] = x_now3[j] + length
    average = sum(x_now3)/10000
    x_ave3[i+1] = average
    
plt.scatter(steps, x_ave1,c='g',s=25,alpha=0.4,marker='o')
plt.scatter(steps, x_ave2,c='y',s=25,alpha=0.4,marker='o')
plt.scatter(steps, x_ave3,c='b',s=25,alpha=0.4,marker='o')
plt.plot(steps, x_y0,'m')
plt.xlim(0,100)
plt.ylim(-1,1)
plt.grid(True)
plt.xlabel('step number')
plt.ylabel('$\overline{x}$')
plt.title('$\overline{x}$ of 10000 walkers with random step length')

plt.show()



    
    




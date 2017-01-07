from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_now = np.zeros(10000)

for i in range(100):
    for j in range(10000):
        ruler = np.random.rand()
        if ruler<=0.75:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/10000
    x_ave[i+1] = average
    
para = np.polyfit(steps, x_ave,1)
poly = np.poly1d(para)
y_fit = poly(steps)

plt.scatter(steps, x_ave,c='g',s=25,alpha=0.4,marker='o')
plt.plot(steps, y_fit, 'm', label = 'fit line')
plt.legend(loc='upper left')


plt.xlim(0,100)
plt.grid(True)
plt.xlabel('step number')
plt.ylabel('$\overline{x}$')
plt.title('$\overline{x}$ of 10000 walkers')

plt.show()


        
    
    




from random import randrange as rand
from numpy import cos, sin, radians
import numpy as np
import matplotlib.pyplot as plt

N = 100   # Size of square as a multiple of the step size.
NSteps = 6666   # Number of steps in simulation.
xStart = 0   # x coordinate of starting location. Origin is at centre of square
yStart = 0   # y coordinate of starting location. Origin is at centre of square

s = 1   # Step number.
x = xStart   # x coordinate of point.
y = yStart   # y coordinate of point.
xList = []   # List of the x coordinates of all points visited.
yList = []   # List of the y coordinates of all points visited.

def wrap(v, N):

    if v > N/2:
        return v - N, True
    elif v < -N/2:
        return v + N, True
    return v, False


for j in range(NSteps):
    angle = radians(rand(361))
    x, wrap_flag_x = wrap(x + cos(angle), N)
    y, wrap_flag_y = wrap(y + sin(angle), N)
    if wrap_flag_x or wrap_flag_y:
        xList.append(np.nan)
        yList.append(np.nan)
    xList.append(x)
    yList.append(y)    

fig, ax = plt.subplots()
ax.plot(xList,yList,c="olivedrab",alpha=0.6, label='Random walk')
ax.scatter(xStart,yStart, c='deepskyblue',s=111,alpha=0.6, marker='o',label='Start point')
ax.scatter(x, y, c='crimson',s=111,alpha=0.6, marker='<',label='End point')
ax.set_xlim(-N/2,N/2)
ax.set_ylim(-N/2,N/2)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.legend()
plt.title('2D random walk')
plt.show()
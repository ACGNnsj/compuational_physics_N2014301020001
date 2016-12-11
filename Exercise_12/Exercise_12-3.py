from __future__ import division
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
from pylab import *

v = []

for i in range(151):
    row_i = []
    for j in range(151):
        if i == 0 or i == 150 or j == 0 or j == 150:
            voltage = 0
        elif 50 <= i <= 90 and j == 50:
            voltage = 1
        elif 50 <= i <= 90 and j == 90:
            voltage = -1
        else:
            voltage = 0
        row_i.append(voltage)
    v.append(row_i)


def update_V(v):
    delta_V = 0

    for i in range(151):
        for j in range(151):
            if i == 0 or i == 150 or j == 0 or j == 150:
                pass
            elif 50 <= i <= 90 and j == 50:
                pass
            elif 50 <= i <= 90 and j == 90:
                pass
            else:
                voltage_new = (v[i + 1][j] + v[i - 1][j] + v[i][j + 1] + v[i][j - 1]) / 4
                voltage_old = v[i][j]
                delta_V += abs(voltage_new - voltage_old)
                v[i][j] = voltage_new

    return v, delta_V


def Laplace_calculate(v):
    epsilon = 0.1
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 10:
        v1, delta_V = update_V(v)
        v2, delta_V = update_V(v1)
        v = v2
        N_iter += 1

    return v2


x = np.linspace(0, 150, 151)
y = np.linspace(0, 150, 151)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(v)
Ex = deepcopy(Z)
Ey = deepcopy(Z)
E = deepcopy(Z)

for i in range(101):
    for j in range(101):
        if i == 0 or i == 100 or j == 0 or j == 100:
            Ex[i][j] = 0
            Ey[i][j] = 0
        else:
            Ex_value = -(Z[i + 1][j] - Z[i][j]) / 2
            Ey_value = -(Z[i][j + 1] - Z[i][j]) / 2
            Ex[i][j] = Ex_value
            Ey[i][j] = Ey_value

for i in range(101):
    for j in range(101):
        E_value = np.sqrt(Ex[i][j] ** 2 + Ey[i][j] ** 2)
        E[i][j] = E_value

plt.figure()
CS = plt.contour(X, Y, Z, 8, alpha=1.0, cmap='jet')
plt.clabel(CS, inline=1, fontsize=12)
plt.colorbar(CS)
plt.title('electric potential near two capacitor plates')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

fig = figure()
ax = Axes3D(fig)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet', linewidth=0, antialiased=False)
ax.set_xlabel('x(m)')   
ax.set_ylabel('y(m)')
ax.set_zlabel('voltage(V)')
ax.set_title('voltage in 3D picture')
ax.grid(True)
fig.colorbar(surf, shrink=0.5, aspect=20)

fig0, ax0 = plt.subplots()
strm = ax0.streamplot(X, Y, np.array(Ey), np.array(Ex), color=np.array(E), linewidth=2, cmap='winter')
fig0.colorbar(strm.lines)
ax0.set_xlabel('x(m)')
ax0.set_ylabel('y(m)')
ax0.set_title('Electric field near two plates')
plt.show()
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

xyz = []
cur = [0, 0, 0]

for _ in range(888):
    axis = random.randrange(0, 3)
    cur[axis] += random.choice([-1, 1])
    xyz.append(cur[:])

x, y, z = zip(*xyz)
ax.plot(x, y, z,c='darkslategrey',alpha=0.6, label='Random walk')
ax.scatter(x[0], y[0], z[0], c='deepskyblue',s=55,alpha=0.6, marker='o',label='Start point')
ax.scatter(x[-1], y[-1], z[-1], c='crimson',s=55,alpha=0.6, marker='<',label='End point')   # End point
ax.legend()
plt.title('3D lattice random walk')
plt.show()
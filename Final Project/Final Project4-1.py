from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import random

N=100
accuracy=1e-10
class Fields:
	def __init__(self):
		self.v=[]
		self.old_v=[]
		for i in range(N):
			self.v.append([])
			self.old_v.append([])

		#print len(self.old_v)

		for i in range(N):
			for j in range(N):
				self.v[i].append(0)
				self.old_v[i].append(0)

		for i in range(N//4,3*N//4):
			for j in range(N//4,3*N//4):
				self.v[i][j]=1

	def update(self):
		self.Delta_v=0.
		for i in range(N):
			self.v[i][0]=0
			self.v[i][N-1]=0

		for j in range(N):
			self.v[0][j]=0   
			self.v[N-1][j]=0

		for i in range(N):
			for j in range(N):
				self.old_v[i][j]=self.v[i][j]


		for i in range(1,N-1):
			for j in range(1,N-1):
				self.v[i][j]=(self.old_v[i+1][j]+self.old_v[i-1][j]+self.old_v[i][j+1]+self.old_v[i][j-1])/4.

		#print self.Delta_v

	def fire(self):
		counter=0
		for i in range(4000):
			self.update()
			counter+=1
			i+=1

		return self.v


Super=Fields()
Soup=Super.fire()

fig = plt.figure()
ax = fig.gca(projection='3d')
x=np.linspace(-1,1,N)
y=np.linspace(-1,1,N)
x, y = np.meshgrid(x, y)
surf = ax.plot_surface(x, y, Soup, rstride=1, cstride=1, cmap='autumn',alpha=0.8,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.set_title('Variation of distriution of the cream with time')

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.xlabel("X")
plt.ylabel("Y")

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
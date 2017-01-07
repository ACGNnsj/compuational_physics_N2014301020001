import random
import matplotlib.pyplot as plt
def randpath(n,tt):
    b=[]
    bb=[]
    bb1=[]
    for i in range(1,2*n):
        b.append(-n+i)
        bb.append(0)
        if i==n:
           bb1.append(n)
        else:
           bb1.append(0)
    for j in range(n):
        x=[]
        x.append(0) 
        for k in range(tt):   
            c=random.random()
            if c<=0.5:
               x.append(x[-1]+1)
            if c>0.5:
               x.append(x[-1]-1)
        ct=b.index(x[-1])
        bb[ct]=bb[ct]+1
    if tt==0:
       return b,bb1
    else:
       return b,bb          
ax1=plt.subplot(811)
ax2=plt.subplot(812)
ax3=plt.subplot(813)
ax4=plt.subplot(814)
ax5=plt.subplot(815)
ax6=plt.subplot(816)
ax7=plt.subplot(817)
ax8=plt.subplot(818)
plt.sca(ax1)
a,b=randpath(1000,0)
plt.plot(a,b,'lime')
plt.xlim(-500,500)
plt.title('variation of particle distribution with time')
plt.sca(ax2)
a,b=randpath(1000,10)
plt.plot(a,b,'aquamarine')
plt.xlim(-500,500)
plt.sca(ax3)
a,b=randpath(1000,100)
plt.plot(a,b,'deepskyblue')
plt.xlim(-500,500)
plt.sca(ax4)
a,b=randpath(1000,500)
plt.plot(a,b,'cornflowerblue')
plt.ylabel('particle number')
plt.xlim(-500,500)
plt.sca(ax5)
a,b=randpath(1000,1000)
plt.plot(a,b,'mediumslateblue')
plt.xlim(-500,500)
plt.sca(ax6)
a,b=randpath(1000,2000)
plt.plot(a,b,'plum')
plt.xlim(-500,500)
plt.sca(ax7)
a,b=randpath(1000,4000)
plt.plot(a,b,'m')
plt.xlim(-500,500)
plt.sca(ax8)
a,b=randpath(1000,8000)
plt.plot(a,b,'crimson')
plt.xlim(-500,500)
plt.xlabel('x')

plt.show()

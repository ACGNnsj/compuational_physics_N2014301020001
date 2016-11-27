import numpy as np
import matplotlib.pyplot as plt
import math
class INVERSE(object):

    def __init__(self, _beta=2.1, _e=0., _m=4*(math.pi**2), _dt=0.001, _time=20):
        self.m=_m
        self.e=_e
        self.x, self.y=[1.],[0.]
        self.vx, self.vy=[0],[math.sqrt(_m)*math.sqrt((1.-_e)/(1.+_e))]
        self.beta=_beta
        self.dt=_dt
        self.time= _time
        self.n=int(_time/_dt)
    
    def cal(self):     
        for i in range(self.n):
            self.r=math.sqrt(self.x[-1]**2+self.y[-1]**2)
            self.vx.append(self.vx[-1]+self.dt*(-self.m*self.x[-1]/self.r**(self.beta+1.)))
            self.vy.append(self.vy[-1]+self.dt*(-self.m*self.y[-1]/self.r**(self.beta+1.)))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def plot_trajectory(self):       # plot the trajectory
        plt.plot(self.x,self.y,markersize=0.5,label='e= %.2f'%self.e)
        plt.plot([self.x[-1]],[self.y[-1]],markersize=8)
        plt.plot([0],[0],'or',markersize=20)
    def precession_rate(self):
        self.x_critical=0
        self.y_critical=0
        self.t_critical=0
        for i in range(len(self.x)-2):
            self.r_i=math.sqrt(self.x[i]**2+self.y[i]**2)
            self.r_i1=math.sqrt(self.x[i+1]**2+self.y[i+1]**2)
            self.r_i2=math.sqrt(self.x[i+2]**2+self.y[i+2]**2)
            if self.r_i<self.r_i1 and self.r_i1>self.r_i2:
                self.x_critical=self.x[i+1]
                self.y_critical=self.y[i+1]
                self.t_critical=self.dt*(i+1)
                break
        self.rate = math.arctan(self.y_critical/self.x_critical)/self.t_critical
        return self.rate
  
for i in range(11):
    fig=plt.figure(figsize=(10,10)) 
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    plt.xlabel(r'$x$'+' (AU)',fontsize=18)
    plt.ylabel(r'$y$'+' (AU)',fontsize=18)
    plt.title(r'$\beta=2.1$'+'  '+'e='+str(i*0.1),fontsize=18)
    cmp=INVERSE(2.1,i*0.1)
    cmp.cal()
    cmp.plot_trajectory()
    plt.show()

e=[]
rate=[]
for i in np.linspace(0.1,0.6,20):
    cmp= INVERSE(2.1,i)
    cmp.cal()
    e.append(i)
    rate.append(180/math.pi*cmp.precession_rate())
plt.xlim(-0,0.7)
plt.xlabel(r'e')
plt.ylabel(r'Precession rate '+r'$ degree/yr $',fontsize=18)
plt.title(r'Precession rate',fontsize=18)
plt.plot(e,rate,'oy')
plt.plot(e,rate,'-r')
plt.show()
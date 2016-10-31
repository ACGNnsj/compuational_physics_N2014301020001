# -*- coding: utf-8 -*-
import math
import pylab as py
g=9.8
l=9.8
q=0.5
ou_D=2/3
class pendulum0:
    def __init__(self,F_D,sita):
        self.sita=[sita]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.F_D=F_D
    def calculate(self):
        while self.t[-1]<150:
            omiga_new=self.omiga[-1]-((g/l)*(math.sin(self.sita[-1]))+q*self.omiga[-1]-self.F_D*math.sin(ou_D*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            sita_new=self.sita[-1]+self.omiga[-1]*self.dt
            t_new=self.t[-1]+self.dt
            
            while sita_new > math.pi:
                sita_new -=2*(math.pi)
            while sita_new < -math.pi:
                sita_new +=2*(math.pi)
                
            self.sita.append(sita_new)
            self.t.append(t_new)
    
py.subplot(121)        
A=pendulum0(0.5,0.2)
A.calculate()
py.plot(A.sita,A.omiga,'.',label='$F_D=0.5$')
py.title('$ω$ versus $θ$')
py.legend(loc="upper right",frameon=False)
py.xlabel('$θ$(radians)')
py.ylabel('$ω$(radians/s)')

py.subplot(122)        
A=pendulum0(1.2,0.2)
A.calculate()
py.plot(A.sita,A.omiga,'.',label='$F_D=1.2$')
py.title('$ω$ versus $θ$')
py.legend(loc="upper right",frameon=False)
py.xlabel('$θ$(radians)')
py.ylabel('$ω$(radians/s)')

py.show()
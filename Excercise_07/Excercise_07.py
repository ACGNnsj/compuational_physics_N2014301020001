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
        while self.t[-1]<60:
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
    def plot(self,color):
        py.plot(self.t,self.sita,'b')
        py.xlabel('time [s]')
        py.ylabel('$\θ$ [radians]')
sub1=py.subplot(251)
A=pendulum0(0,0.2)
A.calculate()
sub1.plot(A.t,A.sita,'g',label='$F_D=0$')
sub1.set_title('$θ$ versus time')
sub1.legend(loc="upper right",frameon=False)
py.ylabel('$θ$(radians)')
py.xlabel('time(s)')

sub2=py.subplot(252)
A=pendulum0(0.5,0.2)
A.calculate()
sub2.plot(A.t,A.sita,'g',label='$F_D=0.5$')
sub2.set_title('$θ$ versus time')
sub2.legend(loc="upper right",frameon=False)
py.ylabel('$θ$(radians)')
py.xlabel('time(s)')

sub3=py.subplot(253)
A=pendulum0(1.2,0.2)
A.calculate()
sub3.plot(A.t,A.sita,'g',label='$F_D=1.2$')
sub3.set_title('$θ$ versus time')
sub3.legend(loc="upper right",frameon=False)
py.ylabel('$θ$(radians)')
py.xlabel('time(s)')

sub4=py.subplot(254)
A=pendulum0(1.5,0.2)
A.calculate()
sub4.plot(A.t,A.sita,'g',label='$F_D=1.5$')
sub4.set_title('$θ$ versus time')
sub4.legend(loc="upper right",frameon=False)
py.ylabel('$θ$(radians)')
py.xlabel('time(s)')

sub5=py.subplot(255)
A=pendulum0(1.9,0.2)
A.calculate()
sub5.plot(A.t,A.sita,'g',label='$F_D=1.9$')
sub5.set_title('$θ$ versus time')
sub5.legend(loc="upper right",frameon=False)
py.ylabel('$θ$(radians)')
py.xlabel('time(s)')

sub6=py.subplot(256)
A=pendulum0(0,0.2)
A.calculate()
sub6.plot(A.t,A.omiga,'r',label='$F_D=0$')
sub6.set_title('$ω$ versus time')
sub6.legend(loc="upper right",frameon=False)
py.ylabel('$ω$(radians/s)')
py.xlabel('time(s)')

sub7=py.subplot(257)
A=pendulum0(0.5,0.2)
A.calculate()
sub7.plot(A.t,A.omiga,'r',label='$F_D=0.5$')
sub7.set_title('$ω$ versus time')
sub7.legend(loc="upper right",frameon=False)
py.ylabel('$ω$(radians/s)')
py.xlabel('time(s)')

sub8=py.subplot(258)
A=pendulum0(1.2,0.2)
A.calculate()
sub8.plot(A.t,A.omiga,'r',label='$F_D=1.2$')
sub8.set_title('$ω$ versus time')
sub8.legend(loc="upper right",frameon=False)
py.ylabel('$ω$(radians/s)')
py.xlabel('time(s)')

sub9=py.subplot(259)
A=pendulum0(1.5,0.2)
A.calculate()
sub9.plot(A.t,A.omiga,'r',label='$F_D=1.5$')
sub9.set_title('$ω$ versus time')
sub9.legend(loc="upper right",frameon=False)
py.ylabel('$ω$(radians/s)')
py.xlabel('time(s)')

sub10=py.subplot(2,5,10)
A=pendulum0(1.9,0.2)
A.calculate()
sub10.plot(A.t,A.omiga,'r',label='$F_D=1.9$')
sub10.set_title('$ω$ versus time')
sub10.legend(loc="upper right",frameon=False)
py.ylabel('$ω$(radians/s)')
py.xlabel('time(s)')


py.show()


    
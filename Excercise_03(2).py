import time
import os
a=("××××××××××××××××××××\n")
b=("××××\n")
c=("××××        ××××        ××××\n")
d=("                                ××××\n")
e=4*a+4*b
f=4*a+4*d
li=[2*e+4*a,4*a+16*c,2*f+4*a,16*c+4*a]
i=0
while i<20:
    print(li[i%4])
    time.sleep(1)
    i=i+1
    os.system('cls')

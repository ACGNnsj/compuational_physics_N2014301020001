import os
import time

s1 = ('#######    #      ###   ##   ##')
s2 = ('   #      # #    #   #  ##  ## ')
s3 = ('   #     #   #  #     # ## ##  ')
s4 = ('   #     #   #  #       ###    ')
s5 = ('   #     #####  #     # ## ##  ')
s6 = ('#  #    #     #  #   #  ##  ## ')
s7 = (' ##     #     #   ###   ##   ##')

for j in range(5) :
    os.system("cls")    
    print (s1)
    print (s2)
    print (s3)
    print (s4)
    print (s5)
    print (s6)
    print (s7)
    s1 = " " + s1
    s2 = " " + s2
    s3 = " " + s3
    s4 = " " + s4
    s5 = " " + s5
    s6 = " " + s6
    s7 = " " + s7
    time.sleep(1)
    continue
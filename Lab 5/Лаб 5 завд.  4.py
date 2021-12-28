"""
Дано x0 = x1 = 1,  xi = sin x(i-1) + х(i-2)/cos(x(i-1)) --> i >= 2.    визначити xn

"""
# 0 задання

"""
x0 = x1 = 1
xi = sin x(i-1) + х(i-2)/cos(x(i-1)) 
n  - int  -  number of X
"""
import math
x1 = x2 = 1
n = int(input("Ведіть значення a: "))
xn = 0
if n <= 2:
    print(1)
else:
    for i in range(2,n+1):
        xn += math.sin(x2) + x1 / math.cos(x2)
        x2 = x1
        x1 = xn
    print(xn)
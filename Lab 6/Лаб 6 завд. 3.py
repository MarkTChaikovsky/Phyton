"""
Ззнайти вектор
c=2(a +c)- b, де a,b,c є R^n

"""
# 0 задання

"""
a b c - вектори
"""
n = int(input("введіть значення виміру: "))
a = []
b = []
c = []
sum = []
for i in range(n):
    a.append(float(input("введіть значення {0} виміру для вектора а".format(i+1))))
    b.append(float(input("введіть значення {0} виміру для вектора b".format(i+1))))
    c.append(float(input("введіть значення {0} виміру для вектора c".format(i+1))))
    sum.append(2*(a[i] + c[i]) - b[i])
print(sum)
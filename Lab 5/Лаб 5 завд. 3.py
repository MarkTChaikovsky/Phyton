"""
чи справедлива нерівність(я не буду то записувати тут))
"""

import math
x = int(input("Введіть число x: "))   # Дійсне число
e = int(input("Завдати значення е: "))     # Задана точінсть
s = 1   # Сума
n = 1   # Натуральне число

while True:
    a = (math.pow(x, n) / math.factorial(n))
    if math.fabs(a) > e:
        s += a
        n += 1
    else:
        break

print("Сума: {0}".format(s))
print("e: {0}".format(e ** x))
if s == e ** x :
    print('Рівність справедлива')
else:
    print('Рівність несправедлива')
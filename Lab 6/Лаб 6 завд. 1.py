"""
Знайти найбільший елемент серед елементів вектора x є R^n з парними індексами.

"""
# 0 задання

"""

"""
n = int(input("введіть кількість чисел: "))

x = []
max1 = 0
for i in range(n):
    number = float(input("Введіть {0} число: ".format(i)))
    x.append(number)
i = 0
for i in range(len(x)):
    if i % 2 == 0:
        if x[i] > max1:
            max1 = x[i]
            p = i
        else:
            continue
    else:
        continue
print("найбільший елемент серед елементів вектора з парними індексами: x{0}".format(p))

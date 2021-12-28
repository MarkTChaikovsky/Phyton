"""
Побудувати масив А=(ai), елементи якого задаються формулою:
ai = (sin x + cos x) + 2(sin 2x + cos 2x) + ... + i(sin ix + cos ix) --> i = (1,2...n)\
Знайти найбільший елемент масиву А
"""
import math

A = []
s = 0
n = int(input("Кількість елементів: "))
x = int(input("Введіть значення х: "))
for i in range(n):
    s += i*(math.sin(i*x) + math.cos(i*x))
    A.append(s)
print(A, max(A))
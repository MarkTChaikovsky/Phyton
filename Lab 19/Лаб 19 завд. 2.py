"""
Дано нетипізований файл, який містить цілі числа. Створити файл «P1.dat», який містить парні цілі числа.
Непарні числа вивести на екран у порядку, зворотному до порядку слідування їх у файлі.
"""
import random

n = int(input("Введіть кількість чисел: "))
a = [random.randint(0, 50) for i in range(n)]
with open('file', 'w') as file:
    file.write(' '.join(map(lambda el: str(el), a)))
with open('file') as file:
    line = file.readline()
    numbers = (map(lambda el: int(el), line.split(sep=' ')))
    numbers = list(filter(lambda el: el % 2 == 0, numbers))
    f = open('P1.dat',"w")
    f.write(str(list(map(lambda el:str(el),numbers))))
with open('file') as file:
    line = file.readline()
    numbers = (map(lambda el: int(el), line.split(sep=' ')))
    other = list(filter(lambda el: el % 2 == 1, numbers))
    other = sorted(other, reverse=True)
    print(*other)
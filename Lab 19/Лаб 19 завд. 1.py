"""
Дано текстовий файл, який містить цілі числа. Визначити середнє арифметичне елементів.
"""
with open("Lab19_1.txt") as file:
  #  numbers = list(map(lambda el: int(el), file))
    sum = 0
    n = 0
    for i in list(map(lambda el: int(el), file)):    # for i in numbers:
        sum += i
        n +=1
    print(sum/n)

"""
Перетворити масив таким чином, щоб спочатку розміщувались всі елементи,
 що мають парні індекси, а потім з непарними індексами.

"""
# 0 задання

"""
a - масив
n - int - кількість елементів масиву
final_v - фінальний масив
"""
n = int(input("введіть кількість елементів масиву: "))
a = []
a1 = []
a2 = []
final_v = []
max1 = 0
for i in range(n):
    number = float(input("Введіть {0} число: ".format(i)))
    a.append(number)
i = 0
for i in range(len(a)):
    if i % 2 == 0:
        a1.append(a[i])
    else:
        a2.append(a[i])
print(a1 + a2)
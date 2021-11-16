from random import randint
n = int(input("кількість рядків: "))
m = int(input("кількість стовпців: "))
sum = 0
A = [[randint(-10, 10) for j in range(m)] for i in range(n)]
print(A)
for j in range(n):
    for i in range(m):
        if j < i:
           sum = sum + abs(A[j][i])
print("Сума модулів елементів,розташованих вище головної діагоналі: {0}".format(sum))
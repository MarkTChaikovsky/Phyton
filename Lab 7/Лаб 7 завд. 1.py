"""
Визначити кількість додатніх елементів матриці з першим парним і другим непарним (індексами(?))
"""
A = []
sum = 0
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n) :
    A.append([int(input("{0} {1} елемент: ".format(i,j))) for j in range(m)])
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > 0 and (i+1) % 2 == 0 and (j+1) % 2 != 0:
            sum += 1
print(A)
print(sum)
#lmin - int - л. мінімум
A = []
lmin = 0
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    A.append([int(input("{0} {1} елемент: ".format((i+1),(j+1)))) for j in range(m)])
print(A)
for i in range(n):
    for j in range(m):
        if A[i][j] < A[i][(j - 1)] and A[i][j] < A[(i - 1)][j]:
            if (i+1) != n and (j+1) != m:
                A[i][j] < A[i][(j + 1)] and A[i][j] < A[(i + 1)][j]
            lmin += 1
print(lmin)
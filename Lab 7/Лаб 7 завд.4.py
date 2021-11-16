A = []
B = []
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n):
    A.append([int(input("{0} {1} елемент: ".format((i+1),(j+1)))) for j in range(m)])
for i in range(n):
    for j in range(m):
        if i == j:
            B.append(A[i][j])
B.sort(reverse=True)
for i in range(n):
    for j in range(m):
        if i == j:
            A[i][j] = B[i]
print(A)
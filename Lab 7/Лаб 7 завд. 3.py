"""
Дано матрицю A. Перевірити, чи є дана матриця нижньою трикутною матрицею.
"""
A = []
sum = 0
ans = 1
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n) :
    A.append([int(input("{0} {1} елемент: ".format(i,j))) for j in range(m)])
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            for i in range(j+1, n):
                if A[j][i] != 0:
                    ans = 0
                    continue
if ans == 0:
    print("дана матриця не є нижньою трикутною матрицею")
else:
    print("матрця є нижньою трикутною матрицею")
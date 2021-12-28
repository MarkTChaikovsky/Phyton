"""
Побудувати прямокутну матрицю А, елементи якої задаються формулою:
Aij = i! - j!, i,j = 1,N
"""
def factorial(x):
    sum = 1
    for i in range(1, x+1):
        sum *= i
    return sum
A = []
sum = 0
N=int(input("N = "))
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(N) :
    A.append([factorial(i) - factorial(j) for j in range(N)])
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > 0 and (i+1) % 2 == 0 and (j+1) % 2 != 0:
            sum += 1
print(A)
print(sum)
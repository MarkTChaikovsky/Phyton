"""
Дано , a R, n N. Знайти 1/a + 1/a*(a+1) + ... + 1/ (a+1)*...*(a+n).
"""
# 0 задання
"""
a - float 
n - int
sum - float - сума 
"""
a = float(input("Введіть а: "))
n = int(input("Введіть n: "))
sum = 1/a
b = a
for i in range(1, n+1):
    b = b * (a + i)
    sum = sum + 1/b
print(sum)

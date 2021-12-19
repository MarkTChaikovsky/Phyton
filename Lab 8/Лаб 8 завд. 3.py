"""
#ФОРМУЛУ ПОМІНЯВ БО НЕ ПРАВИЛЬНА!! НА 0 ДІЛИТИ НЕ МОЖНА!! (x0 = 0 --> x0 = 1)
Нехай x0 = 1, x1=x2=x3=7,  xi = (x(i-1) * (1+x(i-2)) + x(i-3)) / x(i-4)   . знайти хn
"""
def x_Rec(i):
    if i == 0:
        return 1
    elif i == 1 or i == 2 or i == 3:
        return 7
    else:
        return (x_Rec(i-1) * (1+x_Rec(i-2)) + x_Rec(i-3)) / x_Rec(i-4)

print(x_Rec(int(input("який х ви хочете знайти? "))))
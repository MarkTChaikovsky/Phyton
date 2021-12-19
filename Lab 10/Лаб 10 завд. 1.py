"""
---------Об’єкт “Множина цифр”--------

--------------поля-----------
для зберігання множини цифр;

----------методи-------------
додавання нової цифри;
виведення цифр, які входять у множину на екран;
знаходження найбільшої цифри;
знаходження суми цифр.


"""
class NumbersPair:
    def __init__(self,*args):
        self.args = list(args)
    def add_number(self,number):
        self.args.append(number)
    def __str__(self):
        return str(self.args)
    def max_numb(self):
        return max(self.args)
    def sum_numbs(self):
        return sum(self.args)
arr1 = NumbersPair(0,1,2,3,4)
arr1.add_number(12)
print(arr1)
print(arr1.max_numb())
print(arr1.sum_numbs())
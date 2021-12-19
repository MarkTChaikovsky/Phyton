"""
--------Об’єкт “Графічний файл ”--------

-----------поля-----------

назва (ім’я і розширення);
дата створення;
дата останнього редагування;
розміри;
глибина кольору;

-----------методи-----------

визначення часу з останнього редагування;
визначення об’єму файлу за вказаними розмірами;
зміни імені;
зміни розширення;
визначення кількості відтінків, які можна зберегти.

"""
class Graphic_file:
    def __init__(self,name,expansion,data_f,data_l_r,size,color_d):
        self.__name = name
        self.__expansion = expansion
        self.data_f = list(map(lambda el: int(el), data_f.split(sep=' ')))
        self.data_l_r = list(map(lambda el: int(el), data_l_r.split(sep=' ')))
        self.size = list(map(lambda el: int(el), size.split(sep ='x')))
        self.color_d = color_d
    def time(self, actual_date):
        actual_date = list(map(lambda el: int(el), actual_date.split(sep=' ')))
        output = actual_date[0] - self.data_l_r[0]
        output += (actual_date[1] - self.data_l_r[1])*30
        output += (actual_date[2] - self.data_l_r[2]) * 365
        output *= 24
        return "{0} h. ".format(output)
    def size1(self):
        output = (self.size[0] * self.size[1] * self.color_d)/8388608
        return "{0} Mb. ".format(output)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def expansion(self):
        return self.__expansion
    @expansion.setter
    def expansion(self, value):
        self.__expansion = value
    def color_numb(self):
        return 2 ** self.color_d
    def __str__(self):
        return '{0}.{1}'.format(self.__name,self.__expansion)

#----------------------------------------------

f1 = Graphic_file('landscape','png','01 12 2021','12 12 2021','1080x720',8)
print(f1.time('13 12 2021'))
print("\n")
print(f1.size1())
print("\n")
f1.name = 'landscape 2.0'
f1.expansion = 'jpg'
print(f1)
print("\n")
print(f1.color_numb())










"""1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") 
и возвращает количество дней оставшихся до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, 
ReadMixin:

в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key 
по которому нужно добавить 
задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который
 передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова 
 название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое 
значение new_value и заменяет задачу под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
"""


# class CreateMixin:
#     def create(self, todo, key):
#         todos = {}
#         if key in todos:
#             return "Задача под таким ключём уже существует"
#         else:
#             return todos.setdefault(key)

# class DeleteMixin:
#     def delete(self,key):
#         todos = {}
#         return todos.popitem(key)

# class UpdateMixin:
#     def update(self, key, new_value):
#         todos = {}
#         return todos.update(key(new_value))

# class ReadMixin:
#     def read(self):
#         todos = {}
#         return sorted(todos)

        
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def set_deadline(self, date):
#         from datetime import datetime
#         self.date = datetime.strftime('%H:%M:%S')(date)
#         res = datetime.strftime('%H:%M:%S')(self.date) - datetime.now().strftime('%H:%M:%S')
#         return res

# data = ToDo()



"""
2) Создайте классы Dog и Cat с одинаковым методом voice.

Для собак он должен печатать "Гав", для кошек "Мяу".

Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.

Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().

Ввод:

to_pet(barsik) 
to_pet(rex) 
Вывод:

Мяу 
Гав 
"""

# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')

# rex = Dog()
# barsik = Cat()

# def to_pet(animal):
#     animal.voice()

# to_pet(barsik) 
# to_pet(rex) 

"""
1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, 
сколько гласных букв в слове, которое передается в качестве аргумента в методе count, 
а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов. 
С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

!!!! 
Обязательное условие: если в классе A или B не переопределить метод count должна выйти ошибка
!!!!

"""

# class A:
#     def count(self, slovo):
#         self.slovo = 'оаоу'
#         glas = 'АЕЁИОУЫЭЮЯ'.lower()
#         res = []
#         for x in slovo:
#             if x in slovo:
#                 res.append(x)
#                 return len(res)

# a = A()
# print(a.count())



'''
2) Создайте 3 класса:
Bird, Animal, Plant
класс Bird должен иметь методы: fly(), grow(), sound(). Animal: sound(), run(), grow(). Plant: grow(), photosynthesize()
каждый метод должен просто принтить действие. Например: def fly(self): print('я лечу')'''

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):
#     @abstractmethod
#     def fly(self):
#         pass
#     @abstractmethod
#     def grow(self):
#         pass
#     @abstractmethod
#     def sound(self):
#         pass
#     @abstractmethod
#     def run(self):
#         pass
#     @abstractmethod
#     def photosynthesize(self):
#         pass

# class Bird(AbstractAnimal):
#     def fly(self):
#         print('fly')

#     def grow(self):
#         print('grow')
    
#     def sound(self):
#         print('noise')

# class Animal(AbstractAnimal):
#     def sound(self):
#         print('noise')
    
#     def run(self):
#         print('run')

#     def grow(self):
#         print('grow')

# class Planet(AbstractAnimal):
#     def grow(self):
#         print('grow')
    
#     def photosynthesize(self):
#         print('H2O')












# 1) # Напишите класс CustomNumber, который принимает одно число и будет выполнять 
# ту или иную операцию с ним.
# Перезапишите магические методы этих операторов
# Оператор сложения (+) будет выполнять функцию оператора  вычитания (-) и наоборот
# Оператор умножения (*) будет выполнять функцию оператора деления (/) и наоборот
# Так же перезапишите функционал операторов сравнения на противоположные (>, < ,==, !=)

# Вывод:
# num1 = CustomNumber(10)
# num2 = CustomNumber(5)

# print(num1 + num2)  # 5
# print(num2 - num1)  # 15
# print(num1 * num2)  # 2.0
# print(num2 / num1)  # 0.5

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 > num2)   # False
# print(num1 < num2)   # True
# print(num1 >= num2)  # False
# print(num1 <= num2)  # True


# class CustomNumber:
#     def __new__(cls, *args):
#         number = args[0]
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance

#     def __add__(self, other):
#         res = self.number - other.number
#         print(res)
    
#     def __sub__(self, other):
#         res = self.number + other.number
#         print(res)
    
#     def __mul__(self, other):
#         res = self.number / other.number
#         print(res)
    
#     def __truediv__(self, other):
#         res = self.number * other.number
#         print(res)
    
#     def __gt__(self, other):
#         print(False) if self.number > other.number else print(True)
    
#     def __lt__(self, other):
#          print(False) if self.number < other.number else print(True)
    
#     def __eq__(self, other):
#          print(False) if self.number == other.number else print(True)
         
#     def __ne__(self, other):
#          print(False) if self.number != other.number else print(True)
    
#     def __le__(self, other):
#          print(False) if self.number <= other.number else print(True)
    
#     def __ge__(self, other):
#          print(False) if self.number >= other.number else print(True)

# value1 = CustomNumber(124)
# value2 = CustomNumber(53)
# value1 + value2
# value1 - value2
# value1 * value2
# value1 / value2
# value1 > value2
# value1 < value2
# value1 == value2
# value1 != value2
# value1 <= value2
# value1 >= value2



"""
1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, 
сколько гласных букв в слове, которое передается в качестве аргумента в методе count, 
а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов. 
С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

!!!! 
Обязательное условие: если в классе A или B не переопределить метод count должна выйти ошибка
!!!!

"""
# ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я','а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# set('АаЕеЁёИиОоУуЫыЭэЮюЯя')
class A:

    def count(self, word):
        vse_glas = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я','а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
        glas = 0
        for i in word:
            if i in vse_glas:
                glas += 1
        
a = A()
print(a.count('ытоыа'))


# rows = int(input("Сколько будет строк: "))
# gls = 0
# sogls = 0
# vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
# for _ in range(rows):
#     line = input("Введите строку: ")
#     for i in line:
#         if i in vse_gls:
#             gls += 1
#         else:
#             """Проверяем на наличе постороних символов в строке"""
#             if i!=" " or i!="." or i!=",":
#                 sogls +=1


# print(f"Гласных: {gls}\nСогласных: {sogls}")








# """
# 3) Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ 
# от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit,
#  орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. 
#  У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и 
#  расчитывающий ваш возраст на данной планете.
# Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, 
# если возраст earth_age равен 20:

# !!!!!
# обязательное условие: создание абстрактного метода
# !!!!! '
# from abc import ABC, abstractmethod

# class Planet:
#     def __init__(self, name_planet) -> None:
#         self.name = name_planet
    
#     @abstractmethod
#     def get_age(self):
#         pass

# class Mercury(Planet):
#     orbit = 88

#     def get_age(self, earth_age):
#         age = earth_age * 365 / self.orbit / 365
#         print(f'Ваш возраст в годах на планете Меркурий составляет {age} лет')

# class Venus(Planet):
#     orbit = 225

#     def get_age(self, earth_age):
#         age = earth_age * 365 / self.orbit
#         print(f'Ваш возраст в днях на планете Венера составляет {age} дней')

# class Jupiter(Planet):
#     orbit = 12

#     def get_age(self, earth_age):
#         age = earth_age * 365 / self.orbit * 24
#         print(f'Ваш возраст в часах на планете Юпитер составляет {age} часов')
    
# jup = Mercury('123')
# jup.get_age(24)
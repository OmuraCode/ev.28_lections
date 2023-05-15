# class methods, instance methods, static methods


# instance methods - обычные методы которы принимают первым аргументов self(ссылка на объект)
# Нужны они чтобы внутри метода мы могди работать с атрибутами объекта, получать их или изменять

# class Test:
#     def instance_method(self, a):
#         print('метод объекта')
#         print('первый аргумент: ', self)

# obj = Test()
# obj.instance_method(4) # если вызвать у объекта то self передается автоматически
# Test.instance_method(obj, 4) # если вызвать у класса то self нужно передать вручную

# ------------

# class methods = которые принимают первым аргументом cls (ссылка на класс) 
# Они нужны для создания или изменения атрибутов класса ля манипуляций с классом внутри метода. 
# Создаются при помоши декоратора @classmethod

# class Test:
#     @classmethod
#     def class_method(cls, a):
#         print('метод класса')
#         print('первый аргумент: ', cls)

# obj = Test()
# print(Test, '!!!')
# print()
# obj.class_method(5)
# print()
# Test.class_method(5)


# class C:
#     conter = 0

#     def __init__(self) -> None:
#         self.a = 4

# obj1 = C()
# obj2 = C()
# obj3 = C()

# obj2.conter +=1

# print('obj1', obj1.conter)
# print('obj2', obj2.conter)
# print('obj3', obj3.conter)
# print()
# print()

# C.conter += 5

# print('obj1', obj1.conter)
# print('obj2', obj2.conter)
# print('obj3', obj3.conter)




# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()
#         self.a = 4

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter +=1

# obj1 = C() #1
# obj2 = C() #2
# obj3 = C() #3
# print(obj3.counter)
# obj4 = C() 
# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)




# class Pizza:
#     def __init__(self, radius, *ingredients) -> None:
#         self.r = radius
#         self.ingredents = ingredients

#     def cook(self):
#         print(f'готовится пицца размером {self.r * 2} cm')
    
#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r, 'моцарелла', 'голландский', "дарблю", "брынза")
#         return pizza
    
#     def __str__(self) ->str:
#         return f'{self.r} cm - ' + ', '.join(self.ingredents)

# pizza1 = Pizza(20, 'пеперонни', 'грибы', "моцарелла")
# print(pizza1.cook())
# # pizza2 = Pizza(15, 'моцарелла', 'голландский', "дарблю", "брынза")
# # pizza3 = Pizza(20, 'моцарелла', 'голландский', "дарблю", "брынза")
# # pizza4 = Pizza(10, 'моцарелла', 'голландский', "дарблю", "брынза")
# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza.four_cheese(20)
# pizza4 = Pizza.four_cheese(10)
# pizza5 = Pizza(20, 'пеперонни', 'грибы', "моцарелла", 'olivas')
# print(pizza1)
# print(pizza2)
# print(pizza3)
# print(pizza4)
# print(pizza5)



# class Person:
#     surname = 'Stark'

#     def __init__(self, name, age)-> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print (f'Name: {self.name} {self.surname} \nAge: {self.age}')

#     @classmethod
#     def from_birth_year(cls, name, birth_date):
#         from datetime import date
#         age = date.today().year - birth_date
#         return cls(name, age)


# obj = Person('John', 24)
# obj.info()
# obj2 = Person('Sansa', 19)
# obj2.info()
# obj3 = Person.from_birth_year('Rob', 1996)
# obj3.info()




# from datetime import datetime, date
# timeDate = datetime.now()
# print(timeDate, type(timeDate))



# -------------------
# sttic methods - это тк методы в классе которые не принимают в качестве аргументов ни кдасс , н
# и объект, так называемые методы которые не изменяют состояние

# class C:
#     @staticmethod
#     def static_method(a):
#         print('статический метод')

# obj = C
# obj.static_method(5)
# C.static_method(5)


# class Cylinder:
#     def __init__(self, radius, height) -> None:
#         self.area = self.get_area(radius, height)
    
#     @staticmethod
#     def get_area(r, h):
#         from math import pi
#         circle = pi * r ** 2
#         side = pi * h * (r*2)
#         area = circle * 2 * side
#         return round(area, 2)
    
# obj = Cylinder(10,7)  
# print(f'Area: {obj.area}')

# obj2 = Cylinder(5, 70)  
# print(f'Area: {obj2.area}')








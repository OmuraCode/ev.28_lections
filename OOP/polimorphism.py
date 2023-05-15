# Функция полисорфизм - len(): __len__
# print(len('Makers'))
# print(len([1,2,3,4]))
# print(len({1:2, 3:4}))

# +(__add__) метод полиморфизм
# print(1+1)
# print('Hello' + 'World')
# print([1,2,3] + [4,5,6])


# Полиморфизм - это это способность функции(метода) использоваться для разных типов данных(классов)
# Ширико распространенное определение: "один интерфейс - много реализаций"
# list.pop()
# set.pop()
# dict.pop()

# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name 
#         self.age  = age
    
#     def info(self):
#         print(f'It\'s cat. Cats name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Meow meow')
    
# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name 
#         self.age  = age
    
#     def info(self):
#         print(f'It\'s dog. Dogs name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Bark bark')
    
# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()




# from math import pi

# class Shape:
#     def __init__(self, name) -> None:
#         self.name = name

#     def area(self):
#         pass

#     def faсt(self):
#         return f'Я фигура в двумерной плоскости {self.name}!'

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('квадрат')
#         self.length = length
    
#     def area(self):
#         return self.length ** 2
    
#     def fact(self):
#         return super().faсt() + '\nУ квадрата все стороны и углы равны 90 градусам'
    
# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Oкружнгсть')
#         self.radius = radius

#     def area(self):
#         return pi * (self.radius ** 2)
    
#     def fact(self):
#         return 'круг'
    

# a = Square(8)
# b =Circle(4)

# print(a.fact())
# print(a.area())

# print(b.fact())
# print(b.area())


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи,
#  краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.


# class Phone:
#     def __init__(self, imei, oc) -> None:
#         self.__imei = imei
#         self.__oc = oc
#         self.__battery_level = 100

#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен')
#         print(f'уровень заряда: {self.__battery_level}')
#         self.__battery_level -= 0.5

#     @property
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             raise Exception ('Телефон разряжен')
#         print(f'OS: {self.__oc}, imei: {self.__imei}')
#         self.__battery_level -=0.5

#     def play_music(self):
#         if self.__battery_level < 0.5:
#             raise Exception ('Телефон разряжен')
#         print('Слушаем Мирбека Атабекова')
#         self.__battery_level -=5

#     def play_video(self):
#         if self.__battery_level < 10:
#             raise Exception ('Телефон разряжен')
#         print('смотрим видео от кани на плптформе')
#         self.__battery_level -= 7

#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep

#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')
#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__battery_level <100:
#                 self.__battery_level +=1
#             print(f'Идет заряд батареи. Ваш уровень заряда: {self.__battery_level}')    
    

# phone = Phone('123 12313 123', 'ios 15')
# phone.battery_level
# phone.battery_level
# phone.get_info
# phone.play_music()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.battery_level
# phone.charge_battery(134)





# task 3

# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
    
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')

# class Employee(Person):
#     def __init__(self,name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
    
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')
    
# class Student(Person):
#     def __init__(self,name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
    
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')

# def get_human_info(obj):
#     obj.get_info()

# person = Person('Иван', 'Петров')
# employee = Employee('Иван', 'Петров', 'Рога и копыта', 'директор')
# student = Student('Иван', 'Петров', 'КГТУ', '3')

# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 



# task 4

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def get_area(self):
#         res = self.base * self.height / 2
#         return (round(res, 2))
    
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def get_area(self):
#         res = self.length ** 2
#         return (round(res, 2))


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_area(self):
#         res = pi * self.radius ** 2
#         return (round(res, 2))


# triangle = Triangle(7, 3)
# square = Square(4)
# circle = Circle(8)

# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area()) 


# task 5
class OS:
    def __init__(self, version):
        self.version = version

class Windows(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами CTRL + C'

class MacOS(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
    
class Linux(OS):
    def copy(self, text):
        return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'

win = Windows('Windows')
mac = MacOS('MacOS')
lin = Linux('Linux')

print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))
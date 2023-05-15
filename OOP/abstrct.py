'''
Абстракция (абстрактный класс) - это принип ООП, в котором создаются абстрактный класс(пустышка), 
в котором создаются названия атрибутов и методов, для того чтобы в дочерних классах переопределитть 
их нужным образом(есть название - нет логики)
'''

'''@abstrаctmethod - дукоратор который требует переопределение метода в наследуемом классе

@abstrаctproperty - декортаор которы требует переопределения атрибутов класса
'''

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):
#     @abstractmethod
#     def voice(self):
#         ...
    
#     @abstractproperty
#     def legs(self):
#         ...

# # obj = AbstractAnimal() # TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# # class Dog(AbstractAnimal):
#     ...

# # obj = Dog() #TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice


# # class Dog(AbstractAnimal):

# #     def voice(self):
# #         print('bark')

# # obj = Dog() # TypeError: Can't instantiate abstract class Dog with abstract methods legs


# class Dog(AbstractAnimal):
#     legs  = 4

#     def voice(self):
#         print('bark')

# obj = Dog()
# obj.voice()
# print(obj.legs)


# class Cat(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('meow')

# dog = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)





# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         ...

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('square')
#         self.length = length

#     def area(self):
#         return self.length ** 2

# obj = Square(12)
# print(obj.name)
# print(obj.area())




def count(word):
    vse_glas = set('АаЕеЁёИиОоУуЫыЭэЮюЯя')
    glas = 0
    for i in word:
        if i in vse_glas:
            glas += 1
        return glas

print(count('ттоаоаошц'))

# def count(word):
#         vowels = set("aeiouAEIOU")
#         count = 0
#         for char in word:
#             if char in vowels:
#                 count += 1
#         return count

# print(count('terere'))
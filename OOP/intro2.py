# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, weigth, nation) -> None:
#         self.name = f'{first_name} {last_name}'
#         self.weight = weigth
#         self.nationality = nation

#     def birthday(self):
#         from random import randint
#         print(f'\nHappy birthday, {self.name}!!!')
#         self.age +=1
#         self.weight += randint(3, 7)
    
#     def show_info(self):
#         print(self.name, self.age, self.weight, self.nationality)

# human1 = Human('John', 'Snow', 3.300, 'American')
# human2 = Human('Abu-Bakr', 'Al-Nasr', 3.8, 'Arabick')


# human1.show_info()
# human2.show_info()
# print()
# print('After 1 year: ')
# human1.birthday()
# human2.birthday()
# print()
# human1.show_info()
# human2.show_info()

# human1.birthday()
# human2.birthday()
# human1.birthday()
# human2.birthday()
# human1.birthday()
# print()
# human1.show_info()
# human2.show_info()
# ______________-


# class Student:riec

# --------------------

# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model 

    
#     def show_info(self)->str:
#         return f'{self.brand} --> {self.model}'

# obj =Car('BMW', '7 series')
# print(obj.show_info())
# obj2 = 'Lada sedan' 'Baklajan'
# print(obj2)


# -------------------------

# import random

# class Sniper:
#     health = 100

#     def __init__(self,name) -> None:
#         self.name = name

#     def shoot(self, other):
#         other.health -=20
#         print(f'Атаковал {self}')
#         print(f'у {other} осталлось {other.health}')

#     def __str__(self) -> str:
#         return self.name
    
# sniper1 =Sniper('John Snow')
# sniper2 = Sniper('Fridrich Sholtch')

# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 2)
#     sniper1.shoot(sniper2) if choice == 1 else sniper2.shoot(sniper1)

# if sniper1.health:
#     print(f'{sniper1} won the game')
# else:
#     print(f'{sniper2} won the game')


# ---------------------
# !!!!!!!!!!
# class Soda:
#     def __init__(self, ingridient=None) -> None:
#         if isinstance(ingridient, str):
#             self.ingridient = ingridient
#         else:
#             self.ingridient - None

#     def __str__(self) -> str:
#         if self.ingridient:
#             return f'Soda with {self.ingridient} taste'
#         else:
#             return 'Usual soda'

# a = Soda('Malina')
# print(a)

# b = Soda(5)
# print(b)

# c = Soda('Grusha')
# print(c)

# --------------

from typing import List

class TriangleChecker:
    def __init__(self, sides: List[int or float]) -> None:
        self.sides = sides
    
    def __str__(self) -> str:
        if not all(isinstance(x, (int, float)) for x in self.sides):
            return 'Nelzya postrooit tregolnik, Invalid Value!'
        elif any(x <= 0 for x in self.sides):
            return 'Nelzya postrooit tregolnik, Invalid Value!'
        self.sides.sort()
        if self.sides[0] + self.sides[1] <= self.sides[-1]:
            return 'Nelzya postrooit tregolnik, Summa Menshe ili ravna!'
        return 'My mojem postroit treugolnik'
        
t1 = TriangleChecker([10, 10, 10])
print(t1)

t2 = TriangleChecker([-1, 10, 10])
print(t2)

t3 = TriangleChecker([12, 5, 10])
print(t3)

t4 = TriangleChecker([1, 6, 2])
print(t4)
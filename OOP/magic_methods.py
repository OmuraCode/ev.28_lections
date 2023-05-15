# magic methods(маг методы)
# dunder methods(double undderscore)
# служебные мктоды


# Магия заключается в том, что эти методы запускаются без прямого образкния к ним, определенные методы
# могут отвечать за определенные операторы.


# class A(int):
#     pass

# obj = A()
# print(len(dir(obj)))

# Магические методы сравнения

# __eq__(self, other) -> 5 = 8

# __ne__ -> !=
# __lt__ -> <
# __gt__ -> >
# __le__ -> <=
# __ge__ -> >=

# print ('15' > 'abc')
# print(ord('1'), ord('a'))

# !!!!!!!!!!!!!!!!!!
# class Word:
#     def __new__(cls, obj):
#         # print(cls, '!!!')
#         # print(obj, '!!!')
#         obj = obj.replace(' ', "")
#         return super().__new__(cls, obj)

#     def __gt__(self, other):
#         print(' gt srabotal')
#         print(self)
#         print(other)
#         return len(self) > len(other)
    
#     def __lt__(self, __value):
#         return len(self) < len(__value)
    
#     def __eq__(self, __value: object) -> bool:
#         return len(self) == len(__value)

# obj = Word('  Hello')
# obj1 = Word (' M a kers')
# print(obj > obj1)
# print(obj < obj1)
# print(obj == obj1)


# ---------------------------
# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__
# % -> __mod__
# ** -> __pow__

class Cifra:
    def __new__(cls, *args, **kwargs):
        number = abs(args[0])
        instance = super().__new__(cls)
        instance.number = number
        return instance

    def __add__(self, other):
        print('add bylo vyzvano')
        res = self.number - other.number
        print(f'Result: {self.number} - {other.number} = {res}')

value1 = Cifra(-124)
value2 = Cifra(53)
value1 + value2
        
# ------------------

# from random import choice

# class Dog:
#     def sound(self):
#         print('bark bark')

# class Cat:
#     def sound(self):
#         print('Meow meow')

# class Lion:
#     def sound(self):
#         print('roar')

# class Pet:
#     def __new__(cls):
#         other = choice([Dog, Cat, Lion])
#         instance = super().__new__(other)
#         print(f'I am {type(instance).__name__}')
#         return instance
    
#     def __init__(self) -> None:
#         print('Pet newer was called')

# pet = Pet()
# pet.sound()


# ----------------
# SINGLETON

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self) -> str:
#         return str(id(self))

# a = Singleton()
# b = Singleton()
# print(a)
# print(b)
# print(a is b)

# ------------------
# Дандер методы строкового отображения объекта
# __str__
# __repr__

# class Base:
#     def __init__(self, stroka) -> None:
#         self.string = stroka

#     def __str__(self) -> str:
#         return f'Объект: {self.string}'
    
#     def __repr__(self) -> str:
#         return "Base('Example')"
    
# obj = Base('Jay-Z')
# print(obj)
# print(repr(obj))
# obj2 = Base('2pac')
# print(obj2)
# obj3 = eval(repr(obj2))
# print(obj3)




# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)
    
#     def __getitem__(self, index):
#         return self.coins[index - 1]


# obj = Kopilka()
# obj.add_coin(14)
# obj.add_coin(54)
# obj.add_coin(990)
# obj.add_coin(112)
# print(obj.total)
# print(obj.coins)
# print(len(obj))
# print(obj[1])

# for x in obj:
#     print(x)


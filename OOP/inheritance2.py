# Множественное наследование - это когда класс наследуется от двух или более классов

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')
    
#     def ride(self):
#         print('We\'re ridding on the ground')


# class Plane:
#     def play_music_at_station(self):
#         print('Listening Ed Sheeran!')
    
#     def fly(self):
#         print('We\'re flying!')

# class FutureAuto(Auto, Plane):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()

# # print(object, dir(object))

# _____________-
# Проблема ромба - когда поиск шел в родиткльский класс преждк чкм искать у соседнего общего потомка(решена с помощбю mro)


# MRO - (Method Resolution Order)- мезпнизм для корркетного поиска родительских методов
# Был создан для рещения проблемы ромба, которая появидасб посдк введения object в питон object&
# Поиск киде таким образом что если у родительских классов есть общий предокб то идет поск в ширину

# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
#     def say(self):
#         print('class First')

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class Myclass(First, Second):
#     def say(self):
#         super().say()
#         print('class MyClass')

# obj = Myclass()
# obj.say()
# print(Myclass.mro())

# -________________

# class Z: #3
#     pass

# class Y: #5
#     pass

# class A(Z): #2
#     pass

# class B(Y): #4
#     pass

# class X(A, B): #1
#     pass

# print(X.mro())


# -----------------


# Проблема перекрестного наследования

# class Y:
#     pass

# class X:
#     pass

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass

# class MyMRO(type):
#     def mro(cls):
#         return [cls, A, B, X, Y, object]
    

# class MyClass(A,B, metaclass=MyMRO):
#     pass

# print(MyClass.mro())





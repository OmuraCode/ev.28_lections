# -*- coding: utf-8 -*-
# Типы данных -> int, float

# = -> оператор присваивания
# variable (переменная)
# num = 5
# print(num) #5
# num 79 # переопределение
# print(num) # 79

# PEP8
# tommorow_day = "10.03.2023" # Snake case
# tommorowDay = "10.03.2023" #Camel case

# num1 = 5
# num2 = 153
# result = num1 + num2
# print ("Summa:", result)
# 
# num1 = input ('Enter the num1: ') # -> '5'
# num2 = input ('Enter the num2: ') # -> '7'
# num1 = int(num1)
# num2 = int(num2)
# print(num2 - num1)
# print(num2, '-', num1, '=', num2 - num1 )
# 
# *
# num1 = int (input('Enter the num1: '))
# num2 = int (input('Enter the num2: '))
# print(num1, '*', num2, '=', num1 * num2 )

# / and // and % деление
# / обычное деление
# // деление без остатка
# % - модульное деление (получение остатка от деление)

# num1 = 7
# num2 = 3
# print('/', num1 / num2) #2.333
# print('//', num1 // num2)# 2
# print('%', num1 % num2) #1


# ** -> возведение в степень
# print (5 ** 2)
# print (16 ** 55)

# print (9 ** 0.5) #3 квадратный корень


# pow -  возвеление в степень
# pow (num1, num2)
# num1 = 5
# num2 = 10
# print (num1 ** num2)
# print (5 ** 10)

# a = 5 
# b = 2
# res = pow (a, b, 12)
# print(res)

# round () - округление числа с плавающей точкой

# a = 5.728232
# print(round(a, 2))

# abs( ) - абсолютное значение числа -> abs (-5) ->
#                                          |-5| ->
# a = abs (-16)
# b = (15)
# print(a, b)


# divmod(a, b) -> выводит 2 числа ,1е число это результат целочисленного деления (//), 
# а 2е это модульное деление (%)

# res = divmod(5, 2)
# print(res)
# print ((5//2,5 % 2))

# import math 

# a = 5
# print (round(math.sqrt(a), 2))



# множественное присваивание
# оператор присваивание (=)
# a = 51

# b = 15
# c = None

# print ('a:', a, 'b:', b)

# c = a
# a = b
# b = c

# print ('a:', a, 'b:', b)

# c = a
# a = b
# b = c

# a, b = b, a

# print ('a:', a, 'b:', b)

# num1, num2, num3 = input("Num1:"), input("Num2: "), input("Num3: ")
# print (num1)
# print (num2)
# print (num3)




# """Дана переменная с радиусом окружности, найдите периметр и площадь окружности, выведите результат а терминал"""

# from math import pi

# r = int(input( 'Vvedite radius:'))
# res_P = 2 * r * pi
# res_S= pi * r ** 2
# print ("S okruzhnosti: ", round(res_S))
# print ("p okruzhnosti: ", round(res_P))

# Рандом 
# from random import randint

# print (randint (1,10))

# name = input("Vvedite svoe imya: ")
# last_name  = input("Vvedite svoyu familiyu: ")
# num = randint(1000000, 9999999)
# print (name, last_name, num)



from random import randint
num = randint(1, 10)
print(num)
i = 0
while i < 3:
  guess = int(input('Ugadai chislo: '))
  if guess == num:
    print("Ty pobedil! KRASAVA!")
    break
# #   i = i + 1
# i += 1 # increment


# inp1 = int(input('chislo1: '))
# inp2 = int(input('chislo2: '))
# inp3 = int(input('chislo3: '))
# res = inp1 * inp2 % inp3
# print(res)

# num1 = int(input (" ") )
# num2 = int(input (" ") )
# num3 = 3.14
# res = num1 % num2 * num3
# print(res)


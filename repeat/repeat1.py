#1 ZADANIE

# num1 = 1

# while num1 >= 0:
#     num1 = input("vvedite chislo: ")
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else: 
#         num1 = 1
# print('Встретилось отрицательное число!')



# ________________________________________-


# #2 ZADANIE ubrat' dublikaty

# from random import randint

# ls = []
# for x in range(0, 100):
#     ls.append(randint(0, 100))

# ls.sort() 
# print(ls, len(ls))

# res = []
# for x in ls:
#      if x not in res:
#           res.append(x)
# print(res, len(res))

# _____________________________________

# 3 ZADANIE 24 task log vyr


"""
Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
Вводить в порядке x1, y1, x2, y2
"""

# x1 = int(input('Vvedite 1 coordinatu gde sti]oit ladya: '))
# y1 = int(input('Vvedite 2 coordinatu gde sti]oit ladya: '))
# ladya = [x1, y1]  # 2, 5 stoit ladya

# x2 = int(input('Vvedite 1 coordinatu kuda idet ladya: '))
# y2 = int(input('Vvedite 2 coordinatu kuda idet ladya: '))
# target = [x2, y2]

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)






# __________________________________-   GOLODNYE IGRY

# import random

# ls = ['Plov', 'Besh-Barmak', 'Kuurdak', 'Oromo', 'Lagman']
# p = 0
# b = 0
# k = 0
# o = 0 
# l = 0


# for x in range(0, 1_000_000):
#     meal = random.choice(ls)
#     # print(meal)
#     if meal.lower() == 'plov':
#         p += 1
#     elif meal.lower() == 'besh-barmak':
#         b += 1
#     elif meal.lower() == 'kuurdak':
#         k += 1
#     elif meal.lower() == 'oromo':
#         o += 1
#     else:
#         l += 1
# print('Результаты голодных игр: ')
# print(f'Plov: {p}\nBesh-barmak: {b}\nKuurdak: {k}\nOromo: {o}\nLagman: {l}')


#_________________________________________________________

#ZADANIYE
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


# Nomer#1

# nums = [2, 7, 11, 15]
# target = 9
# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         print(f'Otvet: {i}, {nums.index(num)}')
#         break
    


#Nomer#2

nums = [4, 11, 2, 5, 1, 6]
target = 8
for i in range(0, len(nums)):
    num = target - nums[i]
    if num in nums:
        if num != nums[i]:
            print(f'Otvet: {i}, {nums.index(num)}')
            break

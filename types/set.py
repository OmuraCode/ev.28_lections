# set() - множества
# Это изменяемый неупорядоченный, итерируемый, неиндексируемый тип данных
# Множества хранят в себе только неизменяемые типы данных
 

# 1 -> set()

# a = set([1,2,3,4,5])
# print(a)

# a = set({1:2, 3:4})
# print(a)

# 2 -> {}

# set2 = {1, 2, 4}
# print(set2, type(set2))

# set2 = {1,2,2,2,5}
# print(set2)

# set1 = {1, 0, True, False}
# print(set1)
# a = 0
# print(bool(a))

# __________________________
# Методы set

# add -> добавление 

# set1 ={1,2,3}
# set1.add(4)
# print(set1)
# set1.add((1,2,3,4,5))
# print(set1)


# update / он может добавлять, но не повторяя имеющиеся 
# добавляет все итерируемое

# set1 ={1,2,3}
# set1.update({3: '1', 4: '5'})
# print(set1)
# set1.update('string', {1,2,3,4,5,6,7,8})
# print(set1)


# -________________________________
# Удаление в set

# clear() - очищает все множества
# remove(element) - удаляет элемент но если элемента нет то выдает ощибку
# discard(element) - если элемента нет то ничего не происходит

# pop() - удаляет из set (FIFO) first in first out

# set1 = {1,2,3,4,5}
# set1.remove(2)
# set1.clear()
# set1.discard (9)
# print(set1.pop())
# print(set1)


# difference - выводит отличие 1го значения от второго
# set1 = {1,2,3,4,5}
# set2 = {2,3,5,7}
# print(set1.difference(set2))
# print(set1- set2) # 2й способ

# print(set2.difference(set1))
# a = set1.symmetric_difference(set2)
# print(a)
# print(set1^set2) # 2й способ


set1 = {1,2,3,4,5}
set2 = {2,3,5,7}
# print(set1.intersection(set2)) # пересечение множеств
print (set1 & set2)

# print(set1.union(set2)) # соединяет 2 сета
# print(set1 | set2)



# задача №1
# Напишиту программу которая принимает 2 списка и выводит все элементы
# первого которых нет во втором

# set1 = set(['1', '2', '3'])
# set2 = set(['4', '5'])
# print(set1.difference (set2) )
# _____________________

# Задача №2
# Нужно проверить все ли числа в последовательности уникальны

# num = list(input())
# print(len(num) == len(set(num)))

# ___________________________________________

# frozenset - неизменяемое множество
# a = frozenset([1,2,3,4,5])
# # a.add(7)
# print(a)



# __________________________
# tuple - неизменяемый, индексируемый, итерируемый, упорядоченный тип данных

# inex(element) - возврашвет индекс этого элемента в кортеж
# литералы ()
# a = (True, 1, 2, 1, 1, 'a')
# # print(a, type(a))
# # b = tuple()
# # count(element) - возвращает число вхождений этого элемента в кортеж
# print(a.count(1))






























































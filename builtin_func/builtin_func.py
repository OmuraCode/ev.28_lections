# Встроенные функции

# Анонимная функция - lamda (Обычная функция с одной особенностью, у нее нет имени)
# Принимает сколько угодно параметров, но всегда возвращает одно выражение 

# def hello():
#     return 'hello'
# print(hello())

# x = lambda: 'hello'
# print (x())



# x = lambda a, b, c: (a*b) % c
# print(x(5, 5, 3))


# x = lambda a, b, degree=None: a * b ** degree if degree else a * b
# print(x(5,5))
# print(x(5,5,4))



# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# print(my_doubler(50))




# list_ = ['hello', 'bil', 'axaf', 'po']

# a = sorted(list_, key=len, reverse=True)
# print(a)



# dict_ = {
#     'john': 500,
#     'tirion': 160_000,
#     'tom': 150,
#     'sanzhar': 20,
#     'ayana': 100_000
# }
# dict_copy = dict(sorted(dict_.items(), key =lambda x: x[1], reverse=True))
# print(dict_copy)
        
# ________________________

# map(function, iterable) - применяется к каждому элементу внутри iterable фунуцию, которую мы 
# передаем функцию, закидывая в результат те данные, которые возврашает функция. 
# В результате мы получаем mapoject(iterable). в котором хранятся все наши данные.

# ls = ['1', '2', '3']
# new_list = list(map(int,ls))
# print(new_list)




# ls = ['one', 'two', 'three', 'four']
# new_list = list(map(lambda x: str.capitalize(), ls))
# print(new_list)



# names = ['john', 'jamie', 'aria', 'sansa', 'lord drakula']
# new_list = list(map(lambda x: f"Hello mr/mrs {x}", names))
# print(new_list)


# ______________________-
# Функция высшего порядка - функция, которая приниает в качестве аргумента другую функцию

# filter(function, iiterable) - принимает ко всем элементам iterable функцию, которую мы передаели
# и возвращает filterobject(итератор) только с теми элементами , для которых функция вернула True

# ls = ['one', 'lili', 'oleg', 'baila', 'tition']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)


# _______________________________
# enumerate(iterable) - пронумеровывает каждый элемент внутри iterable ее собственным индексом

# ls = ['str1', 'str2', 'str3']
# new_list = list(enumerate(ls))
# print(new_list)




# ---------------------------------- PART 2

# zip(iterables) - она соединяет кадлый элемент итерируемых объектов м/у собой в тип данных tuple и возвращает итератор

ls1 = [1, 2, 3]
ls2 = [100, 200, 300]

res = dict(zip(ls1, ls2))
print(res)



# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]
# res = list(zip(ls1, ls2, ls3))
# print(res)



# zip для создания словарей --->

# d_keys =['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'oktbr': ['bishkek_oktbr', 'gorkaya 213', 'Vefa', 'Cisko', '10.233.43.1'],
#     '1may': ['bishkek_1may', 'jinek jolu 222', 'White house', 'Cisko', '12.253.09.1'],
#     'svrdl': ['bishkek_svrdl', 'almatinka 26', 'zapravka', 'Cisko', '11.276.12.0'],
# }

# bishkek_data = {}

# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))

# print(bishkek_data)


# _______________

# all(), any()


# all(iterable object) -Возврашает True, если все объекты итерируемого обЪекта истина, иначе False


# ls  =[5, 6, 7]
# print(all(ls)) # -> True



# ip = '10.255.0.155' # True
# ip1 = '10.124.0y.202' #False

# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)




# any - Возврашает True, если хотя бы один элемент итерируемого обЪекта истина, иначе False

# ls = [1,2,3,4,'']
# print(any(ls))



# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Vvedite komandu: ')

# if any(x in command for x in ignore):
#     raise Exception('Block you!')
# print('OK!')


# ______________________________________________________
# PASSWORD GENERATOR

# from random import choices
# from string import ascii_letters, digits, punctuation
# from itertools import repeat

# symbols = '_()+-@!#%'
# q_pass = int(input('Vvedite kolichestvo paroley: '))

# result = {
#     f(choices(ascii_letters,k=15), choices(digits, k=6), choices(symbols,k=2))
#     for f in repeat (lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(result)
# print(f'Quantity of passwords: {len(result)}')

# from statistics import mean

# avg = mean(len(x) for x in result)
# print(f'AVG len of password: {avg}')































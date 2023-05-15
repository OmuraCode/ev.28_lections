# num1 = int(input (" ") )
# num2 = int(input (" ") )
# num3 = 3.14
# res = num1 % num2 * num3
# print(res)
# print (num1 % num2 * num3)



# name = input('Your name: ')
# last_name = input ('Your last name: ')
# age = input('Your age: ')
# city = input(' Your city: ')
# print(f'вас зовут {name} {last_name} ваш возраст {age} вы из города {city}') 

#  6 task
# x = 45
# y = 56
# z = 56
# if x == y and x == z and y == z:
#     print('3')
# elif x == y or x==z or y == z:
#     print('2')    
# else:
#     print('0')

# x = int(input())
# y = int(input())
# res = x/y
# res2 = x//y
# res3 = x%y
# if res3 == 0:
#     print ('Частное:' res)

# a = {'x': 1, 'y': 2, 'z': 1} 
# ls = a.keys()
# print(ls[1])


# a = {'a': 1, 'b': 2, 'c': 1} # 3 task
# print(a.setdefault (55, 'f'))



# a = {'1', 4, 5, 'fred'}
# b = {'2', 5, 3, 'mike'}
# c = a.symmetric_difference(b)
# print(c)


# _____________________________ 9 task dictionary
# a = {
#     'a': 1,
#     'b': 4,
#     'c': 1,
#     'd': 5,
#     'e': 6,
# }
# b = a.copy()
# for x, y in list(b.items()):
#     if y % 2 == 0:
#         b.setdefault(y, 2)
# else:
#      b.setdefault(x, y)
# print(b)



# a = {'a': 1, 'b': 2, 'c': 1}
# b = {}
# for k, v in a.items():
#     b.append(k)
# print(b)



# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in a.items():
#     if v % 2 == 0:
#         removed = a.pop(v)
# print(a)


# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# b = a.copy()
# for k, v in b.items():
#     if v % 2 == 0:
#         removed = a.pop(v)
# print(a)





# num1 = int(input())
# num2 = int(input())
# num3 - 7.6
# print((num1 % num2) * num3)



# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x for x in list_ if x > 0 and x % 2 = 0]
# print(int_list)




# import random

# # число попыток угадать
# guesses_made = 0

# # получаем имя пользователя из консольного ввода
# name = input('Привет! Как тебя зовут?\n')

# # получаем случайное число в диапазоне от 1 до 30
# number = random.randint(1, 30)
# print ('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))

# # пока пользователь не превысил число разрешенных попыток - 6
# while guesses_made < 6:
   
#     # получаем число от пользователя
#     guess = int(input('Введи число: '))
   
#     # увеличиваем счетчик числа попыток
#     guesses_made += 1

#     if guess < number:
#         print ('Твое число меньше того, что я загадал.')

#     if guess > number:
#         print ('Твое число больше загаданного мной.')

#     if guess == number:
#         break

# if guess == number:
#     print ('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
# else:
#     print ('А вот и не угадал! Я загадал число {0}'.format(number))





# list_ = [1,2,3,4,5,6,7,8,9,10]
# new_list = [x ** 2 for x in list_ if x % 2 == 0 or x % 2 != 0 ]
# print (new_list)
# list_ = [1,2,3,4,5,6,7,8,9,10]
# new_list = [x ** 2 if x % 2 == 0 else x for x in list_]
# print (new_list)

# string = 'hello world'
# print(f'{string} \n{string} \n{string}')


# string = '1 2 3 4 5 6'
# if string.isdigit():
#     num1 = len(string) / 2
#     num2 = int(string)
#     num3 = sum([0: num1])
#     num4 = sum([num1:-1])
# elif num3 == num4:
#     print('да')
# elif num3 != num4:
#     print("нет")


# task 15 logic operators
# string = '1 2 3 1 2 3'
# if int(string[0]) + int(string[2]) + int(string[4]) == int(string[6]) + int(string[8]) + int(string[-1]):
#     print ("да")
# else:
#     print('нет')


# task 16 logic
# a = int(input())
# b = int(input())
# c = int(input())
# if a < b < c:
#     print(a, b, c)
# elif a < c < b:
#     print(a, c, b)
# elif b < c < a:
#     print(b, c, a)
# elif b < a < c:
#     print(b, a, c)
# elif c < a < b:
#     print(c, a, b)
# elif c < b < a:
#     print(c, b, a)

python3 -m venv venv
. venv/bin/activate
deactivate


# task 21 logic operators
# a = int(input())
# b = int(input())
# c = int(input())
# if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#     print ('rectangular')
# elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
#     print ('acute')
# elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
#     print ('obtuse')
# elif a + b > c or a + c > b or b + c > a:
#     print('impossible')



# n = int(input())
# if n == 1 or n == 21 or n == 31 or n == 41 or n == 51 or n == 61 or n == 71 or n == 81 or n == 91:
#     print(f'На лугу пасется {n} корова')
# n = int(input())
# if n == 1:
#     print(f'На лугу пасется {n} корова')
# elif n >= 2 and n <= 4:
#     print(f'На лугу пасется {n} коровы')
# elif n >= 5 and n <= 9:
#     print(f'На лугу пасется {n} коров')
# temp = n % 10
# if temp == 1:
#     print(f'На лугу пасется {n} корова')
# elif temp >= 2 and temp <= 4:
#     print(f'На лугу пасется {n} коровы')
# elif temp == 0 or temp >= 5 and temp <= 9:
#     print(f'На лугу пасется {n} коров')









# n = int(input()) 
# if n >= 11 and n <= 14: 
#     print(f'На лугу пасется {n} коров') 
# else: 
#    temp = n % 10 
# if temp == 0 or (temp >= 5 and temp <= 9): 
#     print(f'На лугу пасется {n} коров') 
# if temp == 1: 
#     print(f'На лугу пасется {n} корова') 
# if temp >=2 and temp <=4: 
#     print(f'На лугу пасется {n} коровы')





# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0, "панама")
# print(suitcase)



# def is_palindrome(x):
#     if x[:] != x[::-1]:
#         return True
#     else:
#         return False
# is_palindrome('rer')



# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for x in nums:
#     if x < 5:
#         res.append(x)
# print(res)


# a = input()
# list_ = list(a.split(","))
# tuple_ = tuple(a.split(','))
# print(list_)
# print(tuple_)



# list_ =  [1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     new_list.append(str(x))
# print (new_list)



# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     if x % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)



# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# list3 = list1 + list2
# print(sum(list3))



#13 lists
# a = input().split(',')
# list_ = []
# for x in a:
#     list_.append(x)
#     list_.sort
# print(list_)




# list_ = [1,2,2]
# ls = list_
# if len(ls) != len(list_):
#     print('yes')
# else:
#     print('ERROR')

# list_ = [1,1,3] 
# set_ = set(list_) 
# if len(set_) != len(list_): 
#     print('yes') 
# else: 
#     print('ERROR')

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# res = string_.split(' ')
# # print(res, type(res))
# list_ = [x for x in res if x.isdigit()]
# print(list_)


#  {'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
# }

# for k,v in dict_:
#     for ke, va in v:
#         if va

# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for k, v in dict1.items():
#     if v % 2 != 0:
#         dict2.setdefault(k, 1)
#     else:
#         dict2.setdefault(k,v)
# print(dict2)



# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(dict_.items()):
#     if v != None:
#         dict_.pop(k)
# print(dict_)


# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for k, v in dict1.items():
#     dict2 = {k ** 2, v}
# print(dict2)


# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# max_value = max(dict_.values())
# for k, v in dict_.items():
#     if v == max_value:
#         print(k)



# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# dict2 = {}
# for k, v in dict_.items():
#     for x, y in v.items():
#         dict_.update(y)
#         print(dict_)


# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# # dict_ = {k:(v[v2]) for k,v in dict_.items()} 
# # print(dict_) 
# for k,v in list(dict_.items()): 
#     for v2 in v.values(): 
#         dict_[k] = v2 
#     print(dict_)

dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}
for k, v in list(dict1.items()):
    # for v2 in v.values():
    dict1[k] = sum(v.values())
print(dict1)


dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
'Nik': {'history': 84, 'math': 85, 'literature': 87}}


dict2 = {x for k, v in dict_.values if i = max(i)}
print(dict2)
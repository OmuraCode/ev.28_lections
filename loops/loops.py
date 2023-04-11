# while <expression>:
    # <body>

# i = 0
# while i < 10:
#     i += 1 # i = i + 1
#     print(i)
#     print(f'цикл сработап {i} раз')



# ls = list(range(1,51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())
    # print(ls)

# _____________
# пример

# name1 = ''
# name2 = ''
# i = 0 
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Vvedite imya1: ')
#     name2 = input('Vvedite imya2:')
#     print()
#     if i >= 5:
#         print('цикл остановлен!')
#         break # принулительная остановка
#     i += 1 
# else:
#     print('Ты угадал!')





# _________________________________

# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# i = 3
# # password = None
# while password := input (f"{user['username']} Vvedite parol\': ") != user['password']: # ':=' моржовый оператор
#     # #password = input (f"{user['username']} Vvedite parol\': ")
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany!!!')
#         break
# else:
#     print(f'{user["username"]} vy uspeshno zashli v sistemu!')



# ______________________________________

# for <variable> in <iterable object>:
    # <body>

# list_ = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9] # итерация
# i =  iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# ______________________________
# TUPLE
# a, b, c = 1, 2, 3
# print(a, b, c)

# a = 1, 2, 3, 4, 5, 6
# print(a)
# print(type(a))


# import random
# ls =[]
# for x in range(1, 100):
#     ls. append(random.randint(1,50))

# print(len(ls))
# ls = set (ls) # Удалили дубликаты переделав список в set, и обратно в list
# ls = list(ls) 
# print(ls)
# print(len(ls))


# ____________________________________
# continue

# ls = ['Tirion', 'Bilal', 'John', "Sansa", 'Jamie', 'Eddart']
# for x in ls:
#     if x == 'Bilal':
#         continue
#     print(f'Hello Mr/Mrs {x}!')


# нечетные числа
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
    

# _______________________
# Задача
# найти делители числа


# Число 100
# 1, 2, 4, 5, 10
# 20, 25, 50, 100

num = 100_000_000_000
res = []

for x in range(1, int(num ** 0.5) +1):
    if num % x == 0:
        res.extend({x, num // x})

res.sort()
print(res)
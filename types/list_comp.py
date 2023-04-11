# list comprehensions - генераторы списков

# list comprehensions - упрощенный подход к созданию списков который задейстует в себе цикл for, а также 
# конструкцию if для определения того что в итоге попадает в наш списокё


# 1 пример
# list -> 0 -200 -> num%2 ==0

# ls =[]
# for x in range(0, 201):
#     if x % 2 == 0:
#         ls.append(x)
# print(ls)

# в одну строку^->

# ls = [x for x in range(0,201) if x % 2 == 0]
# print(ls)

#2 пример

# list: 0 - 300 -> num % 2 == 0, num % 3 == 0

# ls = [x for x in range(0, 300) if x % 2 == 0 and x % 3 == 0]
# print(ls)

# 3 пример(else)

#list: 0 - 100 -> x % 2 == 0 : x ** 2, x % 3 == 0: x ** 3 

# ls = []
# for x in range(0,100):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     elif x % 3 == 0:
#         ls.append(x ** 3)
# print(ls)

# 2 способ ^

# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0, 101) if x % 2 == 0 or x % 3 == 0]
# print(ls)


# ____________________________________________


# newlist = [expession for item in iterable <if condition == True>]


# ls = [str(i * 2) for i in range(0, 11)]
# print(ls)

# primer


# ls  = [[1,2,3], [4,5,6], [7,8,9]]
# ### result = [1,2,3,4,5,6,7,8,9]
# res = []
# for x in ls:
#     for item in x:
#         res.append(item)
# print(res)


# 2 способ^

# ls  = [[1,2,3], [4,5,6], [7,8,9]]
# res = [item for x in ls for item in x]
# print(res)

# _____________________________


# from datetime import datetime

# start = datetime.now() #19.55.43

# ##### code ... (3 sec)
# ls = []
# for x in range (0, 100_000_000):
#     ls.append(x)
# finish = datetime.now() #19.57.46
# print(finish-start)


# 2 способ ^ быстрее чем 1й через comrehension

# from datetime import datetime

# start = datetime.now()
# ls = [x for x in range(0, 100_000_000)]
# finish = datetime.now() #19.57.46
# print(finish-start)


# _________________________________________________________________
# set comprehensions

# set_ = {x for x in range (1, 100)}
# print(set_, type(set_))

# _________________________________________________________________
# dict comrehensions

# dict = {
#     key: value,
#     key: value,
# }

# пример 1
# dict_ = {x: x**2 for x in range(0, 16)}
# print(dict_)

# пример 2
names = ['John', 'Tirion', 'Eygan', 'Sansa', 'Ramsey']
dict_ = {x: len(x) for x in names}
print(dict_)

# пример 3
# dict1 = {
#     'Soke': {'history': 99, 'phyzics': 95, 'math': 94},
#     "Mazya": {'history': 84, 'phyzics': 75, 'math': 86},
#     "Sokfok": {'history': 100, 'phyzics': 87, 'math': 90},
# }
# res = {}
# for k, v in dict1.items():
#     # ## print(k)
#     # ## print(v)
#     for inner_k, inner_v in v.items():
#         if max(v.values()) == inner_v:
#             res[k] = inner_k
# print(dict1)
# print(res)


# 2 способ^

# dict1 = {
#     'Soke': {'history': 99, 'phyzics': 95, 'math': 94},
#     "Mazya": {'history': 84, 'phyzics': 75, 'math': 86},
#     "Sokfok": {'history': 100, 'phyzics': 87, 'math': 90},
# }

# res = {key: inner_key for key, value in dict1.items() 
# for inner_key, inner_value in value.items() if inner_value == max(value.values())}
# print(res)

 


# ____________________________________

# ZADACHA 10 TASK
 
# try:
#     n = int(input('Vvedite chislo: '))
# except ValueError:
#     print('Invalid number!')
# else:
#     dict_ = {x: x** 2 for x in range(1, 501) if x%n==0}
#     print(dict_)





















# list() -> (списки, массив)- измкеяемый послкдовательеый тип данных 
# который представляет из себя коллекцию каких либо объектов(значения)

# my_list = [1, 'string', False, None, [1,2,3,4,5]]
# print(my_list, type(my_list))



# # range() - возаращает последовательеость элементов(чисел)
# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)


# list()

# my_list = list('Hello world')
# print(my_list)


# tuple_ = ('banana', 'apple', 'cherry')
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls,type(ls))


# Индексакция в списках 
# ls = [1,2,3,4,5, 'string', [True, False, None]]
# print (ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:]) #cрез


# ls = [1,2,3,4,5, 'string', [True, False, None]]
# print(ls[6][0:2])


# ls = list (range(1, 11))
# print(ls)
# for num in ls:
#     print("hui")


# ls = ['john', 'Bran', 'Tirion', 'Akyl', 'Jamie']
# print(ls, len(ls))
# for x in ls: 
#     print(f'Hello mr/mrs {x}! Welocome to the North')
#     print('1')
# print('2')


# ls ->1,21 -> для четных = квадрат
#           - для нечетех = куб

# ls = list(range(1,21))
# print(ls)
# for num1 in ls:
#     if num1 % 2 == 0:
#         print(f'chislo chetnoe {num1}, kvadrat: {num1**2}')
#     else:
#         print(f'chislo chetnoe {num1}, kub: {num1**3}')



# __________________________________________________________________


#методы  списков
# print(dir([]))

# append (element) - Dobavlyaet element v kontse spiska

# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('hello')
# ls.append([True, False])
# print(ls)


# extend(object) - rashiryyaet spisok
# ls = [1, 2, 3]
# ls.append('hello')
# print(ls)
# ls.extend('hello')
# ls.extend(str(45))
# ls.extend([1, 2, 3])
# print(ls)

# ls = [1,2,3]
# ls1 = [4,5,6]
# print(ls + ls1)



# sort() - сортирует список, ксли передать reverse=True, то список отсортируется в убывающем порядке

# from random import randint
# ls = []
# for x in range(0, 100):
#     num = randint(0, 1000)
#     ls.append(num)
# print(ls)
# ls.sort(reverse=True)
# print('After')
# print(ls)



# ls = ['John', 'Daynaris', 'Tirion', 'Aizirek']
# ls.sort(key=len)
# print(ls)


# insert(index, element) -добваляет элемент по указанному index
# ls = ['string', 2, 3, False]
# ls.insert(1, 0)
# print(ls)



# remove(element) - удаляет элемент из списка/ если такого нет то выводится ошибка
# pop (index) - удаляет и вощвразает элемент из списка по index но если index не передать, то удаляет последний элемент

# ls = [5, 1, 2, 4, 4, 5, 5, 5]
# # ls.remove(5)
# # print(ls)
# # print(5 in ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)


# pop
ls = [5, 1, 2, 4, 5, 5]
print(ls.pop(0)) #5
# print (ls.remove(5)) # None
# deleted = ls.pop()
# print(ls)
# print(deleted)






# # update ----------- ЗАМЕНА
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# print (ls[::-1])



# pizza = ['first_item', 'second_time', 'third_item', 'forth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)
# print(spisok)





# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for x in nums:
#     res = []
#     if x < 5:
#         res.append(x)
# print(res)









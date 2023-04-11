# найти квадратб куб результат деления на 100
# num = 5
# -> {'num':  5, '2': 25, '3':125, '100': 0.05}

# num1 = 5
# print({'num1':  5, '2': num1 ** 2, '3': num1 ** 3, '100': num1/100})
# num2 = 16
# print({'num2':  5, '2': num2 ** 2, '3': num2 ** 3, '100': num2/100})
# num3 = 28
# print({'num3':  5, '2': num3 ** 2, '3': num3 ** 3, '100': num3/100})
# num4 = 1154
# print({'num4':  5, '2': num4 ** 2, '3': num4 ** 3, '100': num4/100})
# num5 = 31
# print({'num5':  5, '2': num5 ** 2, '3': num5 ** 3, '100': num5/100})


# DRY - do not repeat yourself
# 2 sposob -->

# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31

# def operations(num):
#     print({'num':  5, '2': num ** 2, '3': num ** 3, '100': num/100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)


# Функция - это именнованная часть программы котороая содерджит в 
# себе определенный набор инструкций, и может вызываться в других частях
# программы столько раз сколько угодно

# syntax -->
# def name_of_function(<a, b> #параметры):
    # <body> # код, какая то логика которая будет давать конечный результат
    # <return> # оператор который помогает вернуть результат

# name_of_func(5, 6 # argumenty)


# Параметры функции - переменные которые будут принимать данные от пользователя
# и хранить в себе эти данные

# Аргументы функции - данные которые мы передаем в функции в моменте вызова


# __________________
# print(len('str'))

# ls = [1,2,3,4,5,6]
# str1 = 'hello world c vami Kani i John Snow!'

# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print(f'result: {i}')

# our_len(ls)
# our_len(str1)



# def isEven(obj):
#     if obj % 2 == 0:
#         return True
#     else:
#         return False
    
# print(isEven(56))


# isEven()
# ---------> аннотации
# def isEven(num: int) -> bool:
#     '''Our funtions returns True or False while cheking number for even number'''
#     return True if num % 2 == 0 else False
# print(isEven(5))
# print(isEven(89))


# ______________________________________________
# ZADACHI

# 1111111

# words = ['john', 'Ono', 'Kazak', 'peter', 'dovod', 'radar']

# def get_polindrom(words):
#     result = []
#     for word in words:
#         if word.lower() == word [::-1].lower():
#             result.append(word)
#     return result
    
# polindrom_words = get_polindrom(words)
# print(polindrom_words)


#222222222 DEPOSIT

# ERROR - POSMOTRI
# def get_percenage(money, period):
#     if money < 30_000:
#         raise ValueError('Вложить можно более 30000')
#     elif period < 3:
#         raise ValueError('Период должены быть не менее 3 лет')
#     year = 0
#     while year < period:
#         money += money * 0,1
#         year += 1
#     return money
# try:
#     money = float(input('Введите сумму: '))
#     period = int(input('Vvedite period: '))
#     print(get_percenage(money, period))
# except ValueError:
#     print('Неправильный ввод')



# def test_func(a=1, b=1):
#     pass
# range
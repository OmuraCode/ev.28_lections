# Обработка исключений
# try ecpept

# Errors -> связаны с кодом
    # SyntaxError
    # IndetationError
    # TabError

# Исключения excetions -> связаны с неправильными данными которые передают в код:
    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndexError
    # KeyError
    # ValueError
    # BaseException # прородитель всех исключений


# try:
#     a = int(input('Enter the number: '))
# except:
#     print('Неправильные данные')
# else:
#     print(a * 5)



# try:
#     <body>
# except:
#     <body> сработает если есть ошибка
# <else>:
#     <body> если Нет ошибки
# <finally>:
#     <body> сработает в любом случае


# ls = ['John Snow', 'Tirion', 'Sansa']
# print(ls)
# try:
#     i = int(input('Vvedite Index: '))
#     print(ls[i])
# except ValueError:
#     print('вы ввели неправильные даннык')
# except IndexError:
#     print('Вы ввели неправильный индекс')



# _________________________

# Отображение ошибки 
# Exceptions as e (error)
# dict_ = {'1': 'one', '2': 'two', 'name': 'John' }
# try:
#     key  = int(input('Vvedite key: '))
#     print(dict_[key])
# except Exception as e:
#     print(f'Oops {e.__class__} error!')




# try:
#     num1 = int(input('Enter the num 1: '))
#     num2 = int(input('Enter the num 2: '))
#     result = num1 / num2 
# except ValueError:
#     print('Invalid input')
# except ZeroDivisionError:
#     print( " na nol delit nelzya")
# else:
#     print(result)
# finally:
#     print('The end')






# Операторы сравнения: < ; > ; == ; != ; <= ; >=

# Условные операторы и логические операторы
# 1 < 5 -> True
# 5 > 1 -> False

# Условные операторы 
# if
# elif
# else

# if <condition>:
#     <body> # сроаботает если в conition if будет True
# [elif] <condition>:
#     <body elif>
# [else]:
#     <body else> #cработает если во всех вышестоящих условиях пришло False

# string = input('enter something: ')
# if string.lower() == 'hello':
#     print('Hello it is me\nI was wondering if after all these years you\'d like to meet')
# elif string.lower() == 'john':
#     print('welcome back north king')
# elif string.lower() == 'abra kadabra':
#     print('Sim Salamon Kadabra')
# else:
#     print('совпадений не найдено')



# ПАРОЛЬ

# print('Registration:')
# email = input("Enter your email: ")
# password = input('Emter the pasword: ')
# if len(password) < 8:
#     raise ValueError('Pasword is too short!\n Need to be 8 symbols or more!')
# elif password.isdigit():
#     raise ValueError('Pasword is invalid!\nmust contain numbers too ')
# elif password.isalpha():
#     raise ValueError('Pasword is invalid!\nmust contain symbols too ')

# password2 = input('Enter pasword confirmation: ')

# if password != password2:
#     raise ValueError('Password is not match!')

# print (f'Succesfully registered! hello mr/mrs {email}')




# Проверка на возраст

# age = input ('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else: 
#     raise Exception ('Invalid value for age!')
# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} year!')
# else:
#     print('You can pass! Welcome to KZ')




# and - логтчкское и
# or - или
# not - лог отрицание

# money = 1_000_001
# status = 'premium'

# if money > 1000_000 and status == 'premium':
#     print("You are president of our club!")
# elif money > 1000_000 or status == "premium":
#     print('You are ministr of our club')
# else:
#     print('You are honorable member of our club')



# str1 = 'heelo world'
# print(str1)
# # symbol = input('Enter the symbol: ')
# # if symbol not in str1:
# #     print(f'Symbol: {symbol} does not exist!')
# # else:
# #     print(f'The symbol: {symbol} exists')

# 2 вариант
# symbol = input('Enter the symbol: ')
# if symbol in str1:
#     print(f'Symbol: {symbol} does not exist!')
# else:
#     print(f'The symbol: {symbol} exists')




# # Разрешаем доступ если он юзер гита или гугла и его возраст больше 21 или у него есть деньги (10000)
# user = 'John'
# is_google_user = True
# is_github_user = False
# age = 21
# user_coins = 12000

# if (is_google_user or is_github_user) and (age > 21 or user_coins > 10000):
#     print(f'You can enter the system Mr/Mrs {user}!')
# else:
#     print('Sorry, you couldn\'t enter')





# -_________________________________________
# TRY EXCEPT




























































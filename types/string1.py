'String- строки'
"hello world True 5"

'''
Hello world my name is akyl
'''

# Строки - набор последовательных символов которые мы используем для хранения и представления текстовой информации

# Индексация в строке
name = 'John'
#     # J = 0 = -4
#     # O = 1 = -3
#     # h = 2 = -2
#     # n = 3 = -1
print(name)
print(name[1])
str1 = 'kani'
print (str1[-1], str1[0])

# Соединение строк
# str1 = 'birthday'
# print (str1[5], str1[6], str1 [7])
# print (str1[0] + str1[1] + str1[2] + str1[3] + str1[4]) 


# Срезы  по индексам
# [start: end: <step>]

# str1 = 'birthday'
# print(str1[5:]) # 5 и пустота
# print(str1[:5])

# text = 'Hello world my name is John I\'m King of North'
# # print (text [:12])
# # print(text[::2]) # шаг (:2 - через один символ)

# print (text[::-1]) # (-1 -- c конца)



# Конкатинация строк (соединение)
# a = "Hello"
# b = "world"
# c = ' '
# print (a + c + b)


# Экранирование - это способ записи символов в строку которые невозможно ввести с клавиатуры

# \n -> перенос строки
# \t - горизонтальеая табуляция
# \v - вертикальная табуляция
# \f - перевод страницы
# \r - возврат указателя
# print('\vHello \tworld \nMy name is John Snow')



# Форматирование строк - изменение строки
# 1. с помощью %
# 2. c исподьзованием .format()
# 3. Интерполяция строк (преобразованик, f-stroki)

# # %
# name = input('Vvedite imya: ')
# last_name = input('Vvedite last name: ')
# # print ('добро пожаловать name + ' ' + last_name + '!')
# print ('Hello mr/mrs %s %s!' % (name, last_name))

# .format
# name = input('Vvedite imya: ')
# last_name = input('Vvedite last name: ')
# print ('приветствую вас, {} {}, в наш клуб! ' .format(name, last_name) )

# # Интерполяция f-stroki
# a = input('Enter mrs/mr: ')
# name = input('Vvedite imya: ')
# last_name = input('Vvedite last name: ')
# print(f'Hello {a} {name} {last_name}! Welcome to the party')




# задание  # len - количество символов
# text = 'Запомни Питтер, с большой силой приходит и ТТТТ большая ответственность.'
# reversed_text =  text[::-1]
# print(reversed_text) 
# i = 0
# count_t = 0
# len_text = len(reversed_text)
# while i < len_text: 
#     symbol = reversed_text[i]
#     if symbol == 'т' or symbol == 'Т':
#         count_t +=1
#     # print(symbol)
#     i += 1
# print(f"В тексте 'т' встретилась {count_t} раз")

# 
# str
# ''
# "hello"
# str(5)

# Методы 
# print(dir(str)) # выведение методов в терминал
# print (dir(int)) 

# a = 'Hello'
# b = 'John'
# # print(a != b)
# # print ('abc' == 'abc')
# print(a > b)
# print(a < b)

# Cравнение по двоичному коду
# print ("a") #97 ->1100001
# print('a' > 'b')
# # print('h' > 'c')
# print('hello' > 'harry') #True
# print('abc' > 'abc') #False

# сравнение количества символов
# len() - возвращает колво символов в строке
# a = 'Hello'
# b = 'john snow'
# print(len(a) < len(b))
# print(len(a), len(b))


# Методы строк
# replace(old, new, [count]) - меняет в строке символы old на new, ecли вы укажету count , то заменит count раз

# text = 'ha ha ha ha'
# result = text.replace('a', 'o', 2)
# print(text)
# print(f'result after replace: {result}')



# str1 = 'Hello world! My name is John Snow'
# result = str1.replace('John Snow', 'Jamie Lanister')
# print(result) 

# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip ()
# print(res)
# print(len(res))


# print(dir(str)


#isdigit -            Проверяет
#isnumeric ->   состоит ли ваша строка
#isdecimal -      полностью из чисел

# num = input ('Vvedite chislo: ')
# print(f'Vvedeno chislo?: {num.isdigit()}' )


# num = input('Vvedite chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vveli ne chisla')


# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())



# isalnum() - проверяет состоит ли наша строка из чисел и символов латинского алфавита и кириллицы
# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())


# isalpha() -> состоит ли наша строка полностью из символов алфавита 
# text = 'Hello world'
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())


# islower()
# isupper()
# istitle()
# str1 = 'Is. Imk'
# print(str1.islower())
# print(str1.istitle())
# str2 = 'ASD'
# print(str2.isupper())


# index(value, [start], [end]) - выводит индекс значения value, которое мы передаем  в нашей строке

# text = 'Hello John Snow'
# print(text.index('John', 2, 5))

# text = 'Hello world! My name is John Snow!' #0
# # print(text.index ('John'))
# res = (text.index ('o'))
# print (res) # 4
# res = text.index('o', res + 1)
# print (res) # 7
# res = text.index('o', res + 1)
# print (res) # 25
# res = text.index('o', res + 1)
# print (res) #31



# count(value, [start]) - считакт колво  вхождений value в нашу строку
# text = 'hello o o o hello'
# print (text.count('o'))
# print(text.count('hello'))




# split(separator) - дробит нашу строку на несколько частей по разделителю, все части сохраняются  в типе list

# text = 'Let me speak by my heart in English! Cause my name is John Snow'
# res = text.split(' ')
# print(res)
# print(len(res))

# a = 'hello#hello#hello#hello'
# res = a.split('#')
# print(res)




# # 'connector'.join(list) -> соединяет по connector строки которые находились в  list
# text = 'Let me speak by my heart in English! Cause my name is John Snow'
# res = text.split(' ')
# print(res)
# str1 = '#'.join(res)
# print(str1)


# find(value, [start], [end]) - делает тоже саамое что и index, но если не нашел то вернется -1
text = 'Hello'
print(text.find('l'))
print((text.find('lrwheg')), type(text.find('lrwheg')))
print('John Snow')


# swapcase() - переводит все символы в противоположенный регистр
# upper() - переволлит все в верхний регистр
# lower() - переводит все нижний регнстр

# text = 'Hello WorLD, 

# name = input('VVedite imya ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')


# fio  = "john edart snow"
# print(fio.title())


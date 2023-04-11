# 'Hello world my name is John, last name is Snow. Nice to meet you!'
# 'you! meet to Nice .Snow >>>....'


# ---->
# str1 = 'Hello world my name is John, last name is Snow. Nice to meet you!'

# def get_reversed_string(text):
#     # print(text[::-1])
#     spisok = text.split()[::-1]
#     # print(spisok[::-1])
#     return ' '.join(spisok)

# print(get_reversed_string(str1))
# print(get_reversed_string('hello woerld fuck you'))
    

# ___________________

# def sum_of_args(a, b, c=5, d=5): #параметры
#     return a + b + c + d

# result = sum_of_args(1,2,3,4) # аргументы
# print(result)
# res = sum_of_args # функция в переменную
# # print(res, type(res))
# print(res(5, 6, 7, 8)) # передать аргументы в переменной
# print(sum_of_args(5, 5))


# __________________________-

# Позиционные и именнованные аргументы

# def printParams(a, b, c): #-----> Позиционные
#     print(a, 'is sorted in param a')
#     print(b, 'is sorted in param b')
#     print(c, 'is sorted in param c')

# printParams(5, 10, 15) #-----> Позиционные
# print()
# printParams(c=5, b=10, a=15) #-----> именнованные
# print()
# printParams(a=20, b=30, c=15)



# def sum_of_args(a, b, c, d):
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # arguments (Позиционные)
# print(sum_of_args(a=5, b=20, d = 45, c =78)) # keyword arguments (именнованные)
# print(sum_of_args(5, 10, d=15, c=20))


# __________________________________

# оператор *

a = [1,2,3]
b = [4,5,6] 
c = [*a, *b]
print(c, type(c))


# --------------------------------------

# *args, **kwargs в функциях

# def printScores(student, *scores):
#     print(f'Name of student: {student}')
#     # #print(*scores)
#     print(f'AVG: {sum(scores)/len(scores)}')
#     for x in scores:
#         print('Score: ', x)

# print(printScores('John Snow', 100,90,80,95,88))



# def printPetNames(owner, **pets): #{'key': 'value'}
#     print(f'Owner name: {owner}')
#     # print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# printPetNames('John Snow', dog = 'Rex', cat = 'Garfild', fish=['Nemo', 'Dori', 'Batya'], turtle = 'leonardo')





# def getSomeData(a, b, *args, **kwargs):
#     print('параметры a и b:', a, b)
#     print('аргументы:', args)
#     print('именнованные аргументы:', kwargs)

# getSomeData(1,2,3,4,5, lang='Python', car = "BMW")






# _________________________________

# def generate_random_string(len_):
#     import string as s
#     import random
#     # print(s.ascii_letters, s.digits , s.punctuation)
#     symbols = s.ascii_letters +s.digits
#     res = list(
#         random.choice(symbols) for i in range(1,len_)
#     ) + list(random.choice(s.punctuation))
#     random.shuffle(res)
#     return ''.join(res)

# print(generate_random_string(7))
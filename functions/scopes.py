# Область видимости и пространства имен (scopes)
# Это технология которая определяет контекст имени(переменные) в рамках которого мы можем ее использовать

# build-ins (встроенная область видимости) -> print, len, max и тд

# global(Глобальная) - область одного файла

# enclosed(не локальная, замкнута(nonelocal))

# local(локальная)- область внутри одной функции

# ---------------

# x = 200
# def myFunc():
#     print(x)
#     a =300
#     print(a)
# myFunc()
# print(x)


# a = 10
# def hello(): #global
#     a = 'hello'
#     print(a, 'local inside func')
# hello()
# print(a,'global')



# LEGB - local -> enclosed -> global -> built-in # последовательность поска имен

# ----------------------------------------------------------


# Enclosed
# замкнутое пространстао имен - это локальное пространство 
# у которого ксть внутреннее(локальнок) локальнок пространство

# x = 'global'
# print(x, '1') #global

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): #local
#         x = 'local'
#         print(x, '3')
#     print(x, '2') #enclosed
#     local()
#     print(x, '4') #enclosed

# enclosed()
# print(x, '5')





# a = 5

# def func():
#     print(a) #5
#     a = a + 1 # error

# func()


# operatorн------>>>>
# global -> позволяет изменять значение горбальной переменной назодясь внутри локальной области

# nonlocal -> позволяет изменять значение нелокальной переменной находясб внутри локальной области


# var = 100

# def increment(): #(LEGB)
#     global var
#     var += 1 #var = var + 1

# print(var) # 100
# increment()
# print(var) # 101
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var) # 106




# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter() #<function counter.<locals>.increment at ......>
# print(c()) #1
# print(c()) #2
# print(c()) #3
# print(c()) #4
# print(c()) #5
# print(c()) #6
# print(c()) #7



# print(dir(__builtins__))
# print(len(dir(__builtins__)))



# globals() # функция, возвращает все именна внутри глобальной области видимости
# locals() # функция, возвращает все именна внутри глобальной области видимости и локальной



def counter():
    num = 0
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

def showStats(heroes, mobs):
    print()
    print(f'John Snow you killed: \n\tЛанистеров: {heroes} \n\tХодоков: {mobs}')

counter_heroes = counter()
counter_mobs = counter()
heroes = 0
mobs = 0
print('Приветствую вас, KING JOHN SNOW 228, в Весторос')
while True:
    print('Тебе доступны следуюшие действия: ')
    print('1-убить героя, 2-убить моба, 3-статистика, 4-выйти из игры')
    choice = input('Введите что хотите сделать: ').strip()
    if choice == '1':
        heroes = counter_heroes()
        print('Вы обезгпавили Ланистера!')
    elif choice == '2':
        mobs = counter_mobs()
        print('Вы убили белого ходока!')
    elif choice == '3':
        showStats(heroes, mobs)
    elif choice == '4':
        print('Пока пока, ждем в  следуюший раз!')
        break
    
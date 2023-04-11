# Декораторы - это функция оборачивает, которая позволяет 
# без изменения кода функции расширить ее функционал

# def decorator(func):
#     print(func)
#     func()

# def hello():
#     print('Hello stranger')

# def john():
#     print('My  name is John Snow I\'m King of North!')

# decorator(hello)
# print('!!!!!!')
# decorator(john)
# ______________

# pythonic way -> @
# Синтаксический сахар -красота кода

def decorator(func):
    def wrappper():
        print(f'МЫ вызвали функцию: {func.__name__}')
        func()
    return wrappper

@decorator  # @decorator -> decorator(hello)
def hello():
    print('Hello stranger')


@decorator
def john():
    print('My  name is John Snow I\'m the King of North!')

hello()
print()
john()

# -----------------

# def benchmark(func):
#     def wrapper(*args, **kvargs):
#         import time
#         start = time.time()
#         func(*args, **kvargs)
#         finish = time.time()
#         print(f'Время выполнения функции: {func.__name__}, заняло: {finish - start}')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_number = 100_000_000
#     while i < range_number:
#         i += 1

# @benchmark
# def add():
#     i = 0
#     range_number = 100_000_000
#     ls = []
#     while i < range_number:
#         ls.append(i)
#         i += 1

# loop()
# add()

# ___________________
# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = 'bold' + func(*args, **kwargs) + '</bold>'
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         res = 'div' + func(*args, **kwargs) + '</div>'
#         return res
#     return wrapper

# @bold
# @div
# def str_(name):
#     return name

# print(str_('John Snow'))


# _________________-

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвала {func.__name__}()\nона приняла args: {args}, kwargs: {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвала {func.__name__}()\nона вернула: {original_result}')
#         return original_result
#     return wrapper

# @trace
# def say(name, adress):
#     return f'{name} --> {adress}'

# @trace
# def hello(name, last_name, country):
#     return f'Hello {name} {last_name} from {country}!'

# say('Sherlock Holms', 'Backery St. 221B')
# print()
# hello('Homer', 'Simpson', 'CANADA')















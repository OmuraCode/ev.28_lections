"""
1) Создайте класс MyString, который будет наследоваться от str.
Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Пример:
example = MyString('String')
example.append('hello')
print(example) -> 'Stringhello'
print(example.pop()) -> 'o'
print(example) -> 'Stringhell'
"""

'''WRITE CODE HERE'''


# class MyString(str):
#     def __init__(self, str1):
#         self.str1 = str1

#     def append(self, str2):
#         self.str2 = str2
#         self.str1 = self.str1 + self.str2
#         return self.str1

#     def pop(self):
#         lastIndex = self.str1[-1]
#         self.str1 = self.str2[:-1]
#         return lastIndex

#     def __str__(self) -> str: 
#         return self.str1

# example = MyString('String')
# print(example.append('hello'))
# print(example.pop())


# class MyString(str): 
#     def __init__(self, stroka1): 
#         self.stroka1 = stroka1 
    
#     def append(self, stroka2): 
#         self.stroka2 = stroka2 
#         self.stroka1 = self.stroka1 + self.stroka2 
#         return self.stroka1 
        
#     def pop(self): 
#         last_w = self.stroka1[-1] 
#         self.stroka1 = self.stroka1[:-1] 
#         return last_w 
    
#     def __str__(self) -> str: 
#         return self.stroka1 
        
# example = MyString('String') 
# example.append('hello') 
# print(example.pop()) 
# print(example)

    

'''2)Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:
dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"
Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
init - инициализирует значение атрибута amount
update - задаёт объекту новое значение amount
repr - возвращает значение float
str - метод, который реализует логику функции dollarize()
//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
'''

def dollarize(num: float):
    if num
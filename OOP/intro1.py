# ООП = это объектно ориентированное прграммирование

# Класс - это описание того, как должен выглядеть объкет, то есть в классе мы
# описываем какими свойствами (данными) и поведениями(функциями) должен обладать объект

# Объект - это сущность, которую мы создаем от класса, у объекта есть собственное
# состояние свойств(данные)

# Целью создания ООП - было связать данные с функциями которые управляли этими данными

# Свойствами(атрибуты) - называют обычные переменные внутри класса, в которых 
# хранятся данные объекта

# Методы - это обычные функции внутри класса, методы описывают поведение в объекта

# _____________________________________________

# class Human:
#     age = 0
#     def __init__(self, first_name, last_name, job, citizenship) -> None:
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizen}'
    
# john = Human('John', 'Snow', 'King of North', 'Northerner', )
# billal = Human('Billal', 'Lanister', 'Programmer', 'KR')

# print(john, type(john))
# print(dir(john))

# print(john.show_info())
# john.age = 24
# print(john.show_info())
# john.job = 'Hanyga'
# print(john.show_info())
# print()
# print(billal.show_info())


# 2----------

# class Dog:
#     #атрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name: str, color: str) -> None:
#         "инициализатор, именно здесь создаются атрибуты объекта"
#         # self - ссылка на объект который только что создался
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')
    
#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, Color: {self.color}, Ushi: {self.ushi}')

# rex = Dog('Rex', 'Brown')
# pluto = Dog('Pluto', 'Red')
# aktosh = Dog('Aktosh', 'Grey')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.age = 2
# pluto.age = 5
# aktosh.age = 3
# aktosh.ushi = False

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.bark()
# pluto.bark()

# 3-------------------

# class Human:
#     def __init__(self) -> None:
#         print('init worked')
#         self.raychel = 'raychel'
#         self.golod = 100
    
#     def eat(self, meal, doela=True):
#         print(f'{self.raychel} покушала {meal}')
#         if doela:
#             self.golod -= 50
#         else:
#             self.golod -= 25

# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat('burger', doela=False)
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)


# 2 task
# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius) -> None:
#         self.radius = radius
#     def get_area(self):
#         area = self.pi * (self.radius**2)
#         return area


# circle = Circle(2)
# circle.color = 'Red'
# # circle = Circle(2)
# # print(circle.color)
# print(circle.color, circle.get_area())



# 3 tsk
# class BankAccount:
#     balance = 0
#     def withdraw(self, amount):
#         self.balance -= amount
#         print (f'Ваш баланс: {self.balance} сом') 

#     def deposit(self,amount):
#         self.balance += amount
#         print (f'Ваш баланс: {self.balance} сом') 

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500) 
        

# # 4 tsk
# class Taxi:
#     def __init__(self,name, cost, cost_km) -> None:
#         self.name = name
#         self.cost = cost
#         self.cost_km  = cost_km

#     def get_total_cost(self, km):
#         self.cost = self.cost_km * km + self.cost
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом' 
    

    
# taxi1 = Taxi(name = 'Namba', cost = 39, cost_km = 14)
# taxi2 = Taxi(name = 'Yandex', cost = 34, cost_km = 13)
# taxi3 = Taxi(name = 'Jorgo', cost = 35, cost_km = 11)

# print(taxi1.get_total_cost(9)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 


# 5 task
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()


# 6 task
# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
    
#     def count_percent(self):
#         self.summ = self.salary * self.experience / 100 * self.percent
#         print(self.summ)
    
# obj = Salary(10000, 10)
# obj.count_percent()



# 7 task
# import datetime
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self): 
#         current = datetime.datetime.now()
#         self.res = current.year - self.year
#         return f'выиграл {self.res} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())



# 8 task

# class Password:
#     def __init__(self, password):
#         self.password = password
    
#     def validate(self):
#         if not len(self.password) == 8 and len(self.password) < 15:
#             print('Password should be longer than 8, and less than 15')

#         if not any(map(lambda i: i.isdigit(), self.password)):
#             print('Password should contain numbers too')

#         if not any(map(lambda i: i.isalpha(), self.password)):
#             print('Password should contain letters as well')
        
#         symbols = [ '@', '#', '&', '$', '%', '!', '~', '*']
#         if not any(map(lambda i: i in symbols, self.password)):
#             print('Your password should have some symbols')
        
#         return 'Ваш пароль сохранен.'

#     def __str__(self) -> str:
#         return '*' * len(self.password)
    
# passw = Password('123qeq@')
# passw.validate()
# print(passw)


# # 9 task
class Math:
    def __init__(self, number):
        self.number = number
    
    def get_factorial(self):
        n = self.number
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial
        
    def get_sum(self):
        n = self.number
        suma = 0
        while n > 0:
            digit = n % 10
            suma = suma + digit
            n = n // 10
        return suma
    
    def get_mul_table(self):
        n = self.number
        for i in range (1, 10):
            res = n * i
            print (f'{n} * {i} = {res}')

obj = Math(5)
print(obj.get_factorial())
print(obj.get_sum())
obj.get_mul_table()



# n =5
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1

# print(factorial)

# n = 3
# d = 0
# for i in range (1, 10):
#    res = n * i
#    print(res)

# number = 4
# def get_mul_table(sd):
#     s = ''  
#     for i in range(10): 
#         s += f'{number}x{i+1}={number * (i+1)}' + '\n' # 
#         return s


# sd = 9
# print(get_mul_table(sd))


# 10 task/
# class ToDo:
#     instances = {}
#     def __init__(self, task):
#         self.task = task

#     def give_priority(self, priority):
#         self.priority = priority
        
#spizjeno
# class ToDo: 
#     def __init__(self,string): 
#         self.todo=string 
#         instances={}
#     def give_priority(self,priority): 
#         ToDo.instances[priority]=self.todo 
#     def list_of_tasks(self): 
#         return sorted(ToDo.instances.items()) 
# var1=ToDo('ckelele')
# var1.give_priority(2) 
# var2=ToDo('lelelele') 
# var2.give_priority(3) 
# var3=ToDo('HIOHOHO') 
# var3.give_priority(1)
# принципы ООП

# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиции
# 6. Агрегация


# --------------------
# Наследование 
# Позволяет принимать родительские методы и атрибуты дочернему классу

# Родительски класс
# дочерний класс
# -----------------

# class Animal:
#     def print_info(self):
#         print('I\'m an Animal')

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# lion  = Lion()
# lion.print_info()
# print(dir(Lion))


# ________________---
# !!!!!!!!!!!!
# class Animal:
#     def say(self):
#         print(f'This name is: {self.name}: {self.golos}')

#     def eat(self):
#         print(f'{self.name} eats {self.meal}')

# class Lion(Animal):
#     name = 'lion'
#     golos = 'ryg'
#     meal = 'meat'
#     griva = True

#     def info(self):
#         print(f'{self.name:{self.griva}}')
# class Dog:
#     name = 'Dog'
#     golos = 'bark'
#     meal = 'meat'

# class Koala:
#     name = 'koala'
#     golos ='roar'
#     meal = 'efcalipt'

# rex =Dog()
# simba = Lion()
# julian = Koala()


# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# simba.info()
# print()
# julian.say()
# julian.eat()


# class Person:
#     def info(self):
#         print('Im person from Bishkek')

# class Student(Person):
#     def info(self):
#         super().info() #!!!!! 
#         print('Im study at Manas University')

# obj = Student()
# obj.info()

# ------------------

class Laptop:
    def __init__(self, brand, model, price) -> None:
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):
        return {'brand': self.brand, 'model': self.model, 'price': self.price}
    

class Acer(Laptop):
    def __init__(self, model, price, year, videocard) -> None:
        super().__init__('acer', model, price)
        self.year = year
        self.videocard = videocard
    
#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['videocard'] = self.videocard
#         return repr
    
# class Apple(Laptop):
#     def __init__(self, model, price, display, year) -> None:
#         super().__init__('Macbook', model, price)
#         self.display = display
#         self.year = year

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['display'] = self.display
#         return repr
    

# mac = Apple('Pro', 1500, 14, 2020)
# print(mac.get_info())

# acer = Acer('swift', 600, 2019, 'Nvidia')
# print(acer.get_info())


# ------------------

# class Employee:
#     bonus = 1.5
#     def __init__(self, first_name, last_name, salary) -> None:
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'
    
#     def give_inncrease(self):
#         self.salary *= self.bonus

#     def __str__(self) -> str:
#         return self.get_info()
    
# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language) -> None:
#         super().__init__(first_name, last_name, salary)
#         self.lang = language

#     def get_info(self):
#         info = super().get_info()
#         info += f', Prog Language: {self.lang}'
#         return info

# class Managers(Employee):
#     def __init__(self, first_name, last_name, salary, devs=[]) -> None:
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs

#     def add_devs(self, developer):
#         self.devs.append(developer)
    
#     def show_devs(self):
#         return [x.get_info() for x in self.devs]
     
# dev1 = Developer('John', 'Snow', 1500, 'Python')
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Page', 1000, 'JS')
# dev4 = Developer('Tirion', 'Lanister', 2000, 'C#')

# man1 = Managers('Jamie', 'Lanister', 4000, [dev2, dev1])
# man2 = Managers('Jason', 'Derulo', 4000)

# print(f'Manager {man1.get_info()} has {man1.show_devs()} delopers!')
# print(f'Manager {man2.get_info()} has {man2.show_devs()} delopers!')

# man1.add_devs(dev3)
# man2.add_devs(dev3)
# man2.add_devs(dev4)

# dev3.give_inncrease()
# dev4.give_inncrease()
# man2.give_inncrease()

# print('AFTER')
# print(f'Manager {man1.get_info()} has {man1.show_devs()} delopers!')
# print(f'Manager {man2.get_info()} has {man2.show_devs()} delopers!')


# task3 nasledovaniye
# class MyString(str):
#     def __init__(self, stroka) -> None:
#         self.stroka = stroka
#     def append(self, string):
#         self.string = string
#         self.stroka = self.stroka + self.string
#         return self.stroka
#     def pop(self):
#         stroka_last = self.stroka[-1]
#         self.stroka1 = self.stroka[:-1]
#         return stroka_last
#     def __str__(self) -> str:
#         return self.stroka1
    
# example = MyString('String')
# print(example.append('hello'))
# print(example.pop())
# print(example)


# 4 task
# class MyDict(dict): 
#     def get(self,key,default = 'Are you kidding?'): 
#         return dict.get(self,key,default) 
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))

# 5 task
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def dispaly(self):
#         return f'{self.name} {self.age}'

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self): 
#         info = super().display() 
#         info += f', faculty:{self.faculty}' 
#         return info 

# obj_student = Student('John', 33, 'grfindoor')
# obj_student.display() 
# obj_student.display_student() 



class Person: 
    def __init__(self,name, age): 
        self.name = name 
        self.age = age 
    
    def display(self): 
        return f'name:{self.name}, age:{self.age}' 
    
class Student(Person): 
    def __init__(self, name, age, faculty): 
        super().__init__(name, age) 
        self.faculty = faculty 
        
    def display_student(self): 
        info = super().display() 
        info += f', faculty:{self.faculty}' 
        return info 
        
obj_student = Student('Rick', 21, 'science') 
print(obj_student.display()) 
print(obj_student.display_student)
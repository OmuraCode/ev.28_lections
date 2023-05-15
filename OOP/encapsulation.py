# Инккапсуляция - это 
# 1 Языковая конструкция которая помогает связать даннын с методами для их обработки 
# и управления(связь между данными и медодами которые управляют ими)(класс-капсула)

# 2. Механизм сокрытия при посощи которого можно ограничить доступ одного компонента от другого


# Инкапсуляция как связь

# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'My number: {Phone.number}')
#         print(f'My number: {self.number}')

# my_phone = Phone()
# my_phone.print_number()


# Инкапсуляция как механизм сокрытия

# 3 уровня сокрытия данных в питоне
    # 1. Публтчные(public) - number, print_number
    # 2 Защищенный (_protected) - number
    # 3. Приватный(__private) - __number

# class Car:
#     _country = "Germany"

#     def __init__(self) -> None:
#         self.marka = 'Mercedec-Benz' #public
#         self._model = 'w140' #protected
#         self.__color = 'Black' #__private

# obj = Car()
# print(dir(obj))
# print(obj._Car__color)
# print(obj._model)
# print(obj.marka)

# ---------

# class Phone:
#     username = 'John'
#     _caller  = 'Jamie' 
#     __count_of_cals = 15

#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         question = input('Взять трубку(yes/no): ')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сбросили трубку')

#     def __increment_cals(self):
#         self.__count_of_cals += 1

#     def __turn_on(self):
#         self.__increment_cals()
#         print('Hello')
#         print(f'Count of cals with {self._caller}: {self.__count_of_cals}')

# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()
# john.call()

# -----------------------------

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old')

# obj = Person('John', 18)
# obj.display_info()
# obj.nationality = "KR"
# print(obj.nationality)
# obj.age = -18
# obj.name = 11111
# obj.display_info()



# -----------------
# getter and setter

# Они нужны чтобы избежать прямого обращения к сокрытым атрибутам, при этом можно добавить логику
# валидации(проверки) данных, которые будут установлены в атрибут
# ш дшлу ф йгшс агсл ш дшлу ьн вшсл ыгсл

# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age

#     def display_info(self):
#         print(f'My name is {self.__name} and I\'m {self.__age} years old')

#     # getter
#     def name(self):
#         return self.__name
    
#     # setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print ('Name must be str object')
#         else:
#             self.__name = name

#     # getter
#     def age(self):
#         return self.__age
    
#     # setter
#     def set_age(self, age):
#         if not isinstance(age, int) or not 0<= age < 150:
#             print ('Invalid value for age')
#         else:
#             self.__age = age

# obj = Person('John', 24)
# print(obj.name())
# obj.set_age(-24)
# obj.display_info()
# obj.set_name('Jamie')
# obj.display_info()

































# task 1

# class A:
#     def public(self):
#         return 'Public method'
    
#     def _protected(self):
#         return 'Protected method'
    
#     def __private(self):
#         return 'Private method'

# obj1 = A()
# obj1.public()
# obj1._protected()
# obj1.__private()






# task 3
class Clock:
    def current_time(self):
        from datetime import datetime
        return datetime.now().strftime('%H:%M:%S')

class Alarm:
    def on(self):
        return 'Будильник включен '

    def off(self):
        return 'Будильник выключен '

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        return self.on()

clock = AlarmClock()
print(clock.current_time())
print(clock.alarm_on())







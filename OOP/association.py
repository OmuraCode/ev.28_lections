# Ассоциация - принцип ООП, в котором два класса связаны друг с другом
# Связью обозначает то что внутри одного объекта будет существовать другой объект от другого кпасса
# агрегация - сдабая связь
# композиция - сильная связь

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100
    
# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # когда мы создаем внутри класса объект от другого класса - композиция

# a = Iphone('red')
# a.battery._power -=50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a
# # при удалении объекта Iphone, батарейка тоже удалятся


class Nokia:
    def __init__(self,battery: Battery, color: str) -> None:
        self.battery = battery
        self.color = color
        # когда объект создается из вне класса и передается внутрь - агрегация

battery = Battery()
nokia1 = Nokia(battery, 'Black')
print(nokia1.battery._power)
del nokia1

nokia2 = Nokia(battery, 'Gray')
# # при удалении объекта Nokia, батарейка остается

# ----------------------

# Композиция 
# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction
        
#     def __str__(self) -> str:
#         return f'{self.type}'
    
# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')

# obj = Room()
# print(obj.west_wall)

# -----------------
# агрегация !!!!!!
# class Stream:
#     def __init__(self) -> None:
#         return 'Stream object'
    
# class Logger:
#     def __init__(self, stream=None) -> None:
#         self.stream = stream
    
#     def print_the_logs(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream')

# stream1 = Stream()
# logger1 = Logger(stream1)
# logger2 = Logger(stream1)
# logger3 = Logger(stream=Stream())

# logger1.print_the_logs()
# logger2.print_the_logs()

# -----------------------------------
# композиция
class Engine:
    country = 'Germany'

    def __init__(self, power) -> None:
        self.power = power

    def __str__(self)->str:
        return f'Power: {self.power}'

class Audi:
    brand = 'Audi'
    country = 'Germany'

    def __init__(self, model, power) -> None:
        self.engine = Engine(power)
        self.model = model

    def __str__(self) -> str:
        return f'{self.brand} {self.model} -> Engine: {self.engine}-> engine country: {self.engine.country}'
    

car = Audi('A8', 400)
print(car)
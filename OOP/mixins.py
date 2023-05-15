# Mixins
# Миксины это классы которые используются для наслкдования и передачи дочкрним классам определенных 
# методов; но не используются для создания объектов

# для чего:
# 1. Вы хотите предоставить множество доп методов для классов
# 2. вы хотите использовать один конкретный мкдтод во множестве разных классов


# class EngineMixin:
#     def start_engine(self):
#         print('started engine')

# class RadioMixin:
#     def play_radio(self):
#         print('Music is playing')

# class Auto(EngineMixin, RadioMixin):
#     pass

# class Plane(EngineMixin):
#     pass

# class SmartPhone(RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass


# ---------------
# class FlyMixin:
#     def fly():
#         print('I can fly')

# class WalkMixin():
#     def walk(self):
#         print('I can walk')

# class SwimMixin:
#     def swim(self):
#         print('I can swim')

# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk():
#         print('I can talk')
    
# class Fish(SwimMixin):
#     name = 'fish'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'Flyinf fish'

# class Duck(SwimMixin, FlyMixin, WalkMixin):
#     name = 'duck'

# obj = Human()
# obj.walk()
# obj.swim()


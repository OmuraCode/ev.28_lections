class Cars:
    def __init__(self, brand, model, year, engine, color, body_type, km, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.capacity = engine
        self.color = color
        self.body_type = body_type
        self.km = km
        self.price = price

    def __str__(self):
        return f"Марка: {self.brand} \nМодель: {self.model} \nГод выпуска: ({self.year}) \nОбъем двигателя{self.capacity} л. \nЦвет: {self.color} \nТип кузова: {self.body_type} \nПробег:{self.km} км \nЦена: {self.price} руб."

class CarsData:
    def __init__(self):
        self.cars = []

    def create(self, car):
        self.cars.append(car)

    def listing(self):
        return self.cars

    def retrieve(self, id):
        for car in self.cars:
            if id == self.cars.index(car):
                return car
        return None

    def update(self, id, car):
        for i, c in enumerate(self.cars):
            if id == i:
                self.cars[i] = car
                return 'обновлено'
        return 'обновлено'

    def delete(self, id):
        for i, c in enumerate(self.cars):
            if id == i:
                self.cars.pop(i)
                return 'удалено'
        return f'удалено'

cars_data = CarsData()

car1 = Cars('Mercedes-Benz', "C63", 2012, 1.6, "белый", "седан", 75_000, 50_0000)
car2 = Cars("Toyota", "Corolla", 2010, 1.8, "серый", "седан", 150000, 600000)
car3 = Cars("BMW", "X5", 2020, 3.0, "черный", "внедорожник", 5000, 5000000)

cars_data.create(car1)
cars_data.create(car2)
cars_data.create(car3)

cars = cars_data.listing()
for car in cars:
    print(car)

car = cars_data.retrieve(1)
print(car)

car2_updated = Cars("Toyota", "Camry", 2015, 2.0, "синий", "седан", 100000, 800000)
result = cars_data.update(1, car2_updated)
print(result)

result = cars_data.delete(2)
print(result)

cars = cars_data.listing()
for car in cars:
    print(car)


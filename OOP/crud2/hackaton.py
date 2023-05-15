class CreateMixin:
    def __init__(self) -> None:
        self.cars = []

    def create(self, car):
        self.cars.append(car)
        self.cars

class ListingMixin:
    def __init__(self) -> None:
        self.cars = []

    def listing(self):
        return self.cars
    
class RetrieveMixin:
    def __init__(self) -> None:
        self.cars = []

    def retrieve(self, id):
        for car in self.cars:
            if id == self.cars.index(car):
                return car
        return None

class UpdateMixin:
    def __init__(self) -> None:
        self.cars = []

    def update(self, id, car):
        for i, c in enumerate(self.cars):
            if id == i:
                self.cars[i] = car
                return True
        return False
    
class DeleteMixin:
    def __init__(self) -> None:
        self.cars = []

    def delete(self, id):
        for i, c in enumerate(self.cars):
            if id == i:
                self.cars.pop(i)
                return True
        return False

class Cars(CreateMixin, RetrieveMixin, ListingMixin, UpdateMixin, DeleteMixin):
    def __init__(self, brand, model, year, engine, color, type_car, km, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.type_car = type_car
        self.km = km
        self.price = price
        self.cars = []

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}), {self.engine} л., {self.color}, {self.type_car}, {self.km} км, {self.price} сом.")

    
# cars_data = Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin)

# создаем автомобили
car1 = Cars("Ford", "Focus", 2015, 1.6, "белый", "хэтчбек", 100000, 500000)
car2 = Cars("Toyota", "Corolla", 2010, 1.8, "серый", "седан", 150000, 600000)

# добавляем автомобили в базу данных
print(car1.create(car1))
print(car2.create(car2))


cars = car1.listing()



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
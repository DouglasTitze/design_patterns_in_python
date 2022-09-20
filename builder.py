"""Example of the builder design pattern, showing how to break down the process of building a car"""


class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """Abstract builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class ToyotaBuilder(Builder):
    """Concrete builder"""

    def add_model(self):
        self.car.model = "Toyota"

    def add_tires(self):
        self.car.tires = "Regular"

    def add_engine(self):
        self.car.engine = "Turbo"


class Car:
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f"{self.model} | {self.tires} | {self.engine}"


builder = ToyotaBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)

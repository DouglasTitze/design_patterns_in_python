import copy


class Prototype:
    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Camry"
        self.color = "Black"
        self.additions = "Bose speakers"

    def __str__(self):
        return f"{self.name} | {self.color} | {self.additions}"


car1 = Car()
prototype = Prototype()
prototype.register_object("Toyota", car1)
car2 = prototype.clone("Toyota")
car3 = prototype.clone("Toyota")
print(car1)
print(car2)
print(car3)

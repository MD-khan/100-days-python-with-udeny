class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

car = Car(make="Toyota")
print(car.model)
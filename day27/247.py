# args are many positional arguments
# kwargs are myny keyword arguments
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# key work arguments; kwargs is a dictionary
def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


# print(add(4, 5, 3, 4, 5, 4, 3, 4))
print(calculator(200, add=5, multiply=34))

my_car = Car(make="Nissan", model="32", colour="blue")
print(my_car.make)


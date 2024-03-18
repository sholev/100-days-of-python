# Unlimited Positional Arguments:
def add(*args):
    return sum(args)


print(add(3, 4, 5))
print(add(3, 4, 5, 7, 8, 9))


# Unlimited Keyword Arguments:
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(5, add=3, multiply=5))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


print(vars(Car(make="Nissan", model="GT-R")))
print(vars(Car(make="Nissan")))

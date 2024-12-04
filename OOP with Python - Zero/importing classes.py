from _1_intro_to_oop import car

bmw = car("bmw", 2002, "Egy", "Green", 100)
print(bmw)
print(car.cars_count)

class pants:
    cnt = 0

    @staticmethod
    def stat():
        return f"hi, static method in python is welcoming you"

    def __str__(self):
        return f"{self.data()}"

    def __init__(self, name, color, size, length, price):
        self.name = name
        self.color = color
        self.size = size
        self.length = length
        self.price = price

        pants.cnt += 1

    def data(self):
        return f"{self.price}, {self.color}, {self.length}"

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        self.change_price(self.price - ((discount / 100) * self.price))
        return f"new price after discount for item \"{self.name}\" is: {self.price} $"


a = pants("a", "g", "m", 120, 12)
b = pants("b", "r", "m", 140, 14)
c = pants("c", "y", "m", 160, 16)

print(pants.cnt)
print(a.discount(45))

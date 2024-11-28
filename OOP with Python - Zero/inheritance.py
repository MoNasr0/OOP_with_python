############################# INHERITANCE IN OOP #############################
# super class can give anything to subclass.
# subclass can take from super class and add more
# super class can't inherit from subclass

class eat:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def total_price(self):
        return self.amount * self.price


class pizza(eat):
    def __init__(self, name, amount, price, city):
        super().__init__(name, amount, price)
        self.city = city

    def info(self):
        return f"{self.name} pizza, {self.amount} pieces cost {eat.total_price(self)}" \
               f" and order to {self.city}"

    def __str__(self):
        return "this is subclass of eat class"


order_1 = pizza("margreta", 2, 150, "zagazig")

print(order_1, "\n")
print(order_1.info())


############################# polymorphism == many forms #############################
# it's a function which do more than one task:
# - + sign ==> 1 + 2 = 3 >> adding ; "A" + "B" = "AB" >> concatenation
# - len()  ==> len([1, 2, 3]); len("Nasr"); len(('a', 'b', 'c'))
# NotImplementedError ==> raise error, and it forces all subclasses to have this method

class start:
    cars = ["bmw", "merc", "kia", "skoda", "opel"]

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def how_old(self):
        return 2024 - self.year

    def define(self):
        if self.name in self.cars:
            return f"{self.name} is a car and it's made from {start.how_old(self)} years"
        else:
            return f"{self.name} is a human and he is {start.how_old(self)} years old"


# one function but used to do many things
instance = start("mo", 2001)
print(instance.define())

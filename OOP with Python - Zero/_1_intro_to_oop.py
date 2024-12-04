# oop is coding style
# oop is used to organize code and make it readable and reusable

############################# CLASS #############################
# class is construct of all objects
# class instantiate ==> creating new instance(object) of a class
# class **may** contains methods and attributes
############################# when creating new object #############################
# - python look for __init__() function "constructor function"
# - any function like __func__ is called Dander or magic function
# - __init__ must have "self" parameter which point to current instance
# - self para could be named anything

# instance attributes are in constructor function "__init__(self)"
# instance methods can access attributes and methods in same object
# instance method can access the class itself

############################# class method #############################
# - use @classmethod before method def
# - use "cls" to point to the class itself == "self" to point to object itself
# - it doesn't need a creation of objects to be called

############################# static method #############################
# - use @staticmethod before method def
# - take arg or not as you like
# - related to the class not the instance
# - not have to access class or instance … but related to class

############################# magic method "Dander" #############################
# - any method between underscores ==> __init__; __len__; __str__
# - __init__ => called auto when creating new instance "constructor"
# - __str__  => return human-readable output about the object
# - __class__=> to know which class the object belongs to
# - __len__  => return the length of the container, called when use "len"

class car:
    # attributes of class itself
    super_cars = ["Bugatti", "Ferrari", "GTR", "Lamborghini"]
    cars_count = 0

    @classmethod
    def production(cls):
        return f"total number of cars is {cls.cars_count}"

    @staticmethod
    def define():
        return "This is class about cars production lines"

    # magic method
    def __len__(self):  # have to be able to use "len" built in func
        return len(self.super_cars)

    def __str__(self):  # to show readable my-text for human user instead of <__main__.car object at 0x000001F3BDC7A390>
        return f"this is instance from car class and here is it's info: {self.car_data()}"

    def __init__(self, model, year, country, color, tank_size):
        # attributes of objects
        self.mod = model
        self.year = year
        self.country = country
        self.color = color
        self.tank_size = tank_size

        # to access class attributes
        car.cars_count += 1

    # adding objects methods
    def total_dis(self):
        return self.tank_size * 10

    def car_data(self):
        return f"{self.mod}, {self.country}, {self.year}, {self.color}"

    def is_super(self):
        if self.mod in car.super_cars:
            return "super car"
        else:
            return "Not super car"

    # method can access another method
    def info(self):
        return f"the car info: {self.car_data()}, " \
               f"total distance is {self.total_dis()}, " \
               f"{self.mod} is {self.is_super()}"


# creating instances
A5 = car("skoda", 2005, "germany", "green", 55)
K3 = car("kia", 2024, "korea", "yellow", 60)
X7 = car("BMW", 2023, "Germany", "black", 90)

# class attribute
print(car.cars_count)

# class method
print(car.production(), "\n")

# static method
print(car.define(), "\n")

# call __len__
print(len(X7), "\n")

# call __str__ and see readable data instead of its location
print(K3, "\n")

## to know a variable is object of which class
print(A5.__class__, "\n")

# to call instance method like "str.upper"
print(K3.info(), '\n')

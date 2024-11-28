############################# Property Decorator ######################
# to convert method to property/attribute
# by adding @property before the method

class car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @property
    def old(self):
        return 2024 - self.model

    # @property
    def welcome(self):
        return f"welcome to {self.name}!"


kia = car("kia", 2010)

print(kia.name)
print(kia.model)

# print(kia.old())  # as method
print(kia.old)  # as property/attribute
print(kia.welcome())  # as method

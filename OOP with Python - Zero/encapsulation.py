############################# ENCAPSULATION #############################
# to restrict access to data stored in attributes and methods
## in python there is no real protect or private
# >> you just know the naming roles of att/methods and how to name them.

## public:
# - can be shown and edited everywhere
class member_1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# can be used everywhere
m1 = member_1("mo", 23)
# print(m1.name)

# can be edited
m1.name = "ali"


# print(m1.name)


## protected:
# - attributes and methods can be used only in superclass or subclasses
# - known by adding _ before att/method name >> _name, _age, _define
# - remember >> python still can show and modify protected att/method in real code everywhere
class member_2:
    def __init__(self, name, age):
        self._name = name
        self._age = age


# in java, it can't be used here
m2 = member_2("amr", 23)
# print(m2._name)

# it can't be modified here
m1._name = "ahmed"


# print(m2._name)


## private
# - attributes and methods can be used only within the class, or it's object
# - att/methods can't be modified from out the class
# - known by adding __ before att/method name >> __name, __age, __define
class member_3:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


# can't be used here
m3 = member_3("walid", 23)
# print(m3.__name)  # error

# can't be modified here
m1._name = "osama"
# print(m3.__name)  # error

# not a professional way to access a private or protected att/method
"""
## but can show by: ##
print(m3._member_3__name, "first")

m3._member_3__name = "osama"
print(m3._member_3__name, "second")
"""


############################# Getter & Setter #############################
class member_4:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getters: used to get and show private/protected attributes
    def get(self):
        return self.__name

    # Setters: used to modify private/protected attributes
    def set(self, new_name):
        self.__name = new_name


m4 = member_4("sayed", 24)
print(m4.get())
m4.set("taher")
print(m4.get())

############################# method override: #############################
# - to create new method in subclass with same name of method in superclass
# .mro() ==> method resolution order >> show the order of execution functions

############################# multiple inheritance: #############################
# - to access class through another class
# - if 1 >> 2 >> 3 then 3 is inherit from 1 and 2

class age_1:
    def __init__(self, fname, yearOfBirth, lname):
        self.fname = fname
        self.lname = lname
        self.yearOfBirth = yearOfBirth

    def age(self):  # first func "age" in super class
        age = 2024 - self.yearOfBirth
        return age


class age_2(age_1):
    def __init__(self, fname, yearOfBirth, lname):
        super().__init__(fname, yearOfBirth, lname)

    # """ to see the difference
    def age(self):  # second func "age" in subclass will override the first
        age = 2019 - self.yearOfBirth
        return age
    # """


class last_ages(age_2):
    def __init__(self, name, yearOfBirth):
        super().__init__(name, yearOfBirth)


nasr = age_2("mo", 2001, "nasr")
print(nasr.age())
print(last_ages.mro())

########################## ABC ==> Abstract Base Class #########################
# class called Abstract class if it has one or many or not any abstract method
# abc module has infrastructure to define Abstract Base Class by using ABCMeta class
# define abstract method by adding @abstractmethod decorator before the method
## it's a general class that define a pattern to all subclasses
## and force all subclasses to have the method that is abstracted

# ABC == ABCMeta
from abc import ABC, abstractmethod


# class general(metaclass=ABCMeta) == class general(ABC)
class general(ABC):
    oop = ["py", "java", "js", "c++"]

    @abstractmethod
    def has_oop(self, lang):
        pass


class with_oop(general):
    def has_oop(self, lang):
        if lang in self.oop:
            return "yes"
        else:
            return "no"


py = with_oop()
print(py.has_oop("py"))

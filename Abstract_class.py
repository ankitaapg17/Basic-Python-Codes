# A class that cannot be instantiated is called an abstract class
# an incomplete class

# A method that can only be declared but not defined-Abstract method
#abc module- Abstract Base Class

from abc import ABC, abstractmethod
class laptop(ABC):    #laptop is an abstract class
    def show(self):   #normal method
        print("Welcome to Python")

    @abstractmethod     #decorator
    def screen(self):   #this is abstract method, so no body part defined
        return 0

class hp(laptop):
    def screen(self):   #we have to define the abstract method here,since the class inherited the abstract class
        print("32 inch") #this is the responsibility of the derived class
    def show1(self):
        print("Welcome to Hp laptop")

s1=hp()
s1.show()
s1.show1()
s1.screen()






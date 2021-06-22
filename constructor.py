
#__init__(self)Function is a built-in function in Python and it's
# the constructor of the class. Constructor is called whenever a new
# object of the class is created, and it should be called only
# during creating the object

## -(self) parameter in the __init__(self) function refers to the
## instance or the object itself, and it's important to use it if you
## want to use a constructor in your class.

class Person():
    def __init__(self,name,age,idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " + self.age
               + " your ID is "+ self.idNum)

john = Person('John','33','56456645')

john.output()

#Accessing variables or functions of a class object

print(john.name)
print(john.age)
print(john.idNum)
print(john.output())
#We use the dot to access a variable or a function

# To make multiple instances of a class

j = Person('Ani','5','6756757')
m = Person('Ankita','45','756756')

j.output()
m.output()






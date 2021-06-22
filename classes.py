# because python is object oriented programming language,
# so classes are very important thing to know and it's very effective in eriting codes

#classes can be used to represent real-world things exactly like a blueprint
#Classes can create objects that are called Instances

#First letter of the class name is always capital
###      To create an object of a class:
###            object = ClassName()

class Person():
    def insert(self,name,age,idNum): #self is important as it stores the passing
        # values of the function calling the variable.
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " + self.age
               + " your ID is "+ self.idNum)

    # creating a class instance or an object
j = Person()
j.insert('Ankita','20','56465')
j.output()

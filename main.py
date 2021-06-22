class stud:
    id=1001
    name="Raj"
    def display(self):
        print("Id=",self.id)
        print("Name=",self.name)

s1=stud()
s1.display()
#self is a keyword to access/represent the data members of the class(class variable) and the class methods

class stud:
    id=None
    name=None
    def display(self):
        self.id=1001
        self.name="Raj"
        print("Id=",self.id)
        print("Name=",self.name)

s1=stud()
s1.display()

#Parameterised function
class stud:
    def display(self,id,name):
        print("Id=",id)
        print("Name=",name)
s1=stud()
s1.display(1001,"Raj")


class stud:
    id=None
    name=None
    def display(self):
        self.id=int(input("Enter Id: "))
        self.name=input("Enter name: ")
        print("Id=",self.id)
        print("Name=",self.name)

s1=stud()
s1.display()

#two different class methods

class stud:
    id=None
    name=None
    def display(self):
        self.id=int(input("Enter Id: "))
        self.name=input("Enter name: ")
        print("Id=",self.id)
        print("Name=",self.name)

    def show(self):
        self.name=input("Enter name")
        print("Name=",self.name)

s1=stud()
s1.display()
s1.show()
s1.name="Neha"
print("Name=",s1.name)

# If we declare a variable in class- it is global
# But if we declare a variable in function- it is local

class stud:
    def display(self):
        id=int(input("Enter Id: "))
        name=input("Enter name: ")
        print("Id=",id)
        print("Name=",name)

    def show(self):
        print("Name=",self.name)

s1=stud()
s1.display()
s1.show() #gives error


#Declaring variables again and again takes up memory space
#so we use the concept of class and objects, to reduce usage of memory space











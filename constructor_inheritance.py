#Default constructor

class A:
    def __init__(self):
        print("A class constructor")

class B(A):
    def __init__(self):
        print("B class constructor")

s1=B() #only B class constructor is invoked in python

##################
class A:
    def __init__(self):
        print("A class constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B class constructor")
s1=B()
#To call a base class constructor method in derived class we use super keyword

##########
#Parameterised constructor
class A:
    def __init__(self,nm,id):
        print("Name=", nm)
        print("ID=", id)

class B(A):
    def __init__(self,nm1,id1,sal):
        super(B, self).__init__(nm1,id1) #we pass two arguments as base class has 2 args
        print("Salary", sal)

s1=B("Raj",1001,8999) #python uses bottom-up approach

#parameterised constructor overloading

class A:
    def __init__(self,l,b):
        print("Length=",l)
        print("Breadth=",b)

class B(A):
    def __init__(self,l,b):
        super(B, self).__init__(l,b)
        print("Area=",l*b)

s1=B(4,3)





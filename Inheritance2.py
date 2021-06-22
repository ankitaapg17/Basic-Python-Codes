#To increase the reusability of the code, and to decrease the memory usage


class A:
    def show(self):
        print("A class method")
class B(A):
    def show1(self):
        print("B class method")

s1=B()
s1.show()
s1.show1()

#A class is inherited in class B. So class B object can also use the method of A class
#This is single level inheritance

#protected is an access-specifier

class A:
    _nm=None
    _id=None
    def show(self):
        self._nm=input("Enter name: ")
        self._id=int(input("Enter id: "))


class B(A):
    def show1(self):
        print("Name=",self._nm)
        print("Id=",self._id)

s1=B()
s1.show()
s1.show1()

#protected method
class A:
    _nm=None
    _id=None
    def _show(self):
        self._nm=input("Enter name: ")
        self._id=int(input("Enter id: "))


class B(A):
    def show1(self):
        #self._show()
        print("Name=",self._nm)
        print("Id=",self._id)

s1=B()
s1._show() #calling protected data method outside class
s1.show1()

#Inherited class can use it, and also can be used as public
print("Name is: ",s1._nm)




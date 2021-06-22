#same name, same form
#different class

class A:
    def show(self):
        print("A class method")
class B(A):
    def show(self):
        print("B class method")

s1=B()
s1.show()
s1.show() #B is called in both cases


print("\n")

############


class A:
    def show(self):
        print("A class method")
class B(A):
    def show(self):
        super(B, self).show()
        print("B class method")

s1=B()
s1.show()


############


class A:
    def show(self):
        print("A class method")
class B(A):
    def show(self):
        print("B class method")


print("\n")
s1=B()
s1.show()
s2=A()
s2.show()







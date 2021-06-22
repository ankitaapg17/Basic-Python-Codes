class A:
    def show(self):
        print("A class method")

class B:
    def show1(self):
        print("B class method")

class C(A,B):
    def show2(self):
        print("C class method")

s1=C()
s1.show()
s1.show1()
s1.show2()
print("\n")

###############
#multiple inheritance and constructors

class A:
    def __init__(self):
        super().__init__()
        print("A class method")

class B:
    def __init__(self):
        print("B class method")

class C(A,B):
    def __init__(self):
        super().__init__()

        print("C class method")
s2=C()


#Diamond inheritance/hybrid inheritance
#ambiguity in C++
#virtual functions

#     a
# b        c
#     d





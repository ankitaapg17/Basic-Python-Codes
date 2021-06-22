class A:
    def __del__(self):
        print("Destructor")
    def show(self):
        print("Show method")
    def __init__(self):
        print("constructor")


s1=A()
s1.show()
s2=A()
s2.show()
#Note the sequence in which constructor and destructor are called



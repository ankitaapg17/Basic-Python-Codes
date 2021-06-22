class A:
    def __init__(self):
        print("A constructor")
    def show(self):
        print("A method")
    def __del__(self):
        print("A destructor")
class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")
    def show(self):
        super().show()
        print("B method")
    def __del__(self):
        super().__del__()
        print("B destructor")

s1=B()
s1.show()

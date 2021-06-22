#Method overloading / polymorphism
#same name different form

class emp:
    def show(self,a=None):
        if a is not None:
            print("Welcome",a)
        else:
            print("Hello")

s1=emp()
s1.show()
s1.show("RAJ")
#prints according to the method arguments

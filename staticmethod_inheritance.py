class A:
    @staticmethod
    def add(a,b):
        return a+b

class B(A):
    def sum(a ,b):
        return a+b

print("Sum of 2 number",B.add(5 , 7))

#we can call a class function even without an object
#but if we write self, then we have to call class method using object
print("Sum of 2 number", B.sum(4 , 9))

#staticmethod can be inherited as well
#dependency is on class not on object

#################
class A:
    a=None
    def __init__(self,m): #we make m global
        self.a=m
    def deposit(self):
        d=int(input("Enter deposit amount: "))
        amp=d+self.a
        print("Total amount after deposit: ", amp)
class B(A):
    def __init__(self, l):
        super().__init__(l)
    def withdraw(self):
        w=int(input("Enter withdraw amount: "))
        w2=self.a-w
        print("Total amount after withdraw: ",w2)
s1=B(5000)
s1.deposit()
s1.withdraw()



class emp:
    def __fun(self):
        print("Private method")
    def fun1(self):
        print("Public Method")

s1=emp()
s1.fun1()
#If we have to call a private method outside a class, then how are we going to do that?

class emp:
    def __fun(self):
        print("Private method")
    def fun1(self):
        self.__fun()
        print("Public Method")

s1=emp()
s1.fun1()





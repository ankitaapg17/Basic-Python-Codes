class calc:
    def add(x,y):
        return x+y

    @staticmethod
    def sub(x,y):
        return x-y

calc.add=staticmethod(calc.add)
print("Sum of 2 numbers",calc.add(5,4))

#using decorator method
print("Subtraction of 2 numbers",calc.sub(8,4))

#we can call the static methods directly without creating object for the class
#It bounds to the class rather than the class's object.






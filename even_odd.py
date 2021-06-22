class A:

    @staticmethod
    def even(x):
        if x%2==0:
            return "even"
        else:
            print("Odd")


a=int(input("Enter a number: "))
print("Number is:", A.even(a))
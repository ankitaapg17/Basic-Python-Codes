#A school has following rules for grading system
marks=int(input("Enter your marks:"))

if marks>80:
    print("A")
elif marks>=60 and marks<=80:
    print("B")
elif marks>=50 and marks<60:
    print("C")
elif marks>=45 and marks<50:
    print("D")
elif marks>=25 and marks<45:
    print("E")
else:
    print("F")





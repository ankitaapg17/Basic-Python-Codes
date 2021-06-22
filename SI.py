p = int(input("Enter the principal amount"))
t = int(input("Enter the number of years:"))

if (t >= 12):


    SI = (p*10*t)/100
    print("Enter the simple interest", SI)

else:

    SI2 = (p*15*t) / 100
    print("Enter the simple interest", SI2)
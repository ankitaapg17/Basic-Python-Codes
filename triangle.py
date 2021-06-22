a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("enter third side"))
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
area=pow(d,(1/2))
print("The area of the triangle with sides "+str(a)+", "+str(b)+" and "+str(c)+" is "+str(area))
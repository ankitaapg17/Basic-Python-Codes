# Difference between error handling and exception handling
#Error occurs during compilation
#Exception occurs during runtime

#Diff bw X-mode and w-mode, in file handling using python
#Trying to access a file which does not exist- exception

#why not use if-else to handle?
#Error can happen because of programmer, exception takes place when the user inputs wrong data


try:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=a/b
    print("Divide: ", c)
except ZeroDivisionError: #we can mention the type of error we encounter
    print("Error")
except ValueError:
    print("Invalid value")
    #can have multiple except blocks

###########################


try:
    f=open("abc.txt","r")
    c=f.read()
    print(c)
except IOError:
    print("File not found")

##########################



try:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=a/b
    print("Divide: ", c)
except(ZeroDivisionError,ValueError):
    print("Please provide a valid value")
else:
    print("Done")



#############################



try:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=a/b
    print("Divide: ", c)
except(ZeroDivisionError,ValueError):
    print("Please provide a valid value")
finally:
    print("Done") #this block executes irrespective of exception generated or not

################

try:
    l=[2,3,4,5,6]
    for i in l:
        print(l[i])
    print(l[10])
except IndexError:
    print("Out of Index")
######################

#custom-defined exceptions/ user-defined exceptions
#Then we use raise keyword

x=50
if not type(x) is str:
    raise TypeError("Only string value used")

#################
# voting concept
try:
    a = int(input("Enter age:"))
    if a < 18:
        raise ValueError
    else:
        print("Eligible")

except ValueError:
    print("Error")
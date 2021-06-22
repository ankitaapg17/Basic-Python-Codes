string = input("Enter your string: ")

string=string.casefold()

rev_str=reversed(string)

if list(string)==list(rev_str):
    print("The string is pallindrome")
else:
    print("Not a pallindrome")

#Decimal to binary,octal and hexadecimal
def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
    print(n%2,end=' ')

dec=int(input())

print(convertToBinary(dec))
print("Octal",oct(dec))
print("Hex",hex(dec))






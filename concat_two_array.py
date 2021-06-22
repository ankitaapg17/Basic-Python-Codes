import array as arr
n=arr.array('d',[1,2,3,4])
print(n)
p=arr.array('d',[5,6,7,8])
print(p)
print("After concatenation:")
n.extend(p)
print(n)

#Taking input in an array

k=arr.array('i', [])
i=int(input("Enter number of element"))
x=0
y=0
print("Enter n Number")
while(x<i):
    k.append(int(input()))
    x=x+1
print("Display Five Number")
while(y<len(k)):
    print(k[y])
    y=y+1


print("Display sum of the elements entered:")
s = 0
for c in k:
    s=s+c
print("The sum:", s)

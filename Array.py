#collection of similar data-type, can hold fixed number of items

#difference between array and list in python
#Array stores data of same type, list can store data of different types
import array as arr

n=arr.array('d',[5,7,4]) #'d'-number values
print(n)

print(n[1])
print(n[-1])

l=[4,5,6,7]
n=arr.array('d',l)
print(n)
print(n[1:3])
#slicing

#Changing value
n[3]=44
print(n)

#Changing more than one values
n[0:2]=arr.array('d',[55,66])
print(n)

#Append and extend
#Append- adding single value at last index location
#Extend- to store multiple values

n.append(98)
print(n)
n.extend([3,4,5,6])
print(n)



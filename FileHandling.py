
#file object=open('filename','mode')

f=open('abc.txt','w+')
a="This is a python program\nHello World\nCpp program"
f.write(a)
print("Written successfully") #Buffer in/op-since this message is temporary and not stored anywhere



##################
f=open('abc1.txt','w+')
for i in range(10):
    f.write('\n')
    #f.write(str(i))
    f.write("%d"%i)
print("Written successfully")
print("Name of file",f.name)
print("Closed of file",f.closed)
print("Mode of file",f.mode)
#################



f=open('abc.txt','r+')
c=f.read()
print(c)

#to open file with looping
with open('abc.txt','r+')as f:
    c=f.read()
    print(c)

#converting file to list
f=open('abc.txt','r+')
l=[]
l=f.readline() #prints the first line of the text file
print(l)

c=f.read()
l=c.splitlines()
print(l)

#To open in append mode

f=open('abc.txt','a+')
a="\nfile handling program in append mode"
f.write(a)
f.close()

#xmode
f=open('abc3.txt','x')
a="This is a new python file"
f.write(a)
if f:
    print('file created')








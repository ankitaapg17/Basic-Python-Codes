#OS module
#OS commands

import os
#os.rename('abc3.txt','xyz.txt')
print("File renamed")
#os.remove('abc2.txt')

#os.mkdir('test')
print('Folder created')
print(os.getcwd())
#os.rmdir('test')

f=open('xyz.txt','r')
print("file pointer",f.tell())
c=f.read()
print("file pointer",f.tell())


import csv
with open('example.csv','r')as f:
    r=csv.reader(f,delimiter='\t')
    for row in r:
        print(row)

import csv
with open('example.csv','r')as f:
    r=csv.DictReader(f,delimiter='\t')
    for row in r:
        print(dict(row))

#json file
#javascipt object notation
#xml does the job of passing data from html to server
#and the format in which that passing is done is- json
#xml is used for server side programming

import json
p='{"name":"raj","marks":[90,70]}'
r=json.loads(p)
print(r["marks"])
print(r["name"])

#example of json file
""""
{
"emp":[
{"name":"raj",
"salary":6000
},
{"name":"gaurav",
"salary":9000
}]"""

#how to work with data in json file using file handling

import json
with open('p.json')as f:
    d=json.load(f)
    print(d["emp"][0]["salary"])

f=open('p.json',)
d=json.load(f)
for i in d["emp"]:
    print(i)





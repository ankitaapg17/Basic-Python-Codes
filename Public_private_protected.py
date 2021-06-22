#private data members
class stud:
    id=1001 #public data member
    __name="Raj" #private data member
    #_address="kolkata" protected data member
    def display(self):
        print("Id=",self.id)
        print("Name=",self.__name)

s1=stud()
s1.display()
#print("Name=",s1.name) #gives error
#private data member cannot be called outside the class

#multiple objects of one class
class college:
    def empdet(self):
        nm=input("Enter employee name")
        salary=int(input("Enter employee salary"))
        print("Employee Name=",nm)
        print("Employee Salary=",salary)
    def studdet(self):
        stdnm=input("Enter student name")
        stdmk=int(input("Enter student marks"))
        print("Student name=",stdnm)
        print("Student Marks=",stdmk)

print("Techno India")
technoindia=college()
technoindia.empdet()

print("NSEC")
nsec=college()
nsec.empdet()
nsec.studdet() #call methods in class, with objects

class IPL:
    def team(self):
        tn=input("Enter team name")
        pnm=input("Player name")
        hs=int(input("Enter highest score"))
        print("Team Name:",tn)
        print("Player Name:",pnm)
        print("Highest score:",hs)

team1=IPL()
team1.team()

team2=IPL()
team2.team()

team3=IPL()
team3.team()


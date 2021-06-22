#to generate exception of your type
#custom exception
class salnotinRange(Exception):
    salary=None
    def __init__(self,salary):
        self.salary = salary

salary=int(input("Enter salary"))

if not 5000 < salary < 15000:
    raise salnotinRange(salary)
else:
    print("Thanks")







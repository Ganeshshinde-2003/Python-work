# class Employee:
#     salary = 0
#     def __init__(self,name,desi,no,wage,hrs):
#         self.name = name
#         self.desi = desi
#         self.no = no
#         self.wage = wage
#         self.hrs = hrs
#         self.salary = self.salary

#     def display(self):
#         return f"Name : {self.name}\nDesignation : {self.desi}\nNumber : {self.no}\n"

#     def calculatesalary(self):
#         self.salary = self.wage*self.hrs
#         return f'Salary : {self.salary}'


# emp1 = Employee("Ganesh","strudent","5252585236",250,10)
# emp2 = Employee("mahesh","teacher","5252585236",1050,10)
# emp3 = Employee("suresh","actor","5252585236",2505,12)
# emp4 = Employee("nani","player","5252585236",320,5)
# emp5 = Employee("robert","raider","5252585236",22,2)
# emp6 = Employee("chris","traveler","5252585236",20,100)

# ls = [emp1,emp2,emp3,emp4,emp5,emp6]
# d1 = {}

# for i in ls:
#     print("\n")
#     print(f"{i.display()}{i.calculatesalary()}")
#     print("\n")
#     d1[i.no] = [i.name,i.desi,i.wage,i.hrs,i.salary] 


class Employee:
    def __init__(self,n,id,d,date):
        self.name = n
        self.id = id
        self.department = d
        self.date = date

class Salary(Employee):
    c = 0
    def __init__(self,n,id,d,date,s):
        Employee.__init__(self,n,id,d,date)
        self.salary = s

    def display(self):
        Salary.c = Salary.c + 1
        return f"\nThe details of the Employee {self.c}\nName : {self.name}\nID : {self.id}\nDepartment : {self.department}\nDate Of Joining : {self.date}\nSalary : {self.salary}"

n = int(input("Enter the number of employee's data you wanna store => "))
d1 = {}
li = []

for i in range(n):
    print(f"Enter the data of employess {i+1}")
    name = (input("Enter Name => ")).upper()
    id = (input("Enter ID => ")).upper()
    d = (input("Enter Department => ")).upper()
    date = input("Enter the data of joining => ")
    salary = int(input("Enter the Salary => "))
    e = Salary(name,id,d,date,salary)
    d1[name] = [id,d,date,salary]
    li.append(e)

for i in li:
    print(i.display())

print("\n",d1,"\n")
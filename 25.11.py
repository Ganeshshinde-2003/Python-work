# class Rectangle:
#     def __init__(self,length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def __str__(self):
#         area = self.length*self.breadth
#         peri = 2*(self.length+self.breadth)
#         return f"AREA and PERIMETER : {area} {peri}"
# area1 = Rectangle(10,20)
# print(f"The area and perimeter of the given rectangle \n{area1} ")

# class Rectangle:
#     def area(self,length,breadth):
#         self.len = length
#         self.bre = breadth
#     def display(self):
#         return (self.len*self.bre),(2*(self.len+self.bre))


# area1 = Rectangle()
# area1.area(10,20)
# print(f"\nThe area and perimeter of the given rectangle : {area1.display()} \n")

# class Python:
#     def lang (self,version,name):
#         self.version = version
#         self.name = name
#     def display(self):
#         return f"{self.version} {self.name}"

# class Java:
#     def lang (self,version,name):
#         self.version = version
#         self.name = name
#     def display(self):
#         return f"{self.version} {self.name}"

# python = Python()
# python.lang(3.10,"PYTHON")
# print(f"{python.display()}")

# java = Java()
# java.lang(3.15,"JAVA")
# print(f"{java.display()}")

# class Python:
#     def __init__(self,version,name):
#         self.version = version
#         self.name = name
#     def __str__(self):
#         return f"Version : {self.version} \nName : {self.name}"

# class Java:
#     def __init__(self,version,name):
#         self.version = version
#         self.name = name
#     def __str__(self):
#         return f"Version : {self.version} \nName : {self.name}"

# python = Python(3.10,"PYTHON")
# print(python)
# java = Java(3.15,"JAVA")
# print(java)

class Employee:
    salary = 0
    def __init__(self,name,desi,no,wage,hrs):
        self.name = name
        self.desi = desi
        self.no = no
        self.wage = wage
        self.hrs = hrs
        self.salary = self.salary

    def display(self):
        return f"Name = {self.name}\nDesignation = {self.desi}\nNumber = {self.no}\n"

    def calculatesalary(self):
        self.salary = self.wage*self.hrs
        return f'Salary = {self.salary}'


emp = Employee("Ganesh","Company","5252585236",250,10)
print(emp.display(),emp.calculatesalary())



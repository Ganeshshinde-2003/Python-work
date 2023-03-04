# class eg:
#     __classv = 0
#     __instav = 0
#     def update(self):
#         eg.__classv += 1
#         self.__instav += 6

#     def show(self):
#         print(f"class variable = {eg.__classv}\ninstant variable = {self.__instav}")

# s1 = eg()
# s1.update()
# s1.show()

# class person:
#     def __init__ (self,n,a):
#         self.name = n 
#         self.age = a 

#     def show1(self):
#         print(f"name = {self.name} and age = {self.age}")

# class student(person):
#     def __init__(self,n,a,id):
#         super().__init__(n,a)
#         self.id = id
#     def show(self):
#         print(f"id = {self.id}")

# s1 = student("gani",19,2333)
# student.show()

print("\n---------------------------------------------")
n = int(input("Enter 1 to calculate 0 to stop => "))
while(n):
    formula = input("Enter the valid expression : ").split(" ")
    print(formula)
    a = float(formula[0])
    b = float(formula[2])
    c = formula[1]
    if c == '+':
        print(f"{a} + {b} = {a+b}")
    elif c == '-':
        print(f"{a} - {b} = {a-b}")
    elif c == '*':
        print(f"{a} * {b} = {a*b}")
    elif c == '/':
        print(f"{a} / {b} = {a/b}")
    n = int(input("Enter 1 to calculate 0 to stop => "))
print("---------------------------------------------\n")

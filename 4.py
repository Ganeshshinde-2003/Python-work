# print("\n---------------------------------------------")
# n = int(input("Enter 1 to calculate 0 to stop => "))
# try:
#     while(n):
#         formula = input("Enter the valid expression : ").split(" ")
#         # print(formula)
#         a = float(formula[0])
#         b = float(formula[2])
#         c = formula[1]
#         if c == '+':
#             print(f"{a} + {b} = {a+b}")
#         elif c == '-':
#             print(f"{a} - {b} = {a-b}")
#         elif c == '*':
#             print(f"{a} * {b} = {a*b}")
#         elif c == '/':
#             print(f"{a} / {b} = {a/b}")
#         n = int(input("Enter 1 to calculate 0 to stop => "))
# except (ValueError,ZeroDivisionError,TypeError) as err:
#     print(err)

# finally:
#     print("---------------------------------------------\n")


while(1):
    n = int(input("Enter => "))
    if(n == 1):
        formula = (input("Enter => ")).split(" ")
        try:
            if(len(formula) != 3):
                raise ValueError("Enter the correct expression")
            else:
                print("The expression is correct")
        except ValueError as err:
            print(err)
        try:
            a = float(formula[0])
            b = float(formula[2])
            c = formula[1]
        except (ValueError,IndexError) as err:
            print(err)
        try:
            if c != "+" and c != "-":
                raise ValueError("Enter the correct operator")
            else:
                if c == "+":
                    result = a+b
                elif c == "-":
                    result = a-b
                print(f"{a} {c} {b} = {result}")
        except (ValueError,NameError) as err:
            print(err)
    elif(n == 0):
        break
class FormulaError(Exception):
    def __str__(self):
        return (f"The input is not sufficient. check you entered the formula correctly or not. OR check the operator you entered is \"+\" or \"-\" ")
while True: 
    formula = input("Enter the formula provideing in between space => ").split()
    try:
        if(len(formula) != 3):
            raise FormulaError()
        else:
            try:
                a = float(formula[0])
                b = float(formula[2])
                c = formula[1]
            except ValueError as err:
                print(err)
    except FormulaError as err:
        print(err)
    try:
            if(c != "+" and c != "-" and c != "*" and c != "/"):
                raise FormulaError()
            else:
                if c == "+":
                    print(f"{a} {c} {b} = {a+b}")
                if c == "-":
                    print(f"{a} {c} {b} = {a-b}")
                if c == "*":
                    print(f"{a} {c} {b} = {a*b}")
                if c == "/":
                    print(f"{a} {c} {b} = {a/b}")
    except (FormulaError,NameError) as err:
            print(f"The operator {err}")
y = 10
for i in range(1,7):
    print(i,end="")
    if(i!=6):
        print(" "*y,end="")
        print(i)
    y = y - 2
    if (i>0):
        print(" "*i,end="")
print("\n")
z = 1
for i in range(5,0,-1):
    print(" "*(i-1),end="")
    print(i,end="")
    print(" "*z,end="")
    print(i)
    z = z + 2

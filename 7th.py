# listofstu = []
# dic = {}

# n = int(input("Enter the number of data you wanna store => "))

# for stu in range(n):
#     usn = input(f"Enter the USN of the student {stu + 1} = ")
#     name = input(f"Enter the NAME of the student {stu + 1} => ")
#     dob = input(f"Enter the DOB of the student {stu + 1} => ")
#     email = input(f"Enter the EMAIL of the student {stu + 1} => ")
#     dic[name] = [usn,dob,email]
#     listofstu.append(dic)

# print(listofstu)
# f1 = open("Studentdata.txt","w")

# for data in listofstu:
#     for key,value in data.items():
#         f1.write("%s : %s \n"%(key,value))

# f1.close()
li = []

f1 = open("Studentdata.txt","r+")

while True:
    str1 = f1.readline()
    print(str1)
    if str1 == "": break
    li.append(str1)


count = 0
" ".join(li)
for line in li:
    for word in line:
        count += 1

print(li)
print(count)
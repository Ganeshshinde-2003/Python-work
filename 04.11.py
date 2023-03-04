# dict = {}

# for i in range(1):
#     name = input("Enter the key : ")
#     value = (input("Enter the value : ")).split(",")
#     dict[name] = value
# print(dict)

# for usn in dict:
#     lst = dict[usn]
#     avg = sum(lst)/len(lst)
#     print(f"{usn} has these marks {lst} with average of {avg}")

# dict = {
#     "India": ['delhi', 121],
#     "US": ['Washington', 100],
#     "AUS": ['Sydney', 80]
# }
# maximum = 0
# for item in dict.items():
#     key, value = item
#     if value[1] > maximum:
#         maximum = value[1]
#         print(f"The {key} has {maximum}B income")

dict = {}
li = []

entry = int(input("Enter the number of data you wanna store : "))

for i in range(0, entry):
    name = input("Enter the name of the country : ")
    values = (input("Enter the capital and income : ").split(","))
    dict[name] = values

print(dict)
maxi = dict[name][1]
for i in dict.items():
    key, value = i
    income = int(value[1])
    li.append(income)
    if income > int(maxi):
        maxi = value[1]
        country = key
print(f"The country {country} has highest income of {maxi}B")
print(li)
j = max(li)
li.remove(j)
print(li)
k = max(li)
print(k)
print(type(k))
for i in dict.items():
    w,v = i;
    print(v)
    if int(v[1]) == k:
        print(f"The country {w} has the second highest income of {maxi}B")
str2 = "hello world"
l = len(str2)
mid = int(l//2)
first_half = str2[:mid:]
print(first_half)
print("t" in str2)

str = (input("Enter the string : "))
count = 0
for i in str:
    if i == "o":
        count = count + 1
print(f"the no of occurence of letter O is {count}")


def count(str, ch):
    count = 0
    for i in str:
        if i == ch:
            count = count + 1
    return count


str = "This is a good day"
ch = "d"
print(f"The no of d in string is {count(str, ch)}")
ch = "i"
print(f"The no of i in string is {count(str, ch)}")

str = "hello world"
l = len(str)
len = l-5
new_str = ""
j = 0
for i in str:
    if j == 3:
        break
    else:
        j = j+1
        new_str = new_str+i
count = 0
for i in str:
    count = count + 1
    if count > len:
        new_str = new_str + i
print(new_str)

str = "hello world"
length = len(str)
mid = int(length//2)
new_str = ""
new_str = new_str + str[0]
new_str = new_str + str[mid]
new_str = new_str + str[length-1]
print(new_str)


str = "DSUCSE"
str2 = "21"
l = len(str)
length = int((l//2))
new_str = ""
new_str = new_str + str[:length]
new_str = new_str + str2 + str[length:]
print(new_str)

str = input("Enter the the string : ")
str2 = ""

for i in str:
    if i.islower():
        str2 = str2 + i
for i in str:
    if i.isupper():
        str2 = str2 + i
print(str2)

str = input("Enter the string : ")

digit = 0
alpha = 0
symble = 0

for i in str:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        alpha = alpha + 1
    else:
        symble = symble + 1
print(
    f"The number of digits are {digit}\nThe number characters are {alpha}\nand the no of symbole are {symble}")

str = input("Enter the string with numbers : ")
sum = 0
count = 0
for i in str:
    if i.isdigit():
        count = count + 1
        sum = sum + int(i)
avg = sum/count
print(avg)


def balance(str1, str2):
    count = 0
    for i in str2:
        if (i in str1):
            count = count + 1
        else:
            count = count - 1
    l = len(str1)
    if l == count:
        return True
    else:
        return False


str1 = "Hel01l2o47"
str2 = "elloh01247235"
print(balance(str1, str2))

str1 = "hello"
print("".join(reversed(str1)))

str = '''Today is a good day
it is my favourite day'''
str1 = str.lower()
str2 = "today"
print(str1.count(str2))

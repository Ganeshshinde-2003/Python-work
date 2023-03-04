# string = input("Enter a string : ")
# new_string = ""

# length = len(string)
# mid = int(length/2)
# for i in range(0, length):
#     if i == 0 or i == mid or i == length-1:
#         new_string += string[i]

# print(new_string)

# string1 = input("Enter a string : ")
# string2 = input("Enter another string to add : ")

# length = len(string1)
# mid = int(length/2)

# new_string = string1[0:mid] + string2 + string1[mid:length]

# print(new_string)

# string = input("Enter a string with lower and upper cases : ")

# new_string = ""

# for i in string:
#     if i.islower():
#         new_string += i
# for i in string:
#     if i.isupper():
#         new_string += i
# print(new_string)

# string1 = input("Enter a string : ")
# string2 = input("Enter another string : ")

# length = len(string1)
# count = 0
# for i in string1:
#     if i in string2:
#         count = count + 1

# if length == count:
#     print("Both strings are same ")
# else:
#     print("Both strings are not the same")

# sentence = (input("Enter a long string with spaces : ")).split(" ")

# dict = {}

# for word in sentence:
#     count = sentence.count(word)
#     if word in dict:
#         pass
#     else:
#         dict[word] = count

# print(dict)

# string = input("Enter a string : ")

# sum = 0
# count = 0

# for i in string:
#     if i.isnumeric() and i != '0':
#         sum += int(i)
#         count += 1

# avg = sum/count

# print(
#     f"The sum of digits present in the string given is {sum} amd the average fo the numbers is {avg}")

string = input("Enter a string : ")
le = len(string)

for i in range(le-1, -1, -1):
    print(string[i], end="")
print("\n")
new_string = string[le::-1]
print(new_string)

reversed(string)
srt = string
print(srt)

# string = (input("Enter a string : ")).split(" ")

# str = ""

# for word in string:
#     str += word[0]

# str2 = str.upper()

# print(str2)

# string = input("Enter a string : ")

# dict = {}

# for i in string:
#     count = string.count(i)
#     if i in dict:
#         pass
#     else:
#         dict[i] = count

# print(dict)

# born = (input("Enter the date of birth : ")).split("/")

# date = born[0]
# month = born[1]
# year = born[2]

# print(f"The date = {date}\nThe month = {month}\nThe year = {year}")

# string = input("Enter a string : ")
# new_string = ""

# for i in string:
#     if i != " ":
#         new_string += i

# print(new_string)

# string = input("Enter a string : ")
# new_string = ""

# for i in string:
#     if i.isalnum():
#         new_string += i

# print(new_string)

# sentence = (input("Enter a string : ")).split(" ")
# ls = []

# for word in sentence:
#     if word.isalpha():
#         pass
#     elif word.isdigit():
#         pass
#     else:
#         ls.append(word)

# print(ls)

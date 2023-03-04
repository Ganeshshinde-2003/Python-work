# name = "Ganesh"
# print("my name is ", name)
# print("my name is "+name)
# print(f"my name is {name}")
# print('{} is my name'.format(name))

# print('{0} and {1} comes after {2}'. format("NLP", "AI", "ML"))

# name = "Ganesh"
# age = 19
# height = 190

# print(
#     f"Hello everyone \nMy name is {name} and i am {age} years old.\ni am {height} cm tall")

# age = int(input("Enter your age : "))
# if age <= 12:
#     print("child")
# else:
#     print("adult")

# age = int(input("Enter your age to confirm : "))

# if age >= 18:
#     print("you are eligible to vote ")
# else:
#     print("You are not eligible to vote ")

# age = float(input("Enter your age to confirm : "))
# if age > 2 and age < 13:
#     print("you are a child")
# elif age < 2:
#     print("toddler")
# elif age >= 13 and age <= 19:
#     print("you are a teenager")
# elif age > 19 and age < 60:
#     print("you are a adult")
# elif age >= 60:
#     print("you ate a senior citizen")


# num1 = int(input("Enter a number to check if it is factor or not : "))
# num2 = int(input("Enter a number : "))
# if num2 % num1 == 0:
#     print(f"The number {num1} is a factor of {num2}")
# else:
#     print(f"The number {num1} is not a factor of {num2}")


# color = (input("Enter the color of the light : ")).lower()

# if color == 'yellow':
#     print("Car has to wait")
# elif color == 'green':
#     print("Car is allowed to go")
# elif color == 'red':
#     print("Car has to stop")
# else:
#     print("unrecognized signal ")

# print(int('0b011', 2))
# print(bin(34))
# for i in range(5, 0, -2):
#     print(i)
# sum = 0
# for i in range(1, 20, 2):
#     print(i)
#     sum = sum + i
# print(sum)

# for i in range(6):
#     for j in range(i):
#         print("*", end=" ")
#     print("\n")

# list = []
# for i in range(1, 11):
#     list.append(int(input("Enter number : ")))
# print(list)
# larg = 0
# for i in list:
#     if i > larg:
#         larg = i
# print(f'largest number is {larg}')

n = int(input("Enter the row : "))
mid = int(n/2)
for i in range(1, mid+1):
    for j in range(i):
        print("*", end=" ")
    print("\n")
for k in range(mid+1, 0, -1):
    for n in range(k):
        print("*", end=" ")
    print("\n")

# n = int(input("Enter the number of rows : "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print("\n")

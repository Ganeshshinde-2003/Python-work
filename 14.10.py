# num = int(input("Enter a number : "))

# for i in range(1, 11):
#     print(f"{num} * {i}  =  {num*i}")

# num = input("Enter a number : ")
# count = 0
# for i in num:
#     count = count + 1
# print(f"The number of digits in {num} = {count}")

# num = int(input("Enter the number : "))

# i = num
# fact = 1
# if num > 0:
#     while i > 0:
#         fact = fact*i
#         i = i-1

#     print(f"The factorial of the number {num} is {fact}")

# elif num == 0:
#     print(f"The factorial of the number {num} is 1")

# else:
#     print("Enter a positive number bozz")

# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num*fact(num-1)


# num = int(input("Enter a number : "))

# result = fact(num)

# print(f"The factorial of the number {num} is {result}")

# set = (input("Enter the numbers : ")).split(" ")
# print(set)
# largest = max(set)
# smallest = min(set)

# print(f"The largest number is {largest} and smallest is {smallest}")

# num = []
# while True:
#     number = input("Enter\n")
#     if number == "done":
#         break
#     elif number.isnumeric:
#         num.append(int(number))
# print(num)
# sum = 0
# count = 0
# for i in num:
#     sum = sum + i
#     count = count + 1
# avg = sum/count

# print(
#     f"The sum is {sum}\nThe average is {avg}\nThe number of elements are {count}")

def min(list):
    maximum = max(list)
    return maximum


list = ((input("Enter numbers : "))).split(" ")
min(list)

print(min(list))

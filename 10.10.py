import random

no1 = int(input("Enter range : "))
no2 = int(input("Enter range : "))
money = 0
number = random.randint(no1, no2)
# print(number)

while True:
    your_number = int(input("Enter the number : "))
    if number == your_number:
        print("You entered the correct one\nYou are genius")
        print(f"You owe me {money} $")
        break
    else:
        print("You dont have luck buddy try again !!!")
        money = money + 5


# i = 1
# while i < 21:
#     if (i % 5 != 0):
#         print(i)
#     i = i+1
# n = int(input("Enter the number of students data you wanna store : "))
# names = []
# atts = []
# cias = []
# print("\n\n!--------STORE THE DATA--------!\n")
# for i in range(0, n):
#     names.append(input(f"\nEnter your name of {i+1} student : "))
#     atts.append(int(input(f"\nYour attendence of {i+1} student : ")))
#     cias.append(int(input(f"\nEnter your cia of {i+1} student : ")))
# print(f"\nNAME\t\tATTENDENCE\tCIA")
# for i in range(0, n):
#     print(f"\n{names[i]}\t\t{atts[i]}\t\t{cias[i]}")
# for i in range(0, n):
#     if atts[i] >= 75 and cias[i] >= 40:
#         print(f"\n{names[i]} is eligible for SEE")
#     else:
#         print(f"\n{names[i]} is not eligible for SEE")
# print('\n')

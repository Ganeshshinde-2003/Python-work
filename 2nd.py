# Write a progam to find whether a number is a factor fo 255
# Here i am just checking what are the factors of 255


for i in range(1, 256):
    if 255 % i == 0:
        print(i, end=" ")
print("\n")


num1 = int(input("Enter a number : "))
if 255 % num1 == 0:
    print(f"The number {num1} is a factor of 255")
else:
    print(f"The number {num1} is not a factor of 255")

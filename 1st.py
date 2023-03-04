num = int(input("Enter a number : "))
revers = 0
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    revers = revers*10+digit
    num = num//10

print(f"The revers order is {revers}")
print(f"The sum of the revers order {sum}")

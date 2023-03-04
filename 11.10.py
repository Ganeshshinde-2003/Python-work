# def my_func():
#     print("Hello world")


# my_func()

# b = max("hello worldz")
# print(b)
# print(type(b))

radius = float(input("Enter the radius of the circle : "))


def area(radius):
    area = 3.142*radius**2
    return area


print(f"area of the circle = {area(radius)}")

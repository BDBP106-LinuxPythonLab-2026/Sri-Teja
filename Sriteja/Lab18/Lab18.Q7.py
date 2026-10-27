"""Program with a function to find whether a given triangle with sides a, b, c is
isosceles, scalene or equilateral triangle"""


def triangle(a, b, c):
    if a == b == c:
        print("It is an equilateral triangle")
    elif a == b or a == c or b == c:
        print("It is an isosceles triangle")
    else:
        print("It is a scalene triangle")


triangle(40, 40, 40)
triangle(20, 50, 20)
triangle(20, 70, 30)
"""Program to find the roots of a quadratic equation and Figure out what the inputs
should be and also have provision to deal with cases where you end up getting complex"""

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

x = b*b - 4*a*c

if x >= 0:
    r1 = (-b + math.sqrt(x)) / (2*a)
    r2 = (-b - math.sqrt(x)) / (2*a)
    print("Roots =", r1, r2)
else:
    print("Complex roots")
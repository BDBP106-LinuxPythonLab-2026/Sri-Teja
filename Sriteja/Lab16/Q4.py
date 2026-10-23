"""Python script to take an input angle in degrees and print the values of all the 6
trigonometric functions for that angle and a code to convert the
input into radians before finding the trigonometric values"""

import math

angle = float(input("Enter angle in degrees: "))
radian = math.radians(angle)

print("sin =", math.sin(radian))
print("cos =", math.cos(radian))
print("tan =", math.tan(radian))
print("cosec =", 1 / math.sin(radian))
print("sec =", 1 / math.cos(radian))
print("cot =", 1 / math.tan(radian))



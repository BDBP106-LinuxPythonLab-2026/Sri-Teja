"""Program to convert a tuple of angles into a list of tuples with each tuple containing
the sine and cosine of an angle"""

import math

angles=[30,45,90,75]
result=list(map(lambda a: (math.sin(math.radians(a)),math.cos(math.radians(a))),angles))
print(result)



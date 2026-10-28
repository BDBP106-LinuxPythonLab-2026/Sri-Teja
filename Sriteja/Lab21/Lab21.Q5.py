"""Program to find the sum of all the elements in a list using lambda and reduce
functions"""

from functools import reduce

nums=[1,2,3,4,5]
result=reduce(lambda a,b: a+b,nums)
print(result)
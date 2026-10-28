"""Program to concatenate a list of strings to make a sentence using reduce function"""

from functools import reduce
w=["India","won","T20","WorldCup","thrice"]
S=reduce(lambda x,y:x+" "+y,w)
print(S)
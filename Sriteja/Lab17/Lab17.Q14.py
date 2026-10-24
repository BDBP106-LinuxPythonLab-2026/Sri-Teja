"""Program to remove all occurrences of an element from a list, L"""

w=[3,24,53,2,2,24,76,1,3,3,24,53,76,3]
element=int(input("Enter an element: "))
while element in w:
        w.remove(element)
print(w)
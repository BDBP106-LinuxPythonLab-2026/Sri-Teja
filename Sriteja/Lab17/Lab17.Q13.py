"""Program to extract elements of a list, if it occurs more than k times"""
w=[3,24,53,2,2,24,76,1,3,3,24,53,76,3]
k=3
extract=[]
for i in w:
    if w.count(i) > k:
        extract.append(i)
print(extract)
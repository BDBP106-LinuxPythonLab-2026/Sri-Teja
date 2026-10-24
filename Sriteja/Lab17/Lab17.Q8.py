"""Script to count the number of occurrences of a word,W, in a sentence,S"""

s=input("Enter string:")
w=input("Enter a word:")
words=s.split()
count=words.count(w)
print("Occurences:",count)
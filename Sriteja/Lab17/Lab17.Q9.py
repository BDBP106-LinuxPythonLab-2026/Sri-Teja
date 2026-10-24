"""Script to check if two strings are anagrams of each other"""

string1=input("Enter first string:").lower()
string2=input("Enter second string:").lower()

if sorted(string1)==sorted(string2):
    print("It is an anagram")
else:
    print("Not an anagram")


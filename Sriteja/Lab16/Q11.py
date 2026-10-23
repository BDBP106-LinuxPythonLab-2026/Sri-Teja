"""Program to check if an input letter is a vowel or consonant"""

text=input("Enter an alphabet:")
if text in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

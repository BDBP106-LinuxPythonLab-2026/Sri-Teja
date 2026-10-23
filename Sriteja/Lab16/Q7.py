"""Script to check whether a number is palindrome or not"""

text=(input("Enter a number: "))
reverse=text[::-1]
if text==reverse:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

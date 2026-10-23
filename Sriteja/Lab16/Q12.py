"""Program to check whether an input string is palindrom  or not"""

text=input("Enter a string: ")
reverse=text[::-1]
if reverse==text:
    print("The string is palindrome")
else:print("The string is not palindrome")
"""Program to extract words from a string list,L whose first character is k"""

L = ["kite", "apple", "king", "banana", "key", "cat"]
result = [word for word in L if word.startswith('k')]
print(result)

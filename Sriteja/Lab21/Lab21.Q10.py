"""Program to extract all vowels of a string"""

text='Board of Control for Cricket in India'
print([char for char in text if char.lower() in "aeiou"])

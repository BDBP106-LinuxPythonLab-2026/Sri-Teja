"""Program to remove all duplicate words from a given sentence using a dictionary"""

a = input("Enter a sentence: ")
words = a.split()
unique_words = dict.fromkeys(words)
result = " ".join(unique_words)
print("Sentence after removing duplicates:", result)

"""Function called nextPrime that finds and returns the first prime number larger
than some integer,n.The value of n will be passed to the function as its only parameter"""
"""Program that reads the integer from the user and display the first prime
number larger than the entered value"""

n = int(input("Enter a number: "))
def nextPrime(n):
    n = n + 1

    while True:
     for i in range(2, n):
         if n % i == 0:
             break
     else:
            return n

print(f"First prime number larger than {n} is", nextPrime(n))


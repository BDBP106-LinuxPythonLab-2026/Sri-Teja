"""Code to get the Fibonacci numbers beginning with f0 = 0 and f1 = 1 up to f25"""
a = 0
b = 1

for i in range(26):
    print(a, end=" ")
    a, b = b, a + b
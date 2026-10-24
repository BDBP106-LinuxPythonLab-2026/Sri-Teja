"""Program to check whether a given number is prime or not."""

N=int(input("Enter a number: "))
if N<2:
    print("Not a prime number")
else:
      prime=True
for i in range(2,N):
      if N%i==0:
            prime=False
if prime is True:
      print("Prime number")
else:
      print("Not a prime number")






"""Program to find the even numbers in a list,L"""

L=list(map(int,input("Enter numbers:").split()))
for num in L:
    if num % 2==0:
        print(num)
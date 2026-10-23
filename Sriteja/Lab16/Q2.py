"""Program to find the simple interest and the amount with simple interest included"""
"""Inputs should be the principal, rate of interest in percentage per annum and the time in years"""

"""Simple Interest (si) = (Principal × Rate × Time) / 100
   Amount = Principal + Simple Interest"""

p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

si = (p * r * t) / 100
amount = p + si

print("Simple Interest =", si)
print("Total Amount =", amount)
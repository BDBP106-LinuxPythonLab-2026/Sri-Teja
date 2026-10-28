"""converting temperature in celsius to fahrenheit using lambda function"""

celsius = [0, 32, 45, 64]
temp=lambda c:(c*9/5)+32
print([temp(c)for c in celsius])

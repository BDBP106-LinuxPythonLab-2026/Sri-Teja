"""Program with a function to calculate the area of a triangle using the formula,
where a, b, c are sides of the triangle, also providing a test case output from the program
Area=(s(s − a)(s − b)(s − c))**1/2 where 2s = a + b + c"""

def area(a,b,c):
    s=(a+b+c)/2
    area = ((s*(s-a)*(s-b)*(s-c))**(1/2))
    a=float(area)
    print("The area of the triangle is",a)

a=4
b=5
c=6
area(a,b,c)
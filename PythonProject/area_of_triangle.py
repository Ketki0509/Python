import math

a = float(input("Enter first length"))
b = float(input("Enter second length"))
c = float(input("Enter third length"))
s = (a+b+c) / 2
result = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of Triangle is :",round(result,2))
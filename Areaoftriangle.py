# Python Program to find the area of triangle
# Take inputs from the user
a = float(input('Enter first side:'))
b = float(input('Enter second side'))
c = float(input('Enter third side:'))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The are of the triangle is %0.3f' %area)
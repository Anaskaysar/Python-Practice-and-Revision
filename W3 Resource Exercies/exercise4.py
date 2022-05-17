'''
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
from math import pi
radius = float(input("Input The Radius Of a Circle : "))
print("The area of the circle with radius " + str(radius) + " is : " + str(pi*radius**2))
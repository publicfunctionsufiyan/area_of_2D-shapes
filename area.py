from ctypes.wintypes import DOUBLE
from email.mime import base
from cupshelpers import Printer
from numpy import double, number



print(""" 

*** Area Calculator ***

Choose Your Shape by Entering a number 1-4

1. Circle
2. Square
3. Rectangle
4. Triangle


""")

shape_number = int(input())

if shape_number == 1:
    print("""You Choose A Circle 
    Please Enter Radius To Calculate The Area""")
    
    radius = double(input())
    circle_area = radius**2*3.14
    print("Area = ",circle_area)

elif shape_number == 2:
    print("""You Choose A Square 
    Please Enter A Side To Calculate The Area""")

    side = double(input())
    square_area = side**2
    print("Area = ",square_area)


elif shape_number == 3:
    print("""You Choose A Rectangle 
    Please Enter Length And Width To Calculate The Area""")

    rectLength = double(input())
    rectWidth = double(input())
    rectangle_area = rectLength*rectWidth
    print("Area = ",rectangle_area)

elif shape_number == 4:
    print("""You Choose A Triangle 
    Please First Enter Perpendicular Then Base And Then Hypotenuse To Calculate The Area And Also To Find If This Is Right Triangle Or Not""")
    
    trianglePerpendicular = double(input())
    triangleBase = double(input())
    triangleHypotenuse = double(input())
    triangle_area = triangleBase*trianglePerpendicular/2
    print("Area = ",triangle_area)
    hypotenuse_square = triangleHypotenuse**2
    perpendicular_sqare = trianglePerpendicular**2
    base_square = triangleBase**2
    x = base_square + perpendicular_sqare
    if hypotenuse_square == x:
        print("Its A Right Triangle")
    else:
        print("Its Not A Right Triangle")

else:
    print("Unknown Shape!")

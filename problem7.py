#! /usr/bin/python

from math import *

feet = raw_input("What is the length of the room in feet? ")
width = raw_input("What is the width of the room in feet? ")
print("You entered dimensions of " + feet + " feet by " + width + " feet. ")

area = int(feet) * int(width)
print("The area is ")
print(str(area) + " square feet")

areaM = area * 0.09290304
print(str(round(areaM,3)) + " square meters")



#m2 = f2 x 0.09290304



# importing math mmodule
from math import pi
class Circle:
             #funtion within the circle class to get area
       def get_area(self):
           self.radius = 1
           return pi * (self.radius * 2)
# obejct
my_circle = Circle()
# has radius of three 
print(my_circle.get_area())
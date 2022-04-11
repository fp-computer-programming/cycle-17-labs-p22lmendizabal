# importing math mmodule
from math import pi
class Circle:
             #funtion within the circle class to get area
       def get_area(self):
           self.radius = self
           return pi * (self.radius * 2)
       def get_perimeter(self):
           return 2 * pi * self.radius
# obejct
my_circle = Circle()
# has radius of three 
print(my_circle.get_area())
print(my_circle.get_perimeter())

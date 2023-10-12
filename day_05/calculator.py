import sys
import os

current_file_path = os.path.realpath(__file__)
current_dir = os.path.dirname(current_file_path)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from constant import Messages, Maths
from shapes import Shape, Circle, Rectangle, Triangle

# -----------------------------------------------------------------
# Circle.
# -----------------------------------------------------------------
radius = 3
shape = Circle(radius)  # Creating an instance of the Circle class
perimeter = shape.perimeter();
area = shape.area();
print('Circle Details:')
print('Radius = ', radius)
print('Perimeter = ', perimeter)
print('Area = ', area)
print(Messages.SEPERATOR)

# -----------------------------------------------------------------
# Rectangle.
# -----------------------------------------------------------------
length = 3
width = 2
shape = Rectangle(length, width)  # Creating an instance of the Rectangle class
perimeter = shape.perimeter();
area = shape.area();
print('Rectangle Details:')
print('Length = ', length)
print('Width = ', width)
print('Perimeter = ', perimeter)
print('Area = ', area)
print(Messages.SEPERATOR)

# -----------------------------------------------------------------
# Triangle.
# -----------------------------------------------------------------
side_1 = 2
side_2 = 3
side_3 = 4
shape = Triangle(side_1, side_2, side_3)  # Creating an instance of the Triangle class
perimeter = shape.perimeter();
area = shape.area();
print('Triangle Details:')
print('Side 1 = ', side_1)
print('Side 2 = ', side_2)
print('Side 3 = ', side_3)
print('Perimeter = ', perimeter)
print('Area = ', area)
print(Messages.SEPERATOR)
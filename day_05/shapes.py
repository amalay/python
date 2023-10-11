from constant import Maths

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Maths.PI * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * Maths.PI * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
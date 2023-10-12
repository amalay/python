from constant import Maths

# -----------------------------------------------------------------
# Define Shape class as a base class.
# -----------------------------------------------------------------
class Shape:
    def __init__(self):
        pass

    def perimeter(self):
        pass

    def area(self):
        pass

# -----------------------------------------------------------------
# Define Circle class as a derived class.
# -----------------------------------------------------------------
class Circle (Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def perimeter(self):
        return 2 * Maths.PI * self.radius

    def area(self):
        return Maths.PI * (self.radius ** 2)

# -----------------------------------------------------------------
# Define Rectangle class as a derived class.
# -----------------------------------------------------------------
class Rectangle (Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
   
# -----------------------------------------------------------------
# Define Triangle class as a derived class.
# -----------------------------------------------------------------
class Triangle (Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def __init__(self, side_1, side_2, side_3):
        super().__init__()
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    
    def perimeter(self):
        return (self.side_1 + self.side_2 + self.side_3)
    
    # -----------------------------------------------------------------
    # Formula: Area = (Base * Height)/2
    # -----------------------------------------------------------------
    def area(self):
        return (self.base * self.height) / 2
    
    # -----------------------------------------------------------------
    # Formula: Area = √(s(s - side_1)*(s - side_2)*(s - side_3)) Where s = (side_1 + side_2 + side_3)/2
    # -----------------------------------------------------------------
    def area_02(self):
        s =  self.perimeter(self) / 2
        area = (s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3)) ** 0.5

        return area
import math

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area
import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")
class Triangle(Shape):
    def __init__(self,height, base):
        self.height = height
        self.base = base
    def area(self):
        return (self.height * self.base)/2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi *(self.radius**2)
shape = [Triangle(2,1), Rectangle(2,4), Circle(3)]
for s in shape:
    print(f"Area: {s.area()}")
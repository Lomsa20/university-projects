import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius **2
    def perimeter(self):
        return 2 * math.pi * self.radius
    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            raise TypeError("Can only multiply by int or float")
        return Circle(self.radius * k) #k is just any number for example 1,2,3,4,5 and so on

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __mul__(self, k):
        if isinstance(k, (int, float)):
            raise TypeError("Can only multiply by int or float")
        return Rectangle(self.width * k, self.height * k)
class Triangle(Shape):
    def __init__(self,height,base,side1,side2):
        self.height = height
        self.base = base
        self.side1 = side1
        self.side2 = side2
    def area(self):
        return (self.base * self.height) / 2
    def perimeter(self):
        return self.base + self.side1 + self.side2
    def __mul__(self, k):
        if isinstance(k, (int, float)):
            raise TypeError("Can only multiply by int or float")
        return Triangle(self.height * k, self.base * k, self.side1 * k, self.side2 * k)

class Canvas:
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        self.shapes.append(shape)
    def total_area(self):
        return sum(shape.area() for shape in self.shapes)
    def __str__(self):
        return f"Total_area: {self.total_area()}"
canvas = Canvas()
canvas.add_shape(Circle(5))
canvas.add_shape(Rectangle(2, 3))
canvas.add_shape(Triangle(4, 5, 3, 6))

print(canvas)
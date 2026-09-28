import math
class Vector:
    def  __init__(self, x, y):
        self._x = x
        self._y = y
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cannot add vectors to vector type")
        return Vector(self._x + other._x, self._y + other._y)
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cannot subtract vectors to vector type")
        return Vector(self._x - other._x, self._y - other._y)
    def distance(self,other):
        return math.sqrt((self._x - other._x)**2 + (self._y - other._y)**2)
    def __str__(self):
        return "({0}, {1})".format(self._x, self._y)
class ColoredVector(Vector):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self._color = color
    def __str__(self):
        return f"{self._color} ({self._x}, {self._y})"

class Shape:
    def __init__(self):
        self._vectors = []
    def add_vector(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("Cannot add vectors to vector type")
        self._vectors.append(vector)
    def perimeter(self):
        if len(self._vectors) < 2:
            return 0
        total = 0
        for i in range(len(self._vectors)):
            current = self._vectors[i]
            next_point = self._vectors[(i + 1) % len(self._vectors)]
            total += current.distance(next_point)
        return total
    def __str__(self):
        points= ', '.join(str(v) for v in self._vectors)
        return "({0})".format(points)
v1 = Vector(0, 0)
v2 = ColoredVector(3, 0, "red")
v3 = ColoredVector(3, 4, "blue")

print(v1 + v2)
print(v3 - v1)

shape = Shape()
shape.add_vector(v1)
shape.add_vector(v2)
shape.add_vector(v3)

print(shape)
print("Perimeter:", shape.perimeter())

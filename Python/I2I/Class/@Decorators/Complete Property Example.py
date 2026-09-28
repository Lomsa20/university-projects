class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property 
    def radius(self):
        """Get radius"""
        return self._radius 
    @radius.setter
    def radius(self, value):
        """Set radius with validation"""
        if value <= 0:
            raise ValueError
        self._radius = value
    @property 
    def area(self):
        """Calculated property(no setter)"""
        return 3.14159 * self._radius**2 
circle = Circle(5)
print(circle.radius)
print(circle.area)

circle.radius = 10
print(circle.area)


















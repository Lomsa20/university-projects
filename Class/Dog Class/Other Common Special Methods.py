class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self): #string repres....
        return f"{self.a} and {self.b}"
    
    def __add__(self, other): # addition
        return Point(self.a+ other.a, other.b + self.b)
    def __eq__(self, other): #Equality
        return self.a == other.a and self.b == other.b
    def __len__(self): #length
        return int((self.a**2 + self.b**2)**0.5) 
p1 = Point(1,2)
p2 = Point(4,5)
p3 = p1 + p2 #calls __add__
print(p3)























class Vector:
    def __init__(self,components):
        self.components = components #now we create place where we can store list of numbers
    def __add__(self,other): # Addition  of vectors
        return Vector([a + b for a,b in zip(self.components,other.components)])
    def __sub__(self,other): #subtraction of vectors
        return  Vector([a-b for a,b in zip(self.components,other.components)])
    def __dot__(self,other): # Dot is same as scalar product(multiplication)
        return sum(a * b for a,b in zip(self.components,other.components))
    def __str__(self):
        return f"{self.components}"
class NamedVector(Vector):
    def __init__(self, name, components):
        super().__init__(components)
        self._name = name
    def __str__(self):
        return f"{self._name}: {super().__str__()}"
v1 = NamedVector("A",[1,2])
v2 = NamedVector("B",[2,3])
print(v1+v2)
print(v1-v2)
print("Dot Product", v1.__dot__(v2))



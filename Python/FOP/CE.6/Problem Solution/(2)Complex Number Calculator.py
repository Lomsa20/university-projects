class ComplexNumber:
    def __init__(self,r,i): #r stand for real number i for imaginary number
        self.r = r
        self.i = i
    def __add__(self,other):
        return self.r + other.r,self.i + other.i
    def __sub__(self,other):
        return self.r - other.r,self.i - other.i
    def __mul__(self,other):
        r = self.r * other.r - self.i * other.i
        i = self.r * other.i + self.i * other.r
        return ComplexNumber(r,i)
    def __str__(self):
        return f"({self.r},{self.i})"
class LabeledComplex(ComplexNumber):
    def __init__(self,r,i, label):
        super().__init__(r,i)
        self.label = label
    def __str__(self):
        return f"{self.label}: {super().__str__()}"
c1 = LabeledComplex(1,1,"C1")
c2 = LabeledComplex(2*(1+3),2,"C2")
print(c1+c2)
print(c1-c2)
print(c1*c2)
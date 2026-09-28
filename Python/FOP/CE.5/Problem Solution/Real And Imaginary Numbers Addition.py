class ComplexNumber: 
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag
        
    def __add__(self, other):
        return ComplexNumber(self._real + other._real, self._imag + other._imag)
    
    def __sub__(self, other):
        return ComplexNumber(self._real - other._real, self._imag - other._imag)
    
    def __mul__(self, other):
        r = self._real * other._real - self._imag * other._imag
        i = self._real * other._imag + self._imag * other._real
        return ComplexNumber(r, i)
    
    def __str__(self):
        return f"{self._real} + {self._imag}i"
    

class LabeledComplex(ComplexNumber):
    def __init__(self, label, real, imag):
        super().__init__(real, imag)
        self._label = label
    
    def __add__(self, other):
        label = f"({self._label}+{other._label})"
        return LabeledComplex(label, self._real + other._real, self._imag + other._imag)
    
    def __sub__(self, other):
        label = f"({self._label}-{other._label})"
        return LabeledComplex(label, self._real - other._real, self._imag - other._imag)
    
    def __mul__(self, other):
        label = f"({self._label}*{other._label})"
        r = self._real * other._real - self._imag * other._imag
        i = self._real * other._imag + self._imag * other._real
        return LabeledComplex(label, r, i)
    
    def __str__(self):
        return f"{self._label}: {super().__str__()}"


c1 = LabeledComplex("X", 3, 12)
c2 = LabeledComplex("Y", 1, 213)
                    
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)






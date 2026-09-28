class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def wag_tail(self):
        return f"{self.name}"
dog= Dog("delpiero")
print(dog.speak())#Inherited
print(dog.wag_tail())# New method










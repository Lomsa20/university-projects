class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name},{self.age}')"
    def __repr__(self):
        return f"Person(name= '{self.name}', age = '{self.age}')"
person = Person("Anania", 16)     
print(str(person),end= ' &&&&')
print(repr(person), end = " %%%")
print(person, end = " *****")
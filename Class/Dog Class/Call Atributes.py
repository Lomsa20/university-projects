class Dog:
    species = "Dzerskoia Familiaris"
    def __init__(self, name, age):
           self.name = name
           self.age = age
dog1 = Dog("Turiko", 6)
dog2 = Dog("Jekuna", 7)
print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)
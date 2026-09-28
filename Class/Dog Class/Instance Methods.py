class Dog:
    def __init__(self, name, age):
           self.name = name
           self.age = age
    def bark(self):
        return f"{self.name} AHHH Woooof Wooof"
    
    def get_age_in_dog_years(self):
        return self.age * 7
dog1 = Dog("Turiko", 6)
dog2 = Dog("Jekuna", 7)

print(dog1.name, dog1.bark())
print(dog2.name, dog2.get_age_in_dog_years())
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __ini__(self,name,breed):
        super().__init__(name) #Call parent
        self.breed = breed
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound}"
dog = Dog("Rex", "Labrador")
print(dog.name)    # "Rex"
print(dog.breed)   # "Labrador"
print(dog.speak()) # "Some sound -> Woof!"
   

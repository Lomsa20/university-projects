class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Override
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meaaawwww!!"
dog = Dog()
cat = Cat()
print(dog.speak())  # "Woof!"
print(cat.speak())  # "Meow!"

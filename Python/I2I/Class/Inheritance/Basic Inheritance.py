class Animal:
    def __init__(self, name):
        self.name = name
    def speack(self):
        return "Some Sound"
    
class Dog(Animal):
    pass #mean that class is end
    
dog = Dog("rex")
print(dog.name) #inherited
print(dog.speack()) #inherited








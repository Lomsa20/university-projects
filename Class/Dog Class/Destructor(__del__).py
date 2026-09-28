class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} Destroyed")
person = Person("Jeeli") #created
del person #destroyed





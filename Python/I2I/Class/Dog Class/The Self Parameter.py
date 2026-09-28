class Person:
    def __init__(self, name):
        self.name = name # self refers to this instance
    def greet(self):
        print(f"Hello, i'm {self.name} ")

person = Person("Jora")
person.greet()      # self = person object





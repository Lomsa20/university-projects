class Person:
    def __init__(self, name):
        self.__secret = "password"
        
    def get_secret(self):
        return self.__secret
person = Person("Alice")
# print(person.__secret)  # AttributeError!
print(person.get_secret())  # Works
print(person._Person__secret)  # Works but shouldn't
   










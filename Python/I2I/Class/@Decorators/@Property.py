class Person:
    def __init__(self, name):
        self._name = name
    @property 
    def name (self):
        return self._name
person = Person("amirani")
print(person.name)#No parentheses needed



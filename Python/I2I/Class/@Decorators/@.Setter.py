class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter 
    def age(self, value):
        if value <0:
            raise ValueError 
        self._age = value

person = Person(25)
print(person.age)  # 25
person.age = 30    # Uses setter
print(person.age)  # 30
# person.age = -5  # ValueError!


        
        
        
        
        
        
        
        
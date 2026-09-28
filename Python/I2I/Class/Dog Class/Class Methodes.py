class Dog:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Dog.count +=1
    @classmethod
    def get_count(cls):
        return cls.count
        
dog1 = Dog("Jepeto")
dog2 = Dog("Jilu")
print((Dog.get_count())) #2

class Flyer:
    def fly(self):
        return "Flying"
class Swimmer:
    def swim(self):
        return "Swiming"
class Duck(Flyer, Swimmer):
    pass

duck = Duck()
print(duck.fly())
print(duck.swim())







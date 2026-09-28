class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def move(self):
        return "Moving"
class Car(Vehicle):
    def __init__(self, brand,doors):
        super().__init__(brand)
        self.doors = doors
    def moves(self):
        return "Driving on road"
class ElectricCar(Car):
    def __init__(self,brand,doors,battery):
        super().__init__(brand, doors)
        self.battery = battery
    def charge(self):
        return "Charging"

tesla = ElectricCar("Tesla", 4, 100)
print(tesla.brand)    # "Tesla"
print(tesla.doors)    # 4
print(tesla.battery)  # 100
print(tesla.move())   # "Driving on road"
print(tesla.charge()) # "Charging battery"













class Item:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    def __str__(self):
        return f'{self._name}: {self._price}'
class PerishableItem(Item):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)
        self._expiry_date = expiry_date
    def __str__(self):
        return f'{self._name}: {self._price} ({self._expiry_date})'
class Inventory:
    def __init__(self):
        self._items = {}
    def add_item(self, item, qty):
        self._items[item._name] = self._items.get(item._name, 0)+ qty
    def __add__(self, other):
        new_inv = Inventory()
        new_inv._items = self._items.copy()
        for name, qty in self._items.items():
            new_inv._items[name] = new_inv._items.get(name, 0) + qty
        return new_inv
    def __sub__(self, other):
        new_inv = Inventory()
        new_inv._items = self._items.copy()
        for name, qty in self._items.items():
            new_inv._items[name] = new_inv._items.get(name, 0) - qty
        return new_inv
    def __str__(self):
        return f", ".join(f'{name}: {qty}'for name, qty in self._items.items())
inv1 = Inventory()
inv1.add_item(Item("Apple", 1), 10)
inv2 = Inventory()
inv2.add_item(Item("Apple", 1), 5)
inv2.add_item(Item("Banana", 2), 3)
print(inv1 + inv2)
print(inv1 - inv2)
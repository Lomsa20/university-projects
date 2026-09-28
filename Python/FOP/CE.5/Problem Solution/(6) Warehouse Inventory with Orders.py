class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    def __str__(self):
        return f'{self._name} : {self._price: .2f}'
class Inventory:
    def __init__(self):
        self._stocks = {}
    def add_product(self, product, quantity):
        self._stocks[product] = self._stocks[product] + quantity
    def check_stock(self, product, quantity):
        return self._stocks.get(product, 0) >= quantity
    def deduct_product(self, product, quantity):
        if self.check_stock(product, quantity):
            self._stocks[product] -= quantity
            return True
        return False
    def __str__(self):
        return f'Inventory: \n' + '\n'.join(f'{p}; {q}' for p,q in self._stocks.items())
class Order:
    def __init__(self):
        self._items = []
    def add_items(self, product , quantity):
        self._items[product] = self._items.get(product,0) + quantity
    def confirm_order(self, inventory):
        for p,q in self._items.items():
            if not inventory.check_stock(p, q):
                return False
        for p,q in self._items.items():
            inventory.deduct_product(p, q)
        return True
    def __str__(self):
        return f'Order:\n' + "\n".join(f"{p}: {q}" for p, q in self._items.items())

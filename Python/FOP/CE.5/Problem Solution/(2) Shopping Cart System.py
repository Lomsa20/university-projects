class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"{self._name}, {self._price:.2f}"

    @property
    def price(self):
        return self._price


class ShoppingCart:
    def __init__(self):
        self._items = {}

    def add_product(self, product, quantity=1):
        self._items[product] = self._items.get(product, 0) + quantity

    def remove_product(self, product):
        if product in self._items:
            del self._items[product]

    def total_price(self):
        return sum(p.price * q for p, q in self._items.items())

    def __str__(self):
        items_str = ', '.join(f'{p} x{q}' for p, q in self._items.items())
        return f"{items_str} | Total: {self.total_price():.2f}"


apple = Product("Apple", 0.5)
banana = Product("Banana", 0.3)

cart = ShoppingCart()
cart.add_p_

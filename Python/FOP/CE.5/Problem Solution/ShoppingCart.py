class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} (${self.__price:.2f})"

    def __eq__(self, other):
        return isinstance(other, Product) and self.__name == other.__name

    def __hash__(self):
        return hash(self.__name)


class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_product(self, product, quantity=1):
        self.__items[product] = self.__items.get(product, 0) + quantity

    def remove_product(self, product):
        if product in self.__items:
            del self.__items[product]

    def total_price(self):
        total = 0
        for product, qty in self.__items.items():
            total += product.price * qty
        return total

    def __str__(self):
        items_str = ", ".join(f"{p.name} x{q}" for p, q in self.__items.items())
        return f"ShoppingCart({items_str}) | Total: ${self.total_price():.2f}"


# Example usage:
apple = Product("Apple", 0.5)
banana = Product("Banana", 0.3)

cart = ShoppingCart()
cart.add_product(apple, 100)
cart.add_product(banana, 6120321)
print(cart)

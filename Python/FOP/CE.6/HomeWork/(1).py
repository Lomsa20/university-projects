class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
class ShoppingCart:
    def __init__(self):
        self._items = []
    def add_product(self, product):
        self._items.append(product)
    def __add__(self, other):
        new_cart = ShoppingCart() #create fresh shoppingcart instance we add new because add creates new object
        new_cart._items = self._items + other._items
        return new_cart
    def total_price(self):
        return sum(p._price for p in self._items) #return price of product p
    def __str__(self):
        return f"Output: {self.total_price()}"
class DiscountedCart(ShoppingCart):
    def __init__(self, discount):
        super().__init__()
        self._discount = discount

    def total_price(self):
        return sum(p._price * (1 - self._discount/100) for p in self._items)
product1 = Product("Brave New World", 10)
product2 = Product("Toy", 20)
discounted_cart = DiscountedCart(20)
cart = ShoppingCart()
discounted_cart.add_product(product1)
discounted_cart.add_product(product2)

print(discounted_cart.total_price())
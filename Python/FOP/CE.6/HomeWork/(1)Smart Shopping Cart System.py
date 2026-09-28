class Product:
    def __init__(self,name,price):
        self._name = name
        self._price = price
class ShoppingCart:
    def __init__(self):
        self._items = []
    def add_product(self,product):
        self._items.append(product)

    def __add__(self,other): # this return shopping cart objects
        new_cart = ShoppingCart()
        new_cart._items = self._items + other._items
        return new_cart
    def total_price(self):
        return sum(p._price for p in self._items)# p.price mean give me the price of the product p
    def __str__(self):
        return f"{self.total_price()}"
class DiscountedCart(ShoppingCart):
    def  __init__(self,discount):
        super().__init__()
        self._discount = discount
    def total_price(self):
        return sum(p.price * (self._discount / 100) for p in self._items)

#creates product
p1 = Product('Book', 10)
p2 = Product('Toy', 20)

#creates cart
cart1 = ShoppingCart()
cart1.add_product(p1)
cart1.add_product(p2)


#print
print(cart1.total_price())

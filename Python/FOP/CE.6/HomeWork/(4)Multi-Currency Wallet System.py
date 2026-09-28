class Currency:
    currency_rate_usd = {"USD":1, "EURO":1.10, "JPY": 0.01}
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def convert_to_usd(self):
        rate = Currency.currency_rate_usd[self.currency]
        return self.amount * rate
    def __add__(self, other):
        total = self.convert_to_usd() + other.currency_to_usd()
        return Currency(total)
    def __sub__(self, other):
        total = self.convert_to_usd() - other.currency_to_usd()
        return Currency(total)
    def __str__(self):
        return f"{self.amount} {self.currency}"
class USD(Currency):
    def __init__(self, currency, amount):
        super().__init__("USD", amount)
    def convert_to_usd(self):
        rate = Currency.currency_rate_usd["USD"]
        return self.amount * rate
class EURO(Currency):
    def __init__(self, currency, amount):
        super().__init__("EURO", amount)
    def convert_to_usd(self,):
        rate = Currency.currency_rate_usd["EURO"]
        return self.amount * rate
class JPY(Currency):
    def __init__(self, currency, amount):
        super().__init__("JPY", amount)
    def convert_to_usd(self):
        rate = Currency.currency_rate_usd["JPY"]
        return self.amount * rate
class Wallet:
    def __init__(self):
        self.currencies = []
    def add_currency(self, currency):
        self.currencies.append(currency)
    def total_usd(self):
        return  sum(c.convert_to_usd() for c in self.currencies)
    def __str__(self):
        details = ", " .join(str(c) for c in self.currencies)
        return f"Total USD: {self.total_usd():.2f}, Details: {details}"

    wallet = Currency("Wallet", 100)
    wallet.add_currency(USD(50))
    wallet.add_currency(EURO(20))
    wallet.add_currency(JPY(2000))

    print(wallet)




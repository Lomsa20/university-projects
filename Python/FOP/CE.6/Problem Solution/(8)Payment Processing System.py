class PaymentMethod:
    def __init__(self, amount):
        self._amount = amount
    def process_payment(self):
        raise  NotImplementedError("Subclasses must override this method")
class CreditCard(PaymentMethod):
    def __init__(self, card_num, cvv, amount):
        super().__init__(amount)
        self._card_num = card_num
        self._cvv = cvv
    def process_payment(self):
        return f"Processing ${self._amount} via Credit Card ending with {self._card_num[-4:]}"
class PayPal(PaymentMethod):
    def __init__(self, email, amount):
        super().__init__(amount)
        self._email = email
    def process_payment(self):
        return f"Processing ${self._amount} via PayPal {self._email}"
class Crypto(PaymentMethod):
    def __init__(self, wallet, amount):
        super().__init__(amount)
        self._wallet = wallet
    def process_payment(self):
        return f"Processing ${self._amount} via Crypto {self._wallet[:6]}"



payment = [PayPal("amiko.lomsianidze222@gmail.com", 100), CreditCard("1234789123213", "124", 100), Crypto("0xzt63211sfe31syn84", 100)]
for p in payment:
    print(p.process_payment())
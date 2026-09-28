class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive")
            return False
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        print("Insufficient balance")
        return False

    def transfer(self, amount, other_account):
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True
        return False

    def show(self):
        return self.__balance

    def __str__(self):
        return f"Bank Account {self.__owner} balance: {self.__balance}"

# Usage
acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 50)

acc1.deposit(5.0)         # balance = 105
acc1.transfer(70, acc2)   # acc1 = 35, acc2 = 120

print(acc1)
print(acc2)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            return False
        self._balance -= amount
        return True

    def __str__(self):
        return f"Account balance: {self._balance:.2f}"


class Customer(Person):
    def __init__(self, name):
        super().__init__(name)
        self._accounts = []

    @property
    def accounts(self):
        return self._accounts

    def add_account(self, account):
        if not isinstance(account, Account):
            raise TypeError("Only Account objects allowed")
        self._accounts.append(account)

    def __str__(self):
        return f"Customer: {self.name} ({len(self._accounts)} accounts)"


class Branch:
    def __init__(self, name):
        self._name = name
        self._customers = []
        self._accounts = []

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be of type Customer")
        self._customers.append(customer)

    def open_account(self, customer, initial_balance=0):
        if customer not in self._customers:
            raise ValueError("Customer not registered in branch")

        account = Account(initial_balance)
        customer.add_account(account)
        self._accounts.append(account)

    def branch_summary(self):
        print(f"Branch: {self._name}")
        print(f"Customers: {len(self._customers)}")
        print(f"Accounts: {len(self._accounts)}")

        total_balance = sum(acc.balance for acc in self._accounts)
        print(f"Total balance in branch: {total_balance:.2f}")

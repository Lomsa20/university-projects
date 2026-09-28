class BankAccount:  # most important one
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        # self._balance increases by the amount of money 

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False  # also handle insufficient funds

    def transfer_to(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        return False

    def get_balance(self):
        return self._balance

    def __str__(self):  # notice the indentation
        return f"BankAccount(owner='{self._owner}', balance={self._balance})"


# Example usage
acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 50)
acc1.deposit(50)
acc1.transfer_to(acc2, 70)
print(acc1)
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# %%
# # # # print(acc2)
# %%

# %%
# 
# %%

# %%


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


    


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError('Deposit amount can\'t be negative or 0')

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('Withdrawal amount can not be more than current balance')
        else:
            self.__balance -= abs(amount)

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.get_balance() * self.interest_rate)

class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__(self)

    def withdraw(self, amount):
        self.__balance += abs(amount)

def test_class_usability():
    saving_example = SavingsAccount('Kyryl')
    saving_example.deposit(500)
    saving_example.withdraw(100)
    saving_example.apply_interest()
    assert saving_example.get_balance() > 0

test_class_usability()
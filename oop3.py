class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into account {self.account_number}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}")
        else:
            print(f"Insufficient balance in account {self.account_number}")

    def check_balance(self):
        print(f"Account {self.account_number} has a balance of ${self.balance}")


class BankCustomer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.accounts = {}  # Dictionary to store accounts

    def add_account(self, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number)
            print(f"Account {account_number} added for {self.customer_name}")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Account {account_number} not found for {self.customer_name}")
            return None


# Example usage:

# Create a customer
alice = BankCustomer("Alice")

# Add accounts for the customer
alice.add_account(1001)
alice.add_account(1002)

# Deposit and withdraw from an account
account1 = alice.get_account(1001)
account2 = alice.get_account(1002)

if account1 and account2:
    account1.deposit(1000)
    account1.check_balance()
    account1.withdraw(500)
    account1.check_balance()

    account2.deposit(500)
    account2.check_balance()
    account2.withdraw(1000)

# Attempt to access a non-existent account
bob = BankCustomer("Bob")
account3 = bob.get_account(1003)
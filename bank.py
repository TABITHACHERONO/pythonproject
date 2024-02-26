import datetime

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Account Opening:", self.date_of_opening)
        print("Balance:", self.balance)

account_number = "153458726"
balance = 5000
date_of_opening = datetime.date(2021, 1, 11)
customer_name = "Martin Morgan"

account = BankAccount(account_number, balance, date_of_opening, customer_name)

print("Deposit:", account.deposit(1000))
print("Withdraw:", account.withdraw(2000))
account.check_balance()
account.customer_details()
#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 


class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive number."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"


# Creating an instance of the BankAccount class
my_account = BankAccount("12345", "John Doe", 1000)

# Testing deposit and withdrawal functionality
print(my_account.display_balance())  # Display initial balance
print(my_account.deposit(500))       # Deposit $500
print(my_account.withdraw(200))      # Withdraw $200
print(my_account.display_balance())  # Display updated balance
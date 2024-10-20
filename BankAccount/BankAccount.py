class BankAccount:

    #class Attributes
    bank_title = "Amir Banking"
    #instance attribute

    #def __init__(self, customer_name, customer_balance, minimum_balance):
      #  self.customer_name = customer_name
       # self.customer_balance = customer_balance
       # self.minimum_balance = minimum_balance
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.customer_balance = customer_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number


    def deposit(self, amount):
        self.customer_balance += amount
        print(f"Deposited {amount}, new balance is {self.customer_balance}")

    def withdraw(self, amount):

        if self.customer_balance - amount < self.minimum_balance:
            print(f"Insufficient funds, cannot withdraw would be below minimum balance {self.minimum_balance} ")
        else:
            self.customer_balance -= amount;
            print(f"Withdrew {amount}, new balance is {self.customer_balance}")

    def print_customer_info(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer Balance: {self.customer_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}")












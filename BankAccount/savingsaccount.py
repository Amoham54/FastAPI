from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, interest):
        super().__init__(customer_name, customer_balance, minimum_balance, account_number, routing_number)
        self.interest = interest

    def apply_interest(self):
        interest = self.customer_balance * self.interest
        self.customer_balance += interest
        print(f"Interest: {interest}, new balance is {self.customer_balance}")

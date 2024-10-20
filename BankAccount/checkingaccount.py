from BankAccount import BankAccount

class checkingAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, limitation):
        super().__init__(customer_name, customer_balance, minimum_balance, account_number, routing_number)
        self.limitation = limitation

    def transfer(self, amount):
        limitation = self.limitation
        if amount > limitation:
            print(f"Cannot Make Transfer Amount is Greater than Sending Limit {limitation}")
        else:
            self.customer_balance -= amount
            print(f"Transfer Successful. Amount sent {amount}, \n "
                  f"your balance is {self.customer_balance}")



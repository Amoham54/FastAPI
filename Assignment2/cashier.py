class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        print("Please insert coins.")
        large_dollars = int(input("How many Large Dollars?: "))
        half_dollars = int(input("How many half Dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        total = large_dollars * 1 + half_dollars * .5 + quarters * .25 + nickels * .05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change} coins left")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

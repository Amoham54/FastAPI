### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"{item} cannot be made, not enough ingredients")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int (input("How many Large Dollars?: "))
        half_dollars = int (input("How many half Dollars?: "))
        quarters = int (input("How many quarters?: "))
        nickels = int (input("How many nickels?: "))
        total = large_dollars * 1 + half_dollars *.5 + quarters * .25 + nickels*.05
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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} is ready. Bon appetit!")

    def report(self):
        for resource, amount in self.machine_resources.items():
            print(f"{resource}: {amount}")




### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

is_on = True
while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report):")
    if choice == "report":
        machine.report()
    elif choice == "off":
        is_on = False
        print("Machine Off")
    elif choice in recipes:
        sandwich = recipes[choice]
        if machine.check_resources(sandwich["ingredients"]):
            payment = machine.process_coins()
            if machine.transaction_result(payment, sandwich["cost"]):
                machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid")





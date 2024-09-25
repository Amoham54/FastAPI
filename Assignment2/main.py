import cashier
import data
import sandwich_maker
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():

    is_on = True
    while is_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report):")
        if choice == "report":
            sandwich_maker_instance.report()
        elif choice == "off":
            is_on = False
            print("Machine Off")
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid")

if __name__ == '__main__':
    main()
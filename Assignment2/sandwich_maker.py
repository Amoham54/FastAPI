
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
           if ingredients[item] > self.machine_resources[item]:
               print(f"{item} cannot be made, not enough ingredients")
               return False
        return True

        #####

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} is ready. Bon appetit!")

    def report(self):
        for resource, amount in self.machine_resources.items():
            print(f"{resource}: {amount}")
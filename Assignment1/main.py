### Data ###
from asyncio.windows_events import NULL

'''
Author: Julian Dominguez
Email: jdomin14@charlotte.edu
Student ID: 801450236
GitHub Link: https://github.com/JukeHub/Assignment1
'''

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
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry, we don't have enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        return large_dollars + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ## added :.2f to more accurately show exact change given in conventional currency formatting.
        if coins >= cost:
            print(f"Thank you, here is ${(coins - cost):.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough for your order. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"Your {sandwich_size} sandwich is ready! Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

is_on = True
Sandwich_Order = SandwichMachine(resources)

while is_on:
    order = input("What would you like? (small / medium / large / off / report): ").lower()

    if order == "report":
        for key, value in Sandwich_Order.machine_resources.items():
            if key == "bread" or key == "ham":
                print(f"{key.capitalize()}: {value} slice(s)")
            else:
                print(f"{key.capitalize()}: {value} ounces(s)")
    elif order in recipes:
        ingredients = recipes[order]["ingredients"]
        cost = recipes[order]["cost"]
        if Sandwich_Order.check_resources(ingredients):
            payment = Sandwich_Order.process_coins()
            if Sandwich_Order.transaction_result(payment, cost):
                Sandwich_Order.make_sandwich(order, ingredients)
    elif order == "off":
        is_on = False
        print("Turning machine off!")
    else:
        print("Invalid entry, please review our options and try again.")



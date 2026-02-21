import data
import sandwich_maker
import cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()

def main():
    is_on = True

    # noinspection DuplicatedCode
    while is_on:

        order = input("What would you like? (small / medium / large / off / report): ").lower()

        if order == "report":
            for key, value in sandwich_maker_instance.machine_resources.items():
                if key == "bread" or key == "ham":
                    print(f"{key.capitalize()}: {value} slice(s)")
                else:
                    print(f"{key.capitalize()}: {value} ounces(s)")
        elif order in recipes:
            ingredients = recipes[order]["ingredients"]
            cost = recipes[order]["cost"]
            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(order, ingredients)
        elif order == "off":
            is_on = False
            print("Turning machine off!")
        else:
            print("Invalid entry, please review our options and try again.")

if __name__=="__main__":
    main()

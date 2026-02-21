class Cashier:
    def __init__(self):
        pass

    # noinspection DuplicatedCode
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
        if coins >= cost:
            print(f"Thank you, here is ${(coins - cost):.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough for your order. Money refunded.")
            return False

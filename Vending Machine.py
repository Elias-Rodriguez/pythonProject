class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print('Inventory: {} bottles'.format(self.bottles))


if __name__ == "__main__":
    # TODO: Create VendingMachine object

    Coke = VendingMachine()

    # TODO: Purchase input number of drinks

    purchase_input = int(input())
    Coke.purchase(purchase_input)

    # TODO: Restock input number of bottles

    restock_input = int(input())
    Coke.restock(restock_input)

    # TODO: Report inventory

    Coke.report()

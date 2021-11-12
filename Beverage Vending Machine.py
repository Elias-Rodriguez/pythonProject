class VendingMachine:
    def __init__(self):
        self.coke = 5
        self.pepsi = 5
        self.sprite = 5
        self.fanta = 5
        self.mt_dew = 5
        self.dr_pepper = 5
        self.root_beer = 5
        self.cream_soda = 5
        self.diet_pepsi = 5

    def purchase(self, product):
        if product == "A1":
            if self.coke != 0:
                self.coke -= 1
                print("One Coke Dispensed")
            else:
                print("Sorry, Out of Stock")
        elif product == "A2":
            if self.pepsi != 0:
                self.pepsi -= 1
                print("One Pepsi Dispensed")
        elif product == "A3":
            if self.sprite != 0:
                self.sprite -= 1
                print("One Sprite Dispensed")
        elif product == "B1":
            if self.fanta != 0:
                self.fanta -= 1
                print("One Fanta Dispensed")
            else:
                print("Sorry, Out of Stock")
        elif product == "B2":
            if self.dr_pepper != 0:
                self.dr_pepper -= 1
                print("One Dr. Pepper Dispensed")
            else:
                print("Sorry, Out of Stock")
        elif product == "B3":
            if self.root_beer != 0:
                self.root_beer -= 1
                print("One Rt. Beer Dispensed")
            else:
                print("Sorry, Out of Stock")
        elif product == "C1":
            if self.mt_dew != 0:
                self.mt_dew -= 1
                print("One Mt. Dew Dispensed")
            else:
                print("Sorry, Out of Stock")
        elif product == "C2":
            if self.diet_pepsi != 0:
                self.diet_pepsi -= 1
                print("One Diet Pepsi Dispensed")
            else:
                print("Sorry, Out of Stock")
        elif product == "C3":
            if self.cream_soda != 0:
                self.cream_soda -= 1
                print("One Cream Soda Dispensed")
            else:
                print("Sorry, Out of Stock")
        else:
            print("Sorry, that is not a valid option.")

    def restock(self):

        self.coke += 5
        self.pepsi += 5
        self.sprite += 5
        self.fanta += 5
        self.mt_dew += 5
        self.dr_pepper += 5
        self.root_beer += 5
        self.cream_soda += 5
        self.diet_pepsi += 5


# prints out the options
print(6 * " ", 10 * '-', "Vending Machine", '-' * 10)
print(2 * " ", 47 * "-")
print(2 * " ", "|", "{}{}{}{}{}{}{}{}".format(3 * " ", "Coke", 9 * " ", "Pepsi", 10 * " ", "Sprite", 7 * " ", "|"))
print(2 * " ", "|", 3* " ", "A1", 9 * " ", "A2", 12 * " ", "A3", 7 * " ","|")
print(2 * " ", "|", 43 * ' ', "|")
print(2 * " ", "|",
      "{}{}{}{}{}{}{}{}".format(3 * " ", "Fanta", 8 * " ", "Dr. Pepper", 5 * " ", "Rt Beer", 6 * " ", "|"))
print(2 * " ", "|", 3* " ", "B1", 9 * " ", "B2", 12 * " ", "B3", 7 * " ","|")
print(2 * " ", "|", 43 * ' ', "|")
print(2 * " ", "|",
      "{}{}{}{}{}{}{}{}".format(3 * " ", "MT. Dew ", 5 * " ", "Diet Pepsi", 5 * " ", "Cream Soda", 3 * " ", "|"))
print(2 * " ", "|", 3* " ", "C1", 9 * " ", "C2", 12 * " ", "C3", 7 * " ","|")
print(2 * " ", "|", 43 * ' ', "|")
print(2 * " ", 47 * "-")
print("\nMake your selection:")

# TODO: Ask user for beverage selection.

selection = input()

# TODO: create our Vending Machine Object

vend_o_matic = VendingMachine()

# TODO: Purchase Beverage

while selection != "cancel":
    if selection == 'restock':
        vend_o_matic.restock()
        selection = input(
            "Make a selection or type cancel to stop:\n")
    else:
        vend_o_matic.purchase(selection)
        selection = input("If selection is out of stock type restock.\nOtherwise, Make a selection or type cancel to "
                          "stop:\n")
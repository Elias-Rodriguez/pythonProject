# import required module
import random

# Creating and opening a new txt file.
f = open('raging_battle.txt', 'w')  # open file
f.writelines("A glorious battle between two enemies is about to unveil.\n")
f.writelines("The fight will be shown as a series of interactions between the Great Warrior of the West(Who's name is "
             "Sherman) and the Mighty Warrior from the East(Who's name is Herman).\n")
f.writelines("LET THE BATTLE BEGIN!\n\n")

# creating two characters


Sherman_Health = 100

Herman_Health = 100

weapon_one = input("What weapon should Sherman use: ")
weapon_two = input("What weapon should Herman use: ")


def attack():
    # getting our global variables for use within out function
    global Sherman_Health
    global Herman_Health
    global weapon_one
    global weapon_two

    # Getting a random attack value for both our warriors
    random_sherman_attack = random.randint(1, int(Herman_Health))
    random_herman_attack = random.randint(1, int(Sherman_Health))

    # Subtracting the attack from our warrior's health
    Herman_Health -= random_sherman_attack
    Sherman_Health -= random_herman_attack

    # Writing our story to the text file
    f.writelines(["Sherman attacked Herman with the mighty " + weapon_one + " for a total of " +
                  str(random_sherman_attack) + " health points." +
                  " Leaving Herman at " + str(Herman_Health) + " health points.\n"])
    f.writelines(["Herman attacked Sherman with the powerful " + weapon_two + " for a total of " +
                  str(random_herman_attack) + " health points." +
                  " Leaving Sherman at " + str(Sherman_Health) + " health points.\n\n"])


while True:
    if Sherman_Health > 0 and Herman_Health > 0:
        attack()
    elif Sherman_Health <= 0 and Herman_Health > 0:
        f.write("We Have our glorious victor!\n")
        f.write("The Mighty Warrior from the East, Herman, has defeated Sherman!\n")
        f.close()
        break
    elif Herman_Health <= 0 and Sherman_Health > 0:
        f.write("We Have our glorious victor!\n")
        f.write("The Great Warrior of the West, Sherman, has defeated Herman!\n")
        f.close()
        break
    else:
        f.write("A tragedy has come upon us.\n")
        f.write("The battle came to an end.\n")
        f.write("The story closes with both warriors now laying limp and lifeless.\n ")

# Opening, reading, and closing the text file.
f = open('raging_battle.txt', 'r')
battle_story = f.read()
f.close()

# Printing the text file
print(battle_story)
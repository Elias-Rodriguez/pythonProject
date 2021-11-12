import random
import AdventureGamesStory as ags
import json
import storyparts as sp


coin = random.randint(0, 10)

player_data = {}
player_data['weapon'] = 'BFG'
player_data['socks'] = 'Blue'
player_data['car'] = 'Crown Vic'
player_data['coin'] = coin
#print('your coin toss was:', player_data['coin'])
name = input('what is your name? ')
player_data['name'] = name
player_data['weapon'] = 'BFG'
player_data['socks'] = 'Blue'
player_data['car'] = 'Crown Vic'
player_data['breakfast'] = 'pancake'
player_data['lunch'] = 'sandwich'
player_data['cat'] = 'Garfield'
player_data['dog'] = 'Snoopy'
player_data['bird'] = 'Tweety'

with open("player_file.json", "w") as outfile:
    json.dump(player_data, outfile)

sp.greet_player()
sp.story()

print("You wake up in a space shuttle on the moon with a month's worth oxygen and no fuel to go home.")
print("a.Check coms to see if theres connection.\nb. Explore shuttle")
answer = input("What would you like to do?")

if answer == 'a':
    ags.user_option_a(coin)

elif answer == 'b':
    answer1 = input("You are currently in the control room. Would you like to explore:\n"
                    "a.The room you are in.\n"
                    "b.The break room.\n"
                    "c.The engine room.\n"
                    "d.Put on space suit and explore the moon.\n")
    if answer1 == 'a':
        print("\nYou decided to check coms and found out they are disconnected.\n You also found a random log that says you are 1 of 50 shuttles stranded on the moon.")
        answer2 = input("There's not much more in here. Where else would you like to explore:\n"
                        "a.The break room.\n"
                        "b.The engine room.\n"
                        "c.Put on space suit and explore the moon.\n")
        if answer2 == 'a':
            print("You explored the break room and found food and water.\n"
                  "Guess you will die from lack of oxygen before you die of starvation.")
            answer3 = input("There's not much more in here. Where else would you like to explore:\n"
                            "a.The control room.\n"
                            "b.The engine room.\n"
                            "d.Put on space suit and explore the moon.\n")
            if answer3 == 'a' or 'b' or 'c':
                print("The door to the break room got jammed.\nThere is no way out.\n"
                      "After exhausting all measures you realize your fate.\n"
                      "A month goes by, you gained some weight, and you finally run out of oxygen.\n"
                      "You Died.")
        if answer2 == 'b':
            print("You explored the engine room and found parts to fix the coms.\n"
                  "You make your way back to the control room and fix the coms.\n"
                  "You get connected and send a message.\n"
                  "Help is on its way.\nYou are saved!")
        if answer2 == 'c':
            print("You put the space suit on and open the latch to step out on the moon.\n"
                  "You take a couple of steps away from the shuttle and admire the beauty of space.\n"
                  "While taking it all in your suit malfunction due to bad seals and the oxygen is let out of your suit.\n"
                  "You try to rush back but did not have enough time.\n"
                  "As you grasp the opening latch, the seal of your suite breaks completely off.\n"
                  "You are left there frozen with your hand on the latch.\n"
                  "You Died.")

    elif answer1 == 'b':
        print("You explored the break room and found food and water.\n"
              "Guess you will die from lack of oxygen before you die of starvation.")
        answer2 = input("There's not much more in here. Where else would you like to explore:\n"
                        "a.The control room.\n"
                        "b.The engine room.\n"
                        "c.Put on space suit and explore the moon.")
        if answer2 == 'a' or 'b' or 'c':
            print("The door to the break room got jammed.\nThere is no way out.\n"
                  "After exhausting all measures you realize your fate.\n"
                  "A month goes by, you gained some weight, and you finally run out of oxygen.\n"
                  "You Died.")
    elif answer1 == 'c':
        print("You explored the engine room and found parts to fix the coms.\n"
              "You make your way back to the control room and fix the coms.\n"
              "You get connected and send a message.\n"
              "Help is on its way.\nYou are saved!")
    elif answer1 == 'd':
        print("You put the space suit on and open the latch to step out on the moon.\n"
              "You take a couple of steps away from the shuttle and admire the beauty of space.\n"
              "While taking it all in your suit malfunction due to bad seals and the oxygen is let out of your suit.\n"
              "You try to rush back but did not have enough time.\n"
              "As you grasp the opening latch, the seal of your suite breaks completely off.\n"
              "You are left there frozen with your hand on the latch.\n"
              "You Died.")
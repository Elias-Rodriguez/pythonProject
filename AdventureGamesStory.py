def user_option_a(coin):
    if coin > 9:
        print("\nNo connection found. Go explore the shuttle.")
        answer1 = input("\nYou are currently in the control room. Would you like to explore:\n"
                        "a.The room you are in.\n"
                        "b.The break room.\n"
                        "c.The engine room.\n"
                        "d.Put on space suit and explore the moon.\n")
        if answer1 == 'a':
            print("\nFound random log. Says you are 1 of 50 shuttles stranded on the moon.")
            answer2 = input("There's not much more in here. Where else would you like to explore:\n"
                            "a.The break room.\n"
                            "b.The engine room.\n"
                            "c.Put on space suit and explore the moon.\n")
            if answer2 == 'a':
                print("\nYou explored the break room and found food and water.\n"
                      "Guess you will die from lack of oxygen before you die of starvation.\n")
                answer3 = input("\nThere's not much more in here. Where else would you like to explore:\n"
                                "a.The engine room.\n"
                                "b.Put on space suit and explore the moon.\n")
                if answer3 == 'a' or 'b':
                    print("'nThe door to the break room got jammed.\nThere is no way out.\n"
                          "After exhausting all measures you realize your fate.\n"
                          "A month goes by, you gained some weight, and you finally run out of oxygen.\n"
                          "You Died.")
            if answer2 ==  'b':
                print("\nYou explored the engine room and found parts to fix the coms.\n"
                      "You make your way back to the control room and fix the coms.\n"
                      "You get connected and send a message.\n"
                      "Help is on its way.\nYou are saved!")
            if answer2 == 'c':
                print("You put the space suit on and open the latch to step out on the moon.\n"
                      "You take a couple of steps away from the shuttle and admire the beauty of space.\n"
                      "While taking it all in, your suit malfunctions due to bad seal and the oxygen is let out of your suit.\n"
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
                            "c.Put on space suit and explore the moon.\n")
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
    else:
        print("Connection found. Message sent. Help is on it's way. You are saved!")
"""Build basic Zork game"""
print("Welcome to Zajork!")
print("If unsure of how to play, type 'commands' in a textbox for more information.")
print("")

inventory = ["flashlight"]

def typing(command):
    """test for basic commands"""
    if command == "commands":
        print("Use 'search', 'take', 'interact with', or 'go through', 'inventory' to use objects during your adventure.")
        print()
        print()
    if command == "inventory":
        print("Your inventory contains:")
        for x in inventory:
            print(x)


print("You find yourself alone in a dark room. You can see nothing. What will you do?")

while True:
    recentInput = input("")
    typing(recentInput)

    if recentInput == "search room":
        break
    else:
        print("That did nothing. Please try a different input.")

print("You find a light switch on the walls. There is a door behind you and another door in front of you.")
lightOn = False

while True:
    recentInput = input("")
    typing(recentInput)

    if recentInput == "interact with switch":
        print("The bright light reveals grey walls and a map of the house and property painted on the wall. On the opposite wall, a golden arrow points behind you.")
        lightOn = True
    elif recentInput == "search map" and lightOn:
        print("There is a fountain with a red circle atound it. A red pin is stuck in a room on the basement floor. A gold pin is stuck in a room adjacent to it.")
    elif recentInput == "go through back door":
        print("you ded. try again later.")
        quit()
    elif recentInput == "go through front door":
        print("You step into a bright room.")
        break
    else:
        print("That did nothing. Please try a different input.")

print("A staircase leading upwards towards the left. The room is furnished with several games and a TV. Cabinets line the wall.")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the Treasure.")
cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if cross_road == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if lake == "wait":
        island = input("You arrive at an island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if island == "blue":
            print("You enter a room of beasts. Game Over.")
        elif island == "red":
            print("It's a room full of fire. Game Over.")
        elif island == "yellow":
            treasure_colour = input("Now there are 2 chests. One is gold and the other is silver. Which one do you choose?\n").lower()
            if treasure_colour == "silver":
                print("You have found the Treasure! You Win!")
                print("\nNow it's time to decide what to do with it.")
                treasure = input("You found the Treasure! You can choose to take it or leave it. Type 'take' or 'leave'\n").lower()
                if treasure == "take":
                    print("You have taken the Treasure. You are a cheat.\nYou should not take something that is not yours.")
                elif treasure == "leave":
                    print("You have left the Treasure. You are such a fool, a dumb and a idiot.\nGET LOST.")
            else:
                print("You have opened a chest full of ghosts who sucks your soul. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

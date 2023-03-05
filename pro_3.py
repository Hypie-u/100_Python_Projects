print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input('You\' are at a crossroad, where do you wan to go? Type "left" or "right".').lower()
if choice == "right":
    print("you are fall into a hole. Game over.")
elif choice == 'left':
    choice2 = input(
        'you\'ve come to a lake. There is an island in the middle of the lake. Type "wait" or "swim" to swim across').lower()
    if choice2 == "swim":
        print("Attacked by an angry trout. Game over.")
    elif choice2 == "wait":
        choice3 = input(
            "You arrive the island unharmed. There is a house wtih 3 doors. One red,one yellow and one blue. Which clour do you choose?").lower()
        if choice3 == "red":
            print("it is a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You enter a room of beats. Game over.")
        else:
            print("You found the teasure! You Win!")
    else:
        print("Attacked by an angry trout. Game over.")
else:
    print("you are fall into a hole. Game over.")

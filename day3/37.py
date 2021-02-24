# triple single quotes create multiple lines

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

direction = input("You are at a cross road, which way do you go? Left or right?\n")
if direction.lower() == "right":
    print("There were crocodiles, and boy they were hungry. Game Over.")
else:
    swim = input("There is an empty lake, what do you do? Swim or wait?\n")
    if swim.lower() == "swim":
        print("A group of piranhas munch you like dinner. Game Over")
    else:
        door = input("There are three doors, which one do you open? The blue, red,"
                     " or yellow door?\n")
        if door.lower() == "yellow":
            print("You WIN!")
        else:
            if door.lower() == "red":
                print("Red riding hood's wolf just found lunch. Game Over")
            else:
                print("This Monday looks much bluer with the ogre eating your arm."
                      "Game Over.")
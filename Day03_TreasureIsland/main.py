print('*******************************************************************************')
print('          |                   |                  |                     |')
print(' _________|________________.=""_;=.______________|_____________________|_______')
print('|                   |  ,-"_,=""     \'"=.|                  |')
print('|___________________|__"=._o\'"-._        \'"=.______________|___________________')
print('         |                \'\"=._o\'\"=._      _\'\"=._                     |')
print(' _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______')
print('|                   |    __.--" , ; \'"=._o." ,-"""-._ ".   |')
print('|___________________|_._"  ,. .\' \' \'\' ,  \'"-._"-._   ". \'__|___________________')
print('          |           |o\'"=._\' , "\' \'; .". ,  "-._"-._; ;              |')
print(' _________|___________| ;\'-.o\'\"=._; .\" \' \'\'."\' . \"-._ /_______________|_______')
print('|                   | |o;    \'\"-.o\'\"=._\'\'  \'\' \" ,__.--o;   |')
print('|___________________|_| ;     (#) \'-.o \'\"=.\'_.--\"_o.-; ;___|___________________')
print('____/______/______/___|o;._    \"      \'\".o|o_.--\"    ;o;____/______/______/____')
print('/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_')
print('____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____')
print('/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_')
print('____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____')
print('/______/______/______/______/______/______/______/______/______/______/_____ /')
print('*******************************************************************************')
print("Welcome to Treasure Island\nYour mission is to find the treasure")
direction = input("You are at a crossroad,Where do you want to go? \n        Type \"left\" or \"right\" \n ")

    
if direction == "left":
    waitOrSwim = input("You have come to a lake,There is an island in the middle of the lake.\n    Type \"wait\" to wait for a boat.Type \"swim\" to swim across.  \n")
    if waitOrSwim == "wait":
        doorChoose = input(" You arrive at the island unharmed. There is a house with 3 doors.\n  One red, one yellow and one blue. Which colour do you choose?")
        if doorChoose == "red":
            print("Burned by fire.\nGame Over.")
        elif doorChoose == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif doorChoose == "yellow":
            print("Treasure Found.\nYou win.")
        else:
            print("Game Over.")
    else:
        print("Attacked by tout.\nGame Over.")
    
else:
    
    print("You fell into a hole.Game Over")
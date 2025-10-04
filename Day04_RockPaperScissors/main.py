import random
import sys
print("Welcome to my Rock Paper Scisscors game")
playerchoice = int(input("What do you choose?\n Type:\n 0 for Rock \n 1 for Paper \n 2 for Scissors\n\n"))
botchoice = random.randint(0, 2)

if playerchoice == 1:
    print("You chose: ")
    print(" \nPAPER!")
    print("    _______")
    print("---'   ____)____")
    print("         ______)")
    print("          _______)")
    print("         _______)")
    print("---.__________)")
    
 
elif playerchoice == 0:
   print("You chose:") 
   print(" \nROCK!")
   print("    _______")
   print("---'   ____)")
   print("      (_____)")
   print("      (_____)")
   print("      (____)")
   print("---.__(___)")
   

elif playerchoice == 2:
 
    print("You chose:") 
    print("\nSCISSORS!")
    
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")
    
    
    

if botchoice == 1:
    print("Computer chose:  ")
    print("\nPAPER!")
    print("    _______")
    print("---'   ____)____")
    print("         ______)")
    print("          _______)")
    print("         _______)")
    print("---.__________)")
    


elif botchoice == 0:
   print("Computer chose:") 
   print(" \nROCK!")
   print("    _______")
   print("---'   ____)")
   print("      (_____)")
   print("      (_____)")
   print("      (____)")
   print("---.__(___)")
   
   
elif botchoice == 2:
 
    print("Computer chose: ") 
    print("\nSCISSORS!")
    
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")
    

if botchoice == playerchoice:
    print("It is a Draw!!!")
elif botchoice == 0 and playerchoice == 1:
    print("Yayyy,You win!!!\nComputer Loses..")
elif botchoice == 1 and playerchoice == 2:
    print("Yayyy,You win!!!\nComputer Loses..")
elif botchoice == 2 and playerchoice == 1:
    print("Oops you lose,Computer wins!!!\nTry Again")
elif botchoice == 0 and playerchoice == 2:
    print("Oops you lose,Computer wins!!!\nTry Again")
elif botchoice == 1 and playerchoice == 0:
    print("Oops you lose,Computer wins!!!\nTry Again")
elif botchoice == 2 and playerchoice == 0:
    print("Yayyy,You win!!!\nComputer Loses..")

    





    

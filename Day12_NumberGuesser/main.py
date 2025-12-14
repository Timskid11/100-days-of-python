import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game")
easy_hard = input("I'm thinking of a number between 1 and 100\nChoose a difficulty.Type 'easy' or 'hard': ").lower()
nums = 0

def all():
    global easy_hard
    global nums
    if easy_hard == "easy":
        nums = 10
    elif easy_hard == "hard":
        nums = 5
    
    numguess = random.randint(1,100)
    while nums > 0:
        
        eachguess = int(input("Make a guess: "))
        if eachguess == numguess:
            nums = 0
            print("You win!!")
                
        if numguess > eachguess:
            print("too low")
            if numguess == eachguess + 1:
               print("But...you're close")
        if numguess < eachguess:
            print("too high")
            if numguess == eachguess - 1:
                print("But...you're close") 
        nums -= 1
        if nums == 0:
            print("You lose")
                
all()
print("Thanks for playing")
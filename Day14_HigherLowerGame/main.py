import random
from art import num,vs
from data import *
print(num)
game_over = False
score = 0
while not game_over:
    
    A = (data[random.randint(0,64)])
    print(f"Compare A: {A['name']},a {A['description']},from {A['country']}")
    print(f'\n\n{vs}')
    
    B = (data[random.randint(1,64)])
    print(f"Compare B: {B['name']},a {B['description']},from {B['country']}")
    
    
    worth = input("Who has more followers? Type A or B: ").upper()
    
    if worth == "A":
        
        if A['follower_count'] > B['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_over = True
            print(num)
            print(f"\nSorry that's wrong\nFinal score: {score}")                
    if worth == "B":
        if B['follower_count'] > A['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_over = True
            
            print(f"Sorry that's wrong\nCurrent score: {score}")                

    
       

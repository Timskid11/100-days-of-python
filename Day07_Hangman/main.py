import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
    
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
        placeholder += "_"
print("Word to guess: "+ placeholder)
game_over = False
correct_letters = []
lives = 6
while not game_over:
    print(f"********* You have {lives}/6 LIVES LEFT *********")
    
           
    guess = input("Guess a letter fron the word: ").lower()
    if guess in correct_letters:
            print(f"You've already guessed {guess}'")
    display = ""
    
    for letter in chosen_word:
        
        if letter == guess:
            
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
            
        else:
            display += "_"
            
            
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}',it is not in the word\nYou lose a life.")
    
    
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"*********'IT WAS {chosen_word}' You lose *********")
                
    print(display)
        
    if "_" not in display:
        game_over = True
        print("********* YOU WIN *********")
    
    print(stages[lives])
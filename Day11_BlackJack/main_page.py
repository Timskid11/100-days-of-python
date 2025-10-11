from art import logo
import random
import sys
def beginning():
   
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player = []
    dealer = []
    playing = True
    
    anothercard="n"
    def playagain():
        def firstpart(player,dealer,anothercard):
            if anothercard == "n":
                for eachindex in range(2):  
                   player.append(random.choice(cards))
                   dealer.append(random.choice(cards))
                totalP =  sum(player)
                totalD = sum(dealer)
                for eachindex in player:
                   if eachindex == 11:
                      if totalP > 21:
                         eachindex = 1
                for eachindex in dealer:
                   if eachindex == 11:
                      if totalD > 21:
                         eachindex = 1
                   continue
            elif anothercard == "y":
                for eachindex in range(1):  
                   player.append(random.choice(cards))
                   dealer.append(random.choice(cards))
                totalP =  sum(player)
                totalD = sum(dealer)
                for eachindex in player:
                   if eachindex == 11:
                      if totalP > 21:
                         eachindex = 1
                for eachindex in dealer:
                   if eachindex == 11:
                      if totalD > 21:
                         eachindex = 1
            
            def choice1(totalD,totalP,player,dealer):
                nonlocal anothercard   
                if totalP > 21:
                    print(f"\nYour cards: {player}, current score: {totalP} ")
                    print(f"Computer's card: {dealer}, current score: {totalD} ")
                    
                    print(f"You went over, You lose! ")
                elif totalP == 21:
                    print(f"\nYour cards: {player}, current score: {totalP} ")
                    print(f"Computer's card: {dealer}, current score: {totalD} ")
                    
                    print("BLACKJACK!!! You win!")
                    if totalD == 21:
                        print("You lose!")
                elif totalP == totalD:
                   print(f"\nYour cards: {player}, current score: {totalP} ")
                   print(f"Computer's card: {dealer}, current score: {totalD} ")
                   print("Draw")
                elif totalP > 21 and totalD > 21:
                   return firstpart(player,dealer,anothercard)
                elif totalD > 21:
                    print(f"\nYour cards: {player}, current score: {totalP} ")
                    print(f"Computer's card: {dealer}, current score: {totalD} ")
                    
                    print("\nOpponent went over,You Win!")
                elif totalD == 21:
                    print(f"\nYour cards: {player}, current score: {totalP} ")
                    print(f"Computer's card: {dealer}, current score: {totalD} ")
                    print("\n BLACKJACK!!!,opponent wins!!")
                
                else:
                   anothercard = "n"
                   if anothercard == "n":
                   
                       print(f"Your cards: {player}, current score: {totalP} ")
                    
                       print(f"Computer's first card: {dealer[0]}")
                         
                       anothercard = input("\nType 'y' to get another card, type 'n' to pass:  ")
                       if anothercard == "y":
                          firstpart(player,dealer,anothercard)
                          choice1(totalD,totalP,player,dealer)
                          
                        
                       elif anothercard == "n":
                          print(f"Your cards: {player}, current score: {totalP} ")
                          print(f"Computer's card: {dealer}, current score: {totalD} ")
                          if totalD > totalP:
                             print("You lose!\nDEALER wins")
                          elif totalP > totalD:
                             print("YOU WIN!!!")
                             
            choice1(totalD,totalP,player,dealer)
            
        firstpart(player,dealer,anothercard)
        playOrNot = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if playOrNot == "y":
           return beginning()
        else:
           print("Thanks for playing")
            
    playagain()
    playOrNot = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if playOrNot == "y":
       return beginning()
    else:
       print("Thanks for playing")
        
beginning()           
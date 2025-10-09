from arts import logo,dictator
from letters import *
from main import *



print(logo)
go_again = True
while go_again:
    
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n")))
    caesar(text,shift,direction)
    
    
    def repeatfunc():
        
        repeat = input("\nEnter 'yes' if you want to go again,else enter 'no' to quit\n")
        if repeat.lower() == "no":
            go_again = False
            print("Goodbye")
            
    repeatfunc()
            
        
        
        
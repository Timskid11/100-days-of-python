from art import logo
print(logo)
print("Hello,Welcome to the Secret Aunction Program\n")
Pause = False
NandB = {}
unitwith0 = 0
while not Pause:
    
    def add_name_and_bid(NandB,unitwith0):
        name = input("What's your name?:  ").lower()
        bid = int(input("What's your bid?: ₦"))
        NandB[name] = bid
        
        otherinput = input("Are there other users that want to bid? ").lower()
        if otherinput == "yes":
            print("\n" * 30)
            return add_name_and_bid(NandB,unitwith0)
        else:
            print("\n" * 30)
            def total():                
                nonlocal NandB
                nonlocal unitwith0
                for key in NandB:
                    unitforeach = NandB[key]
                    unitwith0 += unitforeach
                    if unitwith0 > unitforeach:
                        unitwith0 = unitforeach
                    
                    else:
                        unitwith0 = unitwith0
                    if unitwith0 == NandB[key]:
                        unitwith0name = key
                    
                print(f"The winner is {unitwith0name} with a bid of {unitforeach} naira")
            total()
            
            Pause = False
                        
            
                
    add_name_and_bid(NandB,unitwith0)
                
            
            

    


print("Welcome to Python Pizza deliveries")
size = input("What size of pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra Cheese? Y or N: ")
amount = 0
if size == "s" :
    amount = 15
    if pepperoni == "y":
        amount += 2
    elif pepperoni == "n":
        amount = 15
    if extra_cheese == "y" :
        amount += 1
        print ("Your final bill is  $" + str(amount))
    elif extra_cheese == "n":
        print ("Your final bill is  $" + str(amount))
            
            
if size == "m" :
    amount = 20
    if pepperoni == "y":
        amount += 3
    elif pepperoni == "n":
        amount = 20
    if extra_cheese == "y" :
        amount += 1
        print ("Your final bill is  $" + str(amount))
    elif extra_cheese == "n":
            print ("Your final bill is  $" + str(amount))

if size == "l" :
    amount = 25
    if pepperoni == "y":
        amount += 3
    elif pepperoni == "n":
        amount = 25
    if extra_cheese == "y" :
        amount += 1
        print ("Your final bill is  $" + str(amount))
    elif extra_cheese == "n":
        print ("Your final bill is  $" + str(amount))
        

            
             
        
    

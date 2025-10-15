import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

    
    

while True:

    useropt = input("What would you like? (espresso/latte/cappuccino)").lower()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    
    
    
    
    if useropt == "off":
        
        sys.exit("Swithced off")
    elif useropt == "report":
        print(f"\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney:${money}")
    elif useropt in MENU:
        Awater = MENU[f"{useropt}"]["ingredients"]["water"]
        Amilk = MENU[f"{useropt}"]["ingredients"]["milk"]
        Acoffee = MENU[f"{useropt}"]["ingredients"]["coffee"]
        Acost = MENU[f"{useropt}"]["cost"]
    
        if water >= Awater:
            if milk >= Amilk:
                if coffee >= Acoffee:
                    print("Please insert coins.")
                    try:
                       quarter = int(input("How many quarter: "))*0.25
                       dime = int(input("How many dime: "))*0.1
                       nickel = int(input("How many nickel: "))*0.05
                       penny = int(input("How many penny: "))*0.01
                    except ValueError:             
                        print("Enter only numbers")
                        continue
                        
                    total = quarter+dime+nickel+penny
                    if total >= Acost:
                        total -= Acost
                        print(f"Here is ${total:.2f} in change.")
                        resources["water"] -= Awater
                        resources["milk"] -= Amilk
                        resources["coffee"] -= Acoffee
                        resources["money"] += Acost
                        print(f"Here is your {useropt}... enjoy!")
                        
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                    
                else:          
                    print(f"Sorry there is not enough coffee.\nTURN OFF AND REFILL")
        else:
            print(f"Sorry there is not enough milk.\nTURN OFF AND REFILL")
    else:
        print(f"Sorry there is not enough water.\nTURN OFF AND REFILL")
 
 
              
                 
              
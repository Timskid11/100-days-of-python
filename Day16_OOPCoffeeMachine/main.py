from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money_machine = MoneyMachine()
def stage():
    while True:
        useropt = input(f"What would you love to order: ({menu.get_items()})").lower()
        drink = menu.find_drink(useropt)
        if useropt == "off":
            sys.exit("Power Off.......")
        elif useropt == "report":
            coffee.report()
            return stage() 
        if drink:
            if coffee.is_resource_sufficient(drink) == True:
                
                if money_machine.make_payment(drink.cost) == True:
                    money_machine.report()
                    coffee.make_coffee(drink)
                
                
                
                
            
                
            
        
stage()
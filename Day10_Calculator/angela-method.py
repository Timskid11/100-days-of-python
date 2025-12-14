import art
print(art.logo)
def calculator():
    
    def add(first,second):
        return first + second
    def subtract(first,second):   
        return first - second
    def multiply(first,second):
        return first * second
    def divide (first,second):
        return first / second
        
    opdiction = {
        "+": add,
        "-":subtract,
        "*":multiply,
        "/":divide,
        
        }
        
    
    
    first = float(input("What's the first number: "))
    play = True
    while play:
        
        second = float(input("What's the second number:  "))
        for symbol in opdiction:
            print(f"\n{symbol}")
        op = input("Pick an operation: ")
        opsolve = opdiction[op](first,second)
        print(f"{first} {op} {second} is {opsolve}")
        
        play_again = input(f"\nType y to continue calculating with {opsolve},or type 'n' to start a new calculation:  ").lower()
        if play_again == "y":
            first = opsolve
        else:
            play = False
            print("\n"*20)
            calculator()
                  
calculator() 
     
    
    
       
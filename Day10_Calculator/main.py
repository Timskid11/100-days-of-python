from art import logo
print(logo)

first = 0
solution = 0
def start(solution,first):
    
    first = int(input("What's the first number:  "))
    second = int(input("What's the second number:  "))
    oppick = input("+\n-\n*\n/\nPick an operation:  ")
    
    
    
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
    
    
    if oppick == "+":
        solution = (opdiction["+"](first,second))
        print(f"{first} + {second} is {solution} ") 
    elif oppick == "-":
        solution = (opdiction["-"](first,second))
        print(f"{first} - {second} is {solution} ") 
    elif oppick == "*":
        solution = (opdiction["*"](first,second))
        print(f"{first} * {second} is {solution} ")
    
    elif oppick == "/":
        solution = (opdiction["/"](first,second))
        print(f"{first} / {second} is {solution}" ) 
    
    def start2(solution,first):
        
        first = first
        print(f"The first number is : {first}")
        second = int(input("What's the second number:  "))
        oppick = input("+\n-\n*\n/\nPick an operation:  ")
        
        
        
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
        
        
        if oppick == "+":
            solution = (opdiction["+"](first,second))
            print(f"{first} + {second} is {solution} ") 
        elif oppick == "-":
            solution = (opdiction["-"](first,second))
            print(f"{first} - {second} is {solution} ") 
        elif oppick == "*":
            solution = (opdiction["*"](first,second))
            print(f"{first} * {second} is {solution} ")
        
        elif oppick == "/":
            solution = (opdiction["/"](first,second))
            print(f"{first} / {second} is {solution}" ) 
            
        play_again = input(f"\nType y to continue calculating with {solution},or type 'n' to start a new calculation:  ").lower()    
        if play_again == "n":
           print("\n\n")
           return start(solution)
        elif play_again == "y":
           print("\n")
           first = solution
           return start2(solution ,first)
    
    play_again = input(f"\nType y to continue calculating with {solution},or type 'n' to start a new calculation:  ").lower()    
    if play_again == "n":
        print("\n\n")
        return start(solution)
    elif play_again == "y":
        print("\n")
        first = solution
        return start2(solution ,first)
    

start(solution,first)
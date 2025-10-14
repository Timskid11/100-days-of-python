def prime():
    print("Hello, Welcome to Prime Number Checker")
    number = int(input("Enter a number: "))
    if number == 1:
        return print("False")
    if number == 2:
        return print("True")
        
    for nums in range(2,number):
        if number % nums == 0:
            return print("False")
    return print("True")

prime()
    
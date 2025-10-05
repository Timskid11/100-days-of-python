for x in range(1,101):
    by3 = x % 3
    by5 = x % 5
    by15 = by3 and by5
    if by3 == 0:
        x = "Fizz"
        print(x)
    if by5 == 0:
        x = "Buzz"
        print(x)
    if by15 == True:
        x = "FizzBuzz"
        print(x)
     
    print(x)

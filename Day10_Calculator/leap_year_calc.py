print("Welcome!! to Leap Year Checker")    
year = int(input("\nEnter a year: "))
def leapyear(year):
    
    if year % 4 == 0:
        leap = f"{year} is a leap year"
        return print(leap)
        if year % 100 == 0:
            if year % 400 == 0:
                return print(leap)
            else:
                notleap = f"{year} is not a leap year"
                return print(notleap)
        else:
            notleap = f"{year} is not a leap year"
            return print(notleap)
    else:
        notleap = f"{year} is not a leap year"
        return print(notleap)
    
leapyear(year)
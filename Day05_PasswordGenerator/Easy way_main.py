import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ["!","#","$","%","&","(",")","+","*"]

print("Welcome to the TPassword Generator")
ch_letter = int(input("How many letters would you like in your password: \n"))
ch_symbol = int(input("How many symbols woukd you like in it: \n"))
ch_numbers = int(input("How many numbers would you like in it: \n"))
sumLetter = ""
sumSymbol= ""
sumNumber = ""
for letter in range(ch_letter):
    sumLetters = (random.choice(letters))
    sumLetter += sumLetters

for symbol in range(ch_symbol):
    sumSymbols = (random.choice(symbols))
    sumSymbol += sumSymbols

for number in range(ch_symbol):
    sumNumbers = (random.choice(symbols))
    sumNumber += sumNumbers
shuffle = list(sumLetter+sumSymbol+sumNumber)
random.shuffle(shuffle)
result = "".join(shuffle)
print("Your Password is: " + result)



    
    
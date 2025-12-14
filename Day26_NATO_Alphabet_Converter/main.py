import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for(index,row) in file.iterrows()}  

user_input = input("Enter a Word: " ).upper()
user_input_nato_list = [dictionary[letter] for letter in user_input]
print(user_input_nato_list)


PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    listed_names = names.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter:        
        letter_contents = letter.read()
        for eachname in listed_names:
            stripped_name = eachname.strip()
            new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
            print(new_letter)
            with open(f"./Output/ReadyToSend/letter to __{stripped_name}__.txt",mode = "w") as final_letter:
                final_letter.write(new_letter)                
                
           

    
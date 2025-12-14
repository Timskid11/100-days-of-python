🗓️ Day 26 – NATO Phonetic Alphabet Project

🎯 Goal

Today, I built a NATO Phonetic Alphabet Generator using Python and Pandas.
The program reads data from a CSV file containing the NATO alphabet and translates any input word into its corresponding phonetic code (e.g., CHAT → Charlie Hotel Alpha Tango).


---

🧠 What I Learned

How to read and process CSV files with pandas.read_csv().

How to loop through a DataFrame using .iterrows().

Creating dictionary comprehensions from DataFrame rows.

Handling user input and converting it into a list of phonetic codes.

Basic error handling with try and except to prevent crashes from invalid input.



---

🧩 Code Snippet

import pandas

# Read CSV and create dictionary
file = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in file.iterrows()}

# Ask user for a word and translate
while True:
    user_input = input("Enter a word: ").upper()
    try:
        user_input_nato_list = [dictionary[letter] for letter in user_input]
    except KeyError:
        print("Please enter letters only.")
    else:
        print(user_input_nato_list)
        break


---

📁 File Structure

📂 nato_project
 ┣ 📜 main.py
 ┣ 📜 nato_phonetic_alphabet.csv

Example of the CSV file:

letter,code
A,Alpha
B,Bravo
C,Charlie
...


---

🚀 Example Output

Enter a word: chat
['Charlie', 'Hotel', 'Alpha', 'Tango']


---

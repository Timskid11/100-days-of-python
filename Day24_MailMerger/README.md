🐍 Day 24 – Mail Merge Project: Automating Personalized Letters

📘 Project Overview

Today’s project focuses on file handling and string manipulation in Python.
You’ll build a Mail Merge program that reads a list of names from a file and automatically creates personalized letters for each person.

This is a practical automation project that simulates how businesses send custom letters, certificates, or emails to multiple people efficiently.


---

🧠 Concepts Practiced

Reading and writing files (.txt)

Using relative and absolute file paths

String replacement and formatting

Looping through lists and automating repetitive tasks

Managing folders and file outputs in Python



---

⚙️ How It Works

1. You have three files:

starting_letter.txt → a template letter with a [name] placeholder.

invited_names.txt → a list of names to personalize letters for.

ReadyToSend/ → a folder where completed letters will be saved.



2. The program:

Reads each name from invited_names.txt.

Replaces [name] in the starting_letter.txt with the actual name.

Saves each customized letter in the ReadyToSend folder.





---

🧩 Example Output

If invited_names.txt has:

Angela
James
Jack

Then inside ReadyToSend, you’ll get:

letter_for_Angela.txt
letter_for_James.txt
letter_for_Jack.txt

Each letter is personalized like:

Dear Angela,
You are invited to my birthday this Saturday!


---

🛠️ Key Python Methods Used

file.readlines()
str.replace()
with open() as file:
os.path.join()


---

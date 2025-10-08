🧩 Day 8 – Function Parameters & Caesar Cipher (My Version)

🎯 Concept Focus

Today, I deepened my understanding of:

Functions with parameters

Nested functions (functions inside functions)

Modularization — splitting code into different files for clarity

Conditional logic + loops

Encryption logic using Caesar Cipher



---

💻 Project: Caesar Cipher (My Build)

Instead of keeping everything in one file, I separated my project into different modules:

📁 Folder structure

Day08_CaesarCipher/
│
├── arts.py        → ASCII art and logo designs
├── letters.py     → List of alphabets (a–z)
├── main.py        → Caesar cipher logic
└── in.py          → Main interface (user interaction)


---

🧠 Logic Breakdown

arts.py

logo = """ 
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
...
"""
dictator = """ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
...
"""

letters.py

letters = ['a', 'b', 'c', ..., 'z']

main.py

def caesar(text, shift, direction):
    if direction.lower() == "encode":
        ...
    elif direction.lower() == "decode":
        ...

in.py

from arts import logo, dictator
from letters import *
from main import *

print(logo)
go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    def repeatfunc():
        repeat = input("\nEnter 'yes' if you want to go again, else 'no' to quit\n")
        if repeat.lower() == "no":
            go_again = False
            print("Goodbye")

    repeatfunc()


---

🧩 What I Did Differently

Broke the cipher into modular files — similar to how large projects are structured.

Added ASCII art for creativity and visual appeal.

Defined nested functions (encrypt() and decrypt()) inside the main caesar() function.

Included a looping system that lets the user run the program multiple times without restarting.



---

💬 Lessons Learned

Functions can contain other functions to isolate logic.

Modularizing code improves readability and reusability.

Shifting letters beyond z requires wrapping logic (modular arithmetic).

Attention to details like spaces and punctuation improves program accuracy.



---

💡 Challenge Faced

Debugging the shift logic — especially handling cases where the shift goes beyond z or below a.
This helped me understand index wrapping and list boundaries in Python.


---

🌟 Reflection

Today’s task made me think like a developer, not just a learner.
Instead of copying the tutorial flow, I built my own version with a personal touch — structure, art, and style.
That’s the difference between learning code and understanding it.

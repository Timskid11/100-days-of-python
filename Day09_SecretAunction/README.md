🗓️ Day 9 — Dictionaries, Nesting & The Secret Auction 💰

🔍 Concepts Covered

Creating and accessing Python dictionaries

Nesting lists and dictionaries inside each other

Using loops with dictionaries

Working with functions to find the highest bidder



---

💡 What I Built

🕵️‍♂️ Secret Auction Program

A simple Python program that allows multiple users to bid secretly for an item.
Each participant enters their name and bid amount — when all bids are in, the program reveals the highest bidder and their winning bid.


---

⚙️ How It Works

1. The program asks for each participant’s name and bid.


2. It stores the bids in a dictionary like this:

bids = {
    "Alice": 250,
    "Bob": 300,
    "Charlie": 200
}


3. It clears the screen (to keep bids secret 😉).


4. Once everyone has placed their bids, it loops through the dictionary to find the maximum value.


5. The program finally prints the winner and their bid amount.




---

🧠 What I Learned

How to store key–value pairs efficiently using dictionaries

How to loop through dictionaries and find maximum values

The importance of functions for organizing logic

How to use while loops and conditionals together

That even a small program can feel like a real-world system when structured right!



---

🧰 Tech Stack

🐍 Python 3

No external libraries — just logic and creativity!



---

💭 Personal Reflection

This project made me feel like I was building my first real mini-app.
It helped me understand how data can be mapped and retrieved — something essential for building larger applications later (like user data, databases, etc.).


---

🚀 Next Steps

Experiment with multiple items for bidding

Add input validation

Try a GUI version later using Tkinter



---

🖼️ Sample Output

Welcome to the secret auction program.
What is your name?: Timilehin
What's your bid?: $250
Are there any other bidders? Type 'yes' or 'no': yes

... (next bidder enters) ...

The winner is Bob with a bid of $300!


---

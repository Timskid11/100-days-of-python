🧮 Day 27 - Mile to Kilometer Converter

📘 Project Overview

This project is a simple GUI-based unit converter built using Python’s Tkinter library. It converts distances from miles to kilometers with a single click. The app helps demonstrate the basics of GUI programming — including labels, buttons, entry widgets, and event-driven functions.


---

🛠️ Features

User-friendly interface built with Tkinter

Converts Miles → Kilometers instantly

Dynamic label updates with the result

Input validation handled gracefully (through float conversion)



---

🧩 How It Works

1. The user enters a distance in miles into the input box.


2. Clicking the “Calculate” button triggers the function m_to_km().


3. The entered value is converted to kilometers using the formula:

kilometers = miles * 1.609


4. The result is displayed dynamically on the window.




---

💻 Code Highlights

def m_to_km():
    result = float(input.get()) * 1.609
    Label2["text"] = result

This function retrieves the user input, performs the conversion, and updates the label with the calculated value.



---

🧠 Concepts Learned

Creating and managing Tkinter windows

Using grid() layout for widget positioning

Handling events with button commands

Dynamically updating Label text



---

🚀 Future Improvements

Add error handling for invalid inputs

Add reverse conversion (Km → Miles)

Improve UI with custom fonts or colors



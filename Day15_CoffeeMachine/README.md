# ☕ Coffee Machine Project (Day 15 of #100DaysOfCode)

This is a Python program that simulates the logic of a real coffee vending machine.

### 💡 Features
- User can order **espresso**, **latte**, or **cappuccino**
- Automatically checks if enough **water**, **milk**, and **coffee** are available
- Accepts **coins** (quarters, dimes, nickels, pennies)
- Calculates **change** and updates resources in real time
- Generates a **live report** showing current resource levels
- Shuts down with **"off"** command
- Displays proper **units** for all ingredients (ml/g)
- Warns when resources are too low to make any drink

---

### ⚙️ Technologies Used
- Python 3  
- Basic control structures (loops, conditionals)
- Dictionaries for data organization
- Exception handling (`try` / `except`)

---

### 💭 What I Learned
- How to organize data using **nested dictionaries**
- How to use loops for continuous user input
- How to simulate **real-world logic** in code
- Importance of checking multiple resource conditions
- Handling **user input errors** gracefully

---

### 😅 My Struggles
At first, I couldn't figure out how to:
1. Keep the program running *continuously* after one order (it would end after one input).  
   → I solved this by wrapping the logic in a `while True` loop.  

2. Make the **report** show *real-time* updated values after each drink.  
   → Fixed by updating `resources` and calling a function `show_report()`.

3. Detect when the machine can’t make *any* drink due to low resources.  
   → Added a custom function `can_make_anything()` to handle that.  

---

### 🖼️ Screenshot (Struggle Moment)
*(Suggested Screenshot)*  
Take a screenshot of your terminal showing the **“Sorry, there is not enough milk.”** or **“Machine cannot make any drink — resources too low!”** message — it perfectly shows your debugging phase and adds a human touch.  

---

### 🚀 Run the Program
```bash
python coffee_machine.py

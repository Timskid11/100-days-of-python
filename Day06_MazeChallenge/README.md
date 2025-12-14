# 🌀 Day 6: Reeborg’s World Maze Challenge

**Project Goal:**  
Guide Reeborg through a maze to reach the goal using logical conditions and loops.

---

## 🧠 What I Learned
- How to use **`while` loops** effectively
- Combining **`if / elif / else`** with **logical checks**
- Defining custom functions like `turn_right()` for better code readability
- Applying problem-solving logic step by step

---

## 🧩 How It Works
The maze challenge requires Reeborg to:
1. Move forward while there’s a clear path  
2. Turn left when it meets a wall  
3. Turn right when there’s a path available  
4. Repeat until it reaches the goal 🏁  

---

## 🧾 My Solution
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():  
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

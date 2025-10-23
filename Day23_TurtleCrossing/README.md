
🐍 Day 23 – Turtle Crossing Game

🎯 Project Goal

Build a simple Turtle Crossing game using Python’s turtle module. The objective is to help the turtle cross the road while avoiding moving cars.


---

🧠 Concepts Practiced

Class inheritance & object-oriented design

Collision detection

Event listeners and key bindings

Animation loops and screen updates



---

🏗️ How It Works

1. The player controls a turtle that moves upward with the Up Arrow key.


2. Cars continuously move horizontally across the screen.


3. Each time the player successfully crosses, the level increases, and cars move faster.


4. If the turtle collides with a car, the game ends.




---

🧩 Key Files

player.py – Handles the turtle’s movement and position reset.

car_manager.py – Manages car creation, speed, and movement.

scoreboard.py – Displays and updates the level and game over message.

main.py – Runs the main game loop and connects all components.



---

💡 Lessons Learned

How to manage multiple objects on screen efficiently.

Timing and pacing in animations using time.sleep().

Organizing game logic across multiple classes for readability.

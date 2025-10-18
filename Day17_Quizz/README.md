
This is a simple **True or False Quiz Game** built with Python to practice **Object-Oriented Programming (OOP)** concepts such as **classes, objects, attributes, and methods**.

## 🚀 Features
- Asks multiple true/false questions
- Tracks your current **score**
- Uses **OOP principles** for better structure
- Easy to extend by adding more questions

## 🧩 How It Works
1. Each question is created from a `Question` class that stores:
   - The question text
   - The correct answer (`"True"` or `"False"`)
2. The `QuizBrain` class:
   - Manages the question list  
   - Tracks the score and question number  
   - Checks the user’s answers and gives feedback

## 🗂️ Project Structure

quiz_game/ │ ├── main.py          # Runs the quiz ├── question_model.py # Defines the Question class ├── data.py          # Contains question data (text + answers) └── quiz_brain.py    # Controls quiz logic (QuizBrain class)

## 🧠 Example Output

Q.1: The sky is blue. (True/False): True You got it right! Your current score is: 1/1

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git

2. Navigate to the project folder:

cd <your-repo-name>


3. Run the game:

python main.py



💡 Concepts Practiced

Classes and Objects

Constructors (__init__)

Attributes and Methods

Lists and Loops

User Input Handling


🌟 Future Improvements

Add multiple-choice questions

Build a graphical interface with Tkinter

Load questions from an API or JSON file



---

Author: Timilehin Oyinlola
Internship: Python Developer at CodeAlpha 🐍

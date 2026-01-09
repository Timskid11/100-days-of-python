from tkinter import *
import random
import time

# ---------------- CONSTANTS ---------------- #
GREEN = "#9bdeac"
RED = "#e7305b"
YELLOW = "#f7f5dd"
DARK = "#2f2f2f"
FONT_NAME = "Courier"
TEST_TIME = 60  # seconds

WORD_BANK = [
    "python", "typing", "speed", "keyboard", "focus",
    "practice", "window", "random", "correct", "green",
    "mistake", "accuracy", "timer", "coding", "logic"
]

# ---------------- WINDOW ---------------- #
window = Tk()
window.title("Wordathon")
window.config(padx=40, pady=30, bg=YELLOW)

# ---------------- TITLE ---------------- #
Label(
    window,
    text="WORDATHON",
    font=(FONT_NAME, 32, "bold"),
    fg=GREEN,
    bg=YELLOW
).pack(pady=(0, 10))

# ---------------- TIMER ---------------- #
timer_label = Label(
    window,
    text="60",
    font=("Arial", 32, "bold"),
    fg=GREEN,
    bg=YELLOW
)
timer_label.pack(pady=10)

# ---------------- WORD ROW ---------------- #
words_frame = Frame(window, bg=YELLOW)
words_frame.pack(pady=20)

# ---------------- ENTRY ---------------- #
entry = Entry(
    window,
    width=40,
    font=(FONT_NAME, 16),
    justify="center"
)
entry.pack(pady=20)
entry.focus()

status_label = Label(
    window,
    text="Type a word and press SPACE",
    font=(FONT_NAME, 12),
    fg=RED,
    bg=YELLOW
)
status_label.pack()

# ---------------- LOGIC VARIABLES ---------------- #
labels = []
words = []
current_index = 0
correct_words = 0
time_left = TEST_TIME
timer_running = False

# ---------------- FUNCTIONS ---------------- #
def load_words():
    global labels, words, current_index

    for lbl in labels:
        lbl.destroy()

    labels.clear()
    current_index = 0
    words.clear()

    words = random.sample(WORD_BANK, 6)

    for word in words:
        lbl = Label(
            words_frame,
            text=word,
            font=(FONT_NAME, 16),
            fg=DARK,
            bg=YELLOW,
            padx=6
        )
        lbl.pack(side=LEFT)
        labels.append(lbl)

def start_timer():
    global time_left

    if time_left > 0:
        timer_label.config(text=str(time_left))
        time_left -= 1
        window.after(1000, start_timer)
    else:
        end_test()

def end_test():
    entry.config(state="disabled")

    wpm = correct_words  # because test is 60 seconds
    status_label.config(
        text=f"Time up! WPM: {wpm}",
        fg=GREEN
    )

def check_word(event):
    global current_index, correct_words, timer_running

    # start timer on first SPACE
    if not timer_running:
        start_timer()
        timer_running = True

    if current_index >= len(words):
        return

    typed = entry.get().strip()

    if typed == words[current_index]:
        labels[current_index].config(fg="green")
        correct_words += 1
    else:
        labels[current_index].config(fg="red")

    entry.delete(0, END)
    current_index += 1

    if current_index >= len(words):
        load_words()

# ---------------- START ---------------- #
load_words()
entry.bind("<space>", check_word)

window.mainloop()

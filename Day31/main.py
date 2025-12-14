from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg = BACKGROUND_COLOR,padx=50,pady=50)
window.title("flashy")
current_word = {}

#csv file section
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    f_dict = original_data.to_dict(orient="records")
else:
    f_dict = data.to_dict(orient="records")



#commands
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(f_dict)
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(canvas_heading, text="French",fill="black")
    french_word = current_word["French"]
    canvas.itemconfig(canvas_fr_text, text=french_word,fill="black")
    canvas.itemconfig(canvas_fr_text, text=french_word)
    flip_timer = window.after(3000, func=flip)

def flip():

    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(canvas_heading, text="English",fill="white")
    canvas.itemconfig(canvas_fr_text, text=current_word["English"],fill="white")
def is_known():

    f_dict.remove(current_word)
    data = pandas.DataFrame(f_dict)
    data.to_csv("./data/words_to_learn.csv")
    next_card()
flip_timer = window.after(3000,func = flip)



#static
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
wrong = PhotoImage(file="./images/wrong.png")
right = PhotoImage(file="./images/right.png")

#canvas section
canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400,263,image=front)
canvas_heading = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
canvas_fr_text = canvas.create_text(400,263,text=f"",font=("Arial",60,"bold"))

canvas.grid(row = 0, column = 0,columnspan = 2)
#buttons

right_button = Button(image= right,command=is_known)
right_button.grid(row = 1, column = 1)

wrong_button = Button(image= wrong,command=next_card)
wrong_button.grid(row = 1, column = 0)

next_card()

window.mainloop()
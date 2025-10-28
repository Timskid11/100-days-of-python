
from tkinter import *
window = Tk()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(text,text = '00:00')
    check_marks.config(text="")
    title_label.config(text="Timer",fg=GREEN)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
     global reps
     reps += 1
     work_sec = WORK_MIN * 60
     short_break_sec = SHORT_BREAK_MIN * 60
     long_break_sec = LONG_BREAK_MIN * 60

     if reps % 2 == 0:
         count_down(short_break_sec)
         title_label.config(text='Short Break',fg=PINK)
     elif reps % 8 == 0:
         count_down(long_break_sec)
         title_label.config(text='LONG Break', fg=RED)
     else:
         count_down(work_sec)
         title_label.config(text='Timer',fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)
    if count > 0:
        global timer
        timer = window.after(100,count_down,count-1)
        canvas.itemconfig(text,text = f'{count_min}:{count_sec}')
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro")
window.config(padx=100, pady=100, bg = YELLOW )


canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_img)
text = canvas.create_text(100,130 ,text='00:00',fill="white",font=('arial',20,'bold'))
canvas.grid(column=1, row=1)


#label
title_label = Label(text="Timer",font=(FONT_NAME,30),fg=GREEN,bg=YELLOW)
title_label.grid(column=1,row=0)

check_marks = Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

#button
start_button = Button(text="start",width=5,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="reset",width=5,command=reset)
reset_button.grid(column=2,row=2)





window.mainloop()
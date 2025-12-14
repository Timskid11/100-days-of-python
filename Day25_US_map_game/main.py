import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S States Game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

not_on = False
all_states = data.state.to_list()
correct_guesses =[]
remaining_ones= []
while len(correct_guesses) < 50:
        
    answer = screen.textinput(f"{len(correct_guesses)}/50 States correct","What's another name of state?").title()
    if answer == "Exit":
        break
        remaining_ones = (item for item in all_states if item not in correct_guesses)
        new_data = pandas.DataFrame(remaining_ones)
        new_data.to_csv("states_to_learn.csv")
        
    if answer in all_states:
       t = turtle.Turtle()
       t.penup()
       t.hideturtle()
       correct_guesses.append(answer)
       data_coord= data[data.state == answer]
       t.goto(data_coord.x.item(),data_coord.y.item())
       t.write(answer)
 

from tkinter import *
from tkinter import messagebox
window = Tk()
window.config(padx=50, pady=50,bg="white")
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import choice, randint,shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_data = web_entry.get()
    username_data = username_entry.get()
    password_data = password_entry.get()
    new_data ={
        web_data: {
            "email": username_data,
            "password": password_data
        }
    }
    if len(web_data) == 0 or len(username_data) == 0 or len(password_data) == 0:
        messagebox.showerror("Error","Please fill all fields")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    web_data = web_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            new_data = {
                "web": {
                    "email": "username",
                    "password": "password",
                }
            }
            json.dump(new_data, file, indent=4)
            messagebox.showerror("Error","Empty password manager!!! Fill all fields ")

    else:
        try:
            messagebox.showinfo(title=web_data,message=f"Email: {data[web_data]['email']}\n\nPassword: {data[web_data]['password']}")
        except KeyError:
            messagebox.showerror("Error","Website not registered,Fill in a registered website")

# ---------------------------- UI SETUP ------------------------------- #
window.title("Password Manager")
logo_image = PhotoImage(file="../Day29_PasswordGenerator/logo.png")
canvas = Canvas(width=200, height=200, bg="white",highlightthickness=0)
canvas.grid(column= 1,row=0)
canvas.create_image(100, 100, image=logo_image)

#label
web_label = Label(text="Website: ",font=("Times New Roman", 10),bg="white")
web_label.grid(column=0, row=1)

username_label = Label(text="Email/Username: ",font=("Times New Roman", 10),bg="white")
username_label.grid(column=0, row=2)

password_label = Label(text="Password: ",font=("Times New Roman", 10),bg="white")
password_label.grid(column=0, row=3)

#entry
web_entry = Entry(width=35,bg="white")
web_entry.grid(column=1, row=1,columnspan=2)
web_entry.focus()

username_entry = Entry(width=35,bg="white")
username_entry.grid(column=1, row=2,columnspan=2)
username_entry.insert(0,"timTheEngineer@gmail")

password_entry = Entry(width=16,bg="white")
password_entry.grid(column=1, row=3)


#buttons
gen_pw = Button(text="Generate Password",bg = "white",command=generate_password)
gen_pw.grid(column=2, row=3)
add = Button(text="Add",bg="white",width=30, command=save)
add.grid(column=1, row=4,columnspan=2)

search = Button(text="Search",bg="white",command=find_password)
search.grid(column=2, row=1)


window.mainloop()


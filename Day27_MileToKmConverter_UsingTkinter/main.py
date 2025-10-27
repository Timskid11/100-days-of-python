from tkinter import *

window = Tk()
window.minsize(width = 100,height = 100)
window.title("Mile to Km Converter")
result = 0
def m_to_km():
    result = float(input.get())*1.609
    Label2["text"] = result
    
#button
button = Button(text = "Calculate",command = m_to_km)
button.grid(column = 1,row = 2)
    
#Labels first

Label1 = Label(text= "is equal to",font= ("Arial",10,"bold"))
Label1.grid(column = 0,row = 1)
 
Label2 = Label(text= f"{result}",font= ("Arial",10,"normal"))
Label2.grid(column = 1,row = 1)
Label2.config(padx=200,pady = 10)

Label3 = Label(text= "Miles",font= ("Arial",10,"normal"))
Label3.grid(column = 2,row = 0)

Label4 = Label(text= "Km",font= ("Arial",10,"normal"))
Label4.grid(column = 2, row =1)
#Entry
input = Entry(width = 10)
input.grid(column = 1,row = 0)




window.mainloop()
from tkinter import *

def calculate():
    txt = input.get()
    output.config(text="")
    if txt.find("+") == 1:
        sum=int(txt.split("+")[0])+int(txt.split("+")[1])
        output.config(text=sum)
    elif txt.find("-") == 1:
        sum=int(txt.split("-")[0])-int(txt.split("-")[1])
        output.config(text=sum)
    elif txt.find("*") == 1:
        sum=int(txt.split("*")[0])*int(txt.split("*")[1])
        output.config(text=sum)
    elif txt.find("/") == 1:
        sum=int(txt.split("/")[0])/int(txt.split("/")[1])
        output.config(text=sum)
    else : output.config(text="Error")
    output.grid(row=2, column=1)

app = Tk()
app.title("Calculator")

interduction = Label(app, text="I'm a Calculator!")
explenation = Label(app, text="Please input 2 numbers and an operation >")
input = Entry(app,)
output = Label(app, text="")
button = Button(app, text="Calculate", command=calculate)

interduction.grid(row=0, column=0)
explenation.grid(row=1, column=0)
input.grid(row=1, column=1)
button.grid(row=2, column=0)
output.grid(row=2, column=1)

app.mainloop()
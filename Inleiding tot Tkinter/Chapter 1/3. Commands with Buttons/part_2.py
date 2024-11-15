# Create a program with a button named “Click me!”. When the
# button is clicked the foreground and background colors
# should be changed and the button name should be modified
# to the text “Clicked!”.

from tkinter import *
from random import *

def clicked():
    if button1.cget('text') != "Clicked!":
        hexa = ["0","1","2","3","4","5","6","7","8","9",
                "A","B","C","D","E","F"]
        randomised = "#" + "".join([choice(hexa) for i in range(0,6)])
        button1.config(text="Clicked!")
        window.config(background=randomised)

window = Tk()
window.geometry("300x350")

button1 = Button(window, text="Click me", command=clicked)
button1.pack()

window.mainloop()
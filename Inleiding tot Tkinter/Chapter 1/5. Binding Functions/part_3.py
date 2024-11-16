# Create an application that will change the background if
# you provide left click and display previous color if you
# provide a right click.

from tkinter import *

def leftclick(event):
    window.config(bg="purple")

def rightclick(event):
    window.config(bg="red")

window = Tk()
window.geometry("100x100")
window.config(bg="red")
window.bind("<Button-1>", leftclick)
window.bind("<Button-3>", rightclick)

window.mainloop()
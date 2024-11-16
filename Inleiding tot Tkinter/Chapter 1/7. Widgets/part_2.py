# Create a program that will draw a figure where you have
# point on the canvas

from tkinter import *

def pencil(event):
    cnv.create_oval(
        event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="black"
    )

window = Tk()
window.geometry("400x500")

cnv = Canvas(window)
cnv.pack(fill=BOTH, expand=1)

cnv.bind("<B1-Motion>", pencil)

window.mainloop()
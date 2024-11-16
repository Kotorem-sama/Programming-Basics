# Create a program the will dynamically draw a rectangle.
# It means you should create a program where you will click
# on some place of the canvas. Then by pressing your mouse,
# a rectangle will appear.

from tkinter import *

def draw_triangle(event):
    cnv.create_rectangle(event.x - 5, event.y - 5,
                         event.x + 5, event.y +5)

window = Tk()

cnv = Canvas(window)
cnv.bind("<Button-1>", draw_triangle)
cnv.pack()

window.mainloop()
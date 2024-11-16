# Create an application that will show the message “Hello,
# there!” within the window, if your mouse enters the window
# of the application and message “Bye!” if your mouse leaves
# the window.

from tkinter import *

def enter_screen(event):
    label1.config(text="Hello, there!")
    label1.grid(ipadx=25)

def exit_screen(event):
    label1.config(text="Bye!")
    label1.grid(ipadx=50)

window = Tk()
window.geometry("50x50")

label1 = Label(window)
label1.grid(row=0, column=0)
window.bind("<Enter>", enter_screen)
window.bind("<Leave>", exit_screen)

window.mainloop()
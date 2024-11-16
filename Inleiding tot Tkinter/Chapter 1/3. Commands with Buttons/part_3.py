# Create a program with the following objects and layout:
# After you have clicked the button with the “Message” label,
# the “Welcome (name) (surname)! You have registered” message
# should be displayed.

from tkinter import *

def clicked():
    name = entry1.get()
    surname = entry2.get()

    if name and surname:
        label3.config(text=f"Welcome {name} {surname}! You have registered")

window = Tk()
window.geometry("300x350")

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
frame3 = Frame(window)
frame3.pack()
frame4 = Frame(window)
frame4.pack()

label1 = Label(frame1, text="Name:")
label1.pack(side=LEFT)
entry1 = Entry(frame1)
entry1.pack(side=RIGHT)

label2 = Label(frame2, text="Surname:")
label2.pack(side=LEFT)
entry2 = Entry(frame2)
entry2.pack(side=RIGHT)

button1 = Button(frame3, text="Register", command=clicked)
button1.pack()

label3 = Label(frame4, text="")
label3.pack()

window.mainloop()
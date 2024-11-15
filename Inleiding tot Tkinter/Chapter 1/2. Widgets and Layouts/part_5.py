# Create a program that will align buttons and text in
# this way.

from tkinter import *

window = Tk()

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
frame3 = Frame(frame2)
frame3.pack(side=LEFT)
frame4 = Frame(frame3)
frame4.pack(side=LEFT)
frame5 = Frame(frame3)
frame5.pack(side=RIGHT)
label1 = Label(frame1, text="TEXT 1").pack()

button1 = Button(frame4, text="BUTTON 1").pack()
button2 = Button(frame4, text="BUTTON 2").pack()
button3 = Button(frame5, text="BUTTON 3").pack()
button4 = Button(frame5, text="BUTTON 4").pack()

label2 = Label(frame2, text="TEXT 2").pack(expand=True)

window.mainloop()
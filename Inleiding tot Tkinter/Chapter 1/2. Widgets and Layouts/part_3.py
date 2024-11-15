# Align the objects in the following way:

from tkinter import *

window = Tk()

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
frame3 = Frame(window)
frame3.pack()

label1 = Label(frame1, text='This application demonstrates frame layout')
label1.pack()

button1 = Button(frame2, text="Button 1", fg='green').pack(side=LEFT)
button2 = Button(frame2, text="Button 2", fg='red').pack(side=LEFT)
button3 = Button(frame3, text="Button 3", fg='blue').pack(side=LEFT)
button4 = Button(frame3, text="Button 4", fg='blue').pack(side=LEFT)

window.mainloop()
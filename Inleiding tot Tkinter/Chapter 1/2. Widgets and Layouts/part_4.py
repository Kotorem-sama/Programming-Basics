# Create a program that will align buttons and text in this
# way.

from tkinter import *

window = Tk()

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
frame3 = Frame(window)
frame3.pack()
frame4 = Frame(window)
frame4.pack()
label1 = Label(frame1, text="TEXT").pack()

button1 = Button(frame2, text="BUTTON1").pack(side=LEFT)
button2 = Button(frame2, text="BUTTON2").pack(side=LEFT)
button3 = Button(frame2, text="BUTTON3").pack(side=RIGHT)

button4 = Button(frame3, text="BUTTON4").pack(side=LEFT)
button5 = Button(frame3, text="BUTTON5").pack(side=LEFT)
button6 = Button(frame3, text="BUTTON6").pack(side=RIGHT)

button7 = Button(frame4, text="BUTTON7").pack(side=LEFT)
button8 = Button(frame4, text="BUTTON8").pack(side=LEFT)
button9 = Button(frame4, text="BUTTON9").pack(side=RIGHT)

window.mainloop()
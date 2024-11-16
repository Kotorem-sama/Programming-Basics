# Apply grid layout to create an application with the
# alignment of the objects in the following way.

from tkinter import *

window = Tk()

label1 = Label(window, text="TEXT 1")
button1 = Button(window, text="BUTTON 1")
button2 = Button(window, text="BUTTON 2")
button3 = Button(window, text="BUTTON 3")
button4 = Button(window, text="BUTTON 4")
label2 = Label(window, text="TEXT 2")

label1.grid(column=0, row=0, columnspan=3, ipadx=50)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=0, row=2)
button4.grid(column=1, row=2)
label2.grid(column=2, row=1, rowspan=2)

window.mainloop()
from tkinter import *
window = Tk()
window.title("Application 1")

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack()

text1 = Label(topFrame, text = "This application demonstrates simple layout")
button1 = Button(bottomFrame, text = "Button 1" , fg = "green")
button2 = Button(bottomFrame, text = "Button 2" , fg = "red")
button3 = Button(bottomFrame, text = "Button 3" , fg = "blue")

text1.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()
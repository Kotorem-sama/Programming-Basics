# Fill in the blank (1) to make the following program:
# from tkinter import *
# (1)_____ = Tk()
# window.(2)______("Desktop Application for IT club in the 359 lab")
# text1 = Label(window, text = "Hello, Brogrammers and Prosisters! This our first program, so be sure that we can accomplish this year without any doubts!")
# text1.(3)______
# window.mainloop()

from tkinter import *
window = Tk()
window.title("Desktop Application for IT club in the 359 lab")
text1 = Label(window, text = "Hello, Brogrammers and Prosisters! This our first program, so be sure that we can accomplish this year without any doubts!")
text1.pack()
window.mainloop()
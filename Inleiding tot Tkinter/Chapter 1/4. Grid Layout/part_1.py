from tkinter import *

window = Tk()
window.title("Grid layout application")

username_label = Label(window, text="Username:")
password_label = Label(window, text = "Password:")
username_entry = Entry(window)
password_entry = Entry(window)
submit_button = Button(window, text = "Submit")
clear_button = Button(window, text = "Clear")
close_button = Button(window, text = "Close")

username_label.grid(row = 0, column = 0)
username_entry.grid(row = 0, column = 1, columnspan=2)
password_label.grid(row = 1, column = 0)
password_entry.grid(row = 1, column = 1, columnspan=2)
submit_button.grid(row = 2, column = 0, ipadx = 20)
clear_button.grid(row = 2, column = 1, ipadx = 20)
close_button.grid(row = 2, column = 2, ipadx = 20)

window.mainloop()
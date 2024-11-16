# Add functionality of the buttons to the tutorial of this
# lesson:

# 1) Add widget “Label” which will display the text
# “Logged in” when you press “Submit” button.
# 2) Add “Clear” button that will clear all the text from
# “Username_entry” and “ Password_entry”.
# 3) Lastly add a “Close” button that will simply close the
# application.

from tkinter import *

def submit_click():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        login_label.config(text="Logged in")
    else:
        login_label.config(text="")

def clear_click():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    submit_click()

window = Tk()
window.title("Grid layout application")

username_label = Label(window, text="Username:")
password_label = Label(window, text = "Password:")
username_entry = Entry(window)
password_entry = Entry(window)
submit_button = Button(window, text = "Submit", command = submit_click)
clear_button = Button(window, text = "Clear", command=clear_click)
close_button = Button(window, text = "Close", command=window.destroy)
login_label = Label(window, text="")

username_label.grid(row = 0, column = 0)
username_entry.grid(row = 0, column = 1, columnspan=2)
password_label.grid(row = 1, column = 0)
password_entry.grid(row = 1, column = 1, columnspan=2)
submit_button.grid(row = 3, column = 0, ipadx = 20)
clear_button.grid(row = 3, column = 1, ipadx = 20)
close_button.grid(row = 3, column = 2, ipadx = 20)
login_label.grid(row = 2, column = 1)

window.mainloop()
from tkinter import *

def clicked():
    text = entry_text.get()
    if text:
        display_text = f"Hello, {text}! How are you?"
        text1.config(text=display_text)

window = Tk()
window.title("Clicking application")
window.geometry("300x350")

text1 = Label(window, text="Enter your name here")
text1.pack()

entry_text = Entry(window)
entry_text.pack()

button1 = Button(window, text="Click me!", command=clicked)
button1.pack()

window.mainloop()
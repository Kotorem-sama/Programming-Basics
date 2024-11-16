# Improve the previous practice so that when you press right
# key on the keyboard background color will change. And if you
# press left key previous color will appear.

from tkinter import *
from random import randint

colors = ["#FF0000"]

def leftbutton(event):
    if len(colors) > 1:
        colors.pop()
        window.config(bg=colors[-1])

def rightbutton(event):
    hexa = [hex(randint(0, 15)).removeprefix("0x") for i in range (0,6)]
    hexa = f"#{"".join(hexa)}"
    colors.append(hexa)
    window.config(bg=hexa)

window = Tk()
window.geometry("100x100")
window.config(bg="red")
window.bind("<Left>", leftbutton)
window.bind("<Right>", rightbutton)

window.mainloop()
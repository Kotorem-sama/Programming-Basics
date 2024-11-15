from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

window = Tk()

window.title("Welcome")
window.geometry('350x200')

# lbl = Label(window, text="Hello", font=("Arial Bold", 50))
# lbl.grid(column=0, row=0)

# combo = Combobox(window)

# combo['values']= (1, 2, 3, "Bruh", "Bruh2", "Bruh3")
# combo.current(0)
# combo.grid(column=0, row=1)

# def clicked():
#     lbl.configure(text="De knop is geklikt!")

# btn = Button(window, text="Klik op mij", bg="yellow", fg="red", command=clicked)
# btn.grid(column=1, row=0)

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Eerste tab')
tab_control.add(tab2, text="Tweede tab")

lbl1 = Label(tab1, text="Dit is de tekst van mijn eerste tab")
lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text="En dit is de tekst van tab 2, hallo daar")
lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()
from tkinter import *
from tkinter import messagebox 

window = Tk()
window.geometry("1000x900")

def canvas():

    def brush(event):
        cnv.create_oval(event.x - 5, event.y - 5,
                        event.x + 5, event.y + 5,
                        fill="red", outline="red")

    cnv = Canvas(window)
    cnv.pack(fill=BOTH, expand=1)

    cnv.create_rectangle(10, 20, 300, 200, fill="red")
    cnv.create_oval(50, 210, 300, 460, fill='blue', width=10, outline='grey')
    cnv.create_line(310, 20, 460, 190, width=20)
    cnv.create_arc(215, 210, 505, 460, width=10)
    cnv.create_polygon(470, 20, 570, 20, 570, 120, fill="yellow", outline="black")
    cnv.create_text(610, 210, text="Hello world\nHi, there",
                    justify=CENTER, font= ("Times", "40", "italic"))

    cnv.bind("<B1-Motion>", brush)

def scale_spinbox():
    scale = Scale(window)
    scale.config(from_=10, to=500, orient=HORIZONTAL)
    scale.pack()

    spinbox = Spinbox(window)
    spinbox.config(values = ("One", "Two", "Three"))
    spinbox.pack()

def confirm():
    if yes_no.get() == 1:
        messagebox.showinfo("Hello", f"You have chosen for {clr.get()}")
    else:
        messagebox.showwarning("No no", "Please put a tick")

values = ["Red","Green","Yellow","Blue","Black"]
clr = StringVar()
clr.set("Red")

for i in range(5):
    lbl = Label(window, text=values[i])
    c = Radiobutton(variable=clr, value=values[i])
    lbl.grid(row = i + 1, column=0)
    c.grid(row=i+1, column=1)

yes_no = IntVar()
yes_no_lbl = Label(window, text="Yes/No")
yes_no_cbut = Checkbutton(variable = yes_no, onvalue=1)
yes_no_lbl.grid(row=6, column=0)
yes_no_cbut.grid(row=6, column=1)

button = Button(window, text="Confirm", command=confirm)
button.grid(row=7, column=0, columnspan=2)

window.mainloop()
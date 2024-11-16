# Apply all the given widgets in the lesson

from tkinter import *
import math

color = "#000000"
red = 0
green = 0
blue = 0
size = 1
shape = "Circle"

def create_star(center_x, center_y, size, amount=5):
    points = []
    angle = math.pi / 2

    for i in range(amount):
        outer_x = center_x + size * math.cos(angle)
        outer_y = center_y - size * math.sin(angle)
        points.append((outer_x, outer_y))
        angle += 2 * math.pi / amount

        inner_angle = angle - math.pi / amount
        inner_x = center_x + (size / 2) * math.cos(inner_angle)
        inner_y = center_y - (size / 2) * math.sin(inner_angle)
        points.append((inner_x, inner_y))

    return [coord for point in points for coord in point]

def draw(event):
    global color, size, shape
    if shape == "Circle":
        cnv.create_oval(event.x - size, event.y - size,
                        event.x + size, event.y + size,
                        fill=color, outline=color)
    elif shape == "Square":
        cnv.create_rectangle(event.x - size, event.y - size,
                        event.x + size, event.y + size,
                        fill=color, outline=color)
    elif shape == "Star":
        cnv.create_polygon(create_star(event.x, event.y, size),
                           fill=color, outline=color)

def set_size():
    global size
    size = int(spinbox.get())

def set_red(val):
    global red
    red = int(val)

def set_green(val):
    global green
    green = int(val)

def set_blue(val):
    global blue
    blue = int(val)

def hexa(i):
    if i <= 15:
        return f"0{hex(i).removeprefix("0x")}"
    else:
        return hex(i).removeprefix("0x")

def change_color(event):
    global red, green, blue, color
    red_hexa = hexa(red)
    green_hexa = hexa(green)
    blue_hexa = hexa(blue)
    color = f"#{red_hexa}{green_hexa}{blue_hexa}"

def use():
    global color, shape
    if eraser.get() == 1:
        color = "#FFFFFF"
        scale1.config(state=DISABLED)
        scale2.config(state=DISABLED)
        scale3.config(state=DISABLED)
    else:
        change_color(1)
        scale1.config(state=NORMAL)
        scale2.config(state=NORMAL)
        scale3.config(state=NORMAL)
    
    shape = clr.get()

def clear():
    cnv.delete("all")

window = Tk()
window.geometry("400x500")
window.title("Paint.fake")

cnv = Canvas(window, height=200, width=400)
cnv.config(highlightthickness=1, highlightbackground="black", bg="white")
cnv.bind("<Button-1>", draw)
cnv.bind("<B1-Motion>", draw)
cnv.grid(row=0,column=0,columnspan=2)

scale1 = Scale(window)
scale1.config(from_=0, to=255, orient=HORIZONTAL, command=set_red)
scale1.bind("<B1-Motion>", change_color)
scale1.grid(row=1, column=1)
label1 = Label(window, text="Red:")
label1.grid(row=1, column=0)

scale2 = Scale(window)
scale2.config(from_=0, to=255, orient=HORIZONTAL, command=set_green)
scale2.bind("<B1-Motion>", change_color)
scale2.grid(row=2, column=1)
label2 = Label(window, text="Green:")
label2.grid(row=2, column=0)

scale3 = Scale(window)
scale3.config(from_=0, to=255, orient=HORIZONTAL, command=set_blue)
scale3.bind("<B1-Motion>", change_color)
scale3.grid(row=3, column=1)
label3 = Label(window, text="Blue:")
label3.grid(row=3, column=0)

spinbox = Spinbox(window)
spinbox.config(values=(1, 2, 5, 10, 20, 25), command=set_size)
spinbox.grid(row=4, column=1)
label4 = Label(window, text="Brush size:")
label4.grid(row=4, column=0)

values = ["Circle", "Square", "Star"]
clr = StringVar()
clr.set("Circle")

for i in range(len(values)):
    lbl = Label(window, text=values[i])
    lbl.grid(row = i + 5, column=0)
    
    c = Radiobutton(variable=clr, value=values[i])
    c.grid(row=i+5, column=1)

eraser = IntVar()
eraser_lbl = Label(window, text="Eraser")
eraser_cbut = Checkbutton(variable = eraser, onvalue=1)
eraser_lbl.grid(row=8, column=0)
eraser_cbut.grid(row=8, column=1)

button1 = Button(window, text="Use", command=use)
button1.grid(row=9, column=0)

button2 = Button(window, text="Clear", command=clear)
button2.grid(row=9, column=1)

window.mainloop()
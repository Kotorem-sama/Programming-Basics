# Maak een eenvoudige GUI-applicatie, met behulp van Tkinter in
# Python, waarmee de gebruiker de breedte en hoogte van een
# rechthoek kan invoeren. Zodra de gebruiker de waarden invoert
# en op een knop klikt, wordt een rechthoek met de opgegeven
# afmetingen getekend op een canvas. Bovendien moet er een
# cirkel in het midden van de rechthoek worden geplaatst,
# waarbij de cirkel de maximale grootte heeft die binnen de
# rechthoek past.

from tkinter import *

def getSmallestCircleCentered(width, height):
    if width < height:
        toCenter = (height - width)/2
        return 10, 10+toCenter, width+10, width+10+toCenter
    else:
        toCenter = (width - height)/2
        return 10+toCenter, 10, height+10+toCenter, height+10
        
def draw():
    try:
        width = int(entry1.get())
        if width < 5 or width > 390:
            raise ValueError
    except:
        popupmsg("Graag een breedte invullen tussen de 5 en 390")
        return
    
    try:
        height = int(entry2.get())
        if width < 5 or width > 290:
            raise ValueError
    except:
        popupmsg("Graag een hoogte invullen tussen de 5 en 290")
        return

    canvas1.delete("all")

    coord = 10,10,width+10,height+10
    canvas1.create_rectangle(coord, outline="blue", width=2)

    coords = getSmallestCircleCentered(width, height)
    canvas1.create_oval(coords, outline="red", width=2)

def popupmsg(msg):
    popup = Tk()
    
    popup.title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


window = Tk()
window.title("Tekenen van Rechthoek en Cirkel")
window.geometry('500x475')

frame1 = Frame(window)
frame2 = Frame(window)
frame1.pack(pady=20, expand=True)
frame2.pack(expand=True)

label1:Label = Label(frame1, text="Voer de breedte van de rechthoek in:")
label1.grid(column=0, row=0, pady=7.5)

entry1:Entry = Entry(frame1, width=10)
entry1.grid(column=1, row=0, padx=10)

label2:Label = Label(frame1, text="Voer de hoogte van de rechthoek in:")
label2.grid(column=0, row=1)

entry2:Entry = Entry(frame1, width=10)
entry2.grid(column=1, row=1, padx=10)

button1 = Button(frame2, text="Teken Vormen", command=draw)
button1.grid(column=0, row=0, pady=5)

canvas1 = Canvas(frame2, width=400, height=300, bg="White")
canvas1.grid(column=0, row=1, pady=24)

window.mainloop()
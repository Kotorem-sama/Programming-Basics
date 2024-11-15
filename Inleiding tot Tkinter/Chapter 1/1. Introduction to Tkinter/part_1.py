# Inleiding tot Tkinter
# Voer de volgende code uit om een ​​eenvoudig venster te maken
# met de tekst Hello World!. Stappen:
# 1) importeer de module  tkinter .
# 2) Initialiseer de vensterbeheerder met de  methode
# tkinter.Tk() en wijs deze toe aan een variabel venster.
# Deze methode creëert een leeg venster met knoppen voor
# sluiten, maximaliseren en minimaliseren.
# 3) Hernoem de titel van het venster zoals u wilt met
# window.title(title_of_the_window).
# 4) Label wordt gebruikt om bepaalde objecten in het venster
# in te voegen. Hier voegen we een label toe  met wat tekst.
# 5) pack() attribuut van de widget wordt gebruikt om de widget
# in de gewenste grootte weer te geven.
# 6) Tenslotte de methode mainloop() om het venster weer te
# geven totdat u het handmatig sluit.

import tkinter

window = tkinter.Tk()
window.title("Introduction to Tkinter")

lbl = tkinter.Label(text="First Label")
lbl.pack()

window.mainloop()
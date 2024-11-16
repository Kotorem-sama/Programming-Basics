from tkinter import *

window = Tk()
window.title("Medu Bar App")
window.geometry("400x300")

def print_hello():
    print("Hello World")

menu_bar = Menu(window)
popup_menu = Menu(window, tearoff=False)
file_menu = Menu(menu_bar, tearoff=False)
save_menu = Menu(file_menu, tearoff=False)

def popup(event):
    popup_menu.post(event.x_root, event.y_root)

popup_menu.add_command(label="Copy")
popup_menu.add_command(label="Paste")

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_command(label="Hello!", command=print_hello)
menu_bar.add_command(label="Quit!", command=window.quit)

file_menu.add_command(label="New", command=print_hello)
file_menu.add_command(label="Open", command=print_hello)

file_menu.add_separator()
file_menu.add_cascade(label="Save", menu=save_menu)
save_menu.add_command(label="Save...")
save_menu.add_command(label="Save as...")

window.config(menu=menu_bar)
window.bind("<Button-3>", popup)

window.mainloop()
# Create an application with pulldown menus: “File”, “Edit’,
# “View” and “Help”. Each of them should have at least 4
# commands. With separator between types of command. Also,
# at least 1 command should be pulldown menu with 3 commands
# inside.

from tkinter import *

window = Tk()
window.geometry("350x400")

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=False)
edit_menu = Menu(menu_bar, tearoff=False)
view_menu = Menu(menu_bar, tearoff=False)
help_menu = Menu(menu_bar, tearoff=False)
open_recent = Menu(file_menu, tearoff=False)
paste_menu = Menu(edit_menu, tearoff=False)

menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_cascade(label="Open", menu=open_recent)
file_menu.add_separator()
file_menu.add_command(label="Save...")
file_menu.add_command(label="Save as...")

open_recent.add_command(label="file5.txt", foreground="grey")
open_recent.add_command(label="file4.txt", foreground="grey")
open_recent.add_command(label="file3.txt", foreground="grey")
open_recent.add_command(label="file2.txt", foreground="grey")
open_recent.add_command(label="file1.txt", foreground="grey")

menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_cascade(label="Paste", menu=paste_menu)
edit_menu.add_command(label="Delete")

paste_menu.add_command(label="Keep Source Formatting")
paste_menu.add_command(label="Merge Formatting")
paste_menu.add_command(label="Keep Text Only")

menu_bar.add_cascade(label="View", menu=view_menu)


menu_bar.add_cascade(label="Help", menu=help_menu)


window.config(menu=menu_bar)
window.mainloop()
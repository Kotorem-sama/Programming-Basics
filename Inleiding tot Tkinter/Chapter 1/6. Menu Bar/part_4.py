from tkinter import *
from tkinter import messagebox, filedialog

def popup(event):
    popup_menu.post(event.x_root, event.y_root)

def new_file():
    messagebox.showinfo("File", "New file created.")

def save():
    messagebox.showinfo("File", "File saved.")

def open():
    messagebox.showinfo("Open", "File opened.")

def save_as():
    file = filedialog.asksaveasfilename(defaultextension=".txt", 
                                        filetypes=[("Text files", "*.txt"), 
                                                   ("All files", "*.*")])
    if file:
        messagebox.showinfo("File", f"File saved as: {file}")

def undo():
    messagebox.showinfo("Edit", "Undo action performed.")

def cut():
    messagebox.showinfo("Edit", "Text cut.")

def copy():
    print("Text copied.")
    messagebox.showinfo("Edit", "Text copied.")

def paste(option):
    print(f"Pasted with option: {option}")
    messagebox.showinfo("Edit", f"Pasted with option: {option}")

def delete():
    print("Deleted selected text.")
    messagebox.showinfo("Edit", "Deleted selected text.")

def zoom(action):
    print(f"Zoom action: {action}")
    messagebox.showinfo("View", f"Zoom action: {action}")

def navigate(direction):
    print(f"Navigated {direction}.")
    messagebox.showinfo("View", f"Navigated {direction}.")

def contact():
    print("Contact us selected.")
    messagebox.showinfo("Help", "Contact us at support@example.com.")

def about_us():
    print("About us selected.")
    messagebox.showinfo("Help", "This is a sample application.")

def send_report():
    print("Report sent.")
    messagebox.showinfo("Help", "Report sent successfully.")

def guide(topic):
    print(f"Guide selected: {topic}")
    messagebox.showinfo("Help", f"Guide for {topic} selected.")

window = Tk()
window.geometry("350x400")

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=False)
edit_menu = Menu(menu_bar, tearoff=False)
view_menu = Menu(menu_bar, tearoff=False)
help_menu = Menu(menu_bar, tearoff=False)
open_recent = Menu(file_menu, tearoff=False)
paste_menu = Menu(edit_menu, tearoff=False)
zoom_menu = Menu(view_menu, tearoff=False)
guide_menu = Menu(help_menu, tearoff=False)
popup_menu = Menu(window, tearoff=False)

menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_cascade(label="Open", menu=open_recent)
file_menu.add_separator()
file_menu.add_command(label="Save...", command=save)
file_menu.add_command(label="Save as...", command=save_as)

open_recent.add_command(label="file5.txt", foreground="grey", command=open)
open_recent.add_command(label="file4.txt", foreground="grey", command=open)
open_recent.add_command(label="file3.txt", foreground="grey", command=open)
open_recent.add_command(label="file2.txt", foreground="grey", command=open)
open_recent.add_command(label="file1.txt", foreground="grey", command=open)

menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_cascade(label="Paste", menu=paste_menu)
edit_menu.add_command(label="Delete", command=delete)

paste_menu.add_command(label="Keep Source Formatting", command=lambda: paste("Keep Source Formatting"))
paste_menu.add_command(label="Merge Formatting", command=lambda: paste("Merge Formatting"))
paste_menu.add_command(label="Keep Text Only", command=lambda: paste("Keep Text Only"))

menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_cascade(label='Zoom', menu=zoom_menu)
view_menu.add_separator()
view_menu.add_command(label="Left", command=lambda: navigate("left"))
view_menu.add_command(label="Right", command=lambda: navigate("right"))
view_menu.add_command(label="Up", command=lambda: navigate("up"))
view_menu.add_command(label="Down", command=lambda: navigate("down"))

zoom_menu.add_command(label="Zoom in", command=lambda: zoom("Zoom in"))
zoom_menu.add_command(label="Zoom out", command=lambda: zoom("Zoom out"))
zoom_menu.add_command(label="Restore default zoom", command=lambda: zoom("Restore default zoom"))

menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Contact", command=contact)
help_menu.add_command(label="About us", command=about_us)
help_menu.add_command(label="Send report", command=send_report)
help_menu.add_separator()
help_menu.add_cascade(label="Help", menu=guide_menu)

guide_menu.add_command(label="Creating a file", command=lambda: guide("Creating a file"))
guide_menu.add_command(label="Opening a file", command=lambda: guide("Opening a file"))
guide_menu.add_command(label="Saving a file", command=lambda: guide("Saving a file"))

popup_menu.add_command(label="Cut", command=cut)
popup_menu.add_command(label="Copy", command=copy)
popup_menu.add_command(label="Delete", command=delete)
popup_menu.add_command(label="Paste: Keep Source Formatting", command=lambda: paste("Keep Source Formatting"))
popup_menu.add_command(label="Paste: Merge Formatting", command=lambda: paste("Merge Formatting"))
popup_menu.add_command(label="Paste: Keep Text Only", command=lambda: paste("Keep Text Only"))

window.config(menu=menu_bar)
window.bind("<Button-3>", popup)
window.mainloop()
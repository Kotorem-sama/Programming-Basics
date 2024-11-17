# Create a form application, where a user fills his or her
# data inside. His or her name, surname, to date of birth use
# spinbox. To select gender use radio box. To the preferred
# jobs use check buttons. And to give permission of using this
# data use check button. Also if this check button will not be
# chosen, show a message box with warning.

from tkinter import *
from tkinter import messagebox

def checkdate():
    year = int(spinbox3.get())
    month = int(spinbox2.get())
    day = int(spinbox1.get())
    
    leapyear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    if leapyear and month == 2 and day == 29:
        return True
    if month == 2 and day > 28:
        return False
    if not month in [1, 3, 5, 7, 8, 10, 12] and day > 30:
        return False
    return True

def getjobs():
    jobs = []
    for i in range(len(preferred_jobs)):
        if preferred_jobs[i].get() == 1:
            jobs.append(values[i])
    return jobs

def getuserdata():
    userdata = f"name: {entry1.get().title()} {entry2.get().title()}\n"
    
    day = int(spinbox1.get())
    month = int(spinbox2.get())
    year = int(spinbox3.get())
    
    date = ["0"+str(i) if i < 10 else str(i) for i in [day, month, year]]
    date = "/".join(date)

    userdata += f"Date of birth: {date}\n"
    userdata += f"Gender: {choice.get()}\n"
    userdata += f"Preferred jobs: {", ".join(getjobs())}"
    return userdata

def check():
    if yes_no.get() == 0:
        msg = "Cannot submit form without data usage permission."
        messagebox.showwarning("Warning", msg)
    elif not checkdate():
        messagebox.showwarning("Warning", "Please enter a correct date.")
    elif not entry1.get():
        messagebox.showwarning("Warning", "Please enter a Name.")
    elif not entry2.get():
        messagebox.showwarning("Warning", "Please enter a Surame.")
    elif not getjobs():
        messagebox.showwarning("Warning", "Please select preferred jobs.")
    else:
        userdata = getuserdata()
        msg = messagebox.askyesno("Data", "Is this data correct?\n\n"+userdata)
        if msg:
            messagebox.showinfo("Succes", "The data has been submitted!")

window = Tk()

label1 = Label(window, text="Name:").grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=1, columnspan=2)

label2 = Label(window, text="Surname:").grid(row=1, column=0)
entry2 = Entry(window)
entry2.grid(row=1, column=1, columnspan=2)

label3 = Label(window, text="Date of birth:").grid(row=2, column=0)
spinboxval1 = IntVar(value=1)
spinbox1 = Spinbox(window, from_=1, to=31, wrap=True,
                   width=2, textvariable=spinboxval1)
spinbox1.grid(row=2, column=1)

spinboxval2 = IntVar(value=1)
spinbox2 = Spinbox(window, from_=1, to=12, wrap=True,
                   width=2, textvariable=spinboxval2)
spinbox2.grid(row=2, column=2)

spinboxval3 = IntVar(value=2024)
spinbox3 = Spinbox(window, from_=1900, to=2024, wrap=True,
                   width=4, textvariable=spinboxval3)
spinbox3.grid(row=2, column=3)

values = [ "Man", "Woman", "Apache helicopter",
          "Walmart bag", "Cop (secret)" ]
choice = StringVar()
choice.set("Man")

label4 = Label(window, text="Gender:").grid(row=3, column=0)

for i in range(len(values)):
    radio = Radiobutton(variable=choice, value=values[i])
    radio.grid(row=3, column=i+1)

    label = Label(window, text=values[i])
    label.grid(row=4, column=i+1)

label5 = Label(window, text="Preferred jobs:").grid(row=5, column=0)

preferred_jobs = []
values = [ "Education", "Accountancy", "Marketing",
          "Healthcare", "Management", "Electrician",
          "Florist", "Bad person (Dentist)" ]

for i in range(len(values)):
    job = IntVar()
    preferred_jobs.append(job)

    job_lbl = Label(window, text=values[i])
    job_lbl.grid(row=i+5, column=1)

    job_cbut = Checkbutton(variable = preferred_jobs[i], onvalue=1)
    job_cbut.grid(row=i+5, column=2)

yes_no = IntVar()

yes_no_lbl = Label(window, text="Give permission for data usage:")
yes_no_lbl.grid(row=i+6, column=0)

yes_no_cbut = Checkbutton(variable = yes_no, onvalue=1)
yes_no_cbut.grid(row=i+6, column=1)

button1 = Button(window, text="Submit", command=check)
button1.grid(row=14, column=0, columnspan=2)

window.mainloop()
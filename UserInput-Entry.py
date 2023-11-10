from tkinter import *

root = Tk()
e = Entry(root, width=50, bg="yellow", fg="red")
e.pack()
e.insert(0, "Enter Your Name")


def myclick():
    myLabel = Label(root, text="Hello " + e.get(), fg="green")
    myLabel.pack()


a = Button(
    root,
    text="Click For Magic",
    padx=10,
    pady=10,
    command=myclick,
    fg="yellow",
    bg="red",
)
a.pack()
root.mainloop()

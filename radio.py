from tkinter import *

# from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Deepesh")
# root.iconbitmap("C:/Users/Deepesh/Desktop/image.jpg")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    messagebox.showinfo("done that", "Still ok with that")


def popup1():
    messagebox.showwarning("done that", "Still ok with that")


def popup2():
    messagebox.showerror("done that", "Still ok with that")


def popup3():
    messagebox.askquestion("done that", "Still ok with that")


def popup4():
    messagebox.askokcancel("done that", "Still ok with that")


def popup5():
    a = messagebox.askyesno("done that", "Still ok with that")
    print(a)


Button(root, text="Popup", command=popup).pack()
Button(root, text="Popup1", command=popup1).pack()
Button(root, text="Popup2", command=popup2).pack()
Button(root, text="Popup3", command=popup3).pack()
Button(root, text="Popup4", command=popup4).pack()
Button(root, text="Popup5", command=popup5).pack()


root.mainloop()

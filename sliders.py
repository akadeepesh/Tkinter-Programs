from tkinter import *

root = Tk()
root.title("Deepesh")
root.geometry("400x400")


def fix():
    root.geometry("400x400")


def new():
    def slide(ok):
        root.geometry(str(hor.get()) + "x" + str(ver.get()))

    root2 = Tk()
    ver = Scale(root2, from_=0, to=1000, command=slide)
    ver.pack(anchor=E)
    button = Button(root2, text="Fix", command=fix).pack()
    button2 = Button(root2, text="Quit", command=root2.destroy).pack()
    hor = Scale(root2, from_=0, to=1000, orient=HORIZONTAL, command=slide)
    hor.pack(anchor=SW, side="bottom")


btn = Button(root, text="Adjust From Here", command=new).pack()

root.mainloop()

from tkinter import *
import time

tk = Tk()
tk.title("Timer")
tk.configure(bg="cyan")
tk.overrideredirect(True)


def clock():
    t = time.strftime("%I:%M:%S", time.localtime())
    if t != "":
        label1.config(text=t, font="times 25", bg="cyan")
    tk.after(100, clock)


label1 = Label(tk, justify="center")
label1.pack()
b = Button(tk, text="Exit", fg="red", bg="cyan", command=tk.destroy).pack()
clock()
tk.mainloop()

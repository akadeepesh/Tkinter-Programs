from tkinter import *

# from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Deepesh")
# root.iconbitmap("C:/Users/Deepesh/Desktop/image.jpg")

root.filename = filedialog.askopenfilename(
    initialdir="C:/Users/Deepesh/Desktop/Feedbacks", title="Select Any Feedback"
)
lab = Label(root, text=root.filename).pack()

root.mainloop()

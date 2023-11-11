from tkinter import *
root = Tk()
root.title("MAKE YOUR OWN WINDOW")
root.geometry("500x500+433+110")
root.overrideredirect(True)
Button(root,text="close",command=root.destroy).pack(side="bottom",anchor="se")
def window():
	root1=Tk()
	def conf():
		c=Entry(root)
		c.pack()
		c.insert(0,"BACKGROUND COLOUR")
		e=Entry(root)
		e.pack()
		e.insert(0,"Title")
		f=Entry(root,width=20)
		f.pack()
		f.insert(0,"Size: Horizontal x vertical")
		def but():
			h=Entry(root)
			h.pack()
			h.insert(0,"Title Of Button")
			o=Entry(root)
			o.pack()
			o.insert(0,"BACKGROUND COLOUR")
			p=Entry(root)
			p.pack()
			p.insert(0,"Text COLOUR")

			def lab():
				n=Entry(root)
				n.pack()
				n.insert(0,"Text")
				k=Entry(root)
				k.pack()
				k.insert(0,"BACKGROUND COLOUR")
				l=Entry(root)
				l.pack()
				l.insert(0,"Text COLOUR")
				def lc():
					Label(root1,text=n.get(),bg=k.get(),fg=l.get()).pack()
				m=Button(root,text="ok",command=lc)
				m.pack()
			def tit():
				Button(root1,text=h.get(),bg=o.get(),fg=p.get(),command=root1.destroy).pack()
				j=Button(root,text="Create Lable or text",command=lab)
				j.pack()
			i=Button(root,text="ok",command=tit)
			i.pack()		
		def get():
			root1.configure(bg=c.get())
			root1.title(e.get())
			root1.geometry(f.get())
			g=Button(root,text="Create Button",command=but)
			g.pack()

			
		d=Button(root,text="ok",command=get)
		d.pack()
	b=Button(root,text="Configure Window",command=conf)	
	b.place(x=10,y=10)

a=Button(root,text="Create Window",command=window)
a.place(x=10,y=10)

root.mainloop()

from cProfile import label
from tkinter import *

root = Tk()

text2 = Label(root, text="let's start")
text = Label(root, text="hello")

text2.grid(row=0,column=0)
text.grid(row=0,column=0)

root.mainloop()


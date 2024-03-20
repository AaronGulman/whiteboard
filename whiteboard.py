from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as Ttk

root = Tk()
root.title("Whiteboard")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

#icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)



color_box=PhotoImage(file="color section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)



root.mainloop()


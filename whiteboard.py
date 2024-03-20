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


colors=Canvas(root,bg="#ffffff", width=78,height=420,bd=0)
colors.place(x=25,y=60)

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f5").place(x=38,y=390)

def display_pallete():
        id = colors.create_rectangle((10,10,30,30),fill="#000")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#000'))
        
        id = colors.create_rectangle((10,40,30,60),fill="#CFCFCF")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#CFCFCF'))
        
        id = colors.create_rectangle((10,70,30,90),fill="#7C2E1E")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#7C2E1E'))
        
        id = colors.create_rectangle((10,100,30,120),fill="#FF0000")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#FF0000'))

        id = colors.create_rectangle((10,130,30,150),fill="#FF5D00")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#FF5D00'))

        id = colors.create_rectangle((10,160,30,180),fill="#FFF700")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#FFF700'))
        
        id = colors.create_rectangle((10,190,30,210),fill="#3AFF00")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#3AFF00'))
        
        id = colors.create_rectangle((10,220,30,240),fill="#0051FF")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#0051FF'))
        
        id = colors.create_rectangle((10,250,30,270),fill="#8B00FF")
        colors.tag_bind(id,"Button-1",lambda x: show_color('#8B00FF'))
        
display_pallete()

canvas = Canvas(root,width=930,height=500,background="#fff",cursor="hand2")
canvas.place(x=120,y=10)


canvas.bind('<Button-1>')
canvas.bind('<B1-Motion>')






root.mainloop()


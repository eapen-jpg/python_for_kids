from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_image = PhotoImage(file='d:\\giphy.gif')
import time
from tkinter import *
tk = Tk()
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=my_image)
for x in range(0, 60):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.5)


from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
def triangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(width)
    y2 = random.randrange(height)
    x3 = random.randrange(width)
    y3 = random.randrange(height)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="black")
    
for x in range(0, 50):
    triangle(400, 400)

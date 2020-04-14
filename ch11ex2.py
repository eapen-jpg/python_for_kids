import turtle
t = turtle.Pen()
def octa(size, fill = False, color = (0,0,0)):
    if fill == True:
        t.begin_fill()
    for x in range(1,9):
        t.forward(size)
        t.right(45)
    if fill == True:
        t.end_fill()

octa(100, True, (0,0,0))

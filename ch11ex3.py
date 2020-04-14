import turtle
t = turtle.Pen()
def drawstar(size, points):
    n = points
    angle = 360-(170+((180*(n-2))/n))
    for x in range(0, points):
       t.forward(size)
       t.left(170)
       t.forward(size)
       t.right(180)
       t.left(angle)
drawstar(100, 9)
t.reset()
drawstar(100, 8)
t.reset()
drawstar(100, 7)
t.reset()
drawstar(100, 6)
t.reset()
drawstar(100, 5)
t.reset()
drawstar(100, 4)
 

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")
alex.speed(9)

sidesize = 20
for i in range(5):
    sidesize = sidesize + 20
    drawSquare(alex,sidesize)
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
    
wn.exitonclick()


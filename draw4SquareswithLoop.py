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
alex.penup()
alex.goto(-100,20)
alex.pendown()

for i in range(5):
    drawSquare(alex,20)
    alex.penup()
    alex.forward(40)
    alex.pendown()
    
wn.exitonclick()

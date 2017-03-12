import turtle
wn = turtle.Screen()

star = turtle.Turtle()
star.speed(0)
star.up()
star.goto(-25,40)
star.down()

star.right(36)

def drawStar():
    for i in range(5):
        star.left(144)
        star.forward(100)

for i in range (5):
    #star.up()
    star.forward(120)
    star.right(144)
    #star.down()    
    drawStar()

wn.exitonclick()



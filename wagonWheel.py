import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

def draw_line(length, angle):
    mike = turtle.Turtle()
    mike.speed(0)
    mike.shape("turtle")
    mike.color('blue')
    mike.left(angle)
    mike.forward(length/2)
    mike.left(90)
    mike.up()
    mike.forward(length/2)
    mike.left(180)
    mike.down()
    mike.forward(length)
    mike.up()
    mike.backward(length/2)
    mike.down()
    mike.right(90)
    mike.forward(length/2)
    mike.right(180)
    
def draw_star(nlines):
    for angle in range(0,360, int(360/nlines)):
        draw_line(200,angle)
 

draw_star (20)


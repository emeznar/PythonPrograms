import turtle
wn = turtle.Screen()
triangle = turtle.Turtle()
triangle.color("grey")    
for i in (0,1,3):
    triangle.forward(150)
    triangle.left(360/3)
    
    
square = turtle.Turtle()
square.color("blue")    
for i in (0,1,2,3):
    square.forward(25)
    square.left(90)
    
hexa = turtle.Turtle()
hexa.color("red")    
for i in range(6):
    hexa.forward(50)
    hexa.left(360/6)

octag = turtle.Turtle()
octag.color("green")    
for i in range(8):
    octag.forward(75)
    octag.left(360/8)

    

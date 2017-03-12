import turtle
wn = turtle.Screen()

sides = int(input("How many sides does your figure have?"))
distance = int(input("How long is each side?"))
color = input("What color is your turtle?")
fill = input("What color should it be filled with")

alex = turtle.Turtle()
alex.color(color)
alex.fillcolor(fill)
for i in range(sides):
    alex.forward(distance)
    alex.left(360/(sides))

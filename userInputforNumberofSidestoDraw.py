import turtle

wn = turtle.Screen()

spider = turtle.Turtle()
spider.shape("turtle")
spider.speed(9)

n = int(input("How many legs do you have? "))
angle = 360 / n

for i in range(n):
    # draw the leg
    spider.right(angle)
    spider.forward(65)
    spider.stamp()

    # go back to the middle and turn back around
    spider.right(180)
    spider.forward(65)
    spider.right(180)

spider.shape("circle")

wn.exitonclick()


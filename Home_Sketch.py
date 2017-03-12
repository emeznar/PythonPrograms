import turtle

wn = turtle.Screen()

eric = turtle.Turtle()
eric.shape("arrow")
eric.resizemode("user")


#function to draw a house and return a vector string
def draw_house():
    turn = input("Enter a direction (U,D,L,R) ")
    angle = 0
    #Need to add angle at some point - if v then u/d then l/r
    if turn == "u" or turn =="U":
        angle = 90
        eric.left(angle)
    elif turn == "d" or turn =="D":
        angle = 270
        eric.left(angle)
    elif turn == "l" or turn =="L":
        angle = 180
        eric.left(angle)
    elif turn == "r" or turn =="R":
        angle = 0
        eric.right(angle)
    else:
        print("Please enter a valid direction ")
    distance = int(input("How long is the side "))


    eric.forward(distance/2)
    eric.write(str(distance), align="right")
    eric.forward(distance/2)
    eric.left(0-angle)

    vectorstring =  (turn.upper() + str(distance))
    vectorstring = [vectorstring]
    
    newvectorstring.append(vectorstring)
      

    
    #add code for if = 0,0 don't ask question below:
    more=input("Ready to enter the next side (y or n)? ")
    if more == "y":
        draw_house()
    newnewvectorstring = str(newvectorstring)
    newnewvectorstring = newnewvectorstring.replace("'","").replace("[","").replace("]","")
    return str(newnewvectorstring)
        
#Greet user - add Function that asks if they want to draw
#a main or addition - then prints out each vector string starting
#with main then additions in order


user_start = input("Do you want to draw a main?(y or n) ")
if user_start == "y" or user_start == "Y":
    newvectorstring = []
    mainvector = ""
    additionvector = ""
    eric.goto(0,0)
    mainvector = draw_house()

addition_start = input("Do you want to draw and addition? (y or n) ")
if addition_start == "y" or addition_start == "Y":
    eric.penup()
    newvectorstring = []
    eric.goto(0,0)
    up_down = input("Is the starting point up or down? (u or d)")
    user_distanceud = int(input("What distance? "))
    if up_down == "u" or up_down == "U" :
        angle = 90
        eric.left(angle)
        eric.forward(user_distanceud)
        eric.left(0-angle)
    elif up_down == "d" or up_down =="D":
        angle = 270
        eric.left(angle)
        eric.forward(user_distanceud)
        eric.left(0-angle)
    right_left = input("Is the start point left or rignt? (l or r)")
    user_distancelr = int(input("What distance? "))
    if right_left == "l" or right_left =="L":
        angle = 180
        eric.left(angle)
        eric.forward(user_distancelr)
        eric.left(0-angle)
    elif right_left == "r" or right_left =="R":
        angle = 0
        eric.right(angle)
        eric.forward(user_distancelr)
        eric.left(0-angle)

    eric.pendown()
    additionvector = draw_house()
        
           
            
print ("A0C, " + mainvector)
print ("A01, " + additionvector)
    
wn.exitonclick()    

#TODO - add function that fills area when polygon is completed
#TODO - add function to auto resize distance and turtle image - or fills the page
#TODO  - add ability to draw angles

#TODO - Add buttons for direction (maybe on google app engine - github site with buttons in HTML)
#TODO - include buttons for going back (erase last input)
#TODO - include button for completing vector and/or starting addition (to include multiple additions)



      

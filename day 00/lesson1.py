from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(100)
width(10)
color("blue")

forward(200)
left(90)



forward(200)
left(90)

forward(200)
left(90)



forward(200)
left(90)
#end of square

# drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#paint a window
penup()
goto(200,120)
pendown()
right(60)
forward(60)
right(90)
forward(50)
right(90)
forward(60)

exitonclick()
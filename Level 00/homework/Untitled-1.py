from turtle import *
color("black")
speed(20)
width(2)




forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

color("red")
penup()
goto(200,200)
pendown()

begin_fill()

right(90)
forward(200)
right(120)
forward(200)

end_fill()

color("black")
penup()
goto(70,130)
pendown()


left(120)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
left(90)
forward(20)
left(90)
forward(15)
left(90)
forward(40)


penup()
goto(0,0)
pendown()


forward(70)
color("yellow")
begin_fill()
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
end_fill()

exitonclick()
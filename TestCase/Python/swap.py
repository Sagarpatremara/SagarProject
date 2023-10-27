# a=4
# b=5
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# a=8
# for i in range(a):
#     print(i*"*")



# a='2'
# b="2"
# print(a+b)

# import turtle
# from time import sleep
#
# # Part 1 : Initialize the module
# t = turtle.Turtle()
# t.speed(4)
# turtle.bgcolor("white")
# t.color("white")
# turtle.title('Netflix Logo')
#
# # Part 2 : Drawing the black background
# t.up()
# t.goto(-80, 50)
# t.down()
# t.fillcolor("black")
# t.begin_fill()
#
# t.forward(200)
# t.setheading(270)
# s = 360
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)
#
# t.forward(180)
# s = 270
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)
#
# t.forward(200)
# s = 180
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)
#
# t.forward(180)
# s = 90
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)
# t.forward(30)
# t.end_fill()
#
# # Part 3 : Drawing the N shape
# t.up()
# t.color("black")
# t.setheading(270)
# t.forward(240)
# t.setheading(0)
# t.down()
# t.color("red")
# t.fillcolor("#E50914")
# t.begin_fill()
# t.forward(30)
# t.setheading(90)
# t.forward(180)
# t.setheading(180)
# t.forward(30)
# t.setheading(270)
# t.forward(180)
# t.end_fill()
# t.setheading(0)
# t.up()
# t.forward(75)
# t.down()
# t.color("red")
# t.fillcolor("#E50914")
# t.begin_fill()
# t.forward(30)
# t.setheading(90)
# t.forward(180)
# t.setheading(180)
# t.forward(30)
# t.setheading(270)
# t.forward(180)
# t.end_fill()
# t.color("red")
# t.fillcolor("red")
# t.begin_fill()
# t.setheading(113)
# t.forward(195)
# t.setheading(0)
# t.forward(31)
# t.setheading(293)
# t.forward(196)
# t.end_fill()
# t.hideturtle()
#
# sleep(10)




from turtle import *

speed(10)
Screen().bgcolor("black")
penup()
goto(-20,-20)
pendown()
color("white")
begin_fill()
circle(150)
end_fill()

penup()
goto(-100,10)
pendown()
begin_fill()
right(165)
forward(100)
right(130)
forward(100)
end_fill()

color("green")
penup()
goto(-30,-10)
pendown()
begin_fill()
right(70)
circle(140)
end_fill()

color("green")
penup()
goto(-100,20)
pendown()
begin_fill()
right(160)
forward(80)
right(130)
forward(90)
end_fill()

color("white")
penup()
goto(40,40)
pendown()
begin_fill()
right(60)
circle(140,-90)
right(30)
circle(50,-50)
left(90)
forward(40)
right(90)
forward(20)
penup()
goto(40,40)
pendown()
right(150)
circle(50,50)
left(80)
forward(40)
left(90)
forward(20)
left(98.5)
circle(95,-90)
end_fill()

color("green")
width(2)
begin_fill()
circle(92,90)
end_fill()
left(135)
width(5)

penup()
forward(10)
pendown()
forward(60)

penup()
goto(-150,-100)
pendown()

hideturtle()

done()
from turtle import *
import math 

title("Isosceles triangle circle")
setup(1000, 1000)
setworldcoordinates(-500, -500, 500, 500)
hideturtle()
tracer(0, 0)

def isosceletriangle(x, y, width, height, direction, color):
    up()
    goto(x, y)
    seth(direction-90)
    fd(width/2)
    #bottom right corner
    p1x, p1y = xcor(), ycor()
    back(width)
    #bottom left corner    
    p2x, p2y = xcor(), ycor()
    #top corn of triangle
    goto(x, y)
    seth(direction)
    fd(height)
    p3x, p3y = xcor(), ycor()

    #draw and fill triangle
    goto(p1x, p1y)
    down()
    fillcolor(color)
    begin_fill()
    goto(p2x, p2y)
    goto(p3x, p3y)
    goto(p1x, p1y)
    end_fill()

n = 12
r = 300
width = 2*r*math.sin(math.radians(180/n))
height = 200
for j in range(n):
    isosceletriangle(r*math.cos(math.radians(180/n))*math.radians(180/n)*math.cos(math.radians(j*360/n)))
                    
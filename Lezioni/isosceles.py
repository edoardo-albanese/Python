from turtle import *
import math
title("isosceles triangle circle")
setup(1000,1000)
setworldcoordinates(-500,-500,500,500)
hideturtle()
tracer(0,0)

def isoscelestriangle(x, y, width, height, direction, color)
    up()
    goto(x, y)
    seth(direction-90)
    fd(width/2)
    #bottom right corner
    p1x, p1y = xcor(), ycor()
    back (width) 
    #bottom left corner
    p2x, d    
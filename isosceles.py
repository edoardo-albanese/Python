from turtle import *
import math

setup(600,600)
tracer(0,0)
setworldcoordinates(-500, -500, 500, 500)

def triangle(base, height, x, y, dir, color):
    up()
    goto(x,y)
    seth(dir + 90)
    fd(base / 2)
    p1x, p1y = xcor(), ycor()
    back(base)
    p2x, p2y = xcor(), ycor()
    goto(x,y)
    seth(dir)
    fd(height)
    p3x, p3y = xcor(), ycor()
    
    goto(p1x, p1y)
    down()
    fillcolor(color)
    begin_fill()
    goto(p2x, p2y)
    goto(p3x, p3y)
    goto(p1x, p1y)
    end_fill()


def circle(n, r):
    width = 2*r+math.sin(math.radians(180/n))
    height = 100
    for i in range(n):
        triangle(width, height, )
    pass



circle(12,200)
done()
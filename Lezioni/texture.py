import turtle
import random

turt = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0,1.0)

rows = 2
columns = 2
padding = 50
side_coefficient = 1 + 2/3

width = screen.window_width()
height = screen.window_height()

def polygon(sides : int, size : int):
    turt.pendown()
    #turt.setheading(random.randint(0,30))
    for i in range(sides):
        turt.forward(size)
        turt.right(360/sides)
    turt.penup()

def draw_texture():
    for i in range(rows):
        ypos = height/2 - (height/rows * i)
        for j in range(columns):
            sides = random.randint(3, 10)
            side_lenghth = (width/columns) / sides * side_coefficient - padding
            xpos = - width/2 + width/columns * j
            turt.goto(xpos, ypos)
            polygon(sides, side_lenghth)


turt.penup()
draw_texture()

turtle.done()
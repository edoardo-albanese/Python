import turtle
import random

turt = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0,1.0)

rows = 5
columns = 5
padding = 2

width = screen.window_width()
height = screen.window_height()

def polygon(sides : int, size : int):
    turt.pendown()
    turt.setheading(random.randint(0,360))
    for i in range(sides):
        turt.forward(size)
        turt.right(360/sides)
    turt.penup()

def draw_texture():
    for i in range(columns):
        ypos = (height / columns) * i
        for j in range(rows):
            xpos = (width/rows) * j
            sides = random.randint(3, 20)
            side_lenghth = ((width/rows) - padding) / sides
            turt.goto(xpos, ypos)
            polygon(sides, side_lenghth)


turt.penup()
draw_texture()

turtle.done()
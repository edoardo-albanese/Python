import turtle
import random

screen = turtle.Screen()
screen.setup(420, 380)
gurt = turtle.Turtle()

minside = 10
maxside = 200
amount = random.randint(0, 20)

def rhombus(posx : int, posy : int):
    gurt.goto(posx, posy)
    gurt.pendown()
    gurt.setheading(random.randint(0, 360))
    side_a = random.randint(minside, maxside)
    side_b = random.randint(minside, maxside)
    sides = [side_a, side_b]
    angle_a = random.randint(10, 170)
    angle_b = 180 - angle_a
    angles = [angle_a, angle_b]
    for i in range(4):
        gurt.forward(sides[i % 2])
        gurt.right(angles[i % 2])
    gurt.penup()

gurt.penup()
for i in range(amount):
    posx = random.randint(0, int(screen.xscale))
    posy = random.randint(0, int(screen.yscale))
    print (posx, posy)
    rhombus(posx, posy)


turtle.done()
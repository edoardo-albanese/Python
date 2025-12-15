import turtle

screen = turtle.Screen()
screen.setup(670, 420)
screen.title("Esperimento Classi")
screen.colormode(255)
screen.bgcolor(
    (53, 12, 67)
)

gurt = turtle.Turtle("turtle")
gurt.color("Yellow")

for i in range(4):
    gurt.forward(100)
    gurt.right(30)

input("Enter to end")
import turtle as t
import random

# colors = [
#     "gold",
#     "orchid",
#     "dodgerblue",
#     "mediumseagreen",
#     "salmon",
#     "slateblue",
#     "tomato",
#     "turquoise",
#     "darkorange",
#     "deeppink"
# ]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]

tim = t.Turtle()
t.colormode(255)
tim.pensize(10)
tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()


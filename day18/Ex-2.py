import turtle as t
import random

colors = [
    "gold",
    "orchid",
    "dodgerblue",
    "mediumseagreen",
    "salmon",
    "slateblue",
    "tomato",
    "turquoise",
    "darkorange",
    "deeppink"
]

tim = t.Turtle()

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides  
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()

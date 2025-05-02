# import colorgram

# rgb_colors = []

# colors = colorgram.extract('120123_r21786_g2048.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)


# [(249, 248, 248), (232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

import turtle as t
import random

DOT_SIZE = 20
DOTS_PER_ROW = 10
NUMBER_OF_DOTS = DOTS_PER_ROW * DOTS_PER_ROW
SPACING = 50
START_X = - (DOTS_PER_ROW - 1) * SPACING / 2
START_Y = - (DOTS_PER_ROW - 1) * SPACING / 2

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.penup()
# tim.speed("fastest") # Removed or slowed down for visibility
tim.speed("normal")   # Set to a visible speed (e.g., "normal", "slow", or a number 1-10)

screen = t.Screen()
# screen.tracer(0) # Removed to show drawing process

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.goto(START_X, START_Y)

for row in range(DOTS_PER_ROW):
    current_y = START_Y + row * SPACING
    tim.goto(START_X, current_y)
    for _ in range(DOTS_PER_ROW):
        tim.dot(DOT_SIZE, random_color())
        tim.forward(SPACING)

# screen.update() # Removed as tracer is off, updates happen automatically
screen.exitonclick()
# Building a Snake Game
# -create a snake body, three squares all linedup
# -move the snake
# -control the snake with up,down,ruight,left key
# -detect collision with food# 
# -create a scoreboard 
# -detect collision with wall and tail
# -make the snake faster

from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
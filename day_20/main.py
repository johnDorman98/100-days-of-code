# Inital setup for snake game using turtle.

from turtle import Turtle, Screen

# Setting up the screen for the game.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Creating snakes starting body parts.
snake_body_parts = []

for _ in range(3):
    print(_)
    snake_part = Turtle("square")
    snake_part.color("white")
    snake_part.penup()
    
    # Dynamically getting a x position starting at 0 - (-21 * 0 = 0).
    x_position = -21 * len(snake_body_parts)
    snake_part.goto(x=x_position, y=0)
        
    snake_body_parts.append(snake_part)

screen.exitonclick()
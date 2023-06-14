# Inital setup for snake game using turtle.
from turtle import Turtle, Screen
import time

# Setting up the screen for the game.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating snakes starting body parts.
snake_body_parts = []

for _ in range(3):
    print(_)
    snake_part = Turtle("square")
    snake_part.color("white")
    snake_part.penup()
    
    # Dynamically getting a x position starting at 0 - (-21 * 0 = 0).
    x_position = -20 * len(snake_body_parts)
    snake_part.goto(x=x_position, y=0)
        
    snake_body_parts.append(snake_part)
    
# Continious game loop to be set to false on end conditions of game.
play_snake = True

while play_snake:
    # Updates the screen after each stage such as the snakes inital placement.
    screen.update()
    time.sleep(0.1)
    
    # Loops through a range based on the amount of snake parts.
    for snake_part_number in range(len(snake_body_parts)-1, 0, -1):
        # Getting the x and y locations of the next body part to link them.
        new_x = snake_body_parts[snake_part_number - 1].xcor()
        new_y = snake_body_parts[snake_part_number - 1].ycor()
        
        # Moves the snake part to the next parts locations, using the x and y above.
        snake_body_parts[snake_part_number].goto(new_x, new_y)
    
    # Sets the snakes head to control the snake as a whole.
    snake_head = snake_body_parts[0]
    snake_head.fd(20)
    snake_head.lt(90)
    
screen.exitonclick()
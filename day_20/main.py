# Inital setup for snake game using turtle.
from turtle import Screen
from snake import Snake
import time

# Setting up the screen for the game.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
    
# Continious game loop to be set to false on end conditions of game.
play_snake = True

while play_snake:
    # Updates the screen after each stage such as the snakes inital placement.
    screen.update()
    time.sleep(0.10)
    
    snake.move()
        
screen.exitonclick()
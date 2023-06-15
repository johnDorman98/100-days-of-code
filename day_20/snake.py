from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        
        self.snake_body_parts = []
        self.create_snake()
        self.snake_head = self.snake_body_parts[0]
    
    # Creating snakes starting body parts.
    def create_snake(self):
        for _ in range(3):
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            
            # Dynamically getting a x position starting at 0 - (-21 * 0 = 0).
            x_position = -20 * len(self.snake_body_parts)
            snake_part.goto(x=x_position, y=0)
                
            self.snake_body_parts.append(snake_part)
            
    def move(self):
        # Loops through a range based on the amount of snake parts.
        for snake_part_number in range(len(self.snake_body_parts)-1, 0, -1):
            # Getting the x and y locations of the next body part to link them.
            new_x = self.snake_body_parts[snake_part_number - 1].xcor()
            new_y = self.snake_body_parts[snake_part_number - 1].ycor()
            
            # Moves the snake part to the next parts locations, using the x and y above.
            self.snake_body_parts[snake_part_number].goto(new_x, new_y)
        
        # Sets the snakes head to control the snake as a whole.
        self.snake_head.fd(MOVE_DISTANCE)
        
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
        
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
        
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
        
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
# This is a program that uses the turtle module to creat a mini OOP based turtle racing game.
import random
from turtle import Turtle, Screen

# Starting values for use throughout the code.
start_race = False
screen = Screen() # Screen object
screen.setup(width=500, height=500)

user_bet = screen.textinput(title="Make your bets!", 
    prompt="Which turtle will with the race? Pick a color: ")

# Lists used to store turtle objects and possible colours.
turtle_colours = ["red", "blue", "green", "yellow", "purple", "orange"]
turtles = []

turtle_starting_y = -125

# Loops for each of the colours as a way to create turtle objects.
for turtle_number in range(len(turtle_colours)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(turtle_colours[turtle_number])
    
    # Places the turtle at the start line and updates the y for next turtle.
    turtle.goto(x=-225, y=turtle_starting_y)
    turtle_starting_y += 50
    turtles.append(turtle)

# Making sure the user has placed a bet.
if user_bet:
    start_race = True

# Loop until the race is over once the user has made thier bet.
while start_race:
    # For each of the turtle objest randomly move each one in a range of 0 - 10.
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        
        # Checks if a turtle has reached the finsh line and ends the game.
        if turtle.xcor() >= 225:
            start_race = False
            winning_colour = turtle.color()
            
            # Uses the colour of the winner to check if user was correct.
            if user_bet.lower() == winning_colour[0]:
                print(f"You were correct {winning_colour} has won the race!")
                exit()
            else:
                print("Sorry, better luck next time.")
                exit()

screen.exitonclick()
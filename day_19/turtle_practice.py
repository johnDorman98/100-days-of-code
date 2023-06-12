# Simple drawing game that uses key presses.

from turtle import Turtle, Screen

# W = forwards
# S = backwards
# A = left
# D = right
# C = clear

def forwards():
    turtle.fd(10)
    
def backwards():
    turtle.bk(10)
    
def left():
    turtle.lt(10)
    
def right():
    turtle.rt(10)

def clear():
    turtle.reset()

turtle = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
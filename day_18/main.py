import colorgram
from turtle import Turtle, Screen
import random

def extract_colors():
    colors = colorgram.extract("spots.jpeg", 2 * 32)

    rgb_colors = []

    for color in colors:
        rgb_extracted = color.rgb
        rgb_total = sum([rgb for rgb in rgb_extracted])

        if rgb_total < 680:
            rgb_colors.append(tuple(rgb_extracted))
    
    return rgb_colors


def draw_dots():
    screen.colormode(255)
    extracted_colors = extract_colors()
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    
    for y in range(10):
        turtle.goto(-200, -200 + (y * 50))
        for x in range(10):
            turtle.dot(20, random.choice(extracted_colors))
            turtle.forward(50)


turtle = Turtle()
screen = Screen()

draw_dots()

screen.exitonclick()

# Experimenting with the Turtle module.

from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("dodger blue")

screen.colormode(255)


# Challenge 1.
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# Challenge 2.
# for _ in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# Challenge 3.
# def random_color():
#     R = random.randrange(0, 255)
#     G = random.randrange(0, 255)
#     B = random.randrange(0, 255)
#     turtle.color(R, G, B)
    
# def draw_shape(number_sides):
#     angle = 360 / number_sides
#     random_color()

#     for _ in range(number_sides):
#         turtle.fd(100)
#         turtle.rt(angle)
    
# screen.colormode(255)

# for side in range(3, 11):
#     draw_shape(side)

# Challenge 4.
# def random_walk():
#     angles = [90, 180, 270, 360]
#     turtle.hideturtle()
#     turtle.pensize(15)
#     turtle.speed(0)
    
#     for _ in range(200):
#         random_color()
#         random_angle = random.choice(angles)
#         turtle.setheading(random_angle)
#         turtle.fd(25)
        

# def random_color():
#     R = random.randrange(0, 255)
#     G = random.randrange(0, 255)
#     B = random.randrange(0, 255)
#     turtle.color((R, G, B))
        

# screen.colormode(255)

# random_walk()

# Challenge 5.
# def draw_spirograph():
#     turtle.hideturtle()
#     turtle.speed(0)
#     for _ in range(0, 360, 5):
#         random_color()
#         turtle.setheading(_)
#         turtle.circle(100)


def draw_spirograph(gap_size):
    turtle.hideturtle()
    turtle.speed(0)
    
    for _ in range(int(360 / gap_size)):
        random_color()
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap_size)


def random_color():
    R = random.randrange(0, 255)
    G = random.randrange(0, 255)
    B = random.randrange(0, 255)
    turtle.color((R, G, B))


draw_spirograph(2.5)

screen.exitonclick()

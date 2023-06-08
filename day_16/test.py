# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# screen = Screen()
# print(screen.canvheight)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.penup()
# timmy.forward(100)

# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column(
    "Pokemon Name",
    [
        "Pikachu",
        "Squirtle",
        "Charmander"
    ]
)

table.add_column(
    "Type",
    [
        "Electric",
        "Water",
        "Fire"
    ]
)

table.align = "l"

print(table)

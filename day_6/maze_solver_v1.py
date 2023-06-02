def turn_right():
    turn_left()
    turn_left()
    turn_left()

counter = 0

while not at_goal():
    if right_is_clear() and counter < 3:
        turn_right()
        move()
        counter += 1
    elif front_is_clear():
        move()
    else:
        turn_left()
        counter = 0
        
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
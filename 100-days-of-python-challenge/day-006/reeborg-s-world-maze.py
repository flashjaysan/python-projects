# reeborg's world maze problem

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_to_first_wall():
    while front_is_clear():
        move()

  
def follow_right_walls():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()


def find_exit():
    move_to_first_wall()
    turn_left()
    follow_right_walls()


find_exit()

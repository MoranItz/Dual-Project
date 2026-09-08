
def init_soldier():
    global soldier
    soldier = {"x" : 0, "y" : 0, "status" : ""}

    return soldier

def get_new_coordinates(event_type):
    #TODO: return new soldier move coordinates
    pass

def move_player(coordinates):
    #TODO: move the player in the game field
    pass

def is_move_valid(coordinates):
    #TODO: check if the move exits the boundries of the game field
    pass

def player_touch_mine(coordinates):
    #TODO: return true if player interacts with mine in game field
    pass

def player_touch_flag(coordinates):
    #TODO: return true if player interacts with flag in game field
    pass
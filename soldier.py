import pygame

import consts
import game_field

soldier = {}

""" 
This function initiates the soldier dict
it has its x and y values which are the top left of the image coordinates.
The "img" key which holds the current state of the soldier.
And the "hitbox" key which holds a 2d list of all of the coordinates of the soldiers body/feet
"""
def init_soldier():
    global soldier

    soldier = {
        "x" : 0,
        "y" : 0,
        "img" : consts.SOLDIER_REGULAR_IMG,
        "hitbox" : get_hitboxes(),
    }

"""
Returns the x and y coordinates of the soldier as a tuple
"""
def get_coordinates():
    return soldier["x"], soldier["y"]

"""
This function moves the player in the direction given to it by the get_move_direction
function. it moves the player in the direction given and changes its hitboxes to move and also its
top left coordinate "x" and "y".
"""
def move_player(direction):
    if is_move_valid(soldier["x"]+direction[1], soldier["y"]+direction[0]):
        soldier["x"] += direction[1]
        soldier["y"] += direction[0]
        for index in range(len(soldier["hitbox"])):
            soldier["hitbox"][index][0] += direction[0]
            soldier["hitbox"][index][1] += direction[1]

"""
This function gets an event type and it returns the direction
the soldier needs to move based on the players pressed key
"""
def get_move_direction(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            return -1,0
        elif event.key == pygame.K_DOWN:
            return 1,0
        elif event.key == pygame.K_RIGHT:
            return 0,1
        elif event.key == pygame.K_LEFT:
            return 0,-1
    return 0,0

"""
This function is used to get the starting position hitboxes for the soldier at
the [0, 0] position.
"""
def get_hitboxes():
    hitboxes = []
    for row in range(4):
        for col in range(1, 3):
            hitboxes.append([row, col])

    return hitboxes

"""
This function checkes if a move exists the boundries of the game_field.
if it does it returns False, if not it returns True
"""
def is_move_valid(x, y):
    if consts.BOARD_COLS - 4 < x or x < 0:
        return False
    elif consts.BOARD_ROWS - 4 < y or y < 0:
        return False

    return True

"""
Function returns True weather the soldier feet hitboxes (last two inboxes in the array)
have collided with a mine on the map. Else it returns False
"""
def player_touch_mine():
    index_legs = [soldier["hitbox"][-1], soldier["hitbox"][-2]]
    for leg in index_legs:
        if game_field.game_field[leg[0]][leg[1]] == consts.MINE_IMG:
            soldier["img"] = consts.SOLDIER_INJURED_IMG
            return True

    return False

"""
This function returns True weather the soldier body hitboxes (every hitbox except
the two last ones) has collided with the flag at the bottom right of the map.
"""
def player_touch_flag():
    for i in range(len(soldier["hitbox"]) - 2):
        index = soldier["hitbox"][i][0], soldier["hitbox"][i][1]
        if game_field.game_field[index[0]][index[1]] == consts.FLAG_IMG:
            return True

    return False


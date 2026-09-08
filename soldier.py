import pygame

import consts
import game_field

STEP = 1
X_COORDINATES = 0
Y_COORDINATES = 1

soldier = {}

""" 
    This function initiates the global soldier (player) object
    it returns the object initiated with the [x, y] coordinates as [0, 0]
    and his status (image) as the default soldier image
"""
def init_soldier():
    global soldier # creates global soldier object
    soldier = {"x" : 0, "y" : 0, "status" : ""}

    return soldier

"""
    This function gets the click the user pressed and returns the new
    soldier coordinates based on the click. (up, down, right, left)
    if a click is not one of those, the function just returns the current coordinates
"""
def get_new_coordinates(event_type):
    new_coordinates = ()

    if event_type == pygame.K_UP: # when player presses up key
        new_coordinates = soldier["x"], soldier["y"] + STEP

    elif event_type == pygame.K_DOWN: # when player presses down key
        new_coordinates = soldier["x"], soldier["y"] - STEP

    elif event_type == pygame.K_RIGHT: # when player presses right key
        new_coordinates = soldier["x"] + STEP, soldier["y"]

    elif event_type == pygame.K_LEFT: # when player presses left key
        new_coordinates = soldier["x"] - STEP, soldier["y"]

    if is_move_valid(new_coordinates):
        return new_coordinates

    return soldier["x"], soldier["y"]

"""
    This function gets the new supposed coordinates for the new soldier move.
    if the new coordinates exceed the boundries of the game_field the function
    returns False, else the function returns True.
"""
def is_move_valid(coordinates):
    if coordinates[X_COORDINATES] < 0 or coordinates[X_COORDINATES] >= consts.BOARD_COLS:
        return False
    if coordinates[Y_COORDINATES] < 0 or coordinates[Y_COORDINATES] >= consts.BOARD_ROWS:
        return False

    return True

"""
    This function gets the new coordinates after the checks if the move is valid
    and it updates the soldiers coordinates to the new coordinates.
"""
def move_player(coordinates):
    soldier["x"] = coordinates[X_COORDINATES]
    soldier["y"] = coordinates[Y_COORDINATES]

"""
    This function recieves the coordinates of the player and wants to check if there
    is any collision with the player and any mine on the map.
"""
def player_touch_mine(coordinates):
    for y in range(len(game_field.game_field)): # reversed y and x because of how 2d lists work
        for x in range(y):
            # if the coordinates of the soldier are the same as any mine on the map
            if game_field.game_field[y][x] == consts.MINE_ING and coordinates[X_COORDINATES] == x and coordinates[Y_COORDINATES] == y:
                return True
    return False

"""
    This function recieves the coordinates of the player and wants to check if there
    is any collision with the player and the flag. It returns True if it does and False if not
"""
def player_touch_flag(coordinates):
    # if the coordinates of the soldier are the same as the flag
    if coordinates[X_COORDINATES] == consts.BOARD_COLS - 1 and coordinates[Y_COORDINATES] == consts.BOARD_ROWS - 1:
        return True
    return False
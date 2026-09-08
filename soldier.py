import pygame

import consts
import game_field

soldier = {}

""" 
    This function initiates the global soldier (player) object
    it returns the object initiated with the [x, y] coordinates as [0, 0]
    and his status (image) as the default soldier image
"""
def init_soldier():
    global soldier # creates global soldier object
    soldier = {"x" : 0, "y" : 0, "status" : consts.SOLDIER_REGULAR_IMG}

    return soldier

"""
    This function gets the click the user pressed and returns the new
    soldier coordinates based on the click. (up, down, right, left)
    if a click is not one of those, the function just returns the current coordinates
"""
def get_new_coordinates(event):
    new_coordinates = ()

    if event.key == pygame.K_UP: # when player presses up key
        new_coordinates = soldier["x"], soldier["y"] - consts.STEP

    elif event.key == pygame.K_DOWN: # when player presses down key
        new_coordinates = soldier["x"], soldier["y"] + consts.STEP

    elif event.key == pygame.K_RIGHT: # when player presses right key
        print(soldier["x"])
        new_coordinates = soldier["x"] + consts.STEP, soldier["y"]

    elif event.key == pygame.K_LEFT: # when player presses left key
        new_coordinates = soldier["x"] - consts.STEP, soldier["y"]

    if is_move_valid(new_coordinates):
        if new_coordinates == ():
            return 0, 0
        return new_coordinates

    return soldier["x"], soldier["y"]

"""
    This function gets the new supposed coordinates for the new soldier move.
    if the new coordinates exceed the boundries of the game_field the function
    returns False, else the function returns True.
"""
def is_move_valid(coordinates):
    if coordinates == ():
        return True
    if (coordinates[consts.X_COORDINATES_INDEX] < 0 or
            coordinates[consts.X_COORDINATES_INDEX] > consts.BOARD_COLS - consts.SOLDIER_FEET_ROWS):
        return False
    if (coordinates[consts.Y_COORDINATES_INDEX] < 0 or
            coordinates[consts.Y_COORDINATES_INDEX] > consts.BOARD_ROWS - consts.SOLDIER_BODY_ROWS):
        return False

    return True

"""
    This function gets the new coordinates after the checks if the move is valid
    and it updates the soldiers coordinates to the new coordinates.
"""
def move_player(coordinates):
    soldier["x"] = coordinates[consts.X_COORDINATES_INDEX]
    soldier["y"] = coordinates[consts.Y_COORDINATES_INDEX]

"""
    This function recieves the coordinates of the player and wants to check if there
    is any collision with the player and any mine on the map.
"""
def player_touch_mine(coordinates):
    for y in range(len(game_field.game_field)): # reversed y and x because of how 2d lists work
        for x in range(y):
            # if the coordinates of the soldier are the same as any mine on the map
            if (game_field.game_field[y][x] == consts.MINE_IMG and
                    coordinates[consts.X_COORDINATES_INDEX] == x and
                    coordinates[consts.Y_COORDINATES_INDEX] == y):
                return True
            # if the coordinates of the soldier are the same as any mine on the map (for the second foot)
            elif (game_field.game_field[y][x] == consts.MINE_IMG and
                  coordinates[consts.X_COORDINATES_INDEX] + consts.SOLDIER_FEET_ROWS == x and
                  coordinates[consts.Y_COORDINATES_INDEX] == y):
                return True
    return False

"""
    This function recieves the coordinates of the player and wants to check if there
    is any collision with the player and the flag. It returns True if it does and False if not
"""
def player_touch_flag(coordinates):
    # if the coordinates of the soldier are the same as the flag
    if (coordinates[consts.X_COORDINATES_INDEX] == consts.BOARD_COLS - 1 and
            coordinates[consts.Y_COORDINATES_INDEX] == consts.BOARD_ROWS - 1):
        return True

    elif (coordinates[consts.X_COORDINATES_INDEX] + consts.SOLDIER_FEET_ROWS == consts.BOARD_COLS - 1 and
            coordinates[consts.Y_COORDINATES_INDEX] == consts.BOARD_ROWS - 1):
        return True

    return False
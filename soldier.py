import consts
import game_field
import pygame

soldier = {}

def init_soldier():
    global soldier

    soldier = {
        "x" : 0,
        "y" : 0,
        "img" : consts.SOLDIER_REGULAR_IMG,
        "hitbox" : get_hitboxes(),
        "night_mode" : False
    }

def get_coordinates():
    return soldier["x"], soldier["y"]

def move_player(direction):
    if is_move_valid(soldier["x"]+direction[1], soldier["y"]+direction[0]):
        soldier["x"] += direction[1]
        soldier["y"] += direction[0]
        for index in range(len(soldier["hitbox"])):
            soldier["hitbox"][index][0] += direction[0]
            soldier["hitbox"][index][1] += direction[1]

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


def get_hitboxes():
    hitboxes = []
    for row in range(4):
        for col in range(1, 3):
            hitboxes.append([row, col])

    return hitboxes

def is_move_valid(x, y):
    if consts.BOARD_COLS - 4 < x or x < 0:
        return False
    elif consts.BOARD_ROWS - 4 < y or y < 0:
        return False

    return True

def player_touch_mine():
    index_legs = [soldier["hitbox"][-1], soldier["hitbox"][-2]]
    for leg in index_legs:
        if game_field.game_field[leg[0]][leg[1]] == consts.MINE_IMG:
            soldier["img"] = consts.SOLDIER_INJURED_IMG
            return True

    return False

def player_touch_flag():
    for i in range(len(soldier["hitbox"]) - 2):
        index = soldier["hitbox"][i][0], soldier["hitbox"][i][1]
        if game_field.game_field[index[0]][index[1]] == consts.FLAG_IMG:
            return True

    return False


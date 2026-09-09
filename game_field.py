import pygame
import random
import numpy

import consts


game_field = []

def init_game_field():
    global  game_field

    game_field = generate_random_field()
    grid_copy = copy_grid(game_field)
    dfs(grid_copy, 0, 0)
    while not is_field_valid(grid_copy):
        game_field = generate_random_field()
        grid_copy = copy_grid(game_field)
        dfs(grid_copy,0 ,0)



def generate_random_field():
    field = []
    generate_empty_field(field)
    place_flag(field)
    place_random_mines(field)

    return field

def place_random_mines(field):
    mines_indexes = []
    mines_place = 0

    while mines_place <= 20:
        indexs = [random.randint(0, consts.BOARD_ROWS - 1), random.randint(0, consts.BOARD_COLS - 1)]


        if is_place_ok(field, indexs) and indexs not in mines_indexes:
            for i in range(3):
                field[indexs[0]][indexs[1]+i] = consts.MINE_IMG
                mines_indexes.append([indexs[0], indexs[1]+i])
            mines_place += 1

def place_flag(field):
    for row in range(consts.BOARD_ROWS -3, consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS - 4, consts.BOARD_COLS):
            field[row][col] = consts.FLAG_IMG

def is_place_ok(field, indexes):
    if indexes[1] > consts.BOARD_COLS - 3:
        return False
    elif (0 <= indexes[0] <= 3) and (0 <= indexes[1] <= 3):
        return False
    elif (consts.BOARD_ROWS - 4 <= indexes[0] <= consts.BOARD_ROWS - 1) and (consts.BOARD_COLS - 3 <= indexes[1] <= consts.BOARD_COLS - 1):
        return False

    for i in range(1, 3):
        if field[indexes[0]][indexes[1]+i] == consts.MINE_IMG:
            return False

    return True


def generate_empty_field(field):
    for row in range(consts.BOARD_ROWS):
        field.append([])
        for col in range(consts.BOARD_COLS):
            field[row].append(consts.EMPTY_CELL)

def dfs(grid, x, y):
    if x < 0 or x >= consts.BOARD_ROWS or y < 0 or y >= consts.BOARD_COLS or grid[x][y] == consts.MINE_IMG or grid[x][y] == consts.DFS_SQUARE:
        return

    grid[x][y] = consts.DFS_SQUARE

    dfs(grid, x + 1, y)
    dfs(grid, x - 1, y)
    dfs(grid, x, y + 1)
    dfs(grid, x, y - 1)


def is_field_valid(test_field):
    for row in test_field:
        for col in row:
            if col == consts.FLAG_IMG:
                return False
    return True


def copy_grid(grid):
    grid_copy = []
    for row in grid:
        grid_copy.append(row.copy())
    return grid_copy
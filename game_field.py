import pygame
import random

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

def copy_grid(grid):
    grid_copy = []
    for row in grid:
        grid_copy.append(row.copy())
    return grid_copy

def generate_random_field():
    field = []

    for row in range(consts.BOARD_ROWS):
        field.append([])
        for col in range(consts.BOARD_COLS):
            field[row].append(consts.EMPTY_CELL)

    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if (row != 0 and col != 0) or (row != consts.BOARD_ROWS - 1 and col != consts.BOARD_COLS - 1):
                random_value = random.random()
                if random_value <= 0.2:
                    field[row][col] = consts.MINE_IMG

        field[0][0] = consts.EMPTY_CELL
        field[consts.BOARD_ROWS - 1][consts.BOARD_COLS - 1] = consts.FLAG_IMG
    return field

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

init_game_field()
print(game_field)

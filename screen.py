import consts
import pygame
import random as rnd
import time
import soldier

screen = pygame.display.set_mode(
       (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
grass_coordinates = []

"""
    Function that initiates global screen and list of grass coordinates
"""
def init_screen():
    global screen
    global grass_coordinates

def close_screen():
    pygame.display.quit()

def draw_field():
    screen.fill(consts.GREEN)
    draw_soldier()
    if grass_coordinates == []:
        set_grass_coordinates()
    draw_grass()
    draw_flag()
    pygame.display.flip()

def draw_soldier():
    soldier_img = load_and_transform_img(consts.SOLDIER_REGULAR_IMG,
                                         consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)
    # TODO: change to soldier's position
    screen.blit(soldier_img, (0, 0))

def load_and_transform_img(image_name, width=consts.IMAGE_LENGTH, height=consts.IMAGE_LENGTH):
    image = pygame.image.load(
            f"C:/Users/jbt/PycharmProjects/Dual-Project/images/{image_name}")
    image_small = pygame.transform.scale(image, (width, height))
    return image_small

def set_grass_coordinates():
   count = rnd.randint(15, 30)
   for i in range(count):
       curr_x = rnd.randint(0, consts.WINDOW_WIDTH)
       curr_y = rnd.randint(0, consts.WINDOW_HEIGHT)
       grass_coordinates.append((curr_x, curr_y))

def draw_grass():
    grass_img = load_and_transform_img(consts.GRASS_IMG)
    for grass_x, grass_y in grass_coordinates:
        screen.blit(grass_img, (grass_x, grass_y))

def draw_flag():
    flag_img = load_and_transform_img(consts.FLAG_IMG,
                                      consts.FLAG_WIDTH, consts.FLAG_HEIGHT)
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_COLS * consts.CELL_SIZE
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_ROWS * consts.CELL_SIZE
    screen.blit(flag_img, (flag_x, flag_y))

def draw_night_mode(grid):
    screen.fill(consts.GREEN)
    draw_grid()
    draw_mines(grid)
    draw_injury_soldier()

def draw_grid():
    for y in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for x in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, consts.BLACK, rect, 1)

def draw_mines(grid):
    mine_img = load_and_transform_img(consts.MINE_IMG, consts.MINE_WIDTH,
                                      consts.MINE_HEIGHT)
    for r in range(consts.BOARD_ROWS):
        for c in range(consts.BOARD_COLS):
            if grid[r][c] == consts.MINE_IMG:
                pos_x = r * consts.CELL_SIZE
                pos_y = c * consts.CELL_SIZE
                screen.blit(mine_img, (pos_x, pos_y))

def draw_injury_soldier():
    injury_soldier_img = load_and_transform_img(consts.SOLDIER_INJURED_IMG,
                                                consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)
    # TODO: change to soldier's position
    screen.blit(injury_soldier_img, (0, 0))

def draw_explosion():
    explosion_img = load_and_transform_img(consts.EXPLOSION_IMG)
    # TODO: change to explosion position
    screen.blit(explosion_img, (0, 0))
    time.sleep(consts.ANIMATION_TIME_EXPLOSION)
    injury_soldier = load_and_transform_img(consts.SOLDIER_INJURED_IMG,
                                consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)
    # TODO: change to soldier's position
    screen.blit(injury_soldier, (0, 0))


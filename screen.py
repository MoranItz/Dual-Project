import consts
import pygame
import pygame.font
import random as rnd
import time

import game_field
import soldier

screen = pygame.display.set_mode(
       (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
grass_coordinates = []

# Function that creates global screen with green background
def init_screen():
    pygame.font.init()
    global screen
    global grass_coordinates

# Function that closes the screen
def close_screen():
    pygame.display.quit()

def display_welcome_message():
    text = "Welcome to The Flag game.\n Have Fun!"
    pos_x = ( soldier.get_coordinates()[0] + consts.SOLDIER_COLS + 1 ) * consts.CELL_SIZE
    pos_y = soldier.get_coordinates()[1]
    display_message(text, pos_x, pos_y)

def draw_field():
    screen.fill(consts.GREEN)
    draw_soldier()
    if grass_coordinates == []:
        set_grass_coordinates()
    draw_grass()
    draw_flag()
    pygame.display.flip()

def draw_soldier():
    soldier_img = load_and_transform_img(soldier.soldier["img"],
                                         consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)
    x = soldier.get_coordinates()[0] * consts.CELL_SIZE
    y = soldier.get_coordinates()[1] * consts.CELL_SIZE
    screen.blit(soldier_img, (x, y))

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

def draw_night_mode():
    grid = game_field.game_field
    screen.fill(consts.BLACK)
    soldier.soldier["img"] = consts.SOLDIER_NIGHT_IMG
    draw_grid()
    draw_soldier()
    draw_mines(grid)
    pygame.display.flip()


def draw_grid():
    for y in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for x in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(y, x, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, consts.GREEN, rect, 1)

def draw_mines(grid):
    mine_img = load_and_transform_img(consts.MINE_IMG, consts.MINE_WIDTH,
                                      consts.MINE_HEIGHT)
    c = 0
    for r in range(consts.BOARD_ROWS):
        while c < consts.BOARD_COLS:
            if grid[r][c] == consts.MINE_IMG:
                pos_x = c * consts.CELL_SIZE
                pos_y = r * consts.CELL_SIZE
                screen.blit(mine_img, (pos_x, pos_y))
                c += 3
            c += 1
        c = 0


def draw_explosion():
    soldier.soldier["img"] = consts.SOLDIER_INJURED_IMG
    draw_field()
    explosion_img = load_and_transform_img(consts.EXPLOSION_IMG)
    x = ( soldier.get_coordinates()[0] + consts.SOLDIER_COLS ) * consts.CELL_SIZE
    y = ( soldier.get_coordinates()[1] + consts.SOLDIER_ROWS - 2 ) * consts.CELL_SIZE
    screen.blit(explosion_img, (x, y))
    time.sleep(consts.ANIMATION_TIME_EXPLOSION)
    pygame.display.flip()

def display_message(message_text, pos_x=consts.WINDOW_WIDTH // 2, pos_y=consts.WINDOW_HEIGHT // 2):
    font = pygame.font.SysFont(consts.FONT_NAME, 35)
    message = font.render(message_text, True, color=consts.BLACK)
    screen.blit(message,(pos_x, pos_y))
    pygame.display.flip()



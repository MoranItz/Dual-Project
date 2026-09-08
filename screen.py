import consts
import pygame
import random as rnd
import time

soldier = pygame.Surface
screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# Function that creates global screen with green background
def init_screen():
    #pygame.init()
    global screen # initiate screen as global
    screen.fill(consts.GREEN)
    pygame.display.flip()

# Function that closes the screen
def close_screen():
    pygame.display.quit()

# Function that draws beginning state field
# Draws soldier, grass and flag
def draw_field():
    # Draw soldier
    draw_image(consts.SOLDIER_REGULAR_IMG, 0, 0,
               consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)

    # Draw grass
    grass_coordinates = get_grass_coordinates()
    for grass_x, grass_y in grass_coordinates:
        draw_image(consts.GRASS_IMG, grass_x, grass_y)

    # Draw flag
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_COLS * consts.CELL_SIZE
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_ROWS * consts.CELL_SIZE
    draw_image(consts.FLAG_IMG, flag_x, flag_y,
               consts.FLAG_WIDTH, consts.FLAG_HEIGHT)

    pygame.display.flip()

# Function that loads image to pygame and transform it to given size
def load_image(image_name, width, height):
    image = pygame.image.load(
        f"C:/Users/jbt/PycharmProjects/Dual-Project/images/{image_name}")
    image_small = pygame.transform.scale(image, (width, height))
    return image_small

# Function that gets image name, position on screen and its size
# and draws image on the screen
def draw_image(image_name, pos_x, pos_y, width=consts.IMAGE_LENGTH, height=consts.IMAGE_LENGTH):
    image = load_image(image_name, width, height)
    screen.blit(image,(pos_x, pos_y))

# Function that draws night mode
# Draws grid, mines and night mode soldier
def draw_night_mode(grid):
    draw_grid()

    # Draw mines
    for r in range(consts.BOARD_ROWS):
        for c in range(consts.BOARD_COLS):
            if grid[r][c] == consts.MINE_IMG:
                pos_x = r * consts.CELL_SIZE
                pos_y = c * consts.CELL_SIZE
                draw_image(consts.MINE_IMG, pos_x, pos_y)

    # Draw night mode soldier
    night_soldier = load_image(consts.SOLDIER_NIGHT_IMG,
                                consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)
    soldier.blit(night_soldier, (pos_x, pos_y))

# Function that draws grid
def draw_grid():
    for y in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for x in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, consts.BLACK, rect, 1)

# Function that generate grass coordinates using random
# Returns list of coordinates on the screen
def get_grass_coordinates():
    coordinates = []
    count = rnd.randint(15, 30)
    for i in range(count):
        curr_x = rnd.randint(0, consts.WINDOW_WIDTH)
        curr_y = rnd.randint(0, consts.WINDOW_HEIGHT)
        coordinates.append((curr_x, curr_y))
    return coordinates

# Function that animates mine explosion
# Draws explosion, teleport and injury soldier
def draw_mine_explosion(pos_x, pos_y):
    draw_image(consts.EXPLOSION_IMG, pos_x, pos_y)
    time.sleep(consts.ANIMATION_TIME_EXPLOSION)
    draw_image(consts.TELEPORT_IMG, pos_x, pos_y)

    # Draw injury soldier
    injury_soldier = load_image(consts.SOLDIER_INJURED_IMG, consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)
    soldier.blit(injury_soldier, (pos_x, pos_y))

import consts
import pygame
import random as rnd
import time

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def init_screen():
    pygame.init()
    global screen # initiate screen as global
    screen.fill(consts.GREEN)
    pygame.display.init()

def close_screen():
    pygame.display.quit()

def draw_field():
    # Draw player
    draw_image(consts.SOLDIER_REGULAR_IMG, 0, 0,
               consts.SOLDIER_LENGTH, consts.SOLDIER_LENGTH)

    # Draw grass
    grass_coordinates = get_grass_coordinates()
    for grass_x, grass_y in grass_coordinates:
        draw_image(consts.GRASS_IMG, grass_x, grass_y,
                   consts.GRASS_LENGTH, consts.GRASS_LENGTH)

    # Draw flag
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_COLS * consts.CELL_SIZE
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_ROWS * consts.CELL_SIZE
    draw_image(consts.FLAG_IMG, flag_x, flag_y,
               consts.FLAG_WIDTH, consts.FLAG_HEIGHT)

    pygame.display.flip()

def draw_image(image, pos_x, pos_y, width=consts.IMAGE_LENGTH, height=consts.IMAGE_LENGTH):
    image = pygame.image.load(f"C:/Users/jbt/PycharmProjects/Dual-Project/images/{image}")
    image_small = pygame.transform.scale(image, (width, height))
    screen.blit(image_small,(pos_x, pos_y))

def draw_night_mode(grid):
    for r in range(consts.BOARD_ROWS):
        for c in range(consts.BOARD_COLS):
            pos_x = r * consts.CELL_SIZE
            pos_y = c * consts.CELL_SIZE

            cell_type = grid[r][c]
            if cell_type == consts.EMPTY_CELL:
                pygame.draw.rect(screen, consts.BLACK,
                                 (pos_x, pos_y, consts.CELL_SIZE,
                                  consts.CELL_SIZE))
            elif cell_type == consts.MINE_IMG:
                draw_image(consts.MINE_IMG, pos_x, pos_y)

def get_grass_coordinates():
    coordinates = []
    count = rnd.randint(15, 30)
    for i in range(count):
        curr_x = rnd.randint(0, consts.WINDOW_WIDTH)
        curr_y = rnd.randint(0, consts.WINDOW_HEIGHT)
        coordinates.append((curr_x, curr_y))
    return coordinates

def draw_mine_explosion(pos_x, pos_y):
    draw_image(consts.EXPLOSION_IMG, pos_x, pos_y)
    time.sleep(consts.ANIMATION_TIME_EXPLOSION)
    draw_image(consts.TELEPORT_IMG, pos_x, pos_y)

def draw_mine_hole():
    #TODO: draw mine hole on screen
    pass

init_screen()
draw_field()
time.sleep(50000)
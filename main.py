import pygame

import screen
import consts
import game_field
import soldier
import time


def main():
    game_over = False

    soldier.init_soldier()
    game_field.init_game_field()
    screen.init_screen()

    while not game_over:
        screen.draw_field()
        for event in pygame.event.get():
            if event.key == pygame.K_ESCAPE:
                return
            elif event.key == pygame.K_0:
                screen.draw_night_mode()
                # TIME SLEEP
            else:
                soldier.move_player()

            if soldier.player_touch_flag():
                print("win")
                game_over = True

            elif soldier.player_touch_mine():
                print("lose")
                game_over = True





if __name__ == "__main__":
    main()
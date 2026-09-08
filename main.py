import pygame

import screen
import consts
import game_field
import soldier
import time


def main():
    game_over = False

    game_field.init_game_field()
    screen.init_screen()

    game_field.draw_field()
    while not game_over:

        events = pygame.event.get() # get player events
        for event in events:
            if event.type == pygame.K_KP_ENTER: # if the player presses ENTER
                game_field.show_mines(event.type)
                time.sleep(1) # sleep for 1 second so the player will have a cooldown when seeing the mines
            else:
                soldier.move_player(event.type) # Moves player

        if soldier.player_touch_mine() or soldier.player_touch_flag():
            game_over = True

        game_field.draw_field()


    if is_touch_flag():
        print("game won!")
    else:
        print("game lost!")

screen.close_screen()



if __name__ == "__main__":
    main()
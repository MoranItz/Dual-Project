# Outside source imports
import pygame
import time

# Self defined imports
import screen
import consts
import game_field
import soldier


def main():
    game_over = False

    game_field.init_game_field()
    screen.init_screen()

    screen.draw_field()
    screen.draw_player()
    while not game_over:

        events = pygame.event.get() # get player events
        for event in events:
            if event.type == pygame.K_KP_ENTER: # if the player presses ENTER
                screen.draw_night_mode()
                time.sleep(consts.MINE_PEEK_COOLDOWN) # sleep for 1 second so the player will have a cooldown when seeing the mines
            else:
                new_coordinates = soldier.get_new_coordinates(event.type) # returns the new coordinates for the move

                if soldier.player_touch_mine(new_coordinates):
                    screen.draw_mine_explosion()
                    time.sleep(consts.ANIMATION_TIME_EXPLOSION)
                    game_over = True

                if soldier.player_touch_flag(new_coordinates):
                    game_over = True

                soldier.move_player(new_coordinates)

        screen.draw_player()

    if soldier.player_touch_flag():
        print("game won!")
    else:
        print("game lost!")

screen.close_screen()



if __name__ == "__main__":
    main()
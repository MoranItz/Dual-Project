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

    soldier.init_soldier()
    game_field.init_game_field()
    screen.init_screen()
    screen.draw_field()

    while not game_over:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True

                if event.key == pygame.K_KP_ENTER: # if the player presses ENTER
                    #screen.draw_night_mode()
                    time.sleep(consts.MINE_PEEK_COOLDOWN) # sleep for 1 second so the player will have a cooldown when seeing the mines

                else:
                    new_coordinates = soldier.get_new_coordinates(event) # returns the new coordinates for the move

                    if soldier.player_touch_mine(new_coordinates):
                        screen.draw_mine_explosion()
                        #time.sleep(consts.ANIMATION_TIME_EXPLOSION)
                        game_over = True

                    if soldier.player_touch_flag(new_coordinates):
                        game_over = True

                soldier.move_player(new_coordinates)
                screen.draw_soldier(soldier.soldier["x"]*consts.CELL_SIZE, soldier.soldier["y"]*consts.CELL_SIZE)



    if soldier.player_touch_flag():
        print("game won!")
    else:
        print("game lost!")





if __name__ == "__main__":
    main()
    screen.close_screen()
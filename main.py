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
    events = ""
    night_mode_stop_watch = 0

    soldier.init_soldier()
    game_field.init_game_field()
    screen.init_screen()
    screen.draw_field()

    while not game_over:
        soldier.soldier["img"] = consts.SOLDIER_REGULAR_IMG
        screen.draw_field()

        if time.time() - night_mode_stop_watch < 1:
            screen.draw_night_mode()
            time.sleep(1)
            pygame.event.clear()

        else:
            events = pygame.event.get()
            night_mode_stop_watch = 0

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_0:
                        #screen.draw_night_mode()
                        night_mode_stop_watch = time.time()
                    else:
                        soldier.move_player(soldier.get_move_direction(event))

                if soldier.player_touch_flag():
                    print("win")
                    game_over = True

                elif soldier.player_touch_mine():
                    screen.draw_explosion()
                    print("lose")
                    game_over = True





if __name__ == "__main__":
    main()
    time.sleep(5)

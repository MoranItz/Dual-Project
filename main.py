# Moran Itzkovich - 217278274
# Polina Prokopenko 227390135

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
    night_mode_stop_watch = 0
    is_welcome_message_displayed = False

    soldier.init_soldier()
    game_field.init_game_field()
    screen.init_screen()
    screen.draw_field()

    while not game_over:
        soldier.soldier["img"] = consts.SOLDIER_REGULAR_IMG
        screen.draw_field()
        if not is_welcome_message_displayed:
            screen.display_welcome_message()
            time.sleep(1)
            is_welcome_message_displayed = True

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
                    elif event.key == pygame.K_KP_ENTER:
                        night_mode_stop_watch = time.time()
                    else:
                        soldier.move_player(soldier.get_move_direction(event))

            if soldier.player_touch_flag():
                screen.display_message("Congratulations! :)")
                game_over = True

            elif soldier.player_touch_mine():
                screen.draw_explosion()
                screen.display_message("You lose :(")
                game_over = True





if __name__ == "__main__":
    main()

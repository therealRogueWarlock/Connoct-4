from connect4 import connect4_load_sprits as sprits
import pygame

# window
win_width = 516
win_height = 476

window = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('Connect 4')


def draw_red_or_yellow_piece(plate):
    row = 0
    y = 103
    while row != 6:
        spots = 0
        x = 71
        while spots != 7:
            spot = plate[row][spots]
            if spot == 0:
                pass
            elif spot == 1:
                window.blit(sprits.red_piece, (x, y))
            elif spot == 2:
                window.blit(sprits.yellow_piece, (x, y))
            spots += 1
            x += 59
        row += 1
        y += 59


def draw_player(player_no, selected_column):
    selected_column += 1

    if player_no == 1:
        window.blit(sprits.red_piece2, ((59 * selected_column)+10, 30))

    else:
        window.blit(sprits.yellow_piece2, ((59 * selected_column)+10, 30))


def draw_game_window(plate, player_no, selected_column):
    draw_red_or_yellow_piece(plate)

    window.blit(sprits.sprit_game_plate, (0, 0))

    draw_player(player_no, selected_column)

    pygame.display.update()


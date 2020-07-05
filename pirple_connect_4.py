# Project #1: A Simple Game
import numpy as np
from connect4 import connect4_draw_game as draw_game
import pygame


# game plate
plate_width = 7
plate_height = 6
# creating the game plate
game_plate = np.zeros((plate_height, plate_width))


clock = pygame.time.Clock()


def place_piece(plate, column, player_number):
    if plate[0][column] == 0:  # as long as the column still have room for a piece.
        for row in range(plate_height):
            if plate[row][column] == 1 or plate[row][column] == 2:
                plate[row - 1][column] = player_number
                print("placing on top of piece")
                return row - 1, column, True

            elif row == plate_height - 1:
                plate[row][column] = player_number
                print("placing at the bottom")
                return row, column, True

            elif plate[row][column] == 0:
                continue
    else:
        print("column is full")
        return 0, column, False


def count_pieces_right_left(plate, row, column):
    print("checking right and left")
    count = 1
    check_column = column
    # checking right and left
    while True:  # checking right
        if column != plate_width - 1:  # as long as piece is not in the last column.
            if check_column < plate_width - 1:  # as long as the check column is lower than the width of the plate.
                check_column += 1  # checking the column to the right.
                if plate[row][check_column] == plate[row][column]:  # if the column has same value as the player piece.
                    count += 1  # add one to count. if count reach 4, that player wins.
                else:
                    break
            else:
                break
        else:
            break

    check_column = column
    while True:
        if column != 0:  # if not already at the first column
            check_column -= 1

            if plate[row][check_column] == plate[row][column]:  # checking left
                count += 1
            else:
                break
        else:
            break
    if count == 4:
        return count, plate[row][column]
    return False, 0


def count_pieces_upright_downleft(plate, row, column):
    print("checking upright down left")
    count = 1
    check_row = row
    check_column = column
    # checking upright and downleft
    while True:  # checking upright
        if column != plate_width - 1:  # as long as piece is not in the last column.

            if row <= plate_height - 1:  # os long as not at the first row

                if check_column < plate_width - 1:  # as long as the check column is lower than the width of the plate.

                    if check_row > 0:

                        check_row -= 1
                        check_column += 1
                        # checking the upright corner and  if the spot has same value as the player piece.
                        if plate[check_row][check_column] == plate[row][column]:
                            count += 1  # add one to count. if count reach 4, that player wins.

                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break

    check_row = row
    check_column = column
    while True:  # checking downleft
        if column != 0:  # as long as piece is not in the first column.
            if row != plate_height - 1:  # os long as not at the last row
                if check_column != 0:  # as long as the check column is not checking column -1.
                    if check_row < plate_height - 1:  # as long as the check row is not checking row 7
                        check_row += 1
                        check_column -= 1
                        # checking the upright corner and  if the spot has same value as the player piece.
                        if plate[check_row][check_column] == plate[row][column]:
                            count += 1  # add one to count. if count reach 4, that player wins.
                            print("downleft checked")
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break
    if count == 4:
        return count, plate[row][column]
    return 0, 0


def count_pieces_upleft_downright(plate, row, column):
    print("checking upleft down right")
    count = 1
    check_row = row
    check_column = column
    while True:  # checking upleft
        if column != 0:  # as long as piece is not in the first column.

            if row <= plate_height - 1:  # os long as not at the first row

                if check_column > 0:  # as long as the check is not checking column -1

                    if check_row > 0:

                        check_row -= 1
                        check_column -= 1
                        # checking the upleft corner and  if the spot has same value as the player piece.
                        if plate[check_row][check_column] == plate[row][column]:
                            count += 1  # add one to count. if count reach 4, that player wins.

                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break

    check_row = row
    check_column = column
    while True:  # checking downright
        if column != plate_width-1:  # as long as piece is not in the last column.
            if row != plate_height - 1:  # os long as not at the last row
                if check_column != plate_width-1:  # as long as the check column is not checking column 7.
                    if check_row < plate_height - 1:  # as long as the check row is not checking row 7
                        check_row += 1
                        check_column += 1
                        # checking the upright corner and  if the spot has same value as the player piece.
                        if plate[check_row][check_column] == plate[row][column]:
                            count += 1  # add one to count. if count reach 4, that player wins.
                            print("downright checked")
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break

    if count == 4:
        return count, plate[row][column]
    return 0, 0


def count_pieces_down(plate, row, column):
    print("checking down")
    count = 1
    check_row = row
    # checking down (Don't have to check up)
    while True:  # checking down
        if check_row != plate_height - 1:
            check_row += 1
            if plate[check_row][column] == plate[row][column]:
                count += 1
            else:
                break
        else:
            break

    if count == 4:
        return count, plate[row][column]
    return False, 0


def check_for_win(plate, row, column):

    count, player = count_pieces_down(plate, row, column)
    if count == 4:
        return True, player
    else:
        count, player = count_pieces_right_left(plate, row, column)
        if count == 4:
            return True, player
        else:
            count, player = count_pieces_upright_downleft(plate, row, column)
            if count == 4:
                return True, player
            else:
                count, player = count_pieces_upleft_downright(plate, row, column)
                if count == 4:
                    return True, player
                else:
                    return False, 0


def game_loop(plate):
    # main game loop
    player_no = 1
    run = True
    win = False
    seleted_column = 0
    while run:
        clock.tick(60)
        chosen_column = 0
        action = False

        draw_game.draw_game_window(plate, player_no, seleted_column)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if not win:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        if seleted_column != 0:
                            seleted_column -= 1

                    elif event.key == pygame.K_RIGHT:
                        if seleted_column != 6:
                            seleted_column += 1

                    if event.key == pygame.K_DOWN:
                        chosen_column = seleted_column
                        seleted_column = 3
                        action = True

        if action:
            row, column, placed = place_piece(game_plate, chosen_column, player_no)
            win, player = check_for_win(game_plate, row, column)

            if win:
                print(f"Player {player_no} Wins!")

        if action and placed:
            if player_no == 1:
                player_no += 1
            else:
                player_no -= 1


if __name__ == "__main__":
    game_loop(game_plate)

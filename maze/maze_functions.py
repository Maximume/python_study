import os
import sys

from maze_settings import *

def mode_select():
    if sys.argv[-1] != OPTION_DEBUG:
        mode_selected = input(MSG_WELCOME)
        if mode_selected == KEY_DEBUG:
            sys.argv.append(OPTION_DEBUG)

def set_coord(game_map, startORfinish):
    coord = [0, 0]
    for y, map_lines in enumerate(game_map):     #enumerate() return <<index, value>>
        for x, tile in enumerate(map_lines):
            if tile == startORfinish:
                coord = [x, y]
                return coord

def get_coord(current_coord):
    coord_up = [current_coord[COORD_X] + 0, current_coord[COORD_Y] + 1]
    coord_right = [current_coord[COORD_X] + 1, current_coord[COORD_Y] + 0]
    coord_down =[current_coord[COORD_X] + 0, current_coord[COORD_Y] - 1]
    coord_left =[current_coord[COORD_X] + -1, current_coord[COORD_Y] + 0]
    coord_tiles = [coord_up, coord_right, coord_down, coord_left]
    return coord_tiles

def get_tiles(game_map, current_coord):
    coord_tiles = get_coord(current_coord)

    tile_up = game_map[coord_tiles[TILE_UP][COORD_Y]][coord_tiles[TILE_UP][COORD_X]]
    tile_right = game_map[coord_tiles[TILE_RIGHT][COORD_Y]][coord_tiles[TILE_RIGHT][COORD_X]]
    tile_down = game_map[coord_tiles[TILE_DOWN][COORD_Y]][coord_tiles[TILE_DOWN][COORD_X]]
    tile_left = game_map[coord_tiles[TILE_LEFT][COORD_Y]][coord_tiles[TILE_LEFT][COORD_X]]
    tile_now = game_map[current_coord[COORD_Y]][current_coord[COORD_X]]
    tiles = [tile_up, tile_right, tile_down, tile_left, tile_now]
    return tiles

def check_tiles(game_map, current_coord):
    tiles = get_tiles(game_map, current_coord)
    msg_up = MSG_UP if (tiles[TILE_UP] == TILE_VALID or tiles[TILE_UP] == TILE_START or tiles[TILE_UP] == TILE_FINISH) else MSG_EMPTY
    msg_right = MSG_RIGHT if (tiles[TILE_RIGHT] == TILE_VALID or tiles[TILE_RIGHT] == TILE_START or tiles[TILE_RIGHT] == TILE_FINISH) else MSG_EMPTY
    msg_down = MSG_DOWN if (tiles[TILE_DOWN] == TILE_VALID or tiles[TILE_DOWN] == TILE_START or tiles[TILE_DOWN] == TILE_FINISH) else MSG_EMPTY
    msg_left = MSG_LEFT if (tiles[TILE_LEFT] == TILE_VALID or tiles[TILE_LEFT] == TILE_START or tiles[TILE_LEFT] == TILE_FINISH) else MSG_EMPTY
    checked_tiles = [msg_up, msg_right, msg_down, msg_left]
    return checked_tiles

def check_move(game_map, current_coord, move_input):
    checked_tiles = check_tiles(game_map, current_coord)
    if checked_tiles[move_input] == MSG_EMPTY:
        return False
    else:
        return True

def alert_invalid_input():
    os.system('cls')
    print(MSG_INVALID)

def input_move_input(move_count, current_coord, finish_coord, game_map):
    while True:
        msg_for_input(move_count, current_coord, finish_coord, game_map)
        move_input = input(MSG_ASK_DIRECTION)
        if move_input == INPUT_UP or move_input == INPUT_RIGHT or move_input == INPUT_DOWN or move_input == INPUT_LEFT:
            move_input = int(move_input)
            if check_move(game_map, current_coord, move_input):
                return move_input
            else:
                alert_invalid_input()
        else:
            alert_invalid_input()

def msg_for_input(move_count, current_coord, finish_coord, game_map):
    checked_tiles = check_tiles(game_map, current_coord)
    print(MSG_INFO %(move_count, finish_coord, current_coord))
    print('%s%s%s%s\n' %(checked_tiles[TILE_UP], checked_tiles[TILE_RIGHT], checked_tiles[TILE_DOWN], checked_tiles[TILE_LEFT]), end = '')
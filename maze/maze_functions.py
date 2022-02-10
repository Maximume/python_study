import os
import sys

from maze_settings import *

def mode_select() -> None:
    if sys.argv[-1] != DEBUG.OPTION:
        mode_selected = input(MSG_TEXT.WELCOME)
        if mode_selected == DEBUG.KEY:
            sys.argv.append(DEBUG.OPTION)

def set_coord(game_map:list, startORfinish:str) -> list:
    coord = [0, 0]
    for y, map_lines in enumerate(game_map):     #enumerate() return <<index, value>>
        for x, tile in enumerate(map_lines):
            if tile == startORfinish:
                coord = [x, y]
                return coord

def get_coord(current_coord:list) -> list:
    coord_up    = [current_coord[COORD.X] + 0, current_coord[COORD.Y] + 1]
    coord_right = [current_coord[COORD.X] + 1, current_coord[COORD.Y] + 0]
    coord_down  = [current_coord[COORD.X] + 0, current_coord[COORD.Y] - 1]
    coord_left  = [current_coord[COORD.X] - 1, current_coord[COORD.Y] + 0]
    coord_tiles = [coord_up, coord_right, coord_down, coord_left]
    return coord_tiles

def get_tiles(game_map:list, current_coord:list) -> list:
    coord_tiles = get_coord(current_coord)

    tile_up    = game_map[coord_tiles[TILE_VALUE.UP][COORD.Y]][coord_tiles[TILE_VALUE.UP][COORD.X]]
    tile_right = game_map[coord_tiles[TILE_VALUE.RIGHT][COORD.Y]][coord_tiles[TILE_VALUE.RIGHT][COORD.X]]
    tile_down  = game_map[coord_tiles[TILE_VALUE.DOWN][COORD.Y]][coord_tiles[TILE_VALUE.DOWN][COORD.X]]
    tile_left  = game_map[coord_tiles[TILE_VALUE.LEFT][COORD.Y]][coord_tiles[TILE_VALUE.LEFT][COORD.X]]
    tile_now   = game_map[current_coord[COORD.Y]][current_coord[COORD.X]]
    tiles = [tile_up, tile_right, tile_down, tile_left, tile_now]
    return tiles

def check_tiles(game_map:list, current_coord:list) -> list:
    tiles = get_tiles(game_map, current_coord)
    msg_up    = MSG_TEXT.UP if (tiles[TILE_VALUE.UP] == TILE_VALUE.VALID or tiles[TILE_VALUE.UP] == TILE_VALUE.START or tiles[TILE_VALUE.UP] == TILE_VALUE.FINISH) else MSG_TEXT.EMPTY
    msg_right = MSG_TEXT.RIGHT if (tiles[TILE_VALUE.RIGHT] == TILE_VALUE.VALID or tiles[TILE_VALUE.RIGHT] == TILE_VALUE.START or tiles[TILE_VALUE.RIGHT] == TILE_VALUE.FINISH) else MSG_TEXT.EMPTY
    msg_down  = MSG_TEXT.DOWN if (tiles[TILE_VALUE.DOWN] == TILE_VALUE.VALID or tiles[TILE_VALUE.DOWN] == TILE_VALUE.START or tiles[TILE_VALUE.DOWN] == TILE_VALUE.FINISH) else MSG_TEXT.EMPTY
    msg_left  = MSG_TEXT.LEFT if (tiles[TILE_VALUE.LEFT] == TILE_VALUE.VALID or tiles[TILE_VALUE.LEFT] == TILE_VALUE.START or tiles[TILE_VALUE.LEFT] == TILE_VALUE.FINISH) else MSG_TEXT.EMPTY
    checked_tiles = [msg_up, msg_right, msg_down, msg_left]
    return checked_tiles

def check_move(game_map:list, current_coord:list, move_input:int) -> bool:
    checked_tiles = check_tiles(game_map, current_coord)
    if checked_tiles[move_input] == MSG_TEXT.EMPTY:
        return False
    else:
        return True

def alert_invalid_input() -> None:
    os.system('cls')
    print(MSG_TEXT.INVALID)

def input_move_input(move_count:int, current_coord:list, finish_coord:list, game_map:list) -> int:
    while True:
        msg_for_input(move_count, current_coord, finish_coord, game_map)
        move_input = input(MSG_TEXT.ASK_DIRECTION)
        if move_input == INPUT_VALUE.UP or move_input == INPUT_VALUE.RIGHT or move_input == INPUT_VALUE.DOWN or move_input == INPUT_VALUE.LEFT:
            move_input = int(move_input)
            if check_move(game_map, current_coord, move_input):
                return move_input
            else:
                alert_invalid_input()
        else:
            alert_invalid_input()

def msg_for_input(move_count:int, current_coord:list, finish_coord:list, game_map:list) -> None:
    checked_tiles = check_tiles(game_map, current_coord)
    print(MSG_TEXT.INFO %(move_count, finish_coord, current_coord))
    print('%s%s%s%s\n' %(checked_tiles[TILE_VALUE.UP], checked_tiles[TILE_VALUE.RIGHT], checked_tiles[TILE_VALUE.DOWN], checked_tiles[TILE_VALUE.LEFT]), end = '')
from maze_map import Map

import maze_functions as mfunc
from maze_settings import *

def init_map() -> None:
    global game_map
    global maze_map
    maze_map = Map()
    game_map = maze_map.load_map()

def init_coord() -> None:
    global start_coord
    global finish_coord
    global current_coord
    start_coord = mfunc.set_coord(game_map, CONST_TILE.START)
    finish_coord = mfunc.set_coord(game_map, CONST_TILE.FINISH)
    current_coord = start_coord

def init_var() -> None:
    global move_count
    global move_input
    move_count = 0
    move_input = 0

def init_game() -> None:
    init_map()
    init_coord()
    init_var()

init_game()
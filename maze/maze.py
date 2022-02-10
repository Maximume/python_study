import os
import maze_functions as mfunc
from maze_settings import *

#init_game()
from maze_init import *

#select mode
mfunc.mode_select()

#main loop
while current_coord != finish_coord:
    os.system('cls')
    #show map (run with debug mode)
    maze_map.show_map(game_map)
    #get input
    move_input = mfunc.input_move_input(move_count, current_coord, finish_coord, game_map)
    #move
    current_coord = mfunc.get_coord(current_coord)[move_input]
    move_count += 1
import os
import maze_functions as mfunc
import maze_settings as mset
from maze_map import Map

#initialize and load map
maze_map = Map()
game_map = maze_map.load_map()

#initialize points
starting_point = mfunc.set_Point(game_map, mset.TILE_STARTING)
ending_point = mfunc.set_Point(game_map, mset.TILE_ENDING)
current_coord = starting_point

#initailize variables
move_count = 0
move_last = 0
move_input = 0
is_blocked = 0

#main loop
while current_coord != ending_point:
    
    os.system('cls')
    #show map run with debug mode
    maze_map.show_map(game_map)

    #get input value
    move_input = mfunc.input_move_input(move_count, current_coord, game_map)
    #set cursor pointing direction
    move_last = mfunc.get_move_last(move_last, move_input)

    coord = mfunc.get_coords(current_coord)
    current_coord = coord[move_last]

    move_count += 1
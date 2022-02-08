import os
import maze_functions as mfunc
import maze_settings as mset
from maze_map import Map

maze_map = Map()
loaded_map = maze_map.load_map()

starting_point = mfunc.set_Point(loaded_map, mset.TILE_STARTING)
ending_point = mfunc.set_Point(loaded_map, mset.TILE_ENDING)
current_point = starting_point

move_count = 0
move_last = 0
move_input = 0
is_blocked = 0

while current_point != ending_point:
    os.system('cls')
    maze_map.show_map(loaded_map)

    print(move_last, move_input)
    move_input = mfunc.msg_for_input(move_count, current_point)
    move_last = mfunc.get_move_last(move_last, move_input)

    

    move_count += 1
        

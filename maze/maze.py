import os
import maze.maze_functions as mfunc
import maze_settings as mset
from maze.maze_map import Map

maze_map = Map()
loaded_map = maze_map.load_map()

starting_point = mfunc.set_Point(loaded_map, mset.TILE_STARTING)
ending_point = mfunc.set_Point(loaded_map, mset.TILE_ENDING)
current_point = starting_point

moving_cnt = 0
moving_current = 0
moving_last = 0

is_blocked = 0

while current_point != ending_point:

    os.system('cls')
    maze_map.show_map(loaded_map)


    moving_current = mfunc.set_moving_current(current_point, moving_last)


    moving_last = moving_current % 3 #set
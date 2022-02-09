import sys
from maze_settings import *

class Map():
    def __init__(self):
        self.f = open(FILE_LOCATION_MAP, 'r')
        self.loaded_map = self.f.readlines()
        self.loaded_map = list(reversed(self.loaded_map))
        self.f.close()
        self.map_size = len(self.loaded_map)

    def init_map(self, map_size):
        init_mapsize = map_size + WALL_PADDING
        initialized_map = [[TILE_WALL] * init_mapsize for _ in range(init_mapsize)]

        return initialized_map

    def load_map(self):
        game_map = self.init_map(self.map_size)

        for map_lines in range(len(self.loaded_map)):
            self.loaded_map[map_lines] = self.loaded_map[map_lines].split()

        for y in range(len(self.loaded_map)):
            for x in range(len(self.loaded_map)):
                game_map[y + MAP_PADDING][x + MAP_PADDING] = self.loaded_map[y][x]

        return game_map

    def show_map(self, game_map):
        game_map_reversed = list(reversed(game_map))
        if sys.argv[-1] == OPTION_DEBUG:
            print(MSG_DEBUG)
            for map_lines in game_map_reversed:
                for tile in map_lines:
                    print(tile, end = MAP_DISPLAY_PADDING)
                print()
import sys
from maze_settings import *
class Map:
    def __init__(self) -> None:
        self.f = open(CONST_FILE.LOCATION_MAP, 'r')
        self.loaded_map = self.f.readlines()
        self.loaded_map = list(reversed(self.loaded_map))
        self.f.close()
        self.map_size = len(self.loaded_map)

    def init_map(self, map_size:int) -> list:
        init_mapsize = map_size + CONST_PADDING.WALL
        initialized_map = [[CONST_TILE.WALL] * init_mapsize for _ in range(init_mapsize)]

        return initialized_map

    def load_map(self) -> list:
        game_map = self.init_map(self.map_size)

        for map_lines in range(len(self.loaded_map)):
            self.loaded_map[map_lines] = self.loaded_map[map_lines].split()

        for y in range(len(self.loaded_map)):
            for x in range(len(self.loaded_map)):
                game_map[y + CONST_PADDING.MAP][x + CONST_PADDING.MAP] = self.loaded_map[y][x]

        return game_map

    def show_map(self, game_map:list) -> None:
        game_map_reversed = list(reversed(game_map))
        if sys.argv[-1] == DEBUG.OPTION:
            print(DEBUG.MSG)
            for map_lines in game_map_reversed:
                for tile in map_lines:
                    print(tile, end = CONST_PADDING.MAP_DISPLAY)
                print()
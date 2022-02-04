import maze_settings as mset

class Map():
    def __init__(self):
        self.f = open(mset.FILE_LOCATION_MAP, 'r')
        self.loaded_map = self.f.readlines()
        self.f.close()

        self.map_size = len(self.loaded_map)

    def init_map(self, map_size):
        wall_arounding = 2

        init_size = map_size + wall_arounding
        initialized_map = [['x']*init_size for _ in range(init_size)]

        return initialized_map

    def load_map(self):
        game_map = self.init_map(self.map_size)

        for map_lines in range(len(self.loaded_map)):
            self.loaded_map[map_lines] = self.loaded_map[map_lines].split()

        for y in range(len(self.loaded_map)):
            for x in range(len(self.loaded_map)):
                game_map[y+1][x+1] = self.loaded_map[y][x]

        return game_map

    def show_map(self, game_map):
        for map_lines in game_map:
            for tile in map_lines:
                print(tile, end = ' ')
            print()
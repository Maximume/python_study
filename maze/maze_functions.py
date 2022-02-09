import os

def set_Point(game_map, startORend):
    coord = [0, 0]

    for i, map_lines in enumerate(game_map):     #enumerate -> return <<index, value>>
        for j, tile in enumerate(map_lines):
            if tile == startORend:
                coord = [j, i]
                return coord

def get_coords(current_coord):
    coord_forward = [current_coord[0] + 0, current_coord[1] + 1]
    coord_right = [current_coord[0] + 1, current_coord[1] + 0]
    coord_back =[current_coord[0] + 0, current_coord[1] - 1]
    coord_left =[current_coord[0] + -1, current_coord[1] + 0]
    coord_tiles = [coord_forward, coord_right, coord_back, coord_left]
    return coord_tiles

def get_tiles(game_map, current_coord):
    coord_tiles = get_coords(current_coord)

    tile_forward = game_map[coord_tiles[0][1]][coord_tiles[0][0]]
    tile_right = game_map[coord_tiles[1][1]][coord_tiles[1][0]]
    tile_back = game_map[coord_tiles[2][1]][coord_tiles[2][0]]
    tile_left = game_map[coord_tiles[3][1]][coord_tiles[3][0]]
    tile_now = game_map[current_coord[1]][current_coord[0]]
    tiles = [tile_forward, tile_right, tile_back, tile_left, tile_now]
    return tiles

def check_tiles(game_map, current_coord):
    tiles = get_tiles(game_map, current_coord)
    msg_forward = 'forward = 0\n' if (tiles[0] == 'o') else ''
    msg_right = 'right = 1\n' if (tiles[1] == 'o') else ''
    msg_down = 'down = 2\n' if (tiles[2] == 'o') else ''
    msg_left = 'left = 3\n' if (tiles[3] == 'o') else ''
    checked_tiles = [msg_forward, msg_right, msg_down, msg_left]
    return checked_tiles

def alert_invalid_input():
    os.system('cls')
    print('Invalid input!!')

def input_move_input(move_count, current_coord, game_map):
    while True:
        msg_for_input(move_count, current_coord, game_map)
        move_input = input('Where to go? : ')
        if move_input == '0' or move_input == '1' or move_input == '2' or move_input == '3':
            move_input = int(move_input)
            return move_input
        else:
            alert_invalid_input()

def msg_for_input(move_count, current_coord, game_map):
    checked_tiles = check_tiles(game_map, current_coord)
    print('Moves : (%d) current location : (%d,%d)' % (move_count, current_coord[0]-1, current_coord[1]-1))
    print('%s%s%s%s' %(checked_tiles[0], checked_tiles[1], checked_tiles[2], checked_tiles[3]), end = '')

def get_move_last(move_last, move_input):
    move_last += move_input
    move_last = move_last % 4
    return move_last

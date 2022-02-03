def set_Point(game_map, startORend):
    point = [0, 0]

    for i, map_lines in enumerate(game_map):     #enumerate -> return <<index, value>>
        for j, tile in enumerate(map_lines):
            if tile == startORend:
                point = [j, i]
                return point

def set_moving_current(current_point, moving_last):
    moving_current = (msg_choice(current_point) + moving_last) % 3
    return moving_current

def msg_choice(current_point):
    print('you are here (%d,%d)' % (current_point[0], current_point[1]))
    print('[up = 0, right = 1, down = 2, right = 3]')
    moving_to = input('Where to go? : ')
    return moving_to


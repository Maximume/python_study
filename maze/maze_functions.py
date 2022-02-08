import os

def set_Point(game_map, startORend):
    point = [0, 0]

    for i, map_lines in enumerate(game_map):     #enumerate -> return <<index, value>>
        for j, tile in enumerate(map_lines):
            if tile == startORend:
                point = [j, i]
                return point

def alert_invalid_input():
    os.system('cls')
    print('Invalid input!!')

def input_move_input(current_point):
    move_input = input('Where to go? : ')
    try:
        move_input = int(move_input)
    except:
        alert_invalid_input()
        input_move_input(current_point)
    else:
        if move_input == 0 or move_input == 1 or move_input == 2 or move_input == 3:
            return move_input
        else:
            alert_invalid_input()
            input_move_input(current_point)

def msg_for_input(move_count, current_point):
    print('Moves : (%d), current location(%d,%d)' % (move_count, current_point[0]-1, current_point[1]-1))
    print('[up = 0, right = 1, down = 2, right = 3]')
    move_input = input_move_input(current_point)
    return move_input

def get_move_last(move_last, move_input):
    move_last += move_input
    move_last = move_last % 4
    return move_last
    
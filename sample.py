import os

tile_map = []

def load_map(path):
    file = open(path, 'r', encoding='utf-8')
    load_map_datas = []

    while True:
        line = file.readline()
        if line == '':
            break
        line = line.replace('\n','')
        tileListForRow = line.split()
        load_map_datas.append(tileListForRow)
    file.close()

    return load_map_datas

start_pos = (None, None)
finish_pos = (None, None)
player_pos = (None, None)

def check_start_finish():
    global start_pos
    global finish_pos
    row = 0
    col = 0
    for datas in tile_map:
        for data in datas:
            if data == 'S':
                start_pos = (row, col)
            if data == 'F':
                finish_pos = (row, col)
            col += 1
        row += 1
        col = 0

def display_map():
    for datas in tile_map:
        for data in datas:
            print(data, end=' ')
        print()

def validation(offset, base_pos, std_map_datas, valid_tiles):
    target_pos = (base_pos[0]+offset[0], base_pos[1]+offset[1])
    target_row = target_pos[0]
    target_col = target_pos[1]

    tile = 'x'
    if (target_row >= 0 and target_row < 9) and (target_col >= 0 and target_col < 9):
        tile = std_map_datas[target_row][target_col]
    if tile in valid_tiles:
        return True

    return False

def checking_valid_seletions():
    selections = []
    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(0,1),
    ):
        directionDic = {
            'message':'동쪽으로 가능',
            'offset':(0,1),
        }
        selections.append(directionDic)

    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(0,-1),
    ):
        directionDic = {
            'message':'서쪽으로 가능',
            'offset':(0,-1),
        }
        selections.append(directionDic)

    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(-1,0),
    ):
        directionDic = {
            'message':'북쪽으로 가능',
            'offset':(-1,0),
        }
        selections.append(directionDic)

    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(1,0),
    ):
        directionDic = {
            'message':'남쪽으로 가능',
            'offset':(1,0),
        }
        selections.append(directionDic)

    return selections

def run_loops():
    global player_pos

    while True:
        os.system('cls')
        print(f'현재 플레이어의 위치: {player_pos}')
        valid_selections = checking_valid_seletions()

        i = 1
        for selection in valid_selections:
            print(f'{i}.{selection["message"]}')
            i += 1

        selection_str = input('어느방향으로 가실겁니까?(숫자로만)\n')
        if not selection_str.isdigit():
            continue

        selected_num = int(selection_str)
        if selected_num <= 0 or selected_num > len(valid_selections):
            continue

        selection_dict = valid_selections[selected_num-1]
        offset = selection_dict["offset"]
        
        player_pos = (player_pos[0] + offset[0], player_pos[1] + offset[1])

def prepares():

    global tile_map
    tile_map = load_map('D:/source/level1.map')

    check_start_finish()

    global player_pos
    player_pos = start_pos #(8,0)
    run_loops()

prepares()
class Const:
    def __init__(self) -> None:
        pass
    class File:
        LOCATION_MAP = 'maze_map.txt'

    class Tile:
        WALL = 'X'
        START = 'S'
        FINISH = 'F'
        VALID = 'o'
        #directions
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

    class Padding:
        MAP = 1
        WALL = 2
        MAP_DISPLAY = ' '

    class Input:
        UP = '0'
        RIGHT = '1'
        DOWN = '2'
        LEFT = '3'
CONST_FILE = Const.File()
CONST_TILE = Const.Tile()
CONST_PADDING = Const.Padding()
CONST_INPUT = Const.Input()

class Msg_text:
    UP = ' up = 0 '
    RIGHT = ' right = 1 '
    DOWN = ' down = 2 '
    LEFT = ' left = 3 '
    INVALID = 'Invalid input!!'
    ASK_DIRECTION = 'Where to go? : '
    INFO = 'Moves [%d]   Goal %s   Current Location %s'
    WELCOME = 'PRESS ENTER TO PLAY\n'
    EMPTY = ''
MSG_TEXT = Msg_text()

class Coord:
    X = 0
    Y = 1
COORD = Coord()

class Debug:
    MSG = '<<Debug Mode>>'
    OPTION = '-d'
    KEY = 'black sheep wall'
DEBUG = Debug()
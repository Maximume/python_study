class File_value():
    def __init__(self) -> None:
        self.LOCATION_MAP = 'maze_map.txt'
FILE_VALUE = File_value()

class Tile_value():
    def __init__(self) -> None:
        self.WALL = 'X'
        self.START = 'S'
        self.FINISH = 'F'
        self.VALID = 'o'
        #directions
        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3
TILE_VALUE = Tile_value()

class Padding_value():
    def __init__(self) -> None:
        self.MAP = 1
        self.WALL = 2
        self.MAP_DISPLAY = ' '
PADDING_VALUE = Padding_value()

class Coord():
    def __init__(self) -> None:
        self.X = 0
        self.Y = 1
COORD = Coord()

class Input_value():
    def __init__(self) -> None:
        self.UP = '0'
        self.RIGHT = '1'
        self.DOWN = '2'
        self.LEFT = '3'
INPUT_VALUE = Input_value()

class Msg_text():
    def __init__(self) -> None:
        #direction msg
        self.UP = ' up = 0 '
        self.RIGHT = ' right = 1 '
        self.DOWN = ' down = 2 '
        self.LEFT = ' left = 3 '
        self.INVALID = 'Invalid input!!'
        self.ASK_DIRECTION = 'Where to go? : '
        self.INFO = 'Moves [%d]   Goal %s   Current Location %s'
        self.WELCOME = 'PRESS ENTER TO PLAY\n'
        self.EMPTY = ''
MSG_TEXT = Msg_text()

class Debug():
    def __init__(self) -> None:
        self.MSG = '<<Debug Mode>>'
        self.OPTION = '-d'
        self.KEY = 'black sheep wall'
DEBUG = Debug()
from enum import Enum
from pprint import pprint

class ChessSquareColorEnum (Enum):
    WHITE = 1
    BLACK = 0

def get_chess_square_color(row, col):
    if row % 2 == col % 2:
        return 'w' 
    else:
        return 'b'

board = [[get_chess_square_color(x,y) for x in range(8)] for y in range(8) ]
print(*board, sep='\n')
pprint(board)
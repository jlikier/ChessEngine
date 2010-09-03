class Board():
    squares = [0]*64

class Piece():
    COLOR_WHITE = 1
    COLOR_BLACK = 2
    COLOR_INVALID = 3
    
    def __init__(self):
        self.color = Piece.COLOR_INVALID
class Board():
    squares = [0]*64

class Piece():
    COLOR_WHITE = 1
    COLOR_BLACK = 2
    COLOR_INVALID = 3
    color = COLOR_WHITE
    

class BoardSquare():
    def isOccupied(self):
        if isinstance(self.piece, Piece):
            return True
    	else: 
            return False
    def __init__(self):
        self.color = Piece.COLOR_INVALID
	self.piece = None

class Board(object):
    squares = [0]*64

class Piece(object):
    COLOR_WHITE = 1
    COLOR_BLACK = 2
    COLOR_INVALID = 3
    color = COLOR_WHITE
    

class BoardSquare(object):
    def isOccupied(self):
        return isinstance(self.piece, Piece)
        
    def __init__(self):
        self.color = Piece.COLOR_INVALID
        self.piece = None
        self._x = None
        self._y = None
        
    def get_x(self):
        return self._x
    
    def set_x(self,val):
        if val > 0 and val < 9:
            self._x = val
            
    x = property(get_x,set_x)
            
    def get_y(self):
        return self._y
    
    def set_y(self,val):
        if val > 0 and val < 9:
            self._y = val
            
    y = property(get_y,set_y)
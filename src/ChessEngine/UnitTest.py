import unittest
import ChessBoard

class ChessBoardTest(unittest.TestCase):
    
    #ChessBoard
    def test_ChessBoardSize(self):
        b = ChessBoard.Board()
        self.assertEqual(len(b.squares),64)
        
    #BoardSquare
    def test_BoardSquarePiece(self):
        s = ChessBoard.BoardSquare()
        self.assertTrue(hasattr(s,"piece"), "BoardSquare is missing attribute: piece")
    
#THE BALL!!!1#
    def test_BoardSquareLocation(self):
        s = ChessBoard.BoardSquare()     
	self.assertTrue(hasattr(s,"x"), "BoardSquare is missing attribute: x")
	self.assertTrue(hasattr(s,"y"), "BoardSquare is missing attribute: y")
	self.assertTrue(s.x is None, "BoardSquare x should be None by default")
	self.assertTrue(s.y is None, "BoardSquare y should be None by default")
	s.setX(9)
	self.assertTrue(s.x is None, "BoardSquare setter should not allow illegal locations.")
	s.setX(0)
	self.assertTrue(s.x is None, "BoardSquare setter should not allow illegal locations.")
	s.setX(1)
	self.assertTrue(s.x == 1, "BoardSquare setter should allow legal locations.")
	s.setX(100)
	self.assertTrue(s.x is None, "BoardSquare setter should not allow illegal locations.")
	s.setY(9)
	self.assertTrue(s.y is None, "BoardSquare setter should not allow illegal locations.")
	s.setY(0)
	self.assertTrue(s.y is None, "BoardSquare setter should not allow illegal locations.")
	s.setY(1)
	self.assertTrue(s.y == 1, "BoardSquare setter should allow legal locations.")
	s.setY(100)
	self.assertTrue(s.y is None, "BoardSquare setter should not allow illegal locations.")
#END OF THE BALL!!!1#
    def test_BoardSquareOccupied(self):
        s = ChessBoard.BoardSquare()
	# Temporarily removing this and inserting a replacement test that works with pythons under 2.7
        #self.assertIsNone(s.piece, "BoardSquare piece should be None by default") 
	# This is the replacement
	self.assertTrue(s.piece is None, "BoardSquare piece should be None by default")
        self.assertTrue(hasattr(s,"isOccupied"), "The isOccupied function does not exist")
        self.assertTrue(not s.isOccupied(), "The BoardSquare should be empty, but isOccupied returned true")
        s.piece = ChessBoard.Piece()
        self.assertTrue(s.isOccupied(), "The BoardSquare should be occupied, but isOccupied returned false")
        
    #Piece
    def test_PieceColor(self):
        b = ChessBoard.Piece()
        self.assertFalse(b.color is None)
        
if __name__ == '__main__':
    unittest.main()

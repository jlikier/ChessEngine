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
        
    def test_BoardSquareOccupied(self):
        s = ChessBoard.BoardSquare()
        self.assertIsNone(s.piece, "BoardSquare piece should be None by default")
        self.assertTrue(hasattr(s,"IsOccupied"), "The isOccupied function does not exist")
        self.assertTrue(not s.isOccupied(), "The BoardSquare should be empty, but isOccupied returned true")
        s.piece = ChessBoard.Piece()
        self.assertTrue(s.isOccupied(), "The BoardSquare should be occupied, but isOccupied returned false")
        
    #Piece
    def test_PieceColor(self):
        b = ChessBoard.Piece()
        self.assertFalse(b.color is None)
        
if __name__ == '__main__':
    unittest.main()

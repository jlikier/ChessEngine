import unittest
import ChessBoard

class ChessBoardTest(unittest.TestCase):
    def test_ChessBoardSize(self):
        b = ChessBoard.Board()
        self.assertEqual(len(b.squares),64)
    def test_PieceColor(self):
	b = ChessBoard.Piece()
	self.assertFalse(b.color is None)
    
if __name__ == '__main__':
    unittest.main()

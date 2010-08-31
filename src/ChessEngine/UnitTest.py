import unittest
import ChessBoard

class ChessBoardTest(unittest.TestCase):
    def test_ChessBoardSize(self):
        b = ChessBoard.Board()
        self.assertEqual(len(b.Squares),64)
    
if __name__ == '__main__':
    unittest.main()
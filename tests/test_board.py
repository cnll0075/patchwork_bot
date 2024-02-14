import unittest
from src.game_components.board import PlayerBoard, CommunalBoard
from src.game_components.tertrominos import Tetromino

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = PlayerBoard(3)
        self.t = Tetromino(1, [[1, 0, 0], [1, 1, 1]], 1, 1, 1)
    
    def test_place_tetromino(self):
        self.board.place_tetromino(self.t, 0, 0)
        self.assertEqual(self.board.board, [[1, 0, 0], [1, 1, 1], [0, 0, 0]])
        self.assertEqual(self.board.tetromino_list, [1])
        self.assertEqual(self.board.board_income, 1)
    
    def test_place_tetromino_cannot_exceed_board_border(self):
        with self.assertRaises(ValueError) as cm:
            self.board.place_tetromino(self.t, 1, 1)
        self.assertEqual(str(cm.exception), "Tetromino cannot be placed outside the board")
        self.assertEqual(self.board.tetromino_list, [])
        self.assertEqual(self.board.board_income, 0)
    
    def test_place_tetromino_cannot_cover_existing_tetromino(self):
        t1 = Tetromino(2, [[1, 0], [1, 1]], 1, 1, 3)
        self.board.place_tetromino(t1, 0, 0)
        with self.assertRaises(ValueError) as cm:
            self.board.place_tetromino(self.t, 0, 0)
        self.assertEqual(str(cm.exception), "Tetromino cannot cover existing tetromino")
        self.assertEqual(self.board.tetromino_list, [2])
        self.assertEqual(self.board.board_income, 3)
    
    def test_total_empty_cells(self):
        self.assertEqual(self.board.total_empty_cells(), 9)
        self.board.place_tetromino(self.t, 0, 0)
        self.assertEqual(self.board.total_empty_cells(), 5) 


class TestCommunalBoard(unittest.TestCase):
    def setUp(self):
        self.board = CommunalBoard.create()

    def test_move_player(self):
        self.board.move_player_tracker("red", 5)
        self.assertEqual(self.board.player_red_pos, 5)

        self.board.move_player_tracker("blue", 3)
        self.assertEqual(self.board.player_blue_pos, 3)

    def test_move_pawn(self):
        initial_pawn_loc = self.board.pawn_loc
        initial_tetromino_count = len(self.board.tetromino_list)
        self.board.move_pawn(2)
        self.assertEqual(self.board.pawn_loc, initial_pawn_loc + 2)
        self.assertEqual(len(self.board.tetromino_list), initial_tetromino_count - 1)
        with self.assertRaises(ValueError):
            self.board.move_pawn(4)
        
        self.board.pawn_loc = len(self.board.tetromino_list) 
        self.board.move_pawn(1)
        self.assertEqual(len(self.board.tetromino_list), initial_tetromino_count - 2)
        self.assertEqual(self.board.pawn_loc, 1)

if __name__ == '__main__':
    unittest.main()
    
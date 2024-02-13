import unittest
from src.game_components.tertrominos import Tetromino, load_all_tetrominos

piece_id = 1
time_cost = 1
button_cost = 1
income = 1

class TestTetromino(unittest.TestCase):
    def setUp(self):
        self.t = Tetromino(piece_id, [[1, 0, 0], [1, 1, 1]], time_cost, button_cost, income)

    def test_rotate_clockwise(self):
        self.t.rotate_clockwise()
        self.assertEqual(self.t.shape_matrix, [(1, 1), (1, 0), (1, 0)])

    def test_rotate_counterclockwise(self):
        self.t.rotate_counterclockwise()
        self.assertEqual(self.t.shape_matrix, [(0, 1), (0, 1), (1, 1)])

    def test_flip_horizontal(self):
        self.t.flip_horizontal()
        self.assertEqual(self.t.shape_matrix, [[0, 0, 1], [1, 1, 1]])

    def test_flip_vertical(self):
        self.t.flip_vertical()
        self.assertEqual(self.t.shape_matrix, [[1, 1, 1], [1, 0, 0]])

class TestLoadAllTetrominos(unittest.TestCase):
    def test_load_all_tetrominos(self):
        tetrominos = load_all_tetrominos()
        self.assertEqual(len(tetrominos), 33)
        self.assertEqual(tetrominos[-2].piece_id, 32)
        self.assertEqual(tetrominos[-2].time_cost, 5)
        self.assertEqual(tetrominos[-2].button_cost, 10)
        self.assertEqual(tetrominos[-2].income, 2)
        self.assertEqual(tetrominos[-2].shape_matrix, [[1, 1, 1, 1], [0, 0, 1, 1]])

if __name__ == '__main__':
    unittest.main()
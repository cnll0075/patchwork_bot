from src.game_components.tertrominos import Tetromino, load_all_tetrominos

all_tetrominos = load_all_tetrominos()

class PlayerBoard:
    """
        Individual player's board
    """
    def __init__(self, size=9):
        self.size = size
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self._tetromino_list = []
        self._board_income = 0
    
    def place_tetromino(self, tetromino, row, col):
        if tetromino.piece_id not in [t.piece_id for t in all_tetrominos]:
            raise ValueError("Invalid tetromino")
        if tetromino.piece_id in self._tetromino_list:
            raise ValueError("Tetromino already placed in current board")
        # Place the tetromino on the board at specified position
        if row < 0 or col < 0 or row + len(tetromino.shape_matrix) > self.size or col + len(tetromino.shape_matrix[0]) > self.size:
            raise ValueError("Tetromino cannot be placed outside the board")

        for r in range(len(tetromino.shape_matrix)):
            for c in range(len(tetromino.shape_matrix[0])):
                if tetromino.shape_matrix[r][c]:
                    if self.board[row + r][col + c]:
                        raise ValueError("Tetromino cannot cover existing tetromino")
                    self.board[row + r][col + c] = 1
        self._tetromino_list.append(tetromino.piece_id)
        self._board_income += tetromino.income

    @property
    def board_income(self):
        return self._board_income
    
    @property
    def tetromino_list(self):
        return self._tetromino_list
    
    def total_empty_cells(self):
        return sum([row.count(0) for row in self.board])


class CommunalBoard():
    """
        The board for tracking progress and income
    """
    def __init__(self, player_1_pos, player_2_pos, additional_patch_taken = [False for _ in range(5)]):
        self.length = 53
        self.income_step = [4, 10, 17, 22, 28, 34, 41, 47, 52]
        self.additional_patch_step = [26, 32, 38, 44, 50]
        self.additiona_patch_taken = additional_patch_taken
        self.player_1_pos = player_1_pos
        self.player_2_pos = player_2_pos

    def move_player(self, player, steps):
        if player == 1:
            self.player_1_pos += steps
        else:
            self.player_2_pos += steps
        return self.player_1_pos, self.player_2_pos

    

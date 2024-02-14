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
        The board for tracking progress and income, as well as the tetromino circle.
        Should be used as a singleton class.
    """
    _instance = None

    @staticmethod
    def create(tetromino_list = all_tetrominos, pawn_loc = 0, player_red_pos=0, player_blue_pos=0, additional_patch_taken=[]):
        if additional_patch_taken is None:
            additional_patch_taken = [False for _ in range(5)]
        if CommunalBoard._instance is None:
            CommunalBoard._instance = CommunalBoard(tetromino_list, pawn_loc, player_red_pos, player_blue_pos, additional_patch_taken)
        return CommunalBoard._instance

    def __init__(self, tetromino_list = all_tetrominos, pawn_loc = 0, player_red_pos=0, player_blue_pos=0, additional_patch_taken=[]):
        if CommunalBoard._instance is not None:
            raise Exception("Should not create another instance of the singleton class")

        self.length = 53
        self.income_step = [4, 10, 17, 22, 28, 34, 41, 47, 52]
        self.additional_patch_step = [26, 32, 38, 44, 50]
        self.additional_patch_taken = additional_patch_taken
        self.player_red_pos = player_red_pos
        self.player_blue_pos = player_blue_pos
        self.tetromino_list = tetromino_list
        self.pawn_loc = pawn_loc

    def move_player_tracker(self, player, steps):
        if player == 'red':
            self.player_red_pos += steps
        else:
            self.player_blue_pos += steps
        return self.player_red_pos, self.player_blue_pos
    
    def move_pawn(self, steps):
        if steps >= 3:
            raise ValueError("Pawn cannot move more than 3 steps")
        self.pawn_loc += steps

        if self.pawn_loc >= len(self.tetromino_list):
            ### has made a full loop
            self.pawn_loc -= len(self.tetromino_list)
        tetromino_taken = self.tetromino_list.pop(self.pawn_loc)
        return tetromino_taken
    
    def take_additional_patch(self, position):
        self.additional_patch_taken.append(position)


    

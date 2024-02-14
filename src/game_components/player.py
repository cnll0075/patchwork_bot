class Player:
    def __init__(self, color, player_board, postion_on_communal_board, income=0):
        self.color = color
        self.player_board = player_board
        self.postion_on_communal_board = postion_on_communal_board
        self.income = income

    def make_a_move(self, step, communal_board):
        ## make a valid move
        chosen_tetromino = communal_board.move_pawn(step)
        


    def _place_tetromino(self, tetromino, x, y):
        # self.player_board.place_tetromino(tetromino, x, y)
        # self.income += tetromino.income
        pass
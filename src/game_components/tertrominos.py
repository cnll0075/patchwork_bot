import csv
import os


class Tetromino:
    def __init__(self, piece_id, shape_matrix, button_cost, time_cost, income):
        self.piece_id = piece_id
        self.shape_matrix = shape_matrix
        self.time_cost = time_cost
        self.button_cost = button_cost
        self.income = income

    def rotate_clockwise(self):
        # Rotate the shape matrix clockwise
        self.shape_matrix = list(zip(*self.shape_matrix[::-1]))

    def rotate_counterclockwise(self):
        # Rotate the shape matrix counterclockwise
        self.shape_matrix = list(zip(*self.shape_matrix))[::-1]
    
    def flip_horizontal(self):
        # Flip the shape matrix horizontally
        self.shape_matrix = [row[::-1] for row in self.shape_matrix]

    def flip_vertical(self):
        # Flip the shape matrix vertically
        self.shape_matrix = self.shape_matrix[::-1]

def load_all_tetrominos():
    tertrominos = []
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'tetrominos.csv')
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                piece_id, shape, time_cost, button_cost, income = row[:-1]
                shape = [[int(num.strip()) for num in row.split(',') if num] for row in shape.strip('"').split(';')]
                t = Tetromino(int(piece_id), shape, int(time_cost), int(button_cost), int(income))
                tertrominos.append(t)
    except FileNotFoundError:
        print("{file_path} does not exist.")
    return tertrominos



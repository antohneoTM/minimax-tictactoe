"""
    File: draw_game.py
    Vers: 3.12.5
    Desc: Draws board of the tic-tac-toe game
    Dev:  Antonio Camacho
"""


import pygame as pg

BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)
BLUE: tuple = (0, 0, 255)
GREEN: tuple = (0, 255, 0)
RED: tuple = (255, 0, 0)


class DrawGame:
    """Draw the various elements of the tic-tac-toe game"""

    def __init__(self, game: object, win_size: tuple, num_grid: int) -> None:
        self.game = game  # instance of 'Game' class in main.py
        self.win_size = self.window_width, self.window_height = win_size
        self.num_grid = num_grid
        self.grid_size: int = self.window_width // self.num_grid

    def draw_board(self) -> None:
        """Draws blank board game board"""

        self.game.screen.fill(WHITE)

        for row in range(0, self.window_width, self.grid_size):
            for col in range(0, self.window_height, self.grid_size):
                grid_rect = pg.Rect(row, col, self.grid_size, self.grid_size)
                pg.draw.rect(self.game.screen, BLACK, grid_rect, 1)

    def draw_circle(self, grid_coord: list) -> None:
        """Draws circle at selected move"""

        x = (grid_coord[0] * self.grid_size) + (self.grid_size / 2)
        y = (grid_coord[1] * self.grid_size) + (self.grid_size / 2)
        pg.draw.circle(self.game.screen, BLUE, (x, y), self.grid_size * .4, 5)

    def draw_cross(self, grid_coord: list) -> None:
        """Draws a cross at the selected move. Uses 2 diagonal lines"""

        x_l = (grid_coord[0] * self.grid_size) + (0.1 * self.grid_size)
        x_r = (grid_coord[0] * self.grid_size) + (0.9 * self.grid_size)
        y_t = (grid_coord[1] * self.grid_size) + (0.1 * self.grid_size)
        y_b = (grid_coord[1] * self.grid_size) + (0.9 * self.grid_size)

        # First line diagonal down
        pg.draw.line(self.game.screen, GREEN, (x_l, y_t), (x_r, y_b), 5)
        # Second  line diagonal up
        pg.draw.line(self.game.screen, GREEN, (x_l, y_b), (x_r, y_t), 5)

    def draw_score_line(self, win_sequence: list) -> None:
        """Draws a line across the winning sequence of moves"""

        x_1 = win_sequence[0][0] * self.grid_size + (self.grid_size / 2)
        y_1 = win_sequence[0][1] * self.grid_size + (self.grid_size / 2)
        x_2 = win_sequence[2][0] * self.grid_size + (self.grid_size / 2)
        y_2 = win_sequence[2][1] * self.grid_size + (self.grid_size / 2)
        # print([x_1, y_1], [x_2, y_2])

        for i in range(10):
            pg.draw.line(self.game.screen, RED, (x_1, y_1), (x_2, y_2), 10)

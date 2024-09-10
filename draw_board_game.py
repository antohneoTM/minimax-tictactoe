"""
    File: drawBoardGame.py
    Vers: 3.12.5
    Desc: Draws board of the tic-tac-toe game
    Dev:  Antonio Camacho
"""

import pygame as pg

BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)


class DrawGame:
    """Draw the various elements of the tic-tac-toe game"""

    def __init__(self, game: object, win_size: tuple, num_grid: int) -> None:
        self.game = game  # instance of 'Game' class in mainTTT.py
        self.win_size = self.window_width, self.window_height = win_size
        self.num_grid = num_grid

    def draw_board(self) -> None:
        """Draws the game board"""
        self.game.screen.fill(WHITE)
        self.grid_size: int = self.window_width // self.num_grid

        for row in range(0, self.window_width, self.grid_size):
            for col in range(0, self.window_height, self.grid_size):
                grid_rect = pg.Rect(row, col, self.grid_size, self.grid_size)
                pg.draw.rect(self.game.screen, BLACK, grid_rect, 1)

    def run(self):
        self.draw_board()

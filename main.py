"""
    File: main.py
    Vers: 3.12.5
    Desc: Main file for tic-tac-toe minimax game
    Dev:  Antonio Camacho
"""

import sys

import pygame as pg

import game_status as gs
from draw_board_game import DrawGame


class Game:
    """Class to loop and run the tic tac toe game"""

    def __init__(self) -> None:
        self.win_size = (900, 900)
        self.num_grid = 3
        self.board_state = []
        self.plyr_o_turn = True

        pg.init()  # Initializes pygame package
        self.screen = pg.display.set_mode(self.win_size)  # pygame window size
        pg.display.set_caption("Cool Title")  # TODO: Good game title
        self.clock = pg.time.Clock()
        gs.empty_board_state(self.board_state, self.num_grid)
        self.draw_game = DrawGame(self, self.win_size, self.num_grid)

    def change_window_size(self, event) -> None:
        """Changes window size based on user input"""
        if event.key == pg.K_1:
            self.win_size = (600, 600)
            self.screen = pg.display.set_mode(self.win_size)
            self.draw_game = DrawGame(self, self.win_size, self.num_grid)
        elif event.key == pg.K_2:
            self.win_size = (900, 900)
            self.screen = pg.display.set_mode(self.win_size)
            self.draw_game = DrawGame(self, self.win_size, self.num_grid)
        elif event.key == pg.K_3:
            self.win_size = (1200, 1200)
            self.screen = pg.display.set_mode(self.win_size)
            self.draw_game = DrawGame(self, self.win_size, self.num_grid)

    def change_grid_size(self, event) -> None:
        """Changes grid size based on user input"""
        if event.key == pg.K_q:
            self.num_grid = 3
            self.draw_game = DrawGame(self, self.win_size, self.num_grid)
            gs.empty_board_state(self.board_state, self.num_grid)
        elif event.key == pg.K_w:
            self.num_grid = 4
            self.draw_game = DrawGame(self, self.win_size, self.num_grid)
            gs.empty_board_state(self.board_state, self.num_grid)
        elif event.key == pg.K_e:
            self.num_grid = 5
            self.draw_game = DrawGame(self, self.win_size, self.num_grid)
            gs.empty_board_state(self.board_state, self.num_grid)

    def grid_coord(self, win_size: int, num_grid: int) -> tuple:
        """Determines where on game grid user clicked"""
        mouse_coord = pg.mouse.get_pos()
        sel_x = int(mouse_coord[0] // (win_size // num_grid))
        sel_y = int(mouse_coord[1] // (win_size // num_grid))
        return [sel_x, sel_y]

    def check_events(self) -> None:
        """Check for inputs from user within pygame window"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.close_game()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.close_game()
                self.change_window_size(event)
                self.change_grid_size(event)
            if event.type == pg.MOUSEBUTTONUP:
                grid_coord = self.grid_coord(self.win_size[0], self.num_grid)
                gs.update_board(self.board_state, grid_coord, self.plyr_o_turn)
                self.plyr_o_turn = not self.plyr_o_turn
                # gs.change_turn(self.player_o_turn)

    def close_game(self) -> None:
        pg.quit()
        sys.exit()

    def run(self) -> None:
        while True:
            self.draw_game.run()
            self.check_events()  # Check for inputs
            pg.display.update()  # Displays any changes to screen
            self.clock.tick(30)  # Locks framerate to 30FPS


# Executes game
if __name__ == "__main__":
    game = Game()
    game.run()

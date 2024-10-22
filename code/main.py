"""
    File: main.py
    Vers: 3.12.5
    Desc: Main  file for the tic-tac-toe minimax game
    Dev:  Antonio Camacho
"""

import math
import sys
from pathlib import Path

import pygame as pg

import change_game_settings as cgs
import game_status as gs
from draw_game import DrawGame as dg


class Game:
    """Class to loop and run the tic tac toe game"""

    def __init__(self) -> None:
        self.win_size: tuple = (780, 780)
        self.num_grid: int = 3
        self.board: list = []
        self.game_mode: str = "modern"
        self.depth: int = 9

        # Bools for the state of the game
        self.game_started: bool = False
        self.game_over: bool = False

        # Player turn variables
        self.first_player: int = 1
        self.ai_goal: int = 1
        self.player: int = self.first_player

        # Initialize pygame
        pg.init()
        self.screen = pg.display.set_mode(self.win_size)

        # Load icon image
        script_dir = Path(__file__).parent
        icon_path = script_dir.parent / 'images' / 'temp-icon.png'
        icon_image = pg.image.load(str(icon_path))
        pg.display.set_icon(icon_image)

        self.clock = pg.time.Clock()

        pg.display.set_caption("\'X\' Turn")
        gs.empty_board(self.board, self.num_grid)
        self.vm = gs.valid_moves(self.board)
        self.dg = dg(self, self.win_size, self.num_grid)
        cgs.print_controls(self)

    # User key presses and mouse clicks
    def check_events(self) -> None:
        """Check for inputs from user within pygame window"""

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.close_game()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    cgs.reset_game(self)
                if event.key == pg.K_p:
                    cgs.print_controls(self)
                cgs.change_window_size(self, event)
                cgs.change_grid_size(self, event)
                cgs.change_game_mode(self, event)
                cgs.change_minimax_depth(self, event)
                cgs.change_ai_turn(self, event)
                cgs.print_current_settings(self, event)

                if event.key == pg.K_ESCAPE:
                    self.close_game()

            if event.type == pg.MOUSEBUTTONUP:
                self.game_started = True

                if self.player == self.ai_goal:
                    self.play_ai()
                    return None
                self.human_turn()

    def human_turn(self) -> None:
        """Plays human turn based on where they clicked"""

        if self.game_over:
            print("Game is over, cannot make a move")
            return None

        # Get coordinates of the mouse click
        grid_coord = self.get_coord(self.win_size[0], self.num_grid)
        # print(grid_coord, type(grid_coord))

        # Don't do anything if move has already been played
        if (grid_coord) not in gs.valid_moves(self.board):
            print("Please select a valid move")
            return None

        # Update board with the move and draw move
        self.board = gs.play_move(self.board, grid_coord, self.player)
        if (self.player == 1):
            self.dg.draw_cross(grid_coord)
        elif (self.player == -1):
            self.dg.draw_circle(grid_coord)

        self.determine_winner()

    # Plays AI turn
    def play_ai(self) -> None:
        """Plays AI turn using minimax algorithm"""

        if self.game_over:
            return None

        max_agent: bool = None
        if self.ai_goal == 1:
            max_agent = True
        elif self.ai_goal == -1:
            max_agent = False

        score, ai_move = gs.minimax(self.board, self.depth, max_agent,
                                    self.game_mode, -math.inf, math.inf)

        self.board = gs.play_move(self.board, ai_move, self.player)
        if (self.player == 1):
            self.dg.draw_cross(ai_move)
        elif (self.player == -1):
            self.dg.draw_circle(ai_move)

        self.determine_winner()

    def get_coord(self, ws: int, ng: int) -> list:
        """Determines where on game grid the user clicked"""

        mouse_coord = pg.mouse.get_pos()
        x = int(mouse_coord[0] // (ws // ng))
        y = int(mouse_coord[1] // (ws // ng))
        return [x, y]

    def determine_winner(self) -> None:
        """Determines if there is a winner of the game. If not switch turn.
        If there is, then calcuate final scores and print score lines"""

        # Checks for win
        self.game_over = gs.check_terminal(self.game_mode, self.board)
        if not self.game_over:
            cgs.change_player(self)
            return None

        score, sequence = gs.get_score(self.board)
        # Print score sequences
        for i in range(0, len(sequence), 1):
            self.dg.draw_score_line(sequence[i])

        # Set caption to announce the winner
        if score < 0:
            pg.display.set_caption("\'O' Wins")
        elif score > 0:
            pg.display.set_caption("\'X\' Wins")
        else:
            pg.display.set_caption("Tie")

    def close_game(self) -> None:
        """Notifys user, then closes application"""

        print("Thank you for playing Tic-Tac-Toe!\nClosing application...")
        pg.quit()
        sys.exit()

    def run(self) -> None:
        self.dg.draw_board()
        while True:
            pg.display.update()
            self.check_events()
            self.clock.tick(30)


if __name__ == "__main__":
    game = Game()
    game.run()

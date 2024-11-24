"""
    File: change_game_settings.py
    Vers: 3.12.5
    Desc: Changes game settings such as window size, grid size, and game mode
    Devs: Antonio Camacho
"""

import game_status as gs
import pygame as pg
from draw_game import DrawGame


def reset_game(game: object) -> None:
    """Resets the game back to an empty board"""

    print("Resetting game...")

    game.dg = DrawGame(game, game.win_size, game.num_grid)
    gs.empty_board(game.board, game.num_grid)
    game.dg.draw_board()

    game.game_over = False
    game.game_started = False

    game.player = game.first_player
    pg.display.set_caption("\'X\' Turn")

    game.valid_moves = gs.valid_moves(game.board)


def print_current_settings(game: object, event) -> None:
    """Prints the current game settings"""

    if event.key == pg.K_v:
        print("----------------")
        print("Current Settings")
        print("----------------")
        print("Window Size:", game.win_size)
        print("Number of Grids:", game.num_grid)
        print("Game Mode:", game.game_mode)
        if game.ai_goal == 1:
            print("Player \'X\': AI Player")
            print("Player \'O\': Human Player")
        elif game.ai_goal == 2:
            print("Player \'X\': Human Player")
            print("Player \'O\': AI Player")
        elif game.ai_goal == 0:
            print("Player \'X\': Human Player")
            print("Player \'O\': Human Player")
        else:
            print("WTF Happened")
        print("Minimax Search Depth:", game.depth)


def change_grid_size(game: object, event) -> None:
    """Changes grid size based on user input"""

    # Don't allow user to change size of window mid game
    if game.game_started:
        return None

    if event.key == pg.K_3:
        print("Change number of grids: 3")
        game.num_grid = 3
        reset_game(game)

    elif event.key == pg.K_4:
        print("Change number of grids: 4")
        game.num_grid = 4
        reset_game(game)


def change_window_size(game: object, event) -> None:
    """Changes window size based on user input"""

    # Don't allow user to change size of window mid game
    if game.game_started:
        return None

    # Small window
    if event.key == pg.K_q:
        print("Changing window size: 600x600")
        game.win_size = (600, 600)
        game.screen = pg.display.set_mode(game.win_size)
        # Reset game afterwards
        reset_game(game)

    # Medium window
    elif event.key == pg.K_w:
        print("Changing window size: 780x780")
        game.win_size = (780, 780)
        game.screen = pg.display.set_mode(game.win_size)
        reset_game(game)

    # Large window
    elif event.key == pg.K_e:
        print("Changing window size: 900x900")
        game.win_size = (900, 900)
        game.screen = pg.display.set_mode(game.win_size)
        reset_game(game)


def change_game_mode(game: object, event) -> None:
    """Changes game mode based on user input"""

    # Don't allow user to change game mode mid game
    if game.game_started:
        return None

    # Classic
    if event.key == pg.K_c:
        print("Changing game mode to \'Classic\'")
        game.game_mode = "classic"

    # Modern
    if event.key == pg.K_m:
        print("Change game mode to \'Modern\'")
        game.game_mode = "modern"


def change_minimax_depth(game: object, event) -> None:
    """Changes the depth of the minimax algorithm"""

    # Decrement depth
    if event.key == pg.K_MINUS:
        if game.depth == 1:
            print("Minimum search depth already applied...")
            return None

        game.depth -= 1
        print("Changing search depth to:", game.depth)

    # Increment depth
    if event.key == pg.K_EQUALS:
        if game.depth == 12:
            print("Maximum search depth already applied...")
            return None

        game.depth += 1
        print("Changing search depth to:", game.depth)


def change_ai_turn(game: object, event) -> None:
    """Changes whether the AI plays first or second"""

    if event.key == pg.K_1:
        print("AI will go first")
        game.ai_goal = 1

    elif event.key == pg.K_2:
        print("AI will go second")
        game.ai_goal = -1

    elif event.key == pg.K_0:
        print("AI disabled")
        game.ai_goal = 0


def change_player(game: object) -> None:
    """Swaps players and prints it on window title"""

    game.player = game.player * -1
    if game.player == -1:
        pg.display.set_caption("\'O\' Turn")
    elif game.player == 1:
        pg.display.set_caption("\'X\' Turn")


def print_controls(game: object) -> None:
    """Prints the game's controls in the terminal"""

    print("\nWelcome to Minimax Tic-Tac-Toe")
    print("------------------------------")
    print("Left mouse click on grid to start a game")
    print("Click on empty space to make a move")
    print("Click on AI turn to begin minimax algorithm search")
    print("Q, W, E: Change window size")
    print("3, 4: Change number of grids")
    print("C, M: Change game mode")
    print("1, 2: Switch AI turn order (Enables AI if disabled)")
    print("-, = : Change minimax algorithm search depth")
    print("0: Disable AI")
    print("R: Reset the current game")
    print("V: Print current settings")
    print("P: Reprint these controls")

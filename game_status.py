"""
    File: game_status.py
    Vers: 3.12.5
    Desc: Contains information regarding the current state of the game
    Dev:  Antonio Camacho
"""

import numpy as np  # Vers: 1.26.4

# win_size: tuple = (900, 900)  # Size of the game window
# num_grid: int = 3  # Size of the game board
# board_state: list = []  # 2D array of the current state of the game board
# player_o_turn: bool = False

# Colors used for the game
BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)


def empty_board_state(board_state: list, num_grid: int) -> None:
    """Fills the 2D array for game board based on the grid size"""
    board_state.clear()
    for i in range(num_grid):
        board_state.append([])
        for j in range(num_grid):
            board_state[i].append(0)
    print(np.array(board_state))


def update_board(board_state: list, move: tuple, player_o_turn: bool) -> None:
    """Fills the board game with a move a player chooses"""
    x, y = move[0], move[1]
    board_state[y][x] = 1 if player_o_turn else -1
    print("Updated Board State:")
    print(np.array(board_state))


def change_turn(player_o_turn: bool):
    player_o_turn = not player_o_turn
    print(player_o_turn)

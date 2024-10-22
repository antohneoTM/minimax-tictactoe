"""
    File: game_status.py
    Vers: 3.12.5
    Desc: Contains information regarding the current state of the game
    Dev:  Antonio Camacho
"""

import math


def check_terminal(gm: bool, bs: list) -> bool:
    """Check current state of the game board and return bool"""

    if gm == "modern" and check_board_filled(bs):
        return True

    if gm == "classic":
        score, _ = get_score(bs)
        if score != 0 or check_board_filled(bs):
            return True

    return False


def empty_board(bs: list, ng: int) -> None:
    """Fills the 2D array for game board based on the grid size"""

    bs.clear()

    for i in range(ng):
        bs.append([])
        for j in range(ng):
            bs[i].append(0)
    # print(np.array(bs))


def play_move(bs: list, move: list, player: int) -> list:
    """Plays the move based on the player"""

    bs[move[1]][move[0]] = player
#     print("Old Board:")
#     print(np.array(bs))
#     print("Updated Board:")
#     print(np.array(new_board))

    return bs


def valid_moves(bs: list) -> list:
    """Gets list of valid moves from current board"""

    moves = []

    for x in range(len(bs)):
        for y in range(len(bs)):
            if (bs[x][y] == 0):
                moves.append([y, x])

    return moves


def check_board_filled(bs: list) -> bool:
    """Returns true if there are no more playable moves left on board"""

    moves = valid_moves(bs)

    if len(moves) == 0:
        return True

    return False


def get_score(bs: list) -> (int, list):
    """Calcuates score of board. Looks for 3 in a row in any direction"""

    total_score: int = 0
    score_sequence: list = []

    # Check vertical and horizontal score
    for x in range(len(bs)):
        for y in range(len(bs) - 2):
            # Vertical score
            if bs[y][x] == bs[y+1][x] == bs[y+2][x] != 0:
                score_sequence.append(([x, y], [x, y+1], [x, y+2]))
                total_score += bs[y][x]

            # Horizontal score
            if bs[x][y] == bs[x][y+1] == bs[x][y+2] != 0:
                score_sequence.append(([y, x], [y+1, x], [y+2, x]))
                total_score += bs[x][y]

    # Check diagonal scores
    for x in range(len(bs) - 2):
        # Diagonal down score
        for y in range(len(bs) - 2):
            if bs[x][y] == bs[x+1][y+1] == bs[x+2][y+2] != 0:
                score_sequence.append(([y, x], [y+1, x+1], [y+2, x+2]))
                total_score += bs[x][y]

        # Diagonal up score
        for j in range(len(bs)-1, 1, -1):
            if bs[x][j] == bs[x+1][j-1] == bs[x+2][j-2] != 0:
                score_sequence.append(([j, x], [j-1, x+1], [j-2, x+2]))
                total_score += bs[x][j]

    return (total_score, score_sequence)


def minimax(bs: list, depth: int, mp: bool, gm, alpha, beta) -> (int, list):
    """Minimax algorithm with alpha-beta prunning"""
    # print(np.array(bs))
    # print(depth)

    # If reached the maximum depth, then stop searching further
    if depth <= 0:
        score = get_score(bs)
        return score[0], None

    # Stops searching further if win conditions have been met
    if gm == "classic":
        score = get_score(bs)

        if score[0] != 0:
            return score[0], None
        elif check_board_filled(bs):
            return score[0], None

    elif gm == "modern" and check_board_filled(bs):
        score = get_score(bs)

        return score[0], None

    # Beginning of actual minimax integration
    if mp:
        best_value = -math.inf
        best_move = None

        for move in valid_moves(bs):
            bs = play_move(bs, move, player=1)

            current_value, _ = minimax(bs, depth-1, False, gm, alpha, beta)

            # Undo the move, so its not permenant
            bs = play_move(bs, move, player=0)

            if current_value > best_value:
                best_value = current_value
                best_move = move

            # Prune
            alpha = max(alpha, current_value)
            if beta <= alpha:
                break

        # print(best_value, best_move)
        return best_value, best_move

    else:
        best_value = math.inf
        best_move = None

        for move in valid_moves(bs):
            bs = play_move(bs, move, player=-1)

            current_value, _ = minimax(bs, depth-1, True, gm, alpha, beta)

            # Undo move
            bs = play_move(bs, move, player=0)

            if current_value < best_value:
                best_value = current_value
                best_move = move

            # Prune
            beta = min(beta, current_value)
            if beta <= alpha:
                break

        # print(best_value, best_move)
        return best_value, best_move

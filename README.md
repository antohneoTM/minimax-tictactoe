# Minimax Tic-Tac-Toe (With Alpha-Beta Pruning)
Developed by: Antonio Camacho\
Email: camacho.ant.626@gmail.com\
LinkedIn: <a href="https://www.linkedin.com/in/antcamacho" target="_blank>">/in/antcamacho</a>

## About
Version of the classic Tic-Tac-Toe board game written in Python with the goal to demonstrate the effectiveness of the alpha-beta pruning AI algorithm.\
<a href="https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning" target="_blank">More about Alpha-Beta Pruning</a>

This highly configurable version of Tic-Tac-Toe lets you adjust the game in many ways!\
In this game a human player is tasked to take down a powerful AI powered opponent or another human player.
You can also change game modes from the *"classic"* 3-in-a-row style to a *"modern"* fill the board mode.
The option to change the depth that the algorithm searches is available as well, so **you** can push the AI to its *limits*.

## Instructions
### Requirements
- Project files from this repo:\
    `git clone git@github.com:antohneoTM/minimax-tictactoe.git`

- Python 3.8+

    To install the latest version of Python go to:\
    <a href="https://www.python.org/downloads" target="_blank">python.org/downloads</a>

- Python Package(s):
    - pygame 2.6.1+\
        <a href="https://www.pypi.org/project/pygame" target="_blank">Check it out here</a>

        To install pygame onto your Python enviroment run this command in the project's root directory:\
        `pip install -r requirements.txt`

        or:\
        `pip install pygame`

### How to run
1. Open the project's root directory in a terminal
2. Active your Python environment
3. Make sure pygame package is installed and check for compatible version\
    `pip list`

    Should give an output like:
    ```
    Package Version
    ------- -------
     pip     24.2
     pygame  2.6.1
    ```
4. In the project's root directory run:\
    `python3 code/main.py`
5. Enjoy some Tic-Tac-Toe!

### Controls
- Left click on grid to start a game.

- During a human player's turn:
    - Click on an empty space to make move.

- During an AI player's turn:
    - Click anywhere on grid to begin Alpha-Beta pruning search.
    - Please note that when the search depth and grid size is increased it may take a few minutes for the alogirthm to complete.

- `Q`, `W`, `E`: Change Window Size (600x600 px, 780x780 px, 900x900 px)
- `3`, `4`: Change number of playable grids (3x3 or 4x4)
- `C`, `M`: Change game mode ('Classic' or 'Modern')
    - Classic: First player to 3 in-a-row.
    - Modern: Play until entire board is filled. Player with the most 3 in-a-rows wins.
- `1`, `2`: Switch AI turn order (Enables AI if disabled)
- `0`: Disables AI player. Human versus human.
- `-`, `=`: Change Alpha-Beta pruning algorithm search depth.
    - Minimum: 1
    - Maximum: 12
        - The larger the search depth the longer it will take to finish the search.
- `R`: Reset the game to an empty state
- `V`: Print current game settings in terminal
- `P`: Reprint controls in terminal

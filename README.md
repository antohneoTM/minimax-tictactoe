# Minimax Tic-Tac-Toe (With Alpha-Beta Pruning)
Developed by: Antonio Camacho

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

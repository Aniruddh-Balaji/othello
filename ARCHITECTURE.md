# Architecture of the program
This file contains the architecture of the program, which is everything anyone has to know in order to contribute(or to just understand the codebase entirely).

We have taken an entirely function-based approach to this project; we don't use OOPs.

The filesystem is split as:
```
.
├── .git
│   ├── 
│   └── (truncated)
├── .gitignore
├── ARCHITECTURE.md
├── LICENSE
├── README.md
└── src
    ├── board.py
    ├── cli.py
    ├── game_logic.py
    ├── gui.py
    └── save.txt

```
(This is the output of `tree .` from the root of this project.)

The important parts related to the python project are within the `src/` folder.

## Some important variables
Here, I'll outline a couple important variables that are used throughout the program.
- `state`: This represents the 2D list in which we store the current state of the game.
  It is also maintained in `src/save.txt` as a 2D grid. Empty squares are represented as `0`,
  whereas black coins are `1` and white coins are `2`. A sample initial state of the system
  would be(this is exactly what is stored in `save.txt`):
  ```
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 2 1 0 0 0
  0 0 0 1 2 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  0 0 0 0 0 0 0 0
  ```
- `color`: This is an integer that is either `1` or `2`. `1` represents black coin
  and `2` represents a white coin. It is also used to represent which player plays next.
  Integers are used here for simplification in the codebase, where we just do `3-color` to
  change the player.
- `d`: This is a dictionary that maps from the simplified coordinates of the board(eg: (0,1))
  to the exact coordinates in the TKinter window.
- `d1`: This dictionary maps from the simplified coordinates of the board to the coordinates
  of the diagonal points of each cell(to place the coins appropriately).
- `d2`: This mapping relates the buttons and the cells(simplified coordinates).

## Functions
Here, I'll go over the functions in each module(file).

### `board.py`
- `readsave()`: This function reads the save file `save.txt` and returns the state as a 2D list.
- `writesave(state, color)`: This function overwrites the save file with the current state `state`
  and maintains the `color`(i.e. whose chance is it next?) in the `save.txt` file.
- `resetsave()`: This function just sets the initial state of the game and writes it into `save.txt`
  using `writesave(..)`.

### `game_logic.py`
- `rowcheck(row, color)`: Takes a list `row` and the color `color` and returns the indices of all
  valid moves within that list. Since we are accepting lists in general, this is used for rows,
  columns and all diagonals to check(even though the name is _rowcheck_).
- `listmoves(state, color)`: Takes the current `state` and `color` and returns a `set` of all
  valid moves using `rowcheck()`. It basically iterates over every row, column and diagonal and
  figures out the valid moves.
- `rowmove(row, color, j)`: This function is also named weirdly(it works on any list).
  It takes in a list `row`, a `color` and a value `j`. This returns a list `ans` that tells us
  which all coins have to be turned over within a `row`(this can be used for columns and diagonals also).
  It basically tells us what our next list should be(given a move).
- `moves(state, color, x, y)`: This takes in the current `state`, `color` and the coin just placed as `x`,
  `y`, and returns the modified board. This uses `rowmove(..)`.
- `count(state)`: This takes in the `state` of the system and returns the number of white and black
  pieces in the board currently as a 2-element list.

### `cli.py`
This has no functions, and is just the looping required with inputs and it prints the corresponding material.

### `gui.py`
- `welcome_screen()`: Create root window with a Begin button. This is just the initial _welcome_ screen.
- `open_names_window()`: Removes the previous _welcome_ screen and makes another window that
  inputs the players' names. This contains an inner function `start_game()` in order to use that in
  the `Button()`.
- `initialize_game()`: Sets up the board from the `save.txt` file.
- `create_game_window()`: Places all the labels and the board grid.
- `draw_full_board()`: Draw coins according to the global `state` value.
- `put_coin(i, j, r)`: Place a coin at the cell `(i, j)` with color `r`(Black is `1` and White is `2`).
- `update_counts()`: Gets the count of the black and white pieces from `count(state)` in `game_logic.py` and
  displays it using labels on the screen.
- `clear_move_buttons()`: Destroy the all buttons placed after any move is made.
- `place_buttons(moves_set)`: Places buttons in the necessary locations.
- `on_move(pos)`: Updates the move using functions from `game_logic.py`.
- `next_turn()`: Uses the above functions to find the legal moves, place buttons, handle inputs and so on.

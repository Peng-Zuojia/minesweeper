# Minesweeper

## This project implements the classic game --  Minesweeper. 

## The project can be run using the following commands:

```shell
python3 -m venv ./venv
source ./venv/bin/activate
pip install pyglet
python main.py
deactivate
```

### Through terminal user input, user can determine the parameters of the game, for example the width and height of the mine field as well as the total amount of mines.

![User input paramenters](/pics/input.png)


### When a user opens a tile, the neighboring mines will be counted and shown. If the tile does not have any neighboring tiles, neighboring tiles will be opened as well and a border to the mines will be shown.

### User can also flag or unflag a tile as a mine.

![Game in progress](/pics/progress.png)
The game ends in two ways. Either way, the game statistics will be shown to the user.
1. When the user opens the mine, the game ends and the user loses.
2. When the user opens all the other tiles, the game ends and the user wins

![The game ends](/pics/won.png)

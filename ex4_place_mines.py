import random
from ex3 import count_ninjas
import sweeperlib

state = {
    "field": [],
    "initial": []
}  # game state

window = {
    "height": 0,
    "width": 0
}


# initialize the mine field
def place_mines(field_to_mine, tiles_lists, mines_number):
    selected = random.sample(tiles_lists, mines_number)
    for i in range(mines_number):
        x_co = selected[i][0]
        y_co = selected[i][1]
        field_to_mine[y_co][x_co] = 'x'
    state["initial"] = field_to_mine
    for draw_row in range(len(state["initial"])):
        for draw_col in range(len(state["initial"][draw_row])):
            if state["initial"][draw_row][draw_col] != "x":
                state["initial"][draw_row][draw_col] = "{}".format(count_ninjas(draw_col, draw_row, state["initial"]))

    window["height"] = len(state["initial"]) * 40
    window["width"] = len(state["initial"][0]) * 40

import datetime

import sweeperlib
from sweeperlib import MOUSE_RIGHT, MOUSE_LEFT
from ex4_place_mines import window, state, place_mines
from ex4_flood_fill import floodfill

game_statistics = {
    "time_1": 0,
    "time_2": 0,
    "duration": 0,
    "outcome": [],
    "remaining": []
}

safe_count = {
    "count": 0
}


# user determine dimensions and mines
def set_up(col, row, mines):
    safe_count["count"] = col * row - mines
    window["width"] = col * 40
    window["height"] = row * 40

    field_i = []
    for row_count in range(row):
        field_i.append([])
        for col_count in range(col):
            field_i[-1].append(" ")
    state["field"] = field_i

    field = []
    for row_count in range(row):
        field.append([])
        for col_count in range(col):
            field[-1].append(" ")

    available = []
    for x in range(col):
        for y in range(row):
            available.append((x, y))

    place_mines(field, available, mines)


def draw_initial():
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    sweeperlib.begin_sprite_draw()
    for draw_row in range(len(state["initial"])):
        for draw_col in range(len(state["initial"][draw_row])):
            sweeperlib.prepare_sprite(" ", draw_col * 40, window["height"] - (draw_row + 1) * 40)

    sweeperlib.draw_sprites()


def draw_field():  # draw handler function two-dimensional list -> game window
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    sweeperlib.begin_sprite_draw()
    count = 0
    for draw_row in range(len(state["field"])):
        for draw_col in range(len(state["field"][draw_row])):
            if state["field"][draw_row][draw_col] == "x":
                sweeperlib.close()
                sweeperlib.prepare_sprite("x", draw_col * 40, window["height"] - (draw_row + 1) * 40)
                game_statistics["outcome"].append("LOST")
                game_statistics["time_2"] = datetime.datetime.now().replace(microsecond=0)

            elif state["field"][draw_row][draw_col] == " ":
                sweeperlib.prepare_sprite(" ", draw_col * 40, window["height"] - (draw_row + 1) * 40)
            elif state["field"][draw_row][draw_col] == "0":
                sweeperlib.prepare_sprite("0", draw_col * 40, window["height"] - (draw_row + 1) * 40)
                count += 1
            elif state["field"][draw_row][draw_col] == "f":
                sweeperlib.prepare_sprite("f", draw_col * 40, window["height"] - (draw_row + 1) * 40)
            else:
                sweeperlib.prepare_sprite("{}".format(state["field"][draw_row][draw_col]), draw_col * 40,
                                          window["height"] - (draw_row + 1) * 40)
                count += 1

            if count == safe_count["count"]:
                sweeperlib.close()
                game_statistics["outcome"].append("WON")
                game_statistics["time_2"] = datetime.datetime.now().replace(microsecond=0)

    sweeperlib.draw_sprites()


def handle_mouse(x, y, button, modifier):
    # x -> col, y - > row
    # in a cell if x >= col * 40
    col = int(x / 40)
    row = int((window["height"] - y) / 40)
    if button == MOUSE_LEFT:
        if state["initial"][row][col] == '0':
            floodfill(state["initial"], col, row)

        else:
            if state["initial"][row][col] == ' ':
                pass
            else:
                state["field"][row][col] = state["initial"][row][col]
    else:
        if state["field"][row][col] == " ":
            state["field"][row][col] = 'f'
        elif state["field"][row][col] == "f":
            state["field"][row][col] = " "

    sweeperlib.set_draw_handler(draw_field)


def main():
    sweeperlib.load_sprites("sprites")
    sweeperlib.create_window(window["width"], window["height"])
    sweeperlib.set_draw_handler(draw_initial)

    sweeperlib.set_mouse_handler(handle_mouse)

    sweeperlib.start()


if __name__ == "__main__":
    print("Welcome to Minesweeper")
    print("1. Play")
    print("2. Quit")
    #   print("3. Statistics\n")
    while True:
        choice = int(input("Input the number: "))
        if choice == 1:
            col_defined = int(input("Determine the width: "))
            row_defined = int(input("Determine the height: "))
            mine_number = int(input("Input the mine numbers: "))
            set_up(col_defined, row_defined, mine_number)
            #   print(state["initial"])
            game_statistics["time_1"] = datetime.datetime.now().replace(microsecond=0)
            main()
            print("The game was started at {}, took {} to finish".format(game_statistics["time_1"],
                                                                         game_statistics["time_2"] -
                                                                         game_statistics["time_1"]))
            print("You {} the game".format(game_statistics["outcome"].pop()))
            break
        elif choice == 2:
            break

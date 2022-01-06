import sweeperlib
import ex4_place_mines
from ex4_place_mines import state, window


# the initial field
def floodfill(planet_data, start_x, start_y):
    to_check_list = [(start_x, start_y)]
    border_list = [(start_x, start_y)]
    height = len(planet_data)
    width = len(planet_data[0])
    while to_check_list:
        new_item = to_check_list[0]
        to_check_list = list(filter(new_item.__ne__, to_check_list))
        safe_x = new_item[0]
        safe_y = new_item[1]
        state["field"][safe_y][safe_x] = planet_data[safe_y][safe_x]  # mark the tile as safe
        planet_data[safe_y][safe_x] = " "
        for i in (safe_x - 1, safe_x, safe_x + 1):
            for j in (safe_y - 1, safe_y, safe_y + 1):
                if 0 <= i <= (width - 1) and 0 <= j <= (height - 1):
                    if planet_data[j][i] == '0':
                        to_check_list.append((i, j))
                        border_list.append((i, j))
    while border_list:
        border_item = border_list[0]
        border_list = list(filter(border_item.__ne__, border_list))
        border_x = border_item[0]
        border_y = border_item[1]
        for i in (border_x - 1, border_x, border_x + 1):
            for j in (border_y - 1, border_y, border_y + 1):
                if 0 <= i <= (width - 1) and 0 <= j <= (height - 1):
                    if planet_data[j][i] != ' ':
                        state["field"][j][i] = state["initial"][j][i]

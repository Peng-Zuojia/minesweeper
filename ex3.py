def count_ninjas(x, y, room_data):
    height = len(room_data)
    width = len(room_data[0])
    ninja = 0
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if 0 <= i <= (width - 1) and 0 <= j <= (height - 1) and room_data[j][i] == 'x':
                ninja += 1

    return ninja

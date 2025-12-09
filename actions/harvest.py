def harvest(field, player_x, player_y):
    if field[player_y][player_x] == 0:

        field[player_y][player_x] = 1
    elif field[player_y][player_x] == 1:

        field[player_y][player_x] = 0
    elif field[player_y][player_x] == 2:

        field[player_y][player_x] = 0

    return field
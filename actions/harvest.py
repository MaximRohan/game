def harvest(field, player_x, player_y, growth_time):
    if field[player_y][player_x] == 1:
        field[player_y][player_x] = 0
        growth_time[player_y][player_x] = 0
    elif field[player_y][player_x] == 2:
        field[player_y][player_x] = 0
        growth_time[player_y][player_x] = 0
    else:
        growth_time[player_y][player_x] = 0
    return field, growth_time
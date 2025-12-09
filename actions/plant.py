def plant_grass(field, player_x, player_y):
    if field[player_y][player_x] == 0:
        field[player_y][player_x] = 1
    return field
def plant_tree(field, player_x, player_y):
    if field[player_y][player_x] == 0:
        field[player_y][player_x] = 2
    return field
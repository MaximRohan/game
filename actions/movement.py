def try_move(field, player_x, player_y, dx, dy):
    height = len(field)
    width = len(field[0])

    new_x = player_x + dx
    new_y = player_y + dy

    if 0 <= new_x < width and 0 <= new_y < height:
        return new_x, new_y

    return player_x, player_y

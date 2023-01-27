game = [[2, 0, 2],
        [1, 1, 1],
        [1, 0, 2]]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if not just_display:
            game_map[row][column] = player
        print("   0  1  2")
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: Make sure you input row/column  as 0, 1 or 2", e)
    except Exception as e:
        print("Something went very wrong!!", e)


game = game_board(game, just_display=True)

game = game_board(game, 1, 2, 2)
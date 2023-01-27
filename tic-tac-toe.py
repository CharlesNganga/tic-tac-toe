game = [[2, 0, 2],
        [1, 1, 1],
        [1, 0, 2]]


def win(current_game):
    # Horizontal win
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")

    # Diagonal win
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (/) !")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (\\) !")

    # Vertical win
    for col in range(len(game)):
        check = []
        for row in game:
            # print(row[0])
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically (|) !")


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
import itertools


def win(current_game):

    def all_same(lst):
        if lst.count(lst[0]) == len(lst) and lst[0] != 0:
            return True
        else:
            return False

    # Horizontal win
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # Diagonal win
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/) !")
        return True # This makes the function to stop running

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\) !")
        return True

    # Vertical win
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically (|) !")
            return True
    return False  # Returns no winner and ends the function


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado. Try another one!!")
            return game_map, False  # This gives the player another chance to play after the error
        if not just_display:
            game_map[row][column] = player
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Error: Make sure you input row/column  as 0, 1 or 2", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = game_board(game, just_display=True)  # _ means we don't care about the return
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")

        played = False

        while not played:
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))  # Add error for invalid input eg Enter and strings
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Byeeeee! See yuh!")
                print("Congrats to the winner. Loser when are you gonna win!!")
                play = False
            else:
                print("Oooops entered wrong value!! See you later....")
                play = False
